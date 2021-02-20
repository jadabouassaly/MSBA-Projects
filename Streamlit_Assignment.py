import streamlit as st
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import statsmodels

#loading logos and datasets from google drive
url = 'https://drive.google.com/file/d/1i4utk3ZsVTd9u7PmypHsUrZu2_4K-51c/view?usp=sharing'
image1 = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]

url = 'https://drive.google.com/file/d/1Dp-eWbCcYmNGq4j5dor9Zgh6oRTBKWdD/view?usp=sharing'
image2 = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]

url = 'https://drive.google.com/file/d/1yU8vVr3MFXegrWdnJzwYt75jxH0JauBK/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df_suicides = pd.read_csv(path)


url = 'https://drive.google.com/file/d/1O40dU9C-8eTO4DlMmsdGpn2nKadsHaJB/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df_earthquakes = pd.read_csv(path)
df_earthquakes['Date'] = pd.to_datetime(df_earthquakes['Date'],utc=True)
df_earthquakes['year'] = pd.DatetimeIndex(df_earthquakes['Date']).year


#inserting the images
col1, mid, col2 = st.beta_columns([1,2,1])
with col1:
    st.image(image1,width=200)
with col2:
    st.image(image2,width=200)

#adding few spaces
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

#writing my title and my name centered
st.markdown("<h1 style='text-align: center'>Streamlit Assignment</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center'>Jad Abou Assaly</h2>", unsafe_allow_html=True)

#adding few spaces
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

#writing an overview
expander = st.beta_expander("Overview")
expander.write("In this page we will be exploring 2 datasets: the world yearly Earthquakes and the world  yearly suicides. Please follow the steps in the sidebar.")


#adding few spaces
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

#writing on the sidebar
option = st.sidebar.selectbox( 'What Dataset Would You Like to visualize?',
        ('Earthquakes', 'Suicides'))




if option == "Earthquakes":
    mode = st.sidebar.selectbox( 'How would you like to visualize the Earthquakes?',
            ('Animation Mode', 'Yearly Mode'))

    st.write('You are visualizing Earthquakes in ', mode)

    if mode == "Animation Mode":
        fig = px.scatter_geo(df_earthquakes, lon="Longitude",lat="Latitude", color="Magnitude",
                         hover_name="Magnitude Type",
                         #size="Magnitude",
                         animation_frame="year",
                         projection="natural earth")
        fig.update_layout(title='Earthquakes Graph Animation')
        st.plotly_chart(fig)
        left_column, right_column = st.beta_columns(2)
        pressed = left_column.button('More Info')
        if pressed:
            right_column.write("This is an animation showing the location of all Earthquakes on a yearly basis. Hover over the points for additional info.")


    else:
        year_options=df_earthquakes.year.unique()
        year = st.selectbox('Which year do you want to explore?', year_options)
        rslt_df = df_earthquakes[df_earthquakes['year'] == year]
        fig = go.Figure(data=go.Scattergeo(
            lon = rslt_df['Longitude'],
            lat = rslt_df['Latitude'],
            text = rslt_df['Magnitude'],
            mode = 'markers',
            marker_color = rslt_df['Magnitude'],
            ))
        fig.update_layout(title=f'Earthquakes in {year}',geo_scope="world",)
        st.plotly_chart(fig)
        left_column, right_column = st.beta_columns(2)
        pressed = left_column.button('More Info')
        if pressed:
            right_column.write(f"This is the location of all Earthquakes in {year}. Hover over the points for location and magnitude info.")



if option == "Suicides":
    year_options=df_suicides.year.unique()
    year = st.sidebar.selectbox('Which year do you want to explore?', year_options)
    st.write(f'Exploring suicides in {year}')
    rslt_df=df_suicides[df_suicides['year']==year]

    #adding Scatter Plot button
    left_column, right_column = st.beta_columns(2)
    pressed = left_column.button('Scatter Plot')
    right_column.write("Scatter plot representing the relation between the GDP per capita in USD and the suicide rate per 100,000 of the population. Hover over the points for more info.")
    if pressed:
        fig=px.scatter(rslt_df,x = 'suicides_100k_pop', y = 'gdp_per_capita_us')
        st.plotly_chart(fig)

    #adding trendline button
    left_column, right_column = st.beta_columns(2)
    pressed = left_column.button('Trendline')
    right_column.write("Trendline representing the relation between the GDP per capita in USD and the suicide rate per 100,000 of the population. Hover over the points for more info.")
    if pressed:
        fig=px.scatter(rslt_df,x = 'suicides_100k_pop', y = 'gdp_per_capita_us',trendline="ols")
        st.plotly_chart(fig)

    #adding "by continent" button
    left_column, right_column = st.beta_columns(2)
    pressed = left_column.button('By Continent')
    right_column.write("Scatter plot representing the relation between the GDP per capita in USD and the suicide rate per 100,000 of the population grouped by continent. Hover over the points for more info.")
    if pressed:
        fig=px.scatter(rslt_df,x = 'suicides_100k_pop', y = 'gdp_per_capita_us',color='continent')
        st.plotly_chart(fig)

    #adding "by gender" button
    left_column, right_column = st.beta_columns(2)
    pressed = left_column.button('By Gender')
    right_column.write("Scatter plot representing the relation between the GDP per capita in USD and the suicide rate per 100,000 of the population grouped by gender. Hover over the points for more info.")
    if pressed:
        fig=px.scatter(rslt_df,x = 'suicides_100k_pop', y = 'gdp_per_capita_us',color='continent',symbol='sex')
        st.plotly_chart(fig)
