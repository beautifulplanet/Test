from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from analyzer import SentimentAnalyzer, SentimentResult

# --- Application Setup ---
app = FastAPI(
    title="Saporis Sentiment Analysis API",
    description="A practical API for analyzing influencer statements.",
    version="1.0.0"
)

# Load the model once when the application starts
try:
    analyzer_instance = SentimentAnalyzer()
except Exception as e:
    # If the model fails to load, the app is not usable.
    raise RuntimeError(f"Failed to load the sentiment analysis model: {e}") from e

# --- Pydantic Models (for Request and Response) ---
class StatementRequest(BaseModel):
    statement_text: str = Field(
        ..., 
        min_length=10, 
        max_length=500, 
        description="The influencer statement to be analyzed.",
        example="I'm absolutely thrilled with the new product launch, it's a game-changer!"
    )

class AnalysisResponse(BaseModel):
    sentiment_label: str = Field(..., example="POSITIVE")
    sentiment_score: float = Field(..., example=0.9998, description=f"Confidence score for the label, $S \\in [0, 1]$")
    insight_summary: str = Field(..., example="The statement appears to be POSITIVE with high confidence...")

# --- API Endpoints ---
@app.get("/")
def read_root():
    return {"message": "Welcome to the Saporis Sentiment Analysis API. Please use the /analyze endpoint."}

@app.post("/analyze", response_model=AnalysisResponse)
def analyze_statement(request: StatementRequest):
    """
    Receives an influencer statement, performs sentiment analysis,
    and returns the sentiment along with a generated insight.
    """
    try:
        # 1. Get the text from the request
        text = request.statement_text

        # 2. Perform sentiment analysis using our AI component
        sentiment: SentimentResult = analyzer_instance.analyze(text)

        # 3. Generate the natural language insight summary
        summary: str = analyzer_instance.generate_insight_summary(text, sentiment)

        # 4. Return the structured response
        return AnalysisResponse(
            sentiment_label=sentiment.label,
            sentiment_score=sentiment.score,
            insight_summary=summary
        )

    except Exception as e:
        # A general catch-all for any unexpected errors during processing
        raise HTTPException(status_code=500, detail=f"An internal error occurred: {str(e)}")

# --- To run this application ---
# In your terminal, use the command: uvicorn main:app --reload
