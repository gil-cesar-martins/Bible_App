# Core Packages
import streamlit as st
import streamlit.components.v1 as stc

# EDA Packages
import pandas as pd
import neattext.functions as nfx 

# Data Viz Packages
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import altair as alt

# Utils
@st.cache_resource
def load_bible(data):
    df = pd.read_csv(data)
    return df 

def main():
    
    st.title("📖 Estudo Bíblico - Streamlit 📖")
    menu = ["Home", "Multiverse", "Sobre"]
    
    df = load_bible("data\KJV_BIble.csv")
    
    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Home":
        st.subheader("Buscar um único versículo")
        st.dataframe(df)
        book_list = df['book'].unique().tolist()
        book_name = st.sidebar.selectbox("Book", book_list)
        chapter = st.sidebar.number_input("Chapter",1)
        verse = st.sidebar.number_input("Verse",1)
        bilble_df = df['book'] == book_name
    elif choice == "Multiverse":
        st.subheader("Buscar múltiplos versículos")
    else:
        st.subheader("Sobre o App")
    
if __name__ == '__main__':
    main()
