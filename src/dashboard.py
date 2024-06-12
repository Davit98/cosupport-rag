import streamlit as st
from PIL import Image

from src.rag import rag_chain


def set_layout() -> None:
    """
    Sets the Streamlit layout.

    Returns
    -------
    None
    """
    st.set_page_config(page_title="CoSupport RAG Demo", page_icon=Image.open("favicon.ico"), layout="wide")
    st.title("Welcome to Train Review Bot 🚆")
    st.write(
        "This bot has learned about several reviews of various UK train companies and is aware of customers' honest "
        "opinions. You can ask different questions to learn about what people think about train companies in the UK "
        "and what are their main complaints. "
        "  \n"
        "Example queries:"
        "  \n1. What are the main topics of complaints?"
        "  \n2. Provide examples of good customer reviews."
    )

    if "button_clicked" not in st.session_state:
        st.session_state.button_clicked = False

    text_input = st.text_area(label="Enter your query here", height=100)

    if st.button(label="Submit") or st.session_state.button_clicked:
        st.session_state.button_clicked = True
        answer = rag_chain.invoke(text_input)
        st.markdown('-------')
        st.write(f'**Answer:** {answer}')


if __name__ == '__main__':
    try:
        set_layout()
    except Exception as e:
        st.error(f'The website is unable to respond. An error occurred due to: {e}', icon="🚨")
