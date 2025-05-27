import streamlit as st
import asyncio
from Tutor_agent.agent import Tutor_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from utils import call_agent_async



# Initialize session service
session_service = InMemorySessionService()

# Async helper to run setup once
async def initialize_session(app_name,user_id):

        # Create session
        new_session = await session_service.create_session(
            app_name=app_name,
            user_id=user_id,
        )
        st.session_state.session_id = new_session.id

        # Create Runner
        st.session_state.runner = Runner(
            agent=Tutor_agent,
            app_name=st.session_state.app_name,
            session_service=session_service,
        )

        st.session_state.initialized = True
        st.session_state.messages.append({"role": "assistant", "content": "Hello! I'm your Tutor assistant. How can I help you today?"})

# Main Streamlit UI
async def main():
    app_name="Tutor Agent"
    user_id="007"
    await initialize_session(app_name,user_id)

    st.title("🎓 Tutor AI Assistant")
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Ask me anything...")
    if user_input:
        # Display user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Call the agent and display response
        response = await call_agent_async(
            st.session_state.runner,
            st.session_state.user_id,
            st.session_state.session_id,
            user_input,
        )

        if response:
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)

# Run the async event loop in Streamlit
asyncio.run(main())
