import openai
import streamlit as st
import os

DEV_MODE = os.environ.get("DEV") == "1"
# Initialize session state variable if not present
if "mode" not in st.session_state:
    st.session_state["mode"] = None # | "quiz" | "lesson"

if "button_clicked" not in st.session_state:
    st.session_state["button_clicked"] = False
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

openai_api_key = os.environ.get("OPENAI_KEY")
if openai_api_key is None:
    with st.sidebar:
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
        "[View the source code](https://github.com/TheGrandNobody/CLT-Hackathon-2023-Team-CS)"

st.title("📝 Edion Content Generator V1")
st.caption("🚀 A content-generator made by Edion Management Systems")

if DEV_MODE:
    st.write("state = ", st.session_state)

# write history of messages
if st.session_state["mode"] is None:
    for msg in st.session_state.messages[:1]:
        st.chat_message(msg["role"]).write(msg["content"])

# Display buttons only if none has been clicked yet
if st.session_state["mode"] == "lesson" or st.button("Create a quiz", disabled=st.session_state["button_clicked"]):
    if st.session_state["mode"] is None:
        st.session_state["mode"] = "quiz"
        #st.session_state.messages.clear()
        msg = {"role": "assistant", "content": "Briefly explain what topic you want a quiz about, and how many questions are desired."}
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg["content"])
        st.session_state["button_clicked"] = True
        st.experimental_rerun()

if st.session_state["mode"] == "quiz" or st.button("Create a lesson plan", disabled=st.session_state["button_clicked"]):
    if st.session_state["mode"] is None:
        st.session_state["mode"] = "lesson"
        msg = {"role": "assistant", "content": "What topic would you like the lesson plan about? Provide all desired details."}
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg["content"])
        st.session_state["button_clicked"] = True
        st.experimental_rerun()

for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

if st.session_state["mode"] is not None:
    if prompt := st.chat_input():
        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()
        openai.api_key = openai_api_key
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        st.session_state.messages.append({"role": "user", "content": f"Give me the {'quiz with the answers as well and make it multiple choice please' if st.session_state['mode'] == 'quiz' else 'lesson plan in detail and well-formatted please'}"})
        st.session_state.messages.append({"role": "user", "content": ""})
        st.chat_message("assistant").write("Generating...This may take a while")
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
        msg = response.choices[0].message
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg.content)