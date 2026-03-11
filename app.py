import streamlit as st
from agent import ask_agent

st.title("Monday.com Business Intelligence Agent")

question = st.text_input("Ask a business question about deals or work orders")

if question:
    response, actions = ask_agent(question)

    st.subheader("Answer")
    st.write(response)

    st.subheader("Agent Actions")
    for step in actions:
        st.write("•", step)
