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
from utils.data_loader import (load_movie_titles, read_file,\
                                local_css, remote_css)
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
from views import (html_temp, eda_header, rec_header, sweet, prof,\
                    html_overview, slides, home)

#===============================display a sweetviz report==================================
def st_display_sweetviz(report_html,width=1000,height=500):
	report_file = codecs.open(report_html,'r')
	page = report_file.read()
	components.html(page,width=width,height=height,scrolling=True)

# Data Loading
title_list = load_movie_titles('../unsupervised_data/unsupervised_movie_data/movies.csv')

#====================================load_css============================================
def load_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

load_css("./utils/styles.css")

#===================================load_icons==============================================
def load_icon(icon_name):
    st.markdown('<i class="material-icons">{}</i>'.format(icon_name), unsafe_allow_html=True)

#=================================images loader================================================
# Images
def load_images(file_name):
	img = Image.open(file_name)
	return st.image(img,width=300)

#=================================================================================

# App declaration
def main():

    
    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System", "Pandas profiling", "Sweetviz", "EDA", "Solution Overview", "Slides"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.markdown(rec_header,unsafe_allow_html=True)
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
    if page_selection == "Pandas profiling":
        st.markdown(prof,unsafe_allow_html=True)
        ds = st.radio("choose the data sorce", ("movies data", "ratings data"))
        if ds == "movies data":
            data_file = 'resources/data/movies.csv'
        else:
            data_file = 'resources/data/ratings.csv'
        if data_file is not None:
            df = pd.read_csv(data_file)
            st.dataframe(df.head())
            profile = ProfileReport(df)
            st_profile_report(profile)
        pass
    
    #------------------------------------------------------------------------#
    #                           Sweetviz report                              #
    #------------------------------------------------------------------------#
    if page_selection == "Sweetviz":
        st.markdown(sweet,unsafe_allow_html=True)
        ds = st.radio("choose the data sorce", ("movies data", "ratings data"))
        if ds == "movies data":
            data_file = 'resources/data/movies.csv'
        else:
            data_file = 'resources/data/ratings.csv'
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
    if page_selection == "EDA":
        #Ratings by year
        st.markdown(eda_header,unsafe_allow_html=True)
        
        if st.checkbox("Ratings by year"):
            st.image("resources/imgs/ratings_by_year.PNG", format='PNG')
            st.write("The ratings for the movies span a period of 25 years, from 1995 all the way to 2019, with the last 5 years accumalatively having had the most ratings in comparison to any othe other 5 year interval. From 2006 to 2014 there is decline in user engagement when it comes to rating movies. Prior to 2006 there are 3 good years with ratings above 500000 ratings for the year, 3 more years at 400000 ratings and 3 below 300000 ratings for the year. it would be of interest to the spending behaviour of users for each of these years, as that would tell the complete story.")
            #components.html()

        #Movies Realese before and after 1995
        if st.checkbox("Now for a look at the release year of each of the movies"):
            st.image("resources/imgs/Movie_release_over_T.PNG", format='PNG')
            st.write("29906 movies have been released in total since 1995 up to 2019, in comparison to the 17937 that have released up to 1994 going all the way back to 1874 (this is not including movies that had no release date specified, which amount to 370 movies). The number of released movies per year is increases slowly at the beginning, then increasing faster leading up to 1995, where the is a substantial rise in the number of movies released. So much so that roughly on average a 153 movies have been released a year from 1874 to 1994, while that number increases substantially for the years between 1995 to 2019, averaging roughly 1246 movies per year. This has given users an overwheliming amount of options to choose from, with regards to the movies they can watch, catering to the needs of everyone, which makes the case for a recommendation system compelling.")

            #components.html()
        
        #Distributins of user ratings for movies in the past 25 years
        if st.checkbox("Distributins of user ratings for movies in the past 25 years"):
            st.image("resources/imgs/dst.PNG", format='PNG')
            st.image("resources/imgs/dst1.PNG", format='PNG')
            st.image("resources/imgs/dst2.png", format='PNG')
            st.write("For the entire 25 year period, a rating of 4.0 is the most abundant rating given by users to movies,\
              followed by a rating of 3.0. Ratings of 5.0, 3.5 and 4.5 are next most numerous ratings users give to movies.\
              When the the 25 years are divided into 5, 5 year periods, the first 5 year period between 1995 and 1999,\
              there is an anomaly in the ratings, quite different from th other periods,\
              but still with ratings of 4.0 and 3.0 being the most abundant, followed by a 5.0 rating.\
              The last 3 intervals there is a contant pattern that has emerged with the distributions of the ratings")
            #components.html()

        #Ratings distributions across movie genres
        if st.checkbox("Ratings distributions across movie genres"):
            st.image("resources/imgs/ratings_by_year.png", format='PNG')
            st.write("Movies with between 1 to 4 genres have the most number of ratings for the 25 years, with an average rating for these of roughly bewteen 3.5 to 3.6. Movies with 2 and 3 genres movies get the lions share of the ratings.")
            #components.html()
        
        #Decade movies were released
        if st.checkbox("Decade movies were released"):
            st.image("resources/imgs/dc.png", format='PNG')
            st.write("This is an interesting insight in the data with potentially huge implications, that will be eloborated upon later, in the conclusion when recommendations are put forward. For now however what emerges is the following; movies from before the 1970s have little to no ratings associated with them. Movies released from 1980s have the most ratings. The average rating for movies released for each decade from 1910 onwards is between 3.5 and 4.0., with that average for movies released in later decades carries more weight, since they have more ratings. With movies released in earlier decades having a lower average, perhaps to do with the quality of the movies.")
            #components.html()
        # Merging the train and movies data on the movieId column
        pass

    #------------------------------------------------------------------------#
    #                           Home                                         #
    #------------------------------------------------------------------------#
    #if page_selection == "Home":
    #    st.markdown(home,unsafe_allow_html=True)
    #
    #------------------------------------------------------------------------#
    #                        Slides                               #
    #------------------------------------------------------------------------#
    if page_selection == "Slides":
        st.markdown(slides,unsafe_allow_html=True)
        
        #load_css('utils/icon.css')


    #------------------------------------------------------------------------#
    #                        Solution Overview                               #
    #------------------------------------------------------------------------#
    if page_selection == "Solution Overview":
        st.markdown(html_temp,unsafe_allow_html=True)
        st.markdown(html_overview,unsafe_allow_html=True)
    
    #------------------------------------------------------------------------#
    #                        team                                            #
    #------------------------------------------------------------------------#
    #if page_selection == "Team":
     #   pass
      #  #st.markdown(team,unsafe_allow_html=True)
        #load_css('utils/team.css')
    
    # You may want to add more sections here for aspects such as an EDA,
    

    # or to provide your business pitch.


if __name__ == '__main__':
    main()
