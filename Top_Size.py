import streamlit as st
##streamlit run Top_Size.py
st.title ("Women Top - Size Guide")
#Add image
##pip install Pillow
from PIL import Image
img = Image.open("Top Size pic.png")
st.image(img,width=350)
#Add text
st.text("Available Sizes")
st.text("X-small")
st.text("Small")
st.text("Medium")
st.text("Large")
st.text("X-large")
#Add checkbox
if st.checkbox("Select/Unselect"):
    st.text("Selection Ready")
###Radio button
status = st.radio("Select Chest (inches): ", ('31-32.5', '32.5-34' , '34-37' , '37-40.5' , '40.5-42.5'))
status1 = st.radio("Select Waist (inches): ", ('23-24.5', '24.5-27' , '27-29.5' , '29.5-32.5' , '32.5-36'))
if (status == '31-32.5' and status1 == '23-24.5'):
    st.info ("X-small")
elif (status == '32.5-34' and status1 == '24.5-27'):
    st.info ("Small")
elif (status == '34-37' and status1 == '27-29.5'):
    st.info ("Medium")
elif (status == '37-40.5' and status1 == '29.5-32.5'):
    st.info ("Large")
elif (status == '40.5-42.5' and status1 == '32.5-36'):
    st.info ("X-large")
elif (status == '31-32.5' and status1 == '32.5-36'):
    st.error ("Custom made")
elif (status == '31-32.5' or status == '32.5-34' or status == '34-37' or status == '37-40.5' or status == '40.5-42.5' and status1 == '23-24.5'):
    st.error ("Custom made")
elif (status == '31-32.5' or status == '32.5-34' or status == '34-37' or status == '37-40.5' or status == '40.5-42.5' and status1 == '24.5-27'):
    st.error ("Custom made")
elif (status == '31-32.5' or status == '32.5-34' or status == '34-37' or status == '37-40.5' or status == '40.5-42.5' and status1 == '27-29.5'):
    st.error ("Custom made")
elif (status == '31-32.5' or status == '32.5-34' or status == '34-37' or status == '37-40.5' or status == '40.5-42.5' and status1 == '29.5-32.5'):
    st.error ("Custom made")
elif (status == '31-32.5' or status == '32.5-34' or status == '34-37' or status == '37-40.5' or status == '40.5-42.5' and status1 == '32.5-36'):
    st.error ("Custome made")


