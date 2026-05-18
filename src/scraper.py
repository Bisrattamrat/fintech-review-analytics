from google_play_scraper import reviews, Sort
import pandas as pd

def scrape_bank_reviews(app_id, bank_name, count=400):

    try:
        result, _ = reviews(
            app_id,
            lang='en',
            country='et',
            sort=Sort.NEWEST,
            count=count
        )

        data = []

        for review in result:
            data.append({
                "review": review["content"],
                "rating": review["score"],
                "date": review["at"].strftime("%Y-%m-%d"),
                "bank": bank_name,
                "source": "Google Play"
            })

        return pd.DataFrame(data)

    except Exception as e:
        print(f"Error scraping {bank_name}: {e}")
        return pd.DataFrame()