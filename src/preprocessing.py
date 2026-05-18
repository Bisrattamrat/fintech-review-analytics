def clean_reviews(df):

    # Remove duplicates
    df = df.drop_duplicates(subset=["review"])

    # Remove missing values
    df = df.dropna(subset=["review", "rating"])

    return df