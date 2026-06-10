import streamlit as st
from deep_translator import GoogleTranslator

st.title("Language Translation Tool")

text = st.text_area("Enter text to translate")

languages = {
    "English": "en",
    "Malayalam": "ml",
    "Hindi": "hi",
    "Tamil": "ta",
    "French": "fr",
    "Spanish": "es"
}

source_language = st.selectbox("Source Language", list(languages.keys()))
target_language = st.selectbox("Target Language", list(languages.keys()))

if st.button("Translate"):
    if text:
        translated = GoogleTranslator(
            source=languages[source_language],
            target=languages[target_language]
        ).translate(text)

        st.success(translated)