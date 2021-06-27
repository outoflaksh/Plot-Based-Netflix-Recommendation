# Plot-based Netflix Recommendation
<p align = "center">
<img src = "https://forthebadge.com/images/badges/made-with-python.svg">
</p>
Content recommendation is a machine learning task that involves recommending similar content (tv-shows, movies, books, etc) based on the user's taste or other similar users.


* When recommending content based on other similar users, the techniques employed come under *content-filtering*.
* Whereas, when recommending content based on some content that the user already enjoys, then it comes under *content-based recommendation*.

## About this repository

This repository involves building a "content-based recommendation system" - that is - it aims to recommend content similar to the one the user selects.

The similarity is judged on the basis of genre, plot, cast, and the director of the Netflix Movie or TV-show.

## Dataset

The dataset used for the code can be found [here](https://www.kaggle.com/shivamb/netflix-shows).

## Working

First the dataset is cleaned. All the plot description texts are preprocessed: converting to lowercase, removing punctuation, digits, stopwords and words are lemmatized. 

Then, the description are appended to the director, cast, and genre listings so that all the keywords are obtained for each content type in one sentence.

After that each of these sentences are vectorised using the TF-IDF algorithm. A similarity matrix is then created where each content's **cosine-similarity** with every other content is calculated.

When the user enters a content's title as the input, the corresponding similarity row is fetched from the similarity-matrix and the top ten values and their corresponding titles are extracted and returned.

