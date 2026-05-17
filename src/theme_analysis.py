from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(texts):

    vectorizer = TfidfVectorizer(
        stop_words='english',
        max_features=20,
        ngram_range=(1,2)
    )

    X = vectorizer.fit_transform(texts.astype(str))

    return vectorizer.get_feature_names_out()