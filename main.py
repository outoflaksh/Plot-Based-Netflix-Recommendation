import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def get_similarity_matrix():
    dataset = pd.read_csv('./dataset/processed.csv')
    count = TfidfVectorizer()
    count_matrix = count.fit_transform(dataset['bag_of_words'])
    cosine_sim = cosine_similarity(count_matrix, count_matrix)

    return cosine_sim

def recommendations(title, cosine_sim = get_similarity_matrix()):
    indices = pd.read_csv('./dataset/indices.csv')

    if title not in indices.values:
        return "Movie or TV-show not found in database!"
    
    recommended_movies = []
    # gettin the index of the movie that matches the title
    idx = indices[indices['title'] == title].index[0]

    # creating a Series with the similarity scores in descending order
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)
    
    # getting the indexes of the 10 most similar movies
    top_10_indexes = list(score_series.iloc[1:11].index)

    # populating the list with the titles of the best 10 matching movies
    for i in top_10_indexes:
        recommended_movies.append((i, indices.loc[i]['title']))
        
    return recommended_movies