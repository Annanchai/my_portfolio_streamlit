import streamlit as st
import pandas as pd
import io
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

import statsmodels.api as sm
import statsmodels.stats.api as sms
from statsmodels.stats.outliers_influence import variance_inflation_factor
import scipy.stats as sp
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import train_test_split

st.set_page_config(layout='wide')

# Link to bootstrap cdn
st.markdown('''
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
            ''', unsafe_allow_html=True
            )
#Data
dfnf = pd.read_csv('./data/netflix.csv')
dfjb = pd.read_csv('./data/jamboree.csv')
#functions




# Sidebar section
hcol1, hcol2 = st.sidebar.columns(2)
with hcol1:
    st.image('profile.png', width=150)

with hcol2:
    st.markdown('''<p class='h5 align-middle fw-bold text-center'>Shajeesh Radhakrishnan</p>''', unsafe_allow_html=True)
    st.markdown('''<p class='h6 text-center fw-bold'>Data Analyst</p>''', unsafe_allow_html=True)
    st.markdown('''<p class='h6 text-center'>India</p>''', unsafe_allow_html=True)

st.sidebar.markdown('''<p class='fw-bold'>About me</p>''', unsafe_allow_html=True)
intro = st.sidebar.selectbox(
    'Learn more about me',
    ('Introduction', 'Experience'), label_visibility='collapsed'
)
st.sidebar.markdown('''<p class='fw-bold'>Business Cases</p>''', unsafe_allow_html=True)
project = st.sidebar.selectbox(
    'Select an option to view the project',
    ('Netflix: Data Exploration and visualization',  'Jamboree education: Linear Regression', ), label_visibility='collapsed'
)
# 'Aerofit: Descriptive stats and probablity', 'Walmart: Confidence interval and CLT', 'YULU: Hypothesis testing','LoanTap: Logistic Regression' 


#Tabs Section
tab1, tab2 = st.tabs(['About Me', 'Business Cases'])

with tab1:
    if intro == 'Introduction':
        st.markdown('''
                    <div class='p-1 d-flex flex-row-reverse'>
                        <a class = 'p-2' href=https://www.hackerrank.com/profile/shajeesh>Hackerrank</a>
                        <a class = 'p-2' href=https://github.com/Annanchai>Github</a>
                        <a class='p-2' href=https://www.linkedin.com/in/shajeesh-radhakrishnan>Linkedin</a>
                        <a class = 'p-2' href=https://public.tableau.com/app/profile/shajeesh.radhakrishnan/vizzes>Tableau</a>
                    </div>
                    <div class='card p-5'>
                        <p class='h4'>About me</p>
                        <p class='p-2'>Hello! I'm Shajeesh Radhakrishnan, a passionate and aspiring Data Scientist with a background in Biochemistry and a current pursuit of an MSc in Computer Science: Artificial Intelligence and Machine Learning. Born and raised in Coimbatore, Tamilnadu, and originally from Malappuram, Kerala, I bring a unique blend of cultural diversity and analytical skills to my work.</p>
                        <p class='h4'>Tech Stack</p>  
                        <ul class='p-2'>
                            <li>General Skills: Data Analytics, Data Visualization, Probability and Statistics, Machine learning</li>
                            <li>Programming Languages: Python, HTML, JavaScript, React, React Native</li>
                            <li>Tools: Tableau, SQL, Github, Odoo</li>
                            <li>Libraries: Pandas, Numpy, Seaborn, Matplotlib, SciPy, Scikit-learn</li>
                        </ul> 
                        <p class='h4'>Education</p>
                        <ul class='p-2'>
                            <li>MSc in Computer Science: Artificial Intelligence and Machine Learning (Ongoing)</li>
                            <li>Graduate in Biochemistry</li>
                        </ul>
                        <p class='h4'>Language Proficiency</p>  
                        <p class='p-2'>Fluent in English, Hindi, Tamil, Malayalam, and Arabic(basic).</p>   
                        <p class='h4'>Professional Journey</p>  
                        <p class='p-2'>I embarked on my IT journey by building websites using Weebly and later transitioning to WordPress. As my interest in coding grew, I mastered HTML, CSS, and Javascript, eventually developing apps using React Native. Seeking a career shift, I enrolled in Scaler to specialize in Data Science.</p>   
                        <p class='h4'>Travel Enthusiast</p>  
                        <p class='p-2'>Fueled by a love for exploration, I've had the privilege of visiting Kuwait, Oman, UAE, France, Spain, Portugal, Switzerland, Luxembourg, and Belgium.</p> 
                        <p class='h4'>Passions</p>  
                        <p class='p-2'>In addition to data analysis, I find joy in coding, cooking, and baking.</p>
                        <p class='h4'>Projects</p>  
                        <ul class='p-2'>
                            <li>Developed interactive dashboards using Tableau to visualize complex datasets.</li>
                            <li>Utilized Python (Pandas, Numpy) for data manipulation and analysis.</li>
                            <li>Implemented statistical models to derive meaningful insights.</li>
                        </ul>  
                        <p class='h4'>Future Aspirations</p>  
                        <p class='p-2'>Eager to leverage my analytical skills to contribute meaningfully to the IT industry, I am on a continuous learning journey, exploring the intersection of data science and machine learning.</p> 
                    </div>
                    ''', unsafe_allow_html=True)
    elif intro == 'Experience':
        st.markdown('''
                    <div>
                        <p class='h1'>Experience</p>
                        <div>
                            <div class='d-flex justify-content-between'>
                                <p><span class='h3'>Manager</span><br><span>iTees Eye Hospital<span></p>
                                <p>Sep 2023 to Present</p>
                            </div>
                            <ul>
                                <li>Actively manage clinic operations and administrative activities, ensuring smooth day-to-day functioning.</li>
                                <li>Led the marketing team to achieve a 9% increase in total revenue within six months.</li>
                                <li>Automated incentive calculation processes using Python, resulting in over 50% time savings for accountants and significantly enhancing operational efficiency.</li>
                                <li>Leveraged exploratory data analysis (EDA) methods, such as bootstrapping and confidence intervals, to assist management in making informed decisions regarding target setting and incentive structures for optical sales staff. Conducted in-depth analysis of daily sales metrics to offer actionable insights and facilitate effective decision-making processes.</li>
                                <li>Prepare comprehensive reports on clinic performance and monitor accounting tasks including bookkeeping, bank reconciliations, and financial year auditing.</li>
                            </ul>
                        </div>
                        <div>
                            <div class='d-flex justify-content-between'>
                                <p><span class='h3'>Web Developer</span><br><span>Freelancer<span></p>
                                <p>Mar 2021 to Mar 2023</p>
                            </div>
                            <ul>
                                <li>Collaborated with clients to conceptualize and develop functional, aesthetically pleasing digital solutions for websites and mobile applications.</li>
                                <li>Designed, developed, and maintained e-commerce websites using WordPress.</li>
                                <li>Developed responsive websites using HTML, CSS, and JavaScript, and developed two mobile applications with React Native, integrating MongoDB for robust database management and real-time data retrieval.</li>
                            </ul>
                        </div>
                        <div>
                            <div class='d-flex justify-content-between'>
                                <p><span class='h3'>Hospital Manager</span><br><span>Majan Eye Center, Oman<span></p>
                                <p>Apr 2017 to Aug 2022</p>
                            </div>
                            <ul>
                                <li>Efficiently managed clinic operations, including inventory maintenance, financial record-keeping, payroll processing, and regulatory compliance, resulting in streamlined workflows and enhanced productivity.</li>
                                <li>Led the establishment of a new clinic, overseeing the entire setup process from sourcing equipment to obtaining necessary licenses, ensuring compliance with Ministry of Health standards and operational readiness.</li>
                                <li>Provided comprehensive administrative support to executive leadership, including correspondence preparation, scheduling, travel arrangements, and office organization, facilitating smooth communication and workflow management.</li>
                                <li>Collaborated with team members to coordinate events, campaigns, and seminars, and maintained the clinic's online presence through website updates and social media engagement, enhancing brand visibility and community engagement.</li>
                            </ul>
                        </div>
                        <div>
                            <div class='d-flex justify-content-between'>
                                <p><span class='h3'>Medical Laboratory Technician</span><br><span>Al Jahra Hospital – Ministry of Health, State of Kuwait<span></p>
                                <p>Jan 2014 to Feb 2017</p>
                            </div>
                            <ul>
                                <li>Conducted advanced diagnostic tests on clinical specimens to aid in accurate diagnosis.</li>
                                <li>Recorded control values from technical instruments to uphold reliability and accuracy in test results reporting.</li>
                                <li>Maintained meticulous records and adhered to established procedures for accurately reporting test results.</li>
                                <li>Proficiently managed Laboratory Information System to support the laboratory's quality operations and ensure efficient workflow.</li>
                            </ul>
                        </div>
                        <div>
                            <div class='d-flex justify-content-between'>
                                <p><span class='h3'>Administrator</span><br><span>Al Rayhan Eye Hospital, India<span></p>
                                <p>Oct 2013 to Dec 2013</p>
                            </div>
                            <ul>
                                <li>Developed and executed a successful advertising campaign to recruit healthcare providers for the new Al Rayhan kondotty branch, overseeing all hospital installations.</li>
                                <li>Led a comprehensive advertising campaign to attract patients from local areas to the hospital.</li>
                                <li>Acted as the hospital's representative in meetings with software developers to develop paper-free software, ensuring it met all necessary requirements.</li>
                                <li>Implemented a smart card system for patients, saving time and providing quality information to doctors and hospital staff, while maintaining a highly productive and patient-centric environment.</li>
                            </ul>
                        </div>
                        <div>
                            <div class='d-flex justify-content-between'>
                                <p><span class='h3'>Administrator</span><br><span>treeG Eye Care Hospital,India<span></p>
                                <p>Sep 2011 to Sep 2013</p>
                            </div>
                            <ul>
                                <li>Offered comprehensive support to the Manager while maintaining utmost confidentiality in handling all matters.</li>
                                <li>Prepared various documents including correspondences, memos, reports, and promotional materials according to the Manager's requirements.</li>
                                <li>Developed and executed innovative promotional marketing strategies to achieve organizational goals.</li>
                                <li>Managed patient registration, guided visitors, and provided information while adhering to ISO documentation procedures and maintaining quality systems.</li>
                            </ul>
                        </div>
                        <div>
                            <div class='d-flex justify-content-between'>
                                <p><span class='h3'>Production Chemist</span><br><span>Trivitron Medical Technologies (P) Ltd., India<span></p>
                                <p>Jun 2007 to Nov 2010 </p>
                            </div>
                            <ul>
                                <li>Efficiently execute production plans according to schedule and Master Manufacturing Docket.</li>
                                <li>Coordinate work schedules for technicians, trainees, and production helpers.</li>
                                <li>Oversee raw material dispense and receiving for batch manufacturing, ensuring adherence to procedures.</li>
                                <li>Manage quality monitoring, vessel cleaning, water plant operations, and waste disposal to uphold production standards.</li>
                            </ul>
                        </div>
                    </div>
                    ''', unsafe_allow_html=True)
        

with tab2:
#Netflix Project
    if project == 'Netflix: Data Exploration and visualization':
        st.markdown('''
                    <div>
                        <div class='d-flex justify-content-center'>
                            <p class='h2'>Netflix Project</p>
                        </div>
                        <p class='h4'>Problem Statement</p>
                        <p class='ms-3'>The project aims to address the critical challenge of leveraging data analysis to generate actionable insights for Netflix. By thoroughly analyzing data, the objective is to assist in strategic decision-making, specifically in determining the optimal content (shows/movies) to produce and devising growth strategies for the business.</p>
                    </div>
''', unsafe_allow_html=True)
        st.write('## Basic Analysis')
        st.write('### Observation of data')
        st.write('Load the data')
        st.code('df = pd.read_csv(r"data\ netflix.csv")')
        st.write('Display first five rows of the data')
        st.code('df.head(5)')
        st.dataframe(dfnf.head(5))
        st.code('df.shape')
        dfnf.shape
        st.code('df.info()')
        buffer = io.StringIO()
        dfnf.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

        #Unnesting
        st.write('### Unnesting')
        st.code('''
                df['cast'] = df['cast'].str.split(',')
                df['listed_in'] = df['listed_in'].str.split(',')
                df['director'] = df['director'].str.split(',')
                ''')
        st.code('''
                df = df.explode('cast', ignore_index = True)
                df = df.explode('listed_in', ignore_index = True)
                df = df.explode('director', ignore_index = True)
                ''')
        dfnf['cast'] = dfnf['cast'].str.split(',')
        dfnf['listed_in'] = dfnf['listed_in'].str.split(',')
        dfnf['director'] = dfnf['director'].str.split(',')
        st.code('df.head(10)')
        st.dataframe(dfnf.head(10))
        st.write('### Handling null values')
        st.code('''
                values = {'director': 'unknown_director', 'cast': 'unknown_cast', 'country': 'unknown_country', 'date_added': 'unknown_date_added', 'rating': 'unknown_rating', 'duration': 0}
                df.fillna(value = values, inplace = True)
                df.head(10)
                ''')
        # Shows error on Streamlit
        # values = {'director': 'unknown_director', 'cast': 'unknown_cast', 'country': 'unknown_country', 'date_added': 'unknown_date_added', 'rating': 'unknown_rating', 'duration': 0}
        # dfnf.fillna(value=values, inplace=True)
        # st.dataframe(dfnf.head(10))

        #Question1
        st.write('### Graphical and non-graphical analysis of categorical values')
        st.write('##### a. Non-graphical Analysis')
        st.code('''df['type'].value_counts()''')
        st.text('''
                Movie      111989
                TV Show     49227
                Name: type, dtype: int64
                ''')
        st.write('##### b. Graphical Analysis')
        st.code('''
                plt.figure(figsize=(10,5))
                sns.countplot(x=df['type'])
                plt.xticks(rotation=45)
                ax=sns.countplot(data=df, x="type")
                ax.bar_label(ax.containers[0])
                ax.set(xlabel = 'Type', ylabel = 'Count')
                plt.show()
                ''')
        plt.figure(figsize=(10,5))
        sns.countplot(x=dfnf['type'])
        plt.xticks(rotation=45)
        ax=sns.countplot(data=dfnf, x="type")
        ax.bar_label(ax.containers[0])
        ax.set(xlabel = 'Type', ylabel = 'Count')
        plt.show()
        st.pyplot(ax.get_figure())
        st.markdown('''
                    <div>
                        <p class='h4'>Insights</p>
                        <ul>
                            <li>The number of movies are higher than the number of TV Shows.</li>
                            <li>Movies dominate the Netflix platform 100% more than the TV Shows.</li>
                        </ul>
                    </div>
                    ''', unsafe_allow_html=True)
        #Question2
        st.write('### Comparison of tv shows vs. movies.')
        st.write('##### a. Top 10 countries with most movies produced')
        st.code('''
                movies = df[(df['type'] == 'Movie') & (df['country'] != 'unknown_country')]
                movies.groupby('country')['title'].nunique().sort_values(ascending = False).head(10)
                ''')
        st.text('''
                country
                United States     2058
                India              893
                United Kingdom     206
                Canada             122
                Spain               97
                Egypt               92
                Nigeria             86
                Indonesia           77
                Turkey              76
                Japan               76
                Name: title, dtype: int64
                ''')
        st.write('##### b. Top 10 countries with most TV Shows produced')
        st.code('''
                tvShows = dfnf.loc[(dfnf['type'] == 'TV Show') & (dfnf['country'] != 'unknown_country')]
                tvShowsdf = tvShows.groupby('country')['title'].nunique().sort_values(ascending = False).head(10)
                ''')
        st.text('''
                country
                United States     760
                United Kingdom    213
                Japan             169
                South Korea       158
                India              79
                Taiwan             68
                Canada             59
                France             49
                Australia          48
                Spain              48
                Name: title, dtype: int64
                ''')
        st.markdown('''
                    <div>
                        <p class='h4'>Insights</p>
                        <ul>
                            <li>United States rank number one in the number of Movies and TV Shows produced around the world.</li>
                            <li>India produces the second highest number of movies whereas United Kingdom in the TV Shows category.</li>
                            <li>Japan produces more TV Shows compared to Movies.</li>
                        </ul>
                    </div>
                    ''', unsafe_allow_html=True)
        #Question3
        st.write('### Best time to launch a TV show')
        st.write('##### Add release week column')
        st.code('''
                date_data = df[df['date_added'] != 'unknown_date_added']
                date_data['release_week'] = pd.to_datetime(date_data['date_added']).apply(lambda x: x.week)
                ''')
        date_data = dfnf[dfnf['date_added'] != 'unknown_date_added']
        date_data['release_week'] = pd.to_datetime(date_data['date_added'], format='mixed').apply(lambda x: x.week)
        st.write('##### a. Best week to release Movies')
        st.code('''
                dd_movies = date_data.loc[date_data['type'] == 'Movie']
                dd_movies.groupby('release_week')['title'].nunique().sort_values(ascending = False).head(5)
                ''')
        dd_movies = date_data.loc[date_data['type'] == 'Movie']
        st.text('''
                release_week
                1     316
                44    243
                40    215
                9     207
                26    195
                Name: title, dtype: int64
                ''')

        st.write('##### b. Best week to release TV Shows')
        st.code('''
                dd_tv_show = date_data.loc[date_data['type'] == 'TV Show']
                dd_tv_show.groupby('release_week')['title'].nunique().sort_values(ascending = False).head(5)''')
        dd_tv_show = date_data.loc[date_data['type'] == 'TV Show']
        st.text('''
                release_week
                27    86
                31    83
                13    76
                44    75
                24    75
                Name: title, dtype: int64
                ''')

        st.write('##### Add release month column')
        st.code('''date_data['release_month'] = pd.to_datetime(date_data['date_added']).apply(lambda x: x.  month)''')
        date_data['release_month'] = pd.to_datetime(date_data['date_added'], format='mixed').apply(lambda x: x.  month)

        st.write('##### c. Best month to release Movies')
        st.code('''
                dd_movies = date_data.loc[date_data['type'] == 'Movie']
                dd_movies.groupby('release_month')['title'].nunique().sort_values(ascending = False)
                ''')
        dd_movies = date_data.loc[date_data['type'] == 'Movie']
        st.code('''
                release_month
                7     565
                4     550
                12    547
                1     546
                10    545
                3     529
                8     519
                9     519
                11    498
                6     492
                5     439
                2     382
                Name: title, dtype: int64
                ''')
        st.write('##### d. Best month to release TV Shows')
        st.code('''
                dd_tvshows = date_data.loc[date_data['type'] == 'TV Show']
                dd_tvshows.groupby('release_month')['title'].nunique().sort_values(ascending = False)
                ''')
        dd_tvshows = date_data.loc[date_data['type'] == 'TV Show']
        st.text('''
                release_month
                12    266
                7     262
                9     251
                6     236
                8     236
                10    215
                4     214
                3     213
                11    207
                5     193
                1     192
                2     181
                Name: title, dtype: int64
                ''')
        st.markdown('''
                    <div>
                        <p class='h4'>Insights</p>
                        <ul>
                            <li>The best week to release Movies is week number 1 whereas best week for TV Show release is week number 27.</li>
                            <li>The best month to release Movies is in July and for the TV Show release is December.</li>
                        </ul>
                    </div>
                    ''', unsafe_allow_html=True)
        #Question 4
        st.write('### Analysis of actors/directors of different types of shows/movies.')
        st.write('##### a. Top ten Actors in Movies or TV Shows')
        st.code('''
                actor = df.loc[df['cast'] != 'unknown_cast']
                actor.groupby(by = ['cast'])['title'].nunique().sort_values(ascending = False).head(10)
                ''')
        st.text('''
                cast
                Anupam Kher         39
                Rupa Bhimani        31
                Takahiro Sakurai    30
                Julie Tejwani       28
                Om Puri             27
                Shah Rukh Khan       26
                Rajesh Kava         26
                Boman Irani         25
                Andrea Libman       25
                Yuki Kaji           25
                Name: title, dtype: int64
                ''')
        st.write('##### b. Top ten Directors in Movies or TV Shows')
        st.code('''
                director = df.loc[df['director'] != 'unknown_director'][['director', 'title']]
                director.groupby('director')['title'].nunique().sort_values(ascending = False).head(10)
                ''')
        st.text('''
                director
                Rajiv Chilaka          22
                Raúl Campos            18
                Jan Suter             18
                Suhas Kadav            16
                Marcus Raboy           16
                Jay Karas              15
                Cathy Garcia-Molina    13
                Jay Chapman            12
                Martin Scorsese        12
                Youssef Chahine        12
                Name: title, dtype: int64
                ''')
        st.markdown('''
                    <div>
                        <p class='h4'>Insights</p>
                        <ul>
                            <li>Anupam Kher is the most appeared actor in the Movies/TV Shows.</li>
                            <li>Rajiv Chilaka is the person who has directed the most number of Movies/TV Shows.</li>
                        </ul>
                    </div>
                    ''', unsafe_allow_html=True)
        #Question 5
        st.write('### More popular or more produced genre of movies')
        st.code('''
                text = df.loc[df['type'] == 'Movie']['listed_in']
                w = WordCloud()
                stop_words = list(w.stopwords)
                custom_stop_words = ['Movies', 'International']
                stop_words = set(stop_words + custom_stop_words)
                wordcloud = WordCloud(collocations = False, background_color = 'white', stopwords = stop_words).generate(' '.join(text.tolist()))

                plt.imshow(wordcloud)
                plt.axis("off")
                plt.show()''')
        text = dfnf.loc[dfnf['type'] == 'Movie']['listed_in']
        w = WordCloud()
        stop_words = list(w.stopwords)
        custom_stop_words = ['Movies', 'International']
        stop_words = set(stop_words + custom_stop_words)
        wordcloud = WordCloud(collocations = False, background_color = 'white', stopwords = stop_words).generate(' '.join(str(t) for t in text))

        plt.imshow(wordcloud)
        plt.axis("off")
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
        st.markdown('''
                    <div>
                        <p class='h4'>Insights</p>
                        <ul>
                            <li>The Drama genre movies are most popular</li>
                            <li>The genres Comedies, Action and Adventure are also popular as well.</li>
                        </ul>
                    </div>
                    ''', unsafe_allow_html=True)
        
        #Question 6
        st.write('### Time Gap Between Movie Release and Netflix Availability')
        st.code('''
                date_data['date_added_ts'] = pd.to_datetime(date_data['date_added'])
                date_data['rel_add_diff'] = date_data['date_added_ts'] - pd.to_datetime(date_data['release_year'].apply(lambda x: '31-12-'+str(x)))
                date_data['rel_add_diff'].mode()
                ''')
        date_data['date_added_ts'] = pd.to_datetime(date_data['date_added'], format='mixed')
        date_data['rel_add_diff'] = date_data['date_added_ts'] - pd.to_datetime(date_data['release_year'].apply(lambda x: '31-12-'+str(x)))
        st.text('''
                0   182 days
                Name: rel_add_diff, dtype: timedelta64[ns]
                ''')
        st.markdown('''
                    <div>
                        <p class='h4'>Insights</p>
                        <ul>
                            <li>A movie is added to the Netflix platform, 182 days after it has been reeased.</li>
                        </ul>
                    </div>
                    ''', unsafe_allow_html=True)
        st.markdown('''
                    <div>
                        <p class='h4'>Recommendations</p>
                        <ol>
                            <li>Focus on Movies: Given that movies dominate the Netflix platform 100% more than TV shows, Netflix should continue to prioritize acquiring and producing high-quality movies to cater to its audience preferences.</li>
                            <li>Release Timing: For movies, the best week to release them is in July, and for TV shows, it's week number 27. Netflix should consider these optimal release timings to maximize viewership and engagement.</li>
                            <li>Geographical Preferences: Understanding regional preferences is crucial. For instance, in India, where movies are highly popular, Netflix should continue to invest in acquiring Indian cinema. In Japan, where TV shows are more favored, Netflix should ensure a diverse selection of popular TV shows to cater to the audience.</li>
                            <li>Genre Preferences: Drama genre movies are the most popular, followed by Comedies, Action, and Adventure. Netflix should focus on acquiring and producing content in these genres to appeal to a wider audience base.</li>
                            <li>Regular Content Updates: Given that a movie is added to the Netflix platform 182 days after its release, Netflix should ensure a consistent and timely addition of new content to keep the platform fresh and engaging for subscribers.</li>
                            <li>Featured Personalities: Anupam Kher and Rajiv Chilaka are prominent figures in the industry. Netflix should consider collaborations or featuring content involving these personalities to attract viewers who appreciate their work.</li>
                        </ol>
                        <p>Overall, Netflix should continue to prioritize acquiring and producing content that aligns with audience preferences, focusing on popular genres, regional content, and timely releases to maintain and grow its subscriber base.</p>
                    </div>
                    ''', unsafe_allow_html=True)
        
        
        
#Aerofit Project
    # elif project == 'Aerofit: Descriptive stats and probablity':
    #     st.write('Aerofit')
    # elif project == 'Walmart: Confidence interval and CLT':
    #     st.write('Walmart project')
    # elif project == 'YULU: Hypothesis testing':
    #     st.write('YULU Project')
    elif project == 'Jamboree education: Linear Regression':
        st.markdown('''
                    <div>
                        <div class='d-flex justify-content-center'>
                            <p class='h2'>Jamboree education: Linear Regression</p>
                        </div>
                        <p class='h4'>Problem Statement</p>
                        <p class='ms-3'>Jamboree, a renowned educational institute assisting students in gaining admission to top international colleges, seeks to enhance its services by offering a probability estimation tool for graduate admissions to IVY league colleges. This tool aims to provide insights into the factors influencing graduate admissions from an Indian perspective and predict an individual's likelihood of admission based on various interrelated factors. The project entails analyzing key factors affecting graduate admissions, understanding their interrelationships, and developing a predictive model to assess an applicant's chances of admission.</p>
                    </div>
''', unsafe_allow_html=True)
        st.write('## Basic Analysis')
        st.write('### Observation of data')
        st.write('Load the data')
        st.code('df = pd.read_csv(r"D:\DSML class\Data\Jamboree_Admission.csv")')
        st.dataframe(dfjb.head())
        st.code('df.shape')
        dfjb.shape
        st.code('df.info()')
        buffer = io.StringIO()
        dfjb.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)
        st.write("Uninique values and it's count unique for all columns")
        st.code('df.nunique()')
        st.text('''
                Serial No.           500
                GRE Score             49
                TOEFL Score           29
                University Rating      5
                SOP                    9
                LOR                    9
                CGPA                 184
                Research               2
                Chance of Admit       61
                dtype: int64
                ''')
        st.write('### Data Processing')
        st.write('Duplicate value check')
        st.code('df[df.duplicated()]')
        dfjb[dfjb.duplicated()]
        st.write('Check missing values')
        st.code('''
                print('Missing Values:')
                df.isnull().sum()
                ''')
        st.text('''
                Missing Values:

                Serial No.           0
                GRE Score            0
                TOEFL Score          0
                University Rating    0
                SOP                  0
                LOR                  0
                CGPA                 0
                Research             0
                Chance of Admit      0
                dtype: int64
                ''')
        st.write('### Droping the row identifier')
        st.write("Serial No. is the row identifier and it's being dropped as it will interfere in the model's performance")
        st.code("df.drop('Serial No.', axis=1, inplace=True)")
        dfjb.drop('Serial No.', axis=1, inplace=True)
        st.write('## Non graphical and graphical analysis of the variable')
        st.write('### Nongraphical Analysis')
        st.write('summary of statistics of numerical columns')
        st.code('df.describe()')
        st.dataframe(dfjb.describe())
        st.write('### Graphical analysis')
        st.write('Plotting the distribution chart for the numercal varaibles')
        st.code('''
                plt.figure(figsize=(15,10))
                plt.subplots_adjust(hspace=0.5)
                
                plt.subplot(3,2,1)
                sns.histplot(df['GRE Score'], kde=True)
                
                plt.subplot(3,2,2)
                sns.histplot(df['TOEFL Score'], kde=True)
                
                plt.subplot(3,2,3)
                sns.histplot(df['University Rating'], kde=True)
                
                plt.subplot(3,2,4)
                sns.histplot(df['SOP'], kde=True)
                
                plt.subplot(3,2,5)
                sns.histplot(df['CGPA'], kde=True)
                
                plt.subplot(3,2,6)
                sns.histplot(data=df, x='Research', kde=True)
                
                plt.show()
                ''')
        plt.figure(figsize=(15,10))
        plt.subplots_adjust(hspace=0.5)

        plt.subplot(3,2,1)
        sns.histplot(dfjb['GRE Score'], kde=True)

        plt.subplot(3,2,2)
        sns.histplot(dfjb['TOEFL Score'], kde=True)

        plt.subplot(3,2,3)
        sns.histplot(dfjb['University Rating'], kde=True)

        plt.subplot(3,2,4)
        sns.histplot(dfjb['SOP'], kde=True)

        plt.subplot(3,2,5)
        sns.histplot(dfjb['CGPA'], kde=True)

        plt.subplot(3,2,6)
        sns.histplot(data=dfjb, x='Research', kde=True)

        st.pyplot()
        st.write('### Correlation Analysis of Admission Variables')
        st.code('''
                corr_mat = df.corr()
                plt.figure(figsize=(10,8))
                sns.heatmap(corr_mat, annot=True, linewidths=0.5, cmap='coolwarm')
                plt.title('Correlation Matrix')
                plt.show()
                ''')
        corr_mat = dfjb.corr()
        plt.figure(figsize=(10,8))
        sns.heatmap(corr_mat, annot=True, linewidths=0.5, cmap='coolwarm')
        plt.title('Correlation Matrix')
        st.pyplot()
        
        st.write('### Exploring Interrelations Among Independent Variables')
        st.write('Removing the Target variable chance of admit')
        st.code('''
                df_independent = df.drop('Chance of Admit ', axis=1)
                independent_corr_mat = df_independent.corr()
                plt.figure(figsize=(10,8))
                sns.heatmap(independent_corr_mat, annot=True, cmap='coolwarm')
                plt.title('Independent variable Correlation Matrix')
                plt.show()
                ''')
        df_independent = dfjb.drop('Chance of Admit ', axis=1)
        independent_corr_mat = df_independent.corr()
        plt.figure(figsize=(10,8))
        sns.heatmap(independent_corr_mat, annot=True, cmap='coolwarm')
        plt.title('Independent variable Correlation Matrix')
        st.pyplot()
        st.write('### Linear Regression using Statsmodel Library')
        st.write('Defining independent variables(Features) and dependent variable(Target)')
        st.code('''
                X = df.drop('Chance of Admit ', axis=1)
                y = df['Chance of Admit ']
                ''')
        st.write('Adding constant to independent variable whci is required for stasmodel')
        st.code('X = sm.add_constant(X)')
        st.write('Fit the linear regression model')
        st.code('model = sm.OLS(y, X).fit()')
        st.write('Summary of the regression model')
        st.code('print(model.summary())')
        X = dfjb.drop('Chance of Admit ', axis=1)
        y = dfjb['Chance of Admit ']
        X = sm.add_constant(X)
        model = sm.OLS(y, X).fit()
        st.text('''OLS Regression Results                            
==============================================================================
Dep. Variable:       Chance of Admit    R-squared:                       0.822
Model:                            OLS   Adj. R-squared:                  0.819
Method:                 Least Squares   F-statistic:                     324.4
Date:                Mon, 19 Feb 2024   Prob (F-statistic):          8.21e-180
Time:                        21:31:18   Log-Likelihood:                 701.38
No. Observations:                 500   AIC:                            -1387.
Df Residuals:                     492   BIC:                            -1353.
Df Model:                           7                                         
Covariance Type:            nonrobust                                         
=====================================================================================
                        coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------
const                -1.2757      0.104    -12.232      0.000      -1.481      -1.071
GRE Score             0.0019      0.001      3.700      0.000       0.001       0.003
TOEFL Score           0.0028      0.001      3.184      0.002       0.001       0.004
University Rating     0.0059      0.004      1.563      0.119      -0.002       0.013
SOP                   0.0016      0.005      0.348      0.728      -0.007       0.011
LOR                   0.0169      0.004      4.074      0.000       0.009       0.025
CGPA                  0.1184      0.010     12.198      0.000       0.099       0.137
Research              0.0243      0.007      3.680      0.000       0.011       0.037
==============================================================================
Omnibus:                      112.770   Durbin-Watson:                   0.796
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              262.104
Skew:                          -1.160   Prob(JB):                     1.22e-57
Kurtosis:                       5.684   Cond. No.                     1.30e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.3e+04. This might indicate that there are
strong multicollinearity or other numerical problems.
                ''')
        st.markdown('''
                    <div>
                        <p class='h4'>Insights</p>
                        <ol>
                            <li><p class='h5'>R^2 and Adjusted R^2:</p>
                                <ul>
                                    <li>R^2: R-squared is 0.822 indicating 82.2% of the variability of dependent variable, Chance of Admit is explained by the independednt variable in the model.</li>
                                    <li>Adjusted R^2: Adjusted R-squared is 0.819 which is slightly lesser than the R-squared, indicating that the additional predictors do not significantly contribute to the explanatory poer of the model.</li>
                               </ul>
                            </li>
                            <li><p class='h5'>Coeffcients:</p>
                                <ul>
                                    <li>Constant(Intercept): It's -1.2757 which represents the value of the dependent variable when all the independent variables are zero.</li>
                                    <li>GRE, TOEFL, LOR, CGPA and Research coefficents are all positive and the pValue is greater than 0.05 which shows that these variables are statistically sigificant and are associated with the increase in probablity of admission.</li>
                                    <li>University rating and SOP coefficients are positive but are not statistically significant as pValue is higher than 0.05 which shows that these variables do not have significant impact on the probablity of admission.</li>
                               </ul>
                            </li>
                        </ol>
                    </div>
                    ''', unsafe_allow_html=True)
        st.write('### Assumptions of Linear Regression')
        st.write('#### Multicolinearity check by VIF score')
        st.code('''
                vif = pd.DataFrame()
                vif['Features'] = X.columns
                vif['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
                vif''')
        vif = pd.DataFrame()
        vif['Features'] = X.columns
        vif['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
        st.dataframe(vif)
        st.code('''
                vif = vif.drop(0)
                vif['VIF'] = [variance_inflation_factor(X.values, i) for i in range(1, X.shape[1])]
                vif
                ''')
        vif = vif.drop(0)
        vif['VIF'] = [variance_inflation_factor(X.values, i) for i in range(1, X.shape[1])]
        st.dataframe(vif)
        st.write('#### Mean of residuals')
        st.code('''
                residuals = model.resid
                mean_of_residuals = np.mean(residuals)
                print('Mean of Residuals:', mean_of_residuals)
                ''')
        residuals = model.resid
        mean_of_residuals = np.mean(residuals)
        st.text('Mean of Residuals: 4.0534242629064463e-16')
        st.markdown('''
                    <div>
                        <p class='h4'>Insights</p>  
                        <ul>
                            <li>The mean of residual is 4.0534242629064463e-16 which means that the residuals is centered around zero which means that the residual errors are evenly distributed above and below the regression line.</li>
                        </ul>
                    </div>
                    ''', unsafe_allow_html=True)
        st.write('#### Linearity of variables')
        st.code('''
                sns.residplot(x=model.fittedvalues, y=residuals, lowess=True, line_kws={'color': 'red', 'lw': 1})
                plt.xlabel("Fitted values")
                plt.ylabel("Residuals")
                plt.title("Residual Plot")
                plt.show()
                ''')
        sns.residplot(x=model.fittedvalues, y=residuals, lowess=True, line_kws={'color': 'red', 'lw': 1})
        plt.xlabel("Fitted values")
        plt.ylabel("Residuals")
        plt.title("Residual Plot")
        st.pyplot()
        st.write('#### Test for Homoscedasticity')
        st.code('''
                name = ['F statistic', 'p-value']
                test = sms.het_goldfeldquandt(residuals, X)
                print('F ststistic:', test[0])
                print('p-value:', test[1])
                ''')
        st.text('''
                F ststistic: 0.4494044330462436
                p-value: 0.9999999995739839
                ''')
        st.markdown('''
                    <div>
                        <p class='h4'>Insights</p>  
                        <ul>
                            <li>The p-value is 1 and hence we fail to reject the null hypothesis of Homoscedasticity test which is the varicance of the residuals is constant across oservations.</li>
                        </ul>
                    </div>
                    ''', unsafe_allow_html=True)
        st.write('#### Normality of Residuals (Q-Q Plot)')
        st.write('Plotting the histogram of residuals')
        st.code('''
                plt.figure(figsize=(10,5))
                sns.histplot(x=residuals, kde=True)
                plt.title('Histplot for residuals')
                plt.show()
                ''')
        plt.figure(figsize=(10,5))
        sns.histplot(x=residuals, kde=True)
        plt.title('Histplot for residuals')
        st.pyplot()
        st.write('Plotting the QQ plot fot the residuals')
        st.code('''
                fig, ax = plt.subplots(figsize=(6,4))
                _, (__, ___, r) = sp.probplot(residuals, plot=ax, fit=True)
                r**2
                ''')
        fig, ax = plt.subplots(figsize=(6,4))
        _, (__, ___, r) = sp.probplot(residuals, plot=ax, fit=True)
        r**2
        st.pyplot()
        st.markdown('''
                    <div>
                        <p class='h4'>Insights</p>  
                        <ul>
                            <li>The high R2 score of approximately 0.92 which is close to 1 suggests that the residuals exhibit a high degree of normality supporting the normality assumption of the linear regression model.</li>
                            <li>The histplot of the residuals also supports the normality of the linear regression model.</li>
                        </ul>
                    </div>
                    ''', unsafe_allow_html=True)
        st.write('### Model Evaluation')
        st.write('Predicting the target variable')
        st.code('y_pred = model.predict(X)')  
        st.write('Model evaluation metrics')
        st.code('''
                mae = mean_absolute_error(y, y_pred)
                rmse = mean_squared_error(y, y_pred, squared=False)
                r2 = r2_score(y, y_pred)

                n = len(y)
                d = X.shape[1]
                
                adjusted_r2 = 1 - (1-r2)*(n-1)/(n-d-1)
                
                print("Mean Absolute Error (MAE):", mae)
                print("Root Mean Squared Error (RMSE):", rmse)
                print("R-squared Score:", r2)
                print("Adjusted R-squared Score:", adjusted_r2)
                ''')
        st.text('''
                Mean Absolute Error (MAE): 0.042572390149733436
                Root Mean Squared Error (RMSE): 0.05950420877764953
                R-squared Score: 0.8219007395178417
                Adjusted R-squared Score: 0.8189989185731222
                ''')
        st.markdown('''
                    <div>
                        <p class='h4'>Insights</p> 
                        <p class='h5'>Mean Absolute error:</p> 
                        <ul>
                            <li>The mean absolute error is 0.0426 which shows that the model's predictions are off by approximately 0.0426 units from the actaul values</li>
                        </ul>
                        <p class='h5'>Root mean squared error:</p> 
                        <ul>
                            <li>RMSE is the measure of the spred of the residuals around the resgression line and the average magnitude of the residuals is approximately 0.0595 units.</li>
                        </ul>
                        <p class='h5'>R-squared score:</p> 
                        <ul>
                            <li>The R2 score is approximately 0.8219 which indicates that approximately 82.19% of the variability in the dependent variable is explained by the independent variable in the model.</li>
                        </ul>
                        <p class='h5'>Adjusted R-squared score:</p> 
                        <ul>
                            <li>The adjusted R-squared score, which accounts for the number of predictors in the model, is approximately 0.8190. It is slightly lower than the R-squared score but still indicates a good fit of the model.</li>
                        </ul>
                    </div>
                    ''', unsafe_allow_html=True)
        st.write('### Lasso and Ridge regression using sklearn')
        st.write('Split the data into train and test sets')
        st.code('X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)')
        st.write('#### Lasso Regression')
        st.code('''
                lasso_model = Lasso(alpha=0.01)
                lasso_model.fit(X_train, y_train)
                lasso_y_pred = lasso_model.predict(X_test)
                ''')
        st.write('#### Ridge Regression')
        st.code('''
                ridge_model = Ridge(alpha=0.01)
                ridge_model.fit(X_train, y_train)
                ridge_y_pred = ridge_model.predict(X_test)
                ''')
        st.write('Model evaluation')
        st.code('''
                def evaluate_model(yactual, ypred):
                    mae = mean_absolute_error(y, y_pred)
                    rmse = mean_squared_error(y, y_pred, squared=False)
                    r2 = r2_score(y, y_pred)
                    return mae, rmse, r2
                ''')
        st.code('''
                lasso_metrics = evaluate_model(y_test, lasso_y_pred)
                ridge_metrics = evaluate_model(y_test, ridge_y_pred)
                
                print("Lasso Regression Metrics:")
                print("Mean Absolute Error (MAE):", lasso_metrics[0])
                print("Root Mean Squared Error (RMSE):", lasso_metrics[1])
                print("R-squared Score:", lasso_metrics[2])

                print("Ridge Regression Metrics:")
                print("Mean Absolute Error (MAE):", ridge_metrics[0])
                print("Root Mean Squared Error (RMSE):", ridge_metrics[1])
                print("R-squared Score:", ridge_metrics[2])
                ''')
        st.text('''
                Lasso Regression Metrics:
                Mean Absolute Error (MAE): 0.042572390149733436
                Root Mean Squared Error (RMSE): 0.05950420877764953
                R-squared Score: 0.8219007395178417

                
                Ridge Regression Metrics:
                Mean Absolute Error (MAE): 0.042572390149733436
                Root Mean Squared Error (RMSE): 0.05950420877764953
                R-squared Score: 0.8219007395178417''')
        st.markdown('''
                    <div>
                        <p class='h4'>Insights</p>  
                        <ul>
                            <li>Lasso and Ridge regression models has produced identical results and the metrics suggest thatboth Lasso and Ridge regression models perform similarly with no noticeable improvement over the standard linear regression model.</li>
                        </ul>
                    </div>
                    ''', unsafe_allow_html=True)
        st.markdown('''
                    <div>
                        <p class='h3'>Actionable insights and recommendations</p>  
                        <p>Based on the analysis conducted on the dataset and the performance of various regression models, here are some actionable insights and recommendations:</p>
                        <ul>
                            <li>The features such as GRE Score, TOEFL Score, CGPA, LOR, and Research experience showed significant impact on the chance of admission.</li>
                            <li>Prioritize and focus on improving features that have a significant positive impact on the chance of admission.</li>
                            <li>Students aiming for top colleges abroad should aim to improve their performance in these areas.</li>
                            <li>While the Statement of Purpose (SOP) and Letter of Recommendation (LOR) were included in the model, they did not show significant impact on the chance of admission in the analysis. However, it's important to note that these components are still crucial in the application process and can provide valuable insights into a candidate's character and potential.</li>
                            <li>Candidates with research experience tend to have a slightly higher chance of admission according to the model. Encouraging students to participate in research opportunities during their undergraduate studies could enhance their profiles.</li>
                            <li>Providing students with resources and support to improve their profiles for admissions to top colleges abroad. This could include test preparation assistance for exams like GRE and TOEFL, guidance on crafting strong personal statements and recommendation letters, and opportunities for research experience.</li>
                        </ul>
                        <p>By implementing these insights and recommendations, Jamboree can further enhance its support for students aiming to secure admission to Ivy League colleges and other top universities abroad.</p>
                    </div>
                    ''', unsafe_allow_html=True)
    # elif project == 'LoanTap: Logistic Regression':
    #     st.write('LoanTap project')
    

