import streamlit as st

st.set_page_config(layout='wide')

# Link to bootstrap cdn
st.markdown('''
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
            ''', unsafe_allow_html=True
            )


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
    ('Introduction', 'Previous Experience'), label_visibility='collapsed'
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
    elif intro == 'Previous Experience':
        st.write('This is experience page')

with tab2:
    if project == 'Netflix: Data Exploration and visualization':
        st.write('Netflix Project')
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
    

