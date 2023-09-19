import streamlit as st

# Initialize session state if not present
if 'mode' not in st.session_state:
    st.session_state['mode'] = None

# Display state for debugging
st.write(f"Current mode is: {st.session_state['mode']}")

# Show buttons only if mode is None
if st.session_state['mode'] is None:
    if st.button("Create a quiz"):
        st.session_state['mode'] = 'quiz'
    if st.button("Create a lesson plan"):
        st.session_state['mode'] = 'lesson'

# If mode is not None, do something else
if st.session_state['mode'] is not None:
    st.write(f"Creating a {st.session_state['mode']}")
    if st.button("Reset"):
        st.session_state['mode'] = None