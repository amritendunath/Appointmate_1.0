import streamlit as st
import httpx
import uuid

agent_dict = {
    'get_info':'information_agent',
    'appointment_info':'appointment_agent',
    'primary_assitant':'supervisor_agent'
}
