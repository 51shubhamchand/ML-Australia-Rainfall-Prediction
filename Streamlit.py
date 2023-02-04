import pickle
import bz2
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import warnings
warnings.filterwarnings("ignore")

### Setting the background image
def add_bg_from_url():
    st.markdown(
         f"""<style>.stApp {{
             background-image: url("https://24.media.tumblr.com/41c5486b80a5fd3e0da67e419884f902/tumblr_mjghxdAx1Q1rbz9cko1_500.gif");
             background-attachment: fixed;
             background-size: cover
         }}</style>""",
         unsafe_allow_html=True)
add_bg_from_url()

### Unloading necessary data files
model = pickle.load(bz2.BZ2File('model_rain_prediction.pkl', 'rb'))
orig_data=pd.read_csv('weatherAUS.csv')
label_encoded_data=pd.read_csv('label_encoding_mapping.csv')
scaled_data=pd.read_csv('scaling_mapping.csv')

### Setting Header and Text
st.markdown("<h1 style='text-align: center; color: White;'>Australia Rainfall Predictor</h1>", unsafe_allow_html=True)
st.text('It uses Machine Learning Algorithm to predict the rainfall.')
st.text("Please enter the values below:")

### Taking input from webpage
a=st.date_input('Date', datetime.date(2019, 7, 6))
b=st.selectbox('Location', (orig_data['Location'].dropna().sort_values().unique().tolist()))
c=st.number_input('MinTemp', 0.0)
d=st.number_input('MaxTemp', 0.0)
e=st.number_input('Rainfall', 0.0)
f=st.number_input('Evaporation', 0.0)
g=st.number_input('Sunshine', 0.0)
h=st.selectbox('WindGustDir', (orig_data['WindGustDir'].dropna().sort_values().unique().tolist()))
i=st.number_input('WindGustSpeed', 0.0)
j=st.selectbox('WindDir9am', (orig_data['WindDir9am'].dropna().sort_values().unique().tolist()))
k=st.selectbox('WindDir3pm', (orig_data['WindDir3pm'].dropna().sort_values().unique().tolist()))
l=st.number_input('WindSpeed9am', 0.0)
m=st.number_input('WindSpeed3pm', 0.0)
n=st.number_input('Humidity9am', 0.0)
o=st.number_input('Humidity3pm', 0.0)
p=st.number_input('Pressure9am', 0.0)
q=st.number_input('Pressure3pm', 0.0)
r=st.selectbox('Cloud9am', (orig_data['Cloud9am'].dropna().sort_values().unique().tolist()))
s=st.selectbox('Cloud3pm', (orig_data['Cloud3pm'].dropna().sort_values().unique().tolist()))
t=st.number_input('Temp9am', 0.0)
u=st.number_input('Temp3pm', 0.0)
v=st.selectbox('RainToday', (orig_data['RainToday'].dropna().sort_values().unique().tolist()))

### Creating a list using entered data
input_data=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v]

### Handling DATE column
a=pd.to_datetime(input_data[0], format = '%Y-%m-%d').month

### Handling LABEL ENCODING of data
label_encoding=pd.read_csv('label_encoding_mapping.csv').drop('Unnamed: 0', axis=1)
b=label_encoding[label_encoding['Location']==input_data[1]]['Location1'].unique()[0]
c=label_encoding[label_encoding['WindGustDir']==input_data[7]]['WindGustDir1'].unique()[0]
d=label_encoding[label_encoding['WindDir9am']==input_data[9]]['WindDir9am1'].unique()[0]
e=label_encoding[label_encoding['WindDir3pm']==input_data[10]]['WindDir3pm1'].unique()[0]

### Handling RAIN TODAY column
f= 1 if (input_data[21]=='Yes') else 0

### Handling SCALING of data
scaling=pd.read_csv('scaling_mapping.csv').drop('Unnamed: 0', axis=1)
c1=(a-scaling[scaling['Column']=='Date']['Mean'].values[0])/scaling[scaling['Column']=='Date']['SD'].values[0]
c2=(b-scaling[scaling['Column']=='Location']['Mean'].values[0])/scaling[scaling['Column']=='Location']['SD'].values[0]
c3=(input_data[2]-scaling[scaling['Column']=='MinTemp']['Mean'].values[0])/scaling[scaling['Column']=='MinTemp']['SD'].values[0]
c4=(input_data[3]-scaling[scaling['Column']=='MaxTemp']['Mean'].values[0])/scaling[scaling['Column']=='MaxTemp']['SD'].values[0]
c5=(input_data[4]-scaling[scaling['Column']=='Rainfall']['Mean'].values[0])/scaling[scaling['Column']=='Rainfall']['SD'].values[0]
c6=(input_data[5]-scaling[scaling['Column']=='Evaporation']['Mean'].values[0])/scaling[scaling['Column']=='Evaporation']['SD'].values[0]
c7=(input_data[6]-scaling[scaling['Column']=='Sunshine']['Mean'].values[0])/scaling[scaling['Column']=='Sunshine']['SD'].values[0]
c8=c
c9=(input_data[8]-scaling[scaling['Column']=='WindGustSpeed']['Mean'].values[0])/scaling[scaling['Column']=='WindGustSpeed']['SD'].values[0]
c10=d
c11=e
c12=(input_data[11]-scaling[scaling['Column']=='WindSpeed9am']['Mean'].values[0])/scaling[scaling['Column']=='WindSpeed9am']['SD'].values[0]
c13=(input_data[12]-scaling[scaling['Column']=='WindSpeed3pm']['Mean'].values[0])/scaling[scaling['Column']=='WindSpeed3pm']['SD'].values[0]
c14=(input_data[13]-scaling[scaling['Column']=='Humidity9am']['Mean'].values[0])/scaling[scaling['Column']=='Humidity9am']['SD'].values[0]
c15=(input_data[14]-scaling[scaling['Column']=='Humidity3pm']['Mean'].values[0])/scaling[scaling['Column']=='Humidity3pm']['SD'].values[0]
c16=(input_data[15]-scaling[scaling['Column']=='Pressure9am']['Mean'].values[0])/scaling[scaling['Column']=='Pressure9am']['SD'].values[0]
c17=(input_data[16]-scaling[scaling['Column']=='Pressure3pm']['Mean'].values[0])/scaling[scaling['Column']=='Pressure3pm']['SD'].values[0]
c18=int(input_data[17])
c19=int(input_data[18])
c20=(input_data[19]-scaling[scaling['Column']=='Temp9am']['Mean'].values[0])/scaling[scaling['Column']=='Temp9am']['SD'].values[0]
c21=(input_data[20]-scaling[scaling['Column']=='Temp3pm']['Mean'].values[0])/scaling[scaling['Column']=='Temp3pm']['SD'].values[0]
c22=f

### Saving data in array
output_test = np.array([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22]).reshape(1,22)
output_test2= pd.DataFrame(output_test, columns=['Date', 'Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation',
       'Sunshine', 'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm',
       'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
       'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am',
       'Temp3pm', 'RainToday'])

### Prediction of data
if st.button("Check if it will rain tomorrow or not", key="predict"):
    output = model.predict(output_test2)
    if (output==1):
        st.warning('It will rain tomorrow')
    else:
        st.success('It will not rain tomorrow')


