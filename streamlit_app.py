import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.write("Let's figure out where it saves an uploaded file.")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes = uploaded_file.getvalue()
    st.write(f"Uploaded a file with {len(bytes)} length.")
