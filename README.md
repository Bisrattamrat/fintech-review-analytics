# Fintech Review Analytics
#Bisrat Tamrat Bekele

## Project Overview
This project analyzes customer reviews from Ethiopian banking applications on the Google Play Store as part of the 10 Academy Week 2 Challenge: **Customer Experience Analytics for Fintech Apps**.

The objective of the project is to transform raw customer feedback into actionable business insights using data engineering, sentiment analysis, thematic analysis, and visualization techniques.

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
- database schema design
- stakeholder-ready visualizations

---

# Business Problem

Mobile banking adoption in Ethiopia is rapidly increasing, and customer reviews on the Google Play Store provide valuable insight into user satisfaction, recurring complaints, feature requests, and application performance.

This project helps identify:
- customer satisfaction drivers
- common technical issues
- recurring complaints
- feature improvement opportunities
- sentiment trends across banks

---

# Project Structure

fintech-review-analytics/

├── .github/workflows/unittests.yml  
├── data/raw/  
├── notebooks/  
├── scripts/  
├── src/  
├── tests/  
├── README.md  
├── requirements.txt  
├── schema.sql  

---

# Data Collection

Reviews were scraped using the `google-play-scraper` Python library.

Collected fields:
- review text
- rating
- review date
- bank name
- source

Target:
- minimum 400 reviews per bank
- over 1,200 reviews in total

The scraping pipeline includes basic error handling to improve reliability during data collection.

---

# Preprocessing

The dataset was cleaned by:
- removing duplicate reviews
- handling missing values
- formatting dates consistently
- converting dates into YYYY-MM-DD format

Cleaned datasets were saved locally and excluded from GitHub using `.gitignore`.

---

# Sentiment Analysis

Sentiment analysis was performed using VADER/TextBlob-based scoring methods.

Reviews were classified into:
- Positive
- Neutral
- Negative

Sentiment distributions were visualized using Matplotlib.

The project also compares customer sentiment across different banks and ratings.

---

# Thematic Analysis

Keyword extraction and thematic analysis were performed using TF-IDF techniques.

Identified themes include:
- Transaction Performance
- Account Access Issues
- UI & User Experience
- Customer Support
- Feature Requests

Themes were extracted from recurring keywords and customer feedback patterns.

---

# Database Design

A PostgreSQL relational schema was designed to store:
- bank information
- processed review data
- sentiment labels
- identified themes

Database schema is included in:
- `schema.sql`

---

# Visualizations

The project includes visualizations such as:
- sentiment distribution charts
- review count comparisons
- keyword/theme frequency analysis

Plots were generated using Matplotlib.

---

# Tools Used

- Python
- Pandas
- NLTK
- Matplotlib
- Scikit-learn
- Google Play S
- PostgreSQL
- GitHub Actions
- Git
- Jupyter Notebook

---

# CI/CD

GitHub Actions was configured using:
`.github/workflows/unittests.yml`

The workflow automatically installs project dependencies on pushes to the main branch.

---

# Testing

Basic unit tests were implemented for:
- sentiment classification functions

Tests are located inside:
`tests/`

---

# Ethical Considerations

Potential limitations and biases include:
- users are more likely to leave reviews after negative experiences
- reviews may not represent all users
- scraping limitations and rate limits may affect data completeness

---

# Future Improvements

Future enhancements may include:
- transformer-based sentiment analysis using DistilBERT
- advanced topic modeling (LDA/NMF)
- dashboard deployment
- automated data pipelines
- chatbot integration for complaint handling

---

# Author

Developed as part of the 10 Academy Artificial Intelligence Mastery Program – Week 2 Challeng

