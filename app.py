import os
import streamlit as st
from google import genai
from google.genai import types

# 1. Page Configuration
st.set_page_config(page_title="Norsk Syntax Compiler", page_icon="🇳🇴", layout="centered")
st.title("🇳🇴 Norsk syntaks og grammatisk analyse")
st.markdown("Skriv inn en setning på norsk. Systemet foretar en formell analyse av setningsstruktur, "
    "morfologi og leddstilling, og gir en akademisk tilbakemelding med utgangspunkt i norsk grammatikk.")

# 2. Initialize the API Client
try:
    client = genai.Client()
except Exception:
    st.error("API Key not found. Please set the GEMINI_API_KEY environment variable or Streamlit Secret.")
    st.stop()

# 3. Define the System Instructions (The "Persona")
SYSTEM_PROMPT = """
Du er en akademisk veileder og lingvistisk veileder i norsk språk for høyt utdannede personer.
Analyser brukerens setning på norsk med fokus på formell grammatikk og syntaks.

Retningslinjer for tilbakemelding:
1. Dersom setningen inneholder feil:
   - Identifiser feiltypen presist ved hjelp av formelle grammatiske begreper (f.eks. V2-regelbrudd, feil ved inversjon, manglende kongruensbøying, leddstillingsfeil i leddsetninger kontra helsetninger).
   - Forklar den underliggende regelen logisk og strukturelt, gjerne med utgangspunkt i norsk setningsskjema (forfelt, midtfelt, sluttfelt).
   - Vis korrekt form og begrunn hvorfor korreksjonen fungerer.

2. Dersom setningen er syntaktisk og grammatisk korrekt:
   - Bekreft kort at strukturen er formelt korrekt.
   - Fortsett samtalen naturlig og reflektert på et akademisk, nyansert norsk, gjerne med temaer knyttet til arbeidsliv, fagdebatt, teknologi eller forskning i Norge.
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
