# Core Packages
import streamlit as st
import streamlit.components.v1 as stc

# EDA Packages
import pandas as pd
import neattext.functions as nfx 
import random

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

from utils import HTML_RANDOM_TEMPLATE

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
            st.success("Verse of the Day")
            chapter_list = range(10)
            verse_list = range(20)
            ch_choice = random.choice(chapter_list)
            vs_choice = random.choice(verse_list)
            random_book_name = random.choice(book_list)
            
            #st.write("Livro: {}, Cap: {}, Vers: {}".format(random_book_name,ch_choice,vs_choice))
            rand_bilble_df = df[df['book'] == random_book_name]
           
            try:
                randomly_selected_passage = rand_bilble_df[(rand_bilble_df['chapter'] == ch_choice) & (rand_bilble_df['verse'] == vs_choice)]
                my_text = randomly_selected_passage['text'].values[0]
            except:
                my_text = rand_bilble_df[(rand_bilble_df['chapter'] == 1) & (rand_bilble_df['verse'] == 1)]['text'].values[0]
              
            stc.html(HTML_RANDOM_TEMPLATE.format(my_text), height=300)
            
        # Search topic/term
        search_term = st.text_input("Term/Topic")
        with st.expander("View Results"):
            retrived_df = df[df['text'].str.contains(search_term)]
            st.dataframe(retrived_df[['book','chapter','verse','text']])
                    
    elif choice == "Multiverse":
        st.subheader("Buscar múltiplos versículos")
    else:
        st.subheader("Sobre o App")
    
if __name__ == '__main__':
    main()
