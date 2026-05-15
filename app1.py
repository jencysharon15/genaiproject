import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("API_KEY")
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile")
st.title("JenAI:Innovation Starts Here")
if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    else:
        st.chat_message("assistant").write(msg.content)
user_input = st.chat_input("Curious about anything?")
if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.spinner("Working on it..."):
        try:
            response = llm.invoke(st.session_state.messages)
            ai_reply = response.content
            st.chat_message("assistant").write(ai_reply)
            st.session_state.messages.append(AIMessage(content=ai_reply))

        except Exception as e:
            st.error(f"Error: {e}")