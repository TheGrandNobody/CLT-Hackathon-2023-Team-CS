import openai
import streamlit as st

# Initialize session state variable if not present
if "button_clicked" not in st.session_state:
    st.session_state["button_clicked"] = False

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/TheGrandNobody/CLT-Hackathon-2023-Team-CS)"

st.title("📝 Edion Content Generator V1")
st.caption("🚀 A content-generator made by Edion Management Systems")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)

# Display buttons only if none has been clicked yet
if not st.session_state["button_clicked"]:
    if st.button(""):
        st.session_state["button_clicked"] = True
        # Do something when Button 1 is clicked
        
    if st.button(""):
        st.session_state["button_clicked"] = True
        # Do something when Button 2 is clicked
        
    if st.button(""):
        st.session_state["button_clicked"] = True
        # Do something when Button 3 is clicked
        
else:
    # Display another interface if a button has been clicked
    