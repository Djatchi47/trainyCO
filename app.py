import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration de la page
st.set_page_config(page_title="Analyse COVID-19 Mexique", layout="wide")

st.title("📊 Tableau de Bord - Analyse Pandémie COVID-19")
st.markdown("Cette application analyse les facteurs de risque liés au COVID-19.")

# 1. Chargement des données
@st.cache_data # Pour éviter de recharger le fichier à chaque clic
def load_data():
    df = pd.read_csv('df_nettoye_test_projet.csv')
    # Petit nettoyage rapide
    df['DEATH'] = (df['DATE_DIED'] != '9999-99-99').astype(int)
    return df

df = load_data()

# 2. Barre latérale pour la navigation
menu = st.sidebar.selectbox("Navigation", ["Analyse Exploratoire", "Modèle de Prédiction"])

if menu == "Analyse Exploratoire":
    st.header("Analyse des Données")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Répartition par Genre")
        fig, ax = plt.subplots()
        sns.countplot(data=df, x='SEX', hue='SEX', palette='pastel', ax=ax, legend=False)
        ax.set_xticklabels(['Femme (1)', 'Homme (2)'])
        st.pyplot(fig)

    with col2:
        st.subheader("Distribution des Âges")
        fig, ax = plt.subplots()
        sns.histplot(df['AGE'], bins=30, kde=True, ax=ax)
        st.pyplot(fig)

elif menu == "Modèle de Prédiction":
    st.header("Prédire le Risque Patient")
    st.write("Entrez les informations du patient pour évaluer le risque.")
    
    # Formulaire de saisie
    age = st.slider("Âge du patient", 0, 100, 30)
    sex = st.selectbox("Genre", ["Femme", "Homme"])
    pneu = st.checkbox("Pneumonie ?")
    diab = st.checkbox("Diabète ?")
    hip = st.checkbox("hypertension ?")
    
    
    if st.button("Prédire le Risque"):
        # Ici on pourrait appeler le modèle entraîné à l'étape 5
        if age > 60 or pneu:
            st.error("⚠️ Ce patient est considéré à HAUT RISQUE.")
        else:
            st.success("✅ Ce patient est considéré à BAS RISQUE.")