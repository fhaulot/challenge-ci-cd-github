import os
import streamlit as st

# Récupère l'environnement depuis la variable d'env (définie par ton workflow CD)
env = os.getenv("APP_ENV", "Dev")

# Définition des couleurs et titres
settings = {
    "Dev": {"color": "green", "title": "🚀 Dev Environment"},
    "QA": {"color": "yellow", "title": "🔍 QA Environment"},
    "Prod": {"color": "red", "title": "🔥 Production Environment"},
}

# Sélection des paramètres selon l'environnement courant
current = settings.get(env, settings["Dev"])

# Applique un style coloré dans un container
st.markdown(
    f"""
    <div style='background-color:{current["color"]};
                padding:50px;
                border-radius:15px;
                text-align:center;'>
        <h1>{current["title"]}</h1>
    </div>
    """,
    unsafe_allow_html=True
)