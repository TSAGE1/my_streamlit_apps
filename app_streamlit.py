import streamlit as st
import random

# Utilisation du décorateur @st.cache_data pour mémoriser les résultats
@st.cache_data
def generate_random_value(x): 
    return random.uniform(0, x)

# Générer des valeurs aléatoires
a = generate_random_value(10) 
b = generate_random_value(20)

# Affichage des valeurs
st.write(a) 
st.write(b)
