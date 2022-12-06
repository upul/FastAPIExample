from pydantic import BaseModel


class SentimentDisplay(BaseModel):
    input_text: str
    prediction: str
    confidence_probability: float


class SentimentInput(BaseModel):
    input_text: str
