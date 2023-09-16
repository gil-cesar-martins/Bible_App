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

def main():
    st.title("📖 Estudo Bíblico - Streamlit 📖")
    menu = ["Home", "Multiverse", "Sobre"]
    
    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Home":
        st.subheader("Buscar um único versículo")
    elif choice == "Multiverse":
        st.subheader("Buscar múltiplos versículos")
    else:
        st.subheader("Sobre o App")
    
if __name__ == '__main__':
    main()
