import streamlit as st
import pandas as pd


    

def Page_1():
    st.subheader("Monterey")
    sub_page = st.sidebar.selectbox("Select a sub-page", ["Sub-page 1", "Sub-page 2"])
    if sub_page == "Sub-page 1":
        st.write("This is sub-page 1.")
    elif sub_page == "Sub-page 2":
        st.write("This is sub-page 2.")

def Page_2():   
    st.subheader("Seaside")
    sub_page = st.sidebar.selectbox("Select a sub-page", ["Sub-page 1", "Sub-page 2"])
    if sub_page == "Sub-page 1":
        st.write("This is sub-page 1.")
    elif sub_page == "Sub-page 2":
        st.write("This is sub-page 2.")

def Page_3():
    st.subheader("Marina")
    sub_page = st.sidebar.selectbox("Select a sub-page", ["Sub-page 1", "Sub-page 2"])
    if sub_page == "Sub-page 1":
        st.write("This is sub-page 1.")
    elif sub_page == "Sub-page 2":
        st.write("This is sub-page 2.")

def Page_4():
    st.subheader("Carmel")
    sub_page = st.sidebar.selectbox("Select a sub-page", ["Sub-page 1", "Sub-page 2"])
    if sub_page == "Sub-page 1":
        st.write("This is sub-page 1.")
    elif sub_page == "Sub-page 2":
        st.write("This is sub-page 2.")


def Page_5():
    st.subheader("Salinas")
    sub_page = st.sidebar.selectbox("Select a sub-page", ["Sub-page 1", "Sub-page 2"])
    if sub_page == "Sub-page 1":
        st.write("This is sub-page 1.")
    elif sub_page == "Sub-page 2":
        st.write("This is sub-page 2.")



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