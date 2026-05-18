from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(reviews):

    vectorizer = TfidfVectorizer(
        stop_words='english',
        max_features=10
    )

    X = vectorizer.fit_transform(reviews)

    return vectorizer.get_feature_names_out()