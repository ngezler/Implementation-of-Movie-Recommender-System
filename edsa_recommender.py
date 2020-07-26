"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
import streamlit.components.v1 as components
from streamlit_pandas_profiling import st_profile_report
import sweetviz as sv

# Data handling dependencies
import pandas as pd
import numpy as np 
import codecs
from pandas_profiling import ProfileReport 

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model



def st_display_sweetviz(report_html,width=1000,height=500):
	report_file = codecs.open(report_html,'r')
	page = report_file.read()
	components.html(page,width=width,height=height,scrolling=True)

# Data Loading
title_list = load_movie_titles('../unsupervised_data/unsupervised_movie_data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","pandas profiling", "sweetviz", "custom eda", "Solution Overview"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -----------------------------------------------------------------------#
    #                       SAFE FOR ALTERING/EXTENSION                      #
    #------------------------------------------------------------------------#
    #                           pandas profiling                             #
    #------------------------------------------------------------------------#
    if page_selection == "pandas profiling":
        st.title("pandas profiling")
        ds = st.radio("choose the data sorce", ("upload data", "use internal data"))
        if ds == "upload data":
            data_file = st.file_uploader("Upload CSV",type=['csv'])
        else:
            data_file = "resources/data/ratings.csv"
        if data_file is not None:
            df = pd.read_csv(data_file)
            st.dataframe(df.head())
            profile = ProfileReport(df)
            st_profile_report(profile)
        pass
    
    #------------------------------------------------------------------------#
    #                           Sweetviz report                              #
    #------------------------------------------------------------------------#
    if page_selection == "sweetviz":
        st.title("sweetviz")
        ds = st.radio("choose the data sorce", ("upload data", "use internal data"))
        if ds == "upload data":
            data_file = st.file_uploader("Upload CSV",type=['csv'])
        else:
            data_file = "resources/data/ratings.csv"
        if data_file is not None:
            df1 = pd.read_csv(data_file)
            st.dataframe(df1.head())
            if st.button("Genwrate Sweetviz Report"):
                report = sv.analyze(df1)
                report.show_html()
                st_display_sweetviz("SWEETVIZ_REPORT.html")
        pass

    #------------------------------------------------------------------------#
    #                           Custom EDA                                   #
    #------------------------------------------------------------------------#
    if page_selection == "custom eda":
        # Merging the train and movies data on the movieId column
        pass

    #------------------------------------------------------------------------#
    #                           Best                                         #
    #------------------------------------------------------------------------#

    #------------------------------------------------------------------------#
    #                        Slides                               #
    #------------------------------------------------------------------------#


    #------------------------------------------------------------------------#
    #                        Solution Overview                               #
    #------------------------------------------------------------------------#
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")
    
    #------------------------------------------------------------------------#
    #                        Slides                                          #
    #------------------------------------------------------------------------#
    

    # You may want to add more sections here for aspects such as an EDA,
    

    # or to provide your business pitch.


if __name__ == '__main__':
    main()

    #'sha1:f3da046ef1cc:59a9e49b00196019c48620ad538e7a4c40548e37' ser
