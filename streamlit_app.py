import streamlit as st
from modules.corrector import Corrector
from modules.highlighter import Highlighter

st.title("ProGrammar - AI Grammar Correction & Highlighting")

input_text = st.text_area("Enter text to be corrected:", height=200, value="He are moving here.")

if st.button("Correct Text"):
    if input_text:
        corrector = Corrector(use_gpu=False)
        highlighter = Highlighter()

        corrected_text, edits = corrector.correct(input_text)
        highlighted_text = highlighter.highlight(input_text, edits)

        st.subheader("Corrected Text")
        st.write(f"[Correction]  {corrected_text}")

        st.subheader("Edits")
        st.write(f"[Edits]  {edits}")

        st.subheader("Highlighted Errors")
        st.write(f"[Edits]  {highlighted_text}")
