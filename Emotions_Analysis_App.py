# Core Pkgs
import streamlit as st 
import altair as alt
import plotly.express as px 
import tweepy

# EDA Pkgs
import pandas as pd 
import numpy as np 
from datetime import datetime

# Utils
import joblib 
pipe_lr = joblib.load(open("Emotion_Classifier_Model.pkl","rb"))

import sys


# Fxn
def predict_emotions(docx):
	results = pipe_lr.predict([docx])
	return results[0]

def get_prediction_proba(docx):
	results = pipe_lr.predict_proba([docx])
	return results

emotions_emoji_dict = {"anger":"😠","disgust":"🤮", "fear":"😨😱", "happy":"🤗", "joy":"😂", "neutral":"😐", "sad":"😔", "sadness":"😔", "shame":"😳", "surprise":"😮"}

# Main Application
def main():
	st.title("Emotion Classifier App")
	menu = ["Text","Twitter","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Text":

		st.subheader("Home-Emotion In Text")

		with st.form(key='emotion_clf_form'):
			raw_text = st.text_area("Type Here")
			submit_text = st.form_submit_button(label='Submit')

		if submit_text:
			col1,col2  = st.beta_columns(2)

			# Apply Fxn Here
			prediction = predict_emotions(raw_text)
			probability = get_prediction_proba(raw_text)

			with col1:
				st.success("Original Text")
				st.write(raw_text)

				st.success("Prediction")
				emoji_icon = emotions_emoji_dict[prediction]
				st.write("{}:{}".format(prediction,emoji_icon))
				st.write("Confidence:{}".format(np.max(probability)))



			with col2:
				st.success("Prediction Probability")
				# st.write(probability)
				proba_df = pd.DataFrame(probability,columns=pipe_lr.classes_)
				# st.write(proba_df.T)
				proba_df_clean = proba_df.T.reset_index()
				proba_df_clean.columns = ["emotions","probability"]

				fig = alt.Chart(proba_df_clean).mark_bar().encode(x='emotions',y='probability',color='emotions')
				st.altair_chart(fig,use_container_width=True)



	elif choice == "Twitter":
		st.subheader("Twitter Analysis App")
		tweetText = []
			
		with st.form(key='emotion_clf_form'):
			searchTerm = st.text_input("Search a keyward")
			NoOfTerms = st.text_input("Enter Number of Tweets")
			submit_text = st.form_submit_button(label='Submit')	
			
		if submit_text:		
			tweets = tweepy.Cursor(api.search, q=searchTerm, lang = "en").items(int(NoOfTerms))
			for tweet in tweets:
				tweetText.append((tweet.text).encode('utf-8'))
			
			text_1 = b" ".join(tweetText)
			text = text_1.decode()  
			
			col1,col2  = st.beta_columns(2)

			# Apply Fxn Here
			prediction = predict_emotions(text)
			probability = get_prediction_proba(text)

			with col1:
				st.success("Your Keyward")
				st.write(searchTerm)

				st.success("Prediction")
				emoji_icon = emotions_emoji_dict[prediction]
				st.write("{}:{}".format(prediction,emoji_icon))
				st.write("Confidence:{}".format(np.max(probability)))



			with col2:
				st.success("Prediction Probability")
				# st.write(probability)
				proba_df = pd.DataFrame(probability,columns=pipe_lr.classes_)
				# st.write(proba_df.T)
				proba_df_clean = proba_df.T.reset_index()
				proba_df_clean.columns = ["emotions","probability"]

				fig = alt.Chart(proba_df_clean).mark_bar().encode(x='emotions',y='probability',color='emotions')
				st.altair_chart(fig,use_container_width=True)


	else:
		st.subheader("About")
		st.write("Created by Sumant Reddy")
		st.write('''\n\n Feel free to connect with me on 
		 reddysumant25@gmail.com ''')


if __name__ == '__main__':
	try: 
		consumerKey = sys.argv[0]
		consumerSecret = sys.argv[2]
		accessToken = sys.argv[3]
		accessTokenSecret = sys.argv[4]
		auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
		auth.set_access_token(accessToken, accessTokenSecret)
		api = tweepy.API(auth)
		main()
	except:
		st.title("Error occured while processing Twitter APIs")
		st.subheader("Please try again !")
