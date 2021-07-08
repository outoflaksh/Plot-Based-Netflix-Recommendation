import streamlit as st 
import pandas as pd
from main import recommendations
from datasets import DATASET_FULL

df = DATASET_FULL
st.title("Netflix Content-Based Recommendation")
st.markdown("**Get top 10 most similar suggestions based on the one you choose**")
titles = list(df.loc[:, 'title'])
title = st.selectbox("Enter your favorite Netflix title below!", titles, index = 1089)
btn = st.button("Get recommendations")
if btn:
	st.write(f"Here are top 10 titles most similar to {title} based on its plot description, genre, cast, and directors: ")
	for ind, recom in enumerate(recommendations(title)):
		st.markdown(f"### {ind+1}. {recom[1]} ({df.loc[recom[0], 'duration']})")
		st.markdown(f"*{df.loc[recom[0], 'description']}*")

st.markdown("Built with ❤️ by [Lakshya Malik](https://github.com/outoflaksh)")