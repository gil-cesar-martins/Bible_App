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
        #st.dataframe(df)
        book_list = df['book'].unique().tolist()
        book_name = st.sidebar.selectbox("Book", book_list)
        chapter = st.sidebar.number_input("Chapter",1)
        verse = st.sidebar.number_input("Verse",1)
        bilble_df = df[df['book'] == book_name]
        #st.dataframe(bilble_df)
        
        # Layout
        c1,c2 = st.columns([2,1])
        
        # Single Verse layout
        with c1:
            try:
                selected_passage = bilble_df[(bilble_df['chapter'] == chapter) & (bilble_df['verse'] == verse)]
                #st.write(selected_passage)
                passage_details = "{} Chapter::{} Verse::{}".format(book_name,chapter,verse)
                st.info(passage_details)
                passage = "{}".format(selected_passage['text'].values[0])
                st.write(passage)
            except:
                st.warning("Book out of range")
            
        with c2:
            st.success("Verse of the Day.")
        # Verse of the Day
        
    elif choice == "Multiverse":
        st.subheader("Buscar múltiplos versículos")
    else:
        st.subheader("Sobre o App")
    
if __name__ == '__main__':
    main()
