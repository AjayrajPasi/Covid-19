import streamlit as st
import pandas as pd 
import plotly.express as px 

# Importing data
df=pd.read_csv('covid19.csv')
df1=pd.read_csv('covid-19.csv')
df2=pd.read_csv('test.csv')

# Designing page
st.set_page_config(page_title='COVID-19 ANALYSIS', layout='wide', page_icon="random")
st.title("CORONAVIRUS CASES ANALYSIS")
st.divider()
st.sidebar.divider()
selected_tab = st.sidebar.radio("DASHBOARD", ['Overview','World Wide Analysis','Country Wise Analysis','Conclusion'])
st.sidebar.divider()
st.sidebar.subheader('Symptoms of COVID-19')
st.sidebar.write('Fever or chills')
st.sidebar.write('Cough')
st.sidebar.write('Muscle or body aches')
st.sidebar.divider()
st.sidebar.link_button('REGISTER FOR VACCINATION','https://www.cowin.gov.in/')
st.sidebar.link_button('MONEY DONATION','https://pmcares.gov.in/en/')
st.sidebar.divider()

# Design overview
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
    st.subheader(' FIRST DATASET')
    df
    st.divider()
    st.subheader('SECOND DATASET')
    df1
    

elif selected_tab == 'World Wide Analysis':
    # Overall top 10 country graph
    st.subheader('Top 20 Country with Corona Cases')
    dad=df[['Country/Region','TotalCases']]
    dad.sort_values('TotalCases',inplace=True,ascending=False)
    dt=dad[['Country/Region','TotalCases']].head(20)
    ch1=px.bar(dt,x='Country/Region',y='TotalCases',color_discrete_sequence=px.colors.qualitative.Set1)
    st.plotly_chart(ch1, use_container_width=True)
    st.divider()

    # Continent Wise bar graph
    st.subheader('Top country With most cases')
    selected_region = st.selectbox("select Continent", df['Continent'].unique())
    a = df[df['Continent'] == selected_region][['Country/Region','TotalCases']]
    a.sort_values('TotalCases',inplace=True,ascending=False)
    ch2 = px.bar(data_frame=a, x='Country/Region', y='TotalCases',color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(ch2, use_container_width=True)
    st.divider()

    # New cases and recovered cases graph
    st.subheader('Continent wise cases info')
    selected_reg = st.selectbox("select One Continent", df['Continent'].unique())
    b = df[df['Continent'] == selected_reg][['Country/Region','TotalDeaths','TotalRecovered','ActiveCases']]
    ch3=px.bar(b,x='Country/Region',y=['TotalDeaths','TotalRecovered','ActiveCases'])
    st.plotly_chart(ch3, use_container_width=True)
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        # pie chart
        st.subheader("Covid-19 cases")
        ch5 = px.pie(df2,names='Continent', values='Cases',hole=0.3, color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(ch5, use_container_width=True)
        st.divider()
    
    with col2:
        # pie chart
        st.subheader("Recovered Cases")
        ch6 = px.pie(df2,names='Continent', values='Recovered', color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(ch6, use_container_width=True)
        st.divider()

    # Area chart
    st.subheader('Active VS Death cases')
    cd=df2[['Continent','Deaths','ActiveCases']]
    st.scatter_chart(df2,x='Continent',y=['Deaths','ActiveCases'])
    st.divider()

elif selected_tab == 'Country Wise Analysis':
    st.subheader('Country Wise Analysis')
    selected_country = st.selectbox("select Country", df1['Country'].unique())
    st.divider()
    cty = df1[df1['Country'] == selected_country][['date','total_cases','total_deaths','reproduction_rate','total_tests','total_vaccinations','positive_rate']]
    cn1,cn2 = st.columns(2)
    with cn1:
        st.subheader('No of Cases')
        an1 = px.line(data_frame=cty, x='date', y='total_cases',color_discrete_sequence=px.colors.qualitative.Set1)
        st.plotly_chart(an1, use_container_width=True)
    with cn2:
        st.subheader('Cases Positive rate')
        an2 = px.line(data_frame=cty, x='date', y='positive_rate',color_discrete_sequence=px.colors.qualitative.Set1)
        st.plotly_chart(an2, use_container_width=True)
    st.divider()
    
    cn3,cn4 = st.columns(2)
    with cn3:
        st.subheader('No of death')
        an3 = px.line(data_frame=cty, x='date', y='total_deaths',color_discrete_sequence=px.colors.qualitative.Set2)
        st.plotly_chart(an3, use_container_width=True)
    with cn4:
        st.subheader('Reproduction rate')
        an4 = px.line(data_frame=cty, x='date', y='reproduction_rate',color_discrete_sequence=px.colors.qualitative.Set2)
        st.plotly_chart(an4, use_container_width=True)
    st.divider()

    cn5,cn6 = st.columns(2)
    with cn5:
        st.subheader('No of Tests')
        an5 = px.line(data_frame=cty, x='date', y='total_tests',color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(an5, use_container_width=True)
    with cn6:
        st.subheader('No of Vaccination')
        an6 = px.line(data_frame=cty, x='date', y='total_vaccinations',color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(an6, use_container_width=True)
    st.divider()

# Conclusion
elif selected_tab == 'Conclusion':
    d1=df['Population'].sum()
    d2=df['TotalTests'].sum()
    d3=df['TotalCases'].sum()
    d4=df['TotalRecovered'].sum()
    d5=df['TotalDeaths'].sum()
    d6=df['ActiveCases'].sum()

    # Overall Total
    st.subheader('Total Numbers')
    cl1,cl2,cl3 = st.columns(3)
    with cl1:
        st.metric('Total Population',d1,delta='6.32 B')
    with cl2:
        st.metric('Total Tests',d2,delta='26.78 M')
    with cl3:
        st.metric('Total no cases',d3,delta='1.91 M',delta_color='inverse')       

    cl4,cl5,cl6, = st.columns(3)
    with cl4:
        st.metric('Total Recovered',d4,delta='1.20 M')
    with cl5:
        st.metric('Total death',d5,delta='0.71 M',delta_color='inverse')      
    with cl6:
       st.metric('Total Active Cases',d6,delta='5.67 M') 
    st.divider()

    st.subheader('Graphical Representation')
    # Total representation chart
    ddt1={'Totals':['Population','Tests','Cases'],'Values':[d1,d2,d3]}
    ddt2={'Totals':['Recovered','Deaths','Active Cases'],'Values':[d4,d5,d6]}

    cal1,cal2 = st.columns(2)
    with cal1:
        cch1=px.bar(ddt1,x='Values',y='Totals',orientation='h',color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(cch1, use_container_width=True)

    with cal2:
        cch2=px.bar(ddt2,x='Values',y='Totals',orientation='h',color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(cch2, use_container_width=True)
    st.divider()

    # Final Conclusion
    ccl1,ccl2 = st.columns(2)
    with ccl1:
        st.subheader('Final Conclusion')
        st.markdown(" * Highest number of cases are from United States, Brazil and India") 
        st.markdown(" * Most number of cases are from American Continent")  
        st.markdown(" * Recovery is faster and more than new cases")  
        st.markdown(" * North America and Asia are effected the most")   
        st.markdown(" * Asia is recovering fast followed by North America") 
        st.markdown(" * North America suffered most followed by Asia")
    with ccl2:
        st.subheader('Take Care')
        st.image('safe.jpg')
    st.divider()

    
