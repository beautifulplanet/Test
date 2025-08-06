# Saporis - Practical Sentiment Analysis Task

This project is a simple FastAPI application that provides an endpoint for sentiment analysis of influencer statements, as per the practical task.

### Features
- A `/analyze` endpoint that accepts a POST request with text.
- Sentiment analysis using a pre-trained Hugging Face transformer model.
- Natural language generation for a brief insight summary.

### How to Run
1.  **Clone the repository.**
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the application:**
    ```bash
    uvicorn main:app --reload
    ```
    The API will be available at `http://127.0.0.1:8000`.

### How to Use
You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

From there, you can use the `/analyze` endpoint.

**Example Request Body:**
```json
{
  "statement_text": "I'm absolutely thrilled with the new product launch, it's a game-changer!"
}
```

**Example Response Body:**
```json
{
  "sentiment_label": "POSITIVE",
  "sentiment_score": 0.9998,
  "insight_summary": "The statement appears to be POSITIVE with high confidence. This indicates a favorable view or endorsement, likely to be well-received by the audience."
}
```