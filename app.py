import os
import streamlit as st
from google import genai
from google.genai import types

# 1. Page Configuration
st.set_page_config(page_title="Norsk Syntax Compiler", page_icon="🇳🇴", layout="centered")
st.title("🇳🇴 Norsk Syntax Compiler")
st.markdown("Enter a Norwegian sentence. The compiler will check for syntax errors and explain grammar using computer science concepts.")

# 2. Initialize the API Client
try:
    client = genai.Client()
except Exception:
    st.error("API Key not found. Please set the GEMINI_API_KEY environment variable or Streamlit Secret.")
    st.stop()

# 3. Define the System Instructions (The "Persona")
SYSTEM_PROMPT = """
You are a strict but helpful Norwegian language tutor for high educated users. 
Analyze the user's Norwegian input. 
If there is a grammatical mistake, treat it like a programming syntax error (e.g., 'SyntaxError: V2 violation at index 1'). 
Explain the rule they broke using computer science analogies (e.g., compilers, variables, inheritance, loops). 
If the input is completely correct, respond naturally in Norwegian to continue the conversation, keeping the topic centered on workplace dynamics, software engineering, or academic research in Norway.
"""

# 4. Manage Chat History State
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 5. Handle User Input & LLM Response
if user_input := st.chat_input("Skriv noe på norsk... (e.g., 'Jeg i dag spiste eple')"):
    
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    contents = []
    for msg in st.session_state.messages:
        role = "user" if msg["role"] == "user" else "model"
        contents.append(types.Content(role=role, parts=[types.Part.from_text(text=msg["content"])]))

    with st.chat_message("assistant"):
        with st.spinner("Compiling..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=contents,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT,
                        temperature=0.4, 
                    )
                )
                reply = response.text
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            except Exception as e:
                st.error(f"Execution Error: {e}")
