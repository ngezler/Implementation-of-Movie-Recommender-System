#html temp
html_temp = """
            <div style="background-color:#373645;padding:10px">
            <h2 style="color:white;text-align:center;"><b>Our Approach To Building The Movie Recommender Engine</b></h2>
            </div>
            """

html_overview = """
                <figure style:"align:center;"><img alt="" src="https://cdn-images-1.medium.com/max/591/1*KQxKzb8hE2_t72TBRFl2Bg.png", style:"align:center"><figcaption style="text-align:center;">The diagram above represents recommendation system with collaborative filtering.</figcaption></figure>
                <a>In this project we were given two approaches that acted as a starting point, namely collerborative and content based filtering.</a>
                <br></br>
                <ul><li>Content based filtering: uses item features to recommend similar items to the ones that a user has previously liked or interacted with.</li><li>Collaborative filtering: identifies items that a user will like based on how similar users rated each item. Netflix identifies shows and movies users will enjoy by determining which content similar users&nbsp;watched.</li></ul>
                <br></br>
                <p>As a Team we decided on developing a collaborative filtering recommender engine, we will only look at the building process of a CF model<p>
                <h3>Requirements To Get Started</h3>
                <p>To build the Model for recommender, we used these packages: Pandas, numpy, Surprise, a Python scikit package built for collaborative filtering</p>
                <h3>Surprise<h3>
                <p>
                    we used suprise's built in user-ratings matrix conversion, we started supplying a train dataframe that contains a user id column, an item id column, and a rating column.
                    From there, Surprise helped us generate a user-ratings matrix where each user id is a row and each movie the company offers is a column. This had the same impact as creating a Pandas pivot table. We then divided the dataframe into a train and test set with an 80/20 split.
                </p>
                <h3>algorithms</h3>
                <p>
                   Surprise offers 11 different prediction algorithms including variations of KNN and dimensionality reduction techniques such as SVD and NMF. For this demonstration, we ended up using svd. 
                </p>
                <ul>
                    <li>SVD: A matrix factorization technique popularized by Simon Funk as part of the Netflix prize.</li>
                </ul>

                <h3>Model Accessment</h3>
                <p>
                    There are two ways to assess model performance. Qualitatively, you can look at a given user and determine if the recommendation makes sense given other products they like. For example, if someone likes horror movies and doesn’t like romantic comedies, The Shining would be a good recommendation relative to Love Actually. For this dataset, we did not have information about each product, only a movie id so we used a quantitative measure, root mean squared error. A combination of the two methods is ideal, though a quantitive measure is much more realistic in production
                </p>
                <h3>Model Tuning</h3>
                <p>The surprise package offers an option to tune parameters using GridSearchCV. We provided GridSearchCV with a dictionary of parameters and the rmse will be calculated and compared for every combination of the parameters.</p>

                """



#========================================================================
slide = """<div class="responsive-wrap">
    <!-- this is the embed code provided by Google -->
    <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQoW4r8Dubcay3w5U5yccaHYoT32n1O3tQ-ymUPptBW9vxvptbbHd3xLB45w8bygJ6Yk08QCL0ca9KS/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>    <!-- Google embed ends -->
    </div>"""

#===================================================================================
eda_header = """
            <div style="background-color:#373645;padding:10px;">
            <h2 style="color:white;text-align:center;"><b>Exploratory Data Analysis</b></h2>
            </div>

            """
#===================================================================================
rec_header = """
            <div style="background-color:#373645;padding:10px">
            <h2 style="color:white;text-align:center;"><b>Movie Recommender Engine</b></h2>
            <h3 style ="color:white;text-align:center" >EXPLORE Data Science Academy Unsupervised Predict</h3>
            </div>
            """
#===================================================================================
sweet = """
            <div style="background-color:#373645;padding:10px;">
            <h2 style="color:white;text-align:center;"><b>SWEETVIZ</b></h2>
            <a style="color:white;text-align:center;"><SWEETVIZLIBRARY DISTRIBUTION</a2>
            </div>

            """
#===================================================================================
prof = """
            <div style="background-color:#373645;padding:10px;">
            <h2 style="color:white;text-align:center;"><b>Pandas Profiling</b></h2>
            </div>

            """
#===================================================================================
#===================================================================================
