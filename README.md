# Fintech Review Analytics
#Bisrat Tamrat Bekele

## Project Overview
This project analyzes customer reviews from Ethiopian banking applications on the Google Play Store.

Banks analyzed:
- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The project focuses on:
- scraping reviews
- preprocessing customer feedback
- sentiment analysis
- thematic analysis
- customer experience insights

---

## Data Collection
Reviews were scraped using the `google-play-scraper` Python library.

Collected fields:
- review text
- rating
- review date
- bank name
- source

---

## Preprocessing
The dataset was cleaned by:
- removing duplicate reviews
- handling missing values
- formatting dates consistently

---

## Sentiment Analysis
VADER sentiment analysis was used to classify reviews into:
- Positive
- Neutral
- Negative

---

## Tools Used
- Python
- Pandas
- NLTK
- Matplotlib
- Google Play Scraper
- GitHub Actions
