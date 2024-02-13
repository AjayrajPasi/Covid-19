import streamlit as st
import pandas as pd 
import plotly.express as px 

# Importing data
df=pd.read_csv('covid19.csv')

# Designing page
st.set_page_config(page_title='COVID-19 ANALYSIS', layout='wide', page_icon="random")
st.title("CORONAVIRUS CASES ANALYSIS")
st.divider()
st.sidebar.divider()
selected_tab = st.sidebar.radio("DASHBOARD", ['Overview','Analysis','Conclusion'])
st.sidebar.divider()
st.sidebar.subheader('Symptoms of COVID-19')
st.sidebar.write('Fever or chills')
st.sidebar.write('Cough')
st.sidebar.write('Muscle or body aches')
st.sidebar.divider()
st.sidebar.link_button('REGISTER FOR VACCINATION','https://www.cowin.gov.in/')
st.sidebar.link_button('MONEY DONATION','https://pmcares.gov.in/en/')
st.sidebar.divider()


# Dersign overview
if selected_tab == 'Overview':
    c1,c2 = st.columns(2)
    with c1:
        st.image('covid.png')
    with c2:
        st.subheader('What is COVID-19?')
        st.write('COVID-19 (coronavirus disease 2019) is a disease caused by a virus named SARS-CoV-2. It can be very contagious and spreads quickly. Over one million people have died from COVID-19 in the United States.')
        st.write('COVID-19 most often causes respiratory symptoms that can feel much like a cold, the flu, or pneumonia. COVID-19 may attack more than your lungs and respiratory system. Other parts of your body may also be affected by the disease. Most people with COVID-19 have mild symptoms, but some people become severely ill.')
    st.divider()
    st.subheader('How does COVID-19 spread?')
    st.write('COVID-19 spreads when an infected person breathes out droplets and very small particles that contain the virus. Other people can breathe in these droplets and particles, or these droplets and particles can land on their eyes, nose, or mouth. In some circumstances, these droplets may contaminate surfaces they touch.')
    st.write('Anyone infected with COVID-19 can spread it, even if they do NOT have symptoms.')
    st.write('The risk of animals spreading the virus that causes COVID-19 to people is low. The virus can spread from people to animals during close contact. People with suspected or confirmed COVID-19 should avoid contact with animals.')
    st.divider()
    c3,c4,c5,c6 = st.columns(4)
    with c3:
        st.link_button('Advice for Public (WHO)','https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public')
    with c4:
        st.link_button('Situation Reports','https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports')
    with c5:
        st.link_button('Governments Action','https://www.mohfw.gov.in/')
    with c6:
        st.link_button('Worls Report','https://data.who.int/dashboards/covid19/cases?n=c')
    st.divider()
    st.subheader('DATASET')
    df
    df.describe()

elif selected_tab == 'Analysis':
    # Overall top 10 country graph
    st.subheader('Top 20 Country with Confirmed Cases')
    dt=df[['Country/Region','Confirmed']].head(20)
    ch1=px.bar(dt,x='Country/Region',y='Confirmed',color_discrete_sequence=px.colors.qualitative.Set1)
    st.plotly_chart(ch1, use_container_width=True)
    st.divider()

    # WHO regin Wise bar graph
    st.subheader('Top country With most cases by WHO region')
    selected_region = st.selectbox("select WHO region", df['WHO Region'].unique())
    a = df[df['WHO Region'] == selected_region][['Country/Region','Confirmed']]
    ch2 = px.bar(data_frame=a, x='Country/Region', y='Confirmed',color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(ch2, use_container_width=True)
    st.divider()

    # New cases and recovered cases graph
    st.subheader('Recovery Cases vs New Cases')
    selected_reg = st.selectbox("select Region", df['WHO Region'].unique())
    b = df[df['WHO Region'] == selected_reg][['Country/Region','Recovered','New cases']].head(5)
    ch3=px.line(b,x='Country/Region',y='Recovered')
    ch3.add_scatter(x=b['Country/Region'],y=b['New cases'],mode='lines')
    st.plotly_chart(ch3, use_container_width=True)
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        # pie chart of male female
        st.subheader("region wise increase")
        ch5 = px.pie(names=df['WHO Region'].value_counts().index, values=df['WHO Region'].value_counts().values,hole=0.3, color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(ch5, use_container_width=True)
        st.divider()
    
    with col2:
        # pie chart
        st.subheader('Percentage of new Cases per week')
        d=df[['Country/Region']].head(20)
        st.area_chart(d)
        st.divider()

    # Scatter plot
    st.subheader('Scatter plot of per 100 cases')
    selected_re = st.selectbox("select Region scatter", df['WHO Region'].unique())
    c = df[df['WHO Region'] == selected_re][['Country/Region','Deaths / 100 Cases','Recovered / 100 Cases','Deaths / 100 Recovered']].head(10)
    st.scatter_chart(c,x='Country/Region',y='Deaths / 100 Recovered',color='Deaths / 100 Cases',size='Recovered / 100 Cases')
    st.divider()

elif selected_tab == 'Conclusion':
    st.markdown("Highest number of cases are from United States, Brazil and India") 
    st.markdown("Most number of cases are from American WHO Region")  
    st.markdown("Recovery is less than new cases")  
    st.markdown("Europe and Africa are effecte most")   
    st.markdown("Percentage of increase per week is growing every week") 
    st.markdown("Country with high population are most effected")
