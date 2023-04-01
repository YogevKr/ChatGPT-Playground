import openai
import streamlit as st

# Set your OpenAI API key
openai.api_key = "your_openai_api_key_here"

def generate_response(messages):
    model_engine = "gpt-3.5-turbo"  # You can use any available GPT model, like "gpt-4" or "text-davinci-002"

    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=messages,
        max_tokens=150,
        n=1,
        temperature=0.5,
    )

    return response.choices[0].message['content'].strip()

# Set up the Streamlit app
st.title("ChatGPT Playground")
st.write("Enter your message below and ChatGPT will generate a response.")

# Initialize or retrieve the conversation_history from session state
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

if st.session_state.conversation_history:
    st.write("Conversation History:")
    for message in st.session_state.conversation_history:
        st.write(f"{message['role'].capitalize()}: {message['content']}")
    
# Create a form for user input
with st.form(key="user_input_form", clear_on_submit=True):
    user_input = st.text_input("Your Message", value="", key="1")
    submit_button = st.form_submit_button("Submit")
    clear_history_button = st.form_submit_button("Clear History")

    if submit_button:
        if user_input:
            st.session_state.conversation_history.append({"role": "user", "content": user_input})
            chatgpt_response = generate_response(st.session_state.conversation_history)
            st.session_state.conversation_history.append({"role": "assistant", "content": chatgpt_response})
            st.experimental_rerun()
            
    elif clear_history_button:
        st.session_state.conversation_history.clear()
        st.experimental_rerun()
