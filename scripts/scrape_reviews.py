from google_play_scraper import reviews, Sort
import pandas as pd

# Apps to scrape
apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

# Loop through apps
for bank, app_id in apps.items():

    result, _ = reviews(
        app_id,
        lang='en',
        country='et',
        sort=Sort.NEWEST,
        count=400
    )

    for review in result:
        all_reviews.append({
            "review": review['content'],
            "rating": review['score'],
            "date": review['at'].strftime('%Y-%m-%d'),
            "bank": bank,
            "source": "Google Play"
        })

# Convert to DataFrame
df = pd.DataFrame(all_reviews)

# Remove duplicates
df.drop_duplicates(subset=["review"], inplace=True)

# Remove missing values
df.dropna(subset=["review", "rating"], inplace=True)

# Save cleaned dataset
df.to_csv("data/raw/cleaned_bank_reviews.csv", index=False)

print("Scraping completed successfully.")
print(df.head())
print(f"Total reviews collected: {len(df)}")