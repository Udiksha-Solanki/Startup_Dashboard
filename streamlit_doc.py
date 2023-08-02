import streamlit as st
import pandas as pd
import time

# Text Utility
st.title('Startup Dashboard')
# st.header('I am learning streamlit')
# st.subheader('And I am loving it!')
st.subheader('By Uddu!')
st.subheader("Stay Tuned")
st.write("I am Udiksha Solanki soon joining FAANG as a Data Scientist !")
# 3 level heading by using triple hash
# single and double level hash means heading
# - is a list in a markdown
st.markdown("""
### My Favourite Companies
- Google
- Microsoft
- Amazon
- Meta
""")

st.code("""
def func(input):
    return func**2

x=func(2)    
""")

st.latex('x^2 +y^2 +2 =0')

# DISPLAY ELEMENTS
df = pd.DataFrame({
    'name': ['Uddu', 'Urru', 'Madhu'],
    'marks': [50, 60, 70],
    'package': [80, 25, 50]

})
st.dataframe(df)

st.metric('Revenue', 'Rs 3l', '3%')
st.metric('Loss Incurred', 'Rs 20000', '-0.5%')

st.json({
    'name': ['Uddu', 'Urru', 'Madhu'],
    'marks': [50, 60, 70],
    'package': [80, 25, 50]

})

# DISPLAY MEDIA

# COMPUTER VISION RELATED TASK
# IMAGE PROCESSING

# st.image('pic.jpg')
# st.video('abc.m4v')
# st.audio('filename')

# CREATING LAYOUTS

# SIDEBARS

st.sidebar.image('pic.jpg')
col1, col2 = st.columns(2)

with col1:
    st.image('pic.jpg')

with col2:
    st.image('pic.jpg')

# SHOWING STATUS

st.error('Login Failed')
st.success('Login Successful')
st.info("Designed and developed by Uddu")
st.warning("Stay away from toxic people like my ex lol")
# bar=st.progress(0)
for i in range(1, 101):
    time.sleep(0.1)
    # bar.progress(i)

# TAKING USER INPUT
email1 = st.text_input('enter email')
num = st.number_input('Enter age')
st.date_input('Enter dob')


email=st.text_input('Enter Email')
password=st.text_input('Enter Password')
gender=st.selectbox('Select Gender',['Male','Female','Others'])
btn=st.button('Login')
if btn:
    if email=='udikshasolanki2000@gmail.com' and password=='1234':
        st.success('Login Successful')
        st.balloons()
        st.write(gender)
    else:
        st.error('Login Failed')


file=st.file_uploader('Upload a CSV File')
if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df.describe())