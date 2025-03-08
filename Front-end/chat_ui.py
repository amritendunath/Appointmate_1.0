import streamlit as st
import httpx
import uuid

agent_dict = {
    'get_info':'information_agent',
    'appointment_info':'appointment_agent',
    'primary_assitant':'supervisor_agent'
}


def generate_uuid() -> str:
    return str(uuid.uuid4())


def make_api_call(prompt: str) -> dict:
    """Calls the API and returns the response as a dictionary."""
    API_URL = "http://localhost:8000/api/v1/generate-stream/"  # Replace with your actual API endpoint
    thread_id = st.session_state.thread_id

    try:
        response = httpx.post(API_URL,
                              json={"query": prompt},
                              headers={"X-THREAD-ID": thread_id},
                              timeout=60.0)
        response.raise_for_status()  # Raise an error for HTTP errors
        return response.json()  # Parse response JSON
    except httpx.HTTPStatusError as e:
        st.error(f"API returned an error: {e.response.status_code}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

    return {"answer": "Error retrieving response"}  # Fallback response
