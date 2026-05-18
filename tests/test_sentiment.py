from src.sentiment import classify_sentiment

def test_positive_sentiment():
    assert classify_sentiment(0.8) == "Positive"

def test_negative_sentiment():
    assert classify_sentiment(-0.5) == "Negative"