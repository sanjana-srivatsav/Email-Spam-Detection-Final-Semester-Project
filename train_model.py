import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pickle

data = pd.read_csv("dataset/spam.csv", sep="\t", names=["label", "message"])

data["label"] = data["label"].map({"ham": 0, "spam": 1})

X = data["message"]
y = data["label"]

vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2)

model = MultinomialNB()
model.fit(X_train, y_train)

pickle.dump(model, open("spam_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained successfully")
