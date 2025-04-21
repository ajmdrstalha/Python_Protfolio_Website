import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="MY PORTFOLIO", page_icon=":tada:", layout="wide")

def load_lottie_url(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# ✅ Updated working Lottie link
lottie_coding = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_0yfsb3a1.json")
#image upload for project 1
image1 = Image.open("images/project1.png")
#image upload for project 2
image2 = Image.open("images/project2.png")


# ----- Header Section ----
st.subheader("Welcome to my portfolio")
st.title("AJ MD RS TALHA")
st.write("DevOps Engineer")
st.write("[LinkedIn >](https://www.linkedin.com/in/ajmdrstalha/)")

#------About Section ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write(
            """
            I am a DevOps Engineer with a passion for automating and optimizing processes. 
            I have experience in cloud computing, CI/CD, and infrastructure as code. 
            I am always eager to learn new technologies and improve my skills.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


# ----- Projects ----
    
with st.container():
    st.write("---")
    st.header("Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image1, caption="Project 1 Image")

    with text_column:
        st.subheader("Project 1")
        st.write(
            """
             Discover how to automate OLT configuration with Python and Streamlit, all wrapped up in a Docker container to minimize manual errors and save you precious time
            """
        )
        st.markdown("[GitHub Link >](https://github.com/ajmdrstalha/Epon-Command-Generator)")
    
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image2, caption="Project 2 Image")

    with text_column:
        st.subheader("Project 2")
        st.write(
            """
              Configured Cisco routers and switches with VLANs, inter-VLAN routing, EtherChannel, and STP load-balancing. 
              Secured the network using port security and SSH, and optimized IP addressing through SLSM, VLSM, and other techniques.
            """
        )    
        st.markdown("[File Link >](https://drive.google.com/drive/folders/1NzzuxnJufYZXCIGWM7CDsw-z65xyFdAR)")
  