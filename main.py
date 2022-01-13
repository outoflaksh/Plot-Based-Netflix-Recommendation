import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

from datasets import DATASET_FULL, DATASET_PROCESSED, INDICES


def get_similarity_matrix(dataset=DATASET_PROCESSED):
    try:
        with open("similarity_matrix.pickle", "rb") as f:
            similarity_matrix = pickle.load(f)
            return similarity_matrix
    except:
        count = TfidfVectorizer()
        count_matrix = count.fit_transform(dataset["bag_of_words"])
        cosine_sim = cosine_similarity(count_matrix, count_matrix)

        with open("similarity_matrix.pickle", "wb") as f:
            pickle.dump(cosine_sim, f)

        return cosine_sim


def recommendations(
    title: str, cosine_sim=get_similarity_matrix(), indices=INDICES, df=DATASET_FULL
):
    title = title.lower()
    title_list = np.array([x[1].lower() for x in indices.values])

    if title not in title_list:
        return []

    recommended_movies = []
    # gettin the index of the movie that matches the title
    idx = indices[indices["title"].str.lower() == title].index[0]

    # creating a Series with the similarity scores in descending order
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending=False)

    # getting the indexes of the 10 most similar movies
    top_10_indexes = list(score_series.iloc[1:11].index)

    # populating the list with the titles of the best 10 matching movies
    for i in top_10_indexes:
        recommended_movies.append(
            {
                "index": i,
                "title": indices.loc[i]["title"],
                "description": df.loc[i, "description"],
                "duration": df.loc[i, "duration"],
            }
        )

    return recommended_movies
