import streamlit as st
import assistant as ai

st.set_page_config(page_title="AI Coding Assistant", layout="wide")

st.title("👨‍💻 Local AI Coding Assistant")
st.caption("Running completely offline using Google Gemma 4 on your laptop")

st.sidebar.header("Features")
feature = st.sidebar.radio(
    "Choose a Task:",
    ["Code Generation", "Code Explanation", "Bug Detection", "Code Conversion", "Documentation Generator", "Unit Test Generator"]
)

user_input = st.text_area("Paste your prompt or code snippet here:", height=200)

target_lang = ""
if feature == "Code Conversion":
    target_lang = st.sidebar.text_input("Target Language (e.g., Java, C++):", "Java")

if st.button("Run Assistant"):
    if not user_input.strip():
        st.warning("Please enter some text or code first!")
    else:
        with st.spinner("Gemma 4 is processing locally..."):
            if feature == "Code Generation":
                st.code(ai.generate_code(user_input))
            elif feature == "Code Explanation":
                st.markdown(ai.explain_code(user_input))
            elif feature == "Bug Detection":
                st.markdown(ai.detect_bugs(user_input))
            elif feature == "Code Conversion":
                st.code(ai.convert_code(user_input, target_lang))
            elif feature == "Documentation Generator":
                st.markdown(ai.generate_docs(user_input))
            elif feature == "Unit Test Generator":
                st.code(ai.generate_tests(user_input))
