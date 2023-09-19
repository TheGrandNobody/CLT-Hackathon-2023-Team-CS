import openai
import streamlit as st

# Initialize session state variable if not present
if "mode" not in st.session_state:
    st.session_state["mode"] = None # | "quiz" | "lesson"

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

# Display buttons only if none has been clicked yet
if st.session_state["mode"] is None:
    if st.button("Create a quiz"):
        st.session_state["mode"] = "quiz"

        msg = {"role": "assistant", "content": "Briefly explain what topic you want a quiz about, and how many questions are desired."}
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg["content"])

    if st.button("Create a lesson plan"):
        st.session_state["mode"] = "quiz"
        print("button2 clicked!")

        msg = {"role": "assistant", "content": "What topic would you like the lesson plan about? Provide all desired details."}
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg["content"])
else:
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
        