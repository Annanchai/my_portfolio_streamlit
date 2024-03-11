import streamlit as st
import pandas as pd
import io
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout='wide')

# Link to bootstrap cdn
st.markdown('''
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
            ''', unsafe_allow_html=True
            )
#Data
dfnf = pd.read_csv('./data/netflix.csv')
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
st.sidebar.markdown('''<p class='fw-bold'>My Projects</p>''', unsafe_allow_html=True)
project = st.sidebar.selectbox(
    'Select an option to view the project',
    ('Netflix: Data Exploration and visualization', 'Aerofit: Descriptive stats and probablity', 'Walmart: Confidence interval and CLT', 'YULU: Hypothesis testing', 'Jamboree education: Linear Regression', 'LoanTap: Logistic Regression' ), label_visibility='collapsed'
)


#Tabs Section
tab1, tab2 = st.tabs(['About Me', 'Projects'])

with tab1:
    if intro == 'Introduction':
        st.markdown('''
                    <div class='p-1 d-flex flex-row-reverse'>
                        <a class = 'p-2' href=https://www.hackerrank.com/profile/shajeesh>Hackerrank</a>
                        <a class = 'p-2' href=https://github.com/Annanchai>Github</a>
                        <a class='p-2' href=https://www.linkedin.com/in/shajeesh-radhakrishnan>Linkedin</a>
                    </div>
                    <div class='card p-5'>
                        <p class='h4'>About me</p>
                        <p class='p-2'>Hello! I'm Shajeesh Radhakrishnan, a passionate data analyst with a background in Biochemistry and a current pursuit of an MSc in Computer Science: Artificial Intelligence and Machine Learning. Born and raised in Coimbatore, Tamilnadu, and originally from Malappuram, Kerala, I bring a unique blend of cultural diversity and analytical skills to my work.</p>
                        <p class='h4'>Data Science Skills</p>  
                        <ul class='p-2'>
                            <li>Programming Languages: Python</li>
                            <li>Tools: Tableau, SQL</li>
                            <li>Libraries: Pandas, Numpy, Seaborn, Matplotlib</li>
                            <li>Statistics: Probability and Statistics</li>
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
        st.code('''df['cast'] = df['cast'].str.split(',')
df['listed_in'] = df['listed_in'].str.split(',')
df['director'] = df['director'].str.split(',')''')
        st.code('''df = df.explode('cast', ignore_index = True)
df = df.explode('listed_in', ignore_index = True)
df = df.explode('director', ignore_index = True)''')
        dfnf['cast'] = dfnf['cast'].str.split(',')
        dfnf['listed_in'] = dfnf['listed_in'].str.split(',')
        dfnf['director'] = dfnf['director'].str.split(',')
        st.code('df.head(10)')
        st.dataframe(dfnf.head(10))
        st.write('### Handling null values')
        st.code('''values = {'director': 'unknown_director', 'cast': 'unknown_cast', 'country': 'unknown_country', 'date_added': 'unknown_date_added', 'rating': 'unknown_rating', 'duration': 0}
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
        st.dataframe(dfnf['type'].value_counts())
        st.write('##### b. Graphical Analysis')
        st.code('''plt.figure(figsize=(10,5))
sns.countplot(x=df['type'])
plt.xticks(rotation=45)
ax=sns.countplot(data=df, x="type")
ax.bar_label(ax.containers[0])
ax.set(xlabel = 'Type', ylabel = 'Count')
plt.show()''')
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
        st.code('''movies = df[(df['type'] == 'Movie') & (df['country'] != 'unknown_country')]
                movies.groupby('country')['title'].nunique().sort_values(ascending = False).head(10)''')
        movies = dfnf[(dfnf['type'] == 'Movie') & (dfnf['country'] != 'unknown_country')]
        moviesdf = movies.groupby('country')['title'].nunique().sort_values(ascending = False).head(10)
        st.dataframe(moviesdf)
        st.write('##### b. Top 10 countries with most TV Shows produced')
        tvShows = dfnf.loc[(dfnf['type'] == 'TV Show') & (dfnf['country'] != 'unknown_country')]
        tvShowsdf = tvShows.groupby('country')['title'].nunique().sort_values(ascending = False).head(10)
        st.dataframe(tvShowsdf)
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
        st.dataframe(dd_movies.groupby('release_week')['title'].nunique().sort_values(ascending = False).head(5))

        st.write('##### b. Best week to release TV Shows')
        st.code('''
                dd_tv_show = date_data.loc[date_data['type'] == 'TV Show']
                dd_tv_show.groupby('release_week')['title'].nunique().sort_values(ascending = False).head(5)''')
        dd_tv_show = date_data.loc[date_data['type'] == 'TV Show']
        st.dataframe(dd_tv_show.groupby('release_week')['title'].nunique().sort_values(ascending = False).head(5))

        st.write('##### Add release month column')
        st.code('''date_data['release_month'] = pd.to_datetime(date_data['date_added']).apply(lambda x: x.  month)''')
        date_data['release_month'] = pd.to_datetime(date_data['date_added'], format='mixed').apply(lambda x: x.  month)

        st.write('##### c. Best month to release Movies')
        st.code('''
                dd_movies = date_data.loc[date_data['type'] == 'Movie']
                dd_movies.groupby('release_month')['title'].nunique().sort_values(ascending = False)
                ''')
        dd_movies = date_data.loc[date_data['type'] == 'Movie']
        st.dataframe(dd_movies.groupby('release_month')['title'].nunique().sort_values(ascending = False))
        st.write('##### d. Best month to release TV Shows')
        st.code('''
                dd_tvshows = date_data.loc[date_data['type'] == 'TV Show']
                dd_tvshows.groupby('release_month')['title'].nunique().sort_values(ascending = False)
                ''')
        dd_tvshows = date_data.loc[date_data['type'] == 'TV Show']
        st.dataframe(dd_tvshows.groupby('release_month')['title'].nunique().sort_values(ascending = False))
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
        st.dataframe(pd.DataFrame({'cast': ['Anupam Kher', 'Rupa Bhimani', 'Takahiro Sakurai', 'Julie Tejwani', 'Om Puri', 'Shah Rukh Khan', 'Rajesh Kava ', 'Boman Irani ', 'Andrea Libman', 'Yuki Kaji  '], 'title': [39, 31,30,28,27,26,26,25,25,25] }))
        st.write('##### b. Top ten Directors in Movies or TV Shows')
        st.code('''
                director = df.loc[df['director'] != 'unknown_director'][['director', 'title']]
                director.groupby('director')['title'].nunique().sort_values(ascending = False).head(10)
                ''')
        director = dfnf.loc[dfnf['director'] != 'unknown_director'][['director', 'title']]
        director.groupby('director')['title'].nunique().sort_values(ascending = False).head(10)

    elif project == 'Aerofit: Descriptive stats and probablity':
        st.write('Aerofit')
    elif project == 'Walmart: Confidence interval and CLT':
        st.write('Walmart project')
    elif project == 'YULU: Hypothesis testing':
        st.write('YULU Project')
    elif project == 'Jamboree education: Linear Regression':
        st.write('Jamboree Project')
    elif project == 'LoanTap: Logistic Regression':
        st.write('LoanTap project')
    

