import streamlit as st
import pandas as pd


    


def Page_1():
    st.subheader("Monterey")
    # Add an image
    


    sub_page = st.sidebar.selectbox("Select a sub-page", ["Sub-page 1", "Sub-page 2"])
    if sub_page == "Sub-page 1":
        st.write("This is sub-page 1.")
        video_url = "https://www.youtube.com/watch?v=1ehjVGvjQDw"
        st.video(video_url)
    elif sub_page == "Sub-page 2":
        st.write("This is sub-page 2.")

def Page_2():   
    st.subheader("Seaside")
    sub_page = st.sidebar.selectbox("Select a sub-page", ["Sub-page 1", "Sub-page 2"])
    if sub_page == "Sub-page 1":
        st.write("This is sub-page 1.")
        video_url = "https://www.youtube.com/watch?v=aYZV_y3PaYk"
        st.video(video_url)
    elif sub_page == "Sub-page 2":
        st.write("This is sub-page 2.")

def Page_3():
    st.subheader("Marina")
    sub_page = st.sidebar.selectbox("Select a sub-page", ["Sub-page 1", "Sub-page 2"])
    if sub_page == "Sub-page 1":
        st.write("This is sub-page 1.")
        video_url = "https://www.youtube.com/watch?v=vxt5wGaLJRI"
        st.video(video_url)
    elif sub_page == "Sub-page 2":
        st.write("This is sub-page 2.")

def Page_4():
    st.subheader("Carmel")
    sub_page = st.sidebar.selectbox("Select a sub-page", ["Sub-page 1", "Sub-page 2"])
    if sub_page == "Sub-page 1":
        st.write("This is sub-page 1.")
        video_url = "https://www.youtube.com/watch?v=sW45LPQ07TQ"
        st.video(video_url)
    elif sub_page == "Sub-page 2":
        st.write("This is sub-page 2.")


def Page_5():
    st.subheader("Salinas")
    sub_page = st.sidebar.selectbox("Select a sub-page", ["Sub-page 1", "Sub-page 2"])
    if sub_page == "Sub-page 1":
        st.write("This is sub-page 1.")
        video_url = "https://www.youtube.com/watch?v=apBi8B1UbuE"
        st.video(video_url)
    elif sub_page == "Sub-page 2":
        st.write("This is sub-page 2.")
        image_url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.forbes.com%2Fsites%2Ftomsanderson%2F2023%2F05%2F17%2Flionel-messis-fc-barcelona-return-has-a-set-date-reports%2F&psig=AOvVaw0wBuHjb4git8y0IeTL172w&ust=1684560878819000&source=images&cd=vfe&ved=0CA0QjRxqFwoTCIiy2LnUgP8CFQAAAAAdAAAAABAD"
        st.image(image_url, caption="Monterey Image", use_column_width=True)



def main():
    st.set_page_config(page_title="Atmospheric Rivers", page_icon=":guardsman:", layout="wide")
    st.title("Coastal Resiliency and the 2023 Atmospheric Rivers")
    # Adding a logo
    logo_url = 'https://images.unsplash.com/photo-1501594907352-04cda38ebc29?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80'
    st.sidebar.image(logo_url, width=50)
    pages = {"Monterey":Page_1,"Seaside":Page_2,"Marina":Page_3,"Carmel":Page_4,"Salinas":Page_5}
    choice = st.sidebar.selectbox("Select a city", list(pages.keys()))
    pages[choice]()

if __name__ == '__main__':
    main()
