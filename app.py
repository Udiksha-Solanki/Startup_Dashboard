import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#to reduce sidespace and page title
st.set_page_config(layout='wide',page_title='StartUp Analysis')

df=pd.read_csv('startup_clean.csv')
df['date']=pd.to_datetime(df['date'],errors='coerce')
df['month']=df['date'].dt.month
df['year']=df['date'].dt.year
def load_overall_analysis():
    st.title('Overall Analysis')
    col1,col2,col3,col4=st.columns(4)

    #total invested amount
    total=round(df['amount'].sum())
    with col1:
        st.metric('Total',str(total)+' Cr')
    #max amount infused in a startup
    max_funding=df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    with col2:
        st.metric('Maximum Funding', str(max_funding) + ' Cr')
    #avg ticket size
    avg_funding=df.groupby('startup')['amount'].sum().mean()
    with col3:
        st.metric('Average Funding', str(round(avg_funding)) + ' Cr')
    #total funded startups
    num_startups=df['startup'].nunique()
    with col4:
        st.metric('Total Funded Startups',num_startups)
    st.header('MoM graph')
    selected_option=st.selectbox('Select Type',['Total','Count'])#(Count=Funding done in how many startups)
    if selected_option=='Total':

        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')
    fig3, ax3 = plt.subplots()
    ax3.plot(temp_df['x_axis'],temp_df['amount'])
    st.pyplot(fig3)



def load_investor_details(investor):
    st.title(investor)
    #load the recent 5 investments of the investor
    last5_df=df[df['investors'].str.contains(investor)].head(10)[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('MOST RECENT INVESTMENTS')
    st.dataframe(last5_df)
    col1,col2=st.columns(2)
    with col1:
        # BIGGEST INVESTMENTS
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(
        ascending=False).head()
        st.subheader('BIGGEST INVESTMENTS')
        # st.dataframe(bigdf)
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)
    with col2:
        vertical_series=df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader('SECTORS INVESTED IN')
        # st.dataframe(bigdf)
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_series,labels=vertical_series.index,autopct="%0.01f%%")
        st.pyplot(fig1)
    df['year'] = df['date'].dt.year
    year_series=df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
    st.subheader('YOY INVESTMENTS')
    # st.dataframe(bigdf)
    fig2, ax2 = plt.subplots()
    ax2.plot(year_series.index,year_series.values)
    st.pyplot(fig2)
#DATA CLEANING
#df['Investors Name']=df['Investors Name'].fillna('Undisclosed')
l1=sorted(df['startup'].unique().tolist())
l2=sorted(set(df['investors'].str.split(',').sum()))
#st.dataframe(df)
st.sidebar.title('Startup Funding Analysis!')
option=st.sidebar.selectbox('Select one option from below: ',['Overall Analysis','Startup','Investor'])


if option=='Overall Analysis':
    #st.title('Overall Analysis')
    #btn0=st.sidebar.button('SHOW OVERALL ANALYSIS')
    #if btn0:
    load_overall_analysis()

elif option=='Startup':
    st.sidebar.selectbox('Select Startup',l1)

    st.title('Startup Analysis')
    btn1 = st.sidebar.button('Find Startup Details')
else:
    selected_investor=st.sidebar.selectbox('Select Investor',l2)


    btn2 = st.sidebar.button('Find Investors Details')

    if btn2:
        load_investor_details(selected_investor)

    #st.title('Investor Analysis')


