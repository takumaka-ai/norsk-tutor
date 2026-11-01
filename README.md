# Norsk syntaks og grammatisk analyse (Norwegian Syntax & Grammar Engine)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://norsk-tutor-ebykyus2vtiv7u4xdjmjin.streamlit.app)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Google Gemini API](https://img.shields.io/badge/LLM-Gemini%20API-orange.svg)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

En webapplikasjon utviklet for formell lingvistisk analyse og pedagogisk tilbakemelding på norsk setningsstruktur, leddstilling og morfologi. 

Prosjektet er rettet mot høyt utdannede språkbrukere og andrespråksinnlærere som søker strukturelle og vitenskapelige forklaringer fremfor forenklede korreksjoner.

---

## 🌐 Prøv applikasjonen

Applikasjonen kjører live i nettleseren via Streamlit Community Cloud:  
👉 **[Åpne Norsk syntaks og grammatisk analyse](https://norsk-tutor-ebykyus2vtiv7u4xdjmjin.streamlit.app)**

---

## 🎯 Formål og lingvistisk forankring

Verktøyet kombinerer store språkmodeller med etablerte prinsipper fra skandinavisk syntaksteori:

* **Topologisk feltanalyse (Setningsskjema):** Forklaringer tar utgangspunkt i Diderichsens setningsskjema (forfelt, midtfelt, sluttfelt) for helsetninger og leddsetninger.
* **V2-regelen og inversjon:** Nøyaktig diagnostikk av leddstillingsavvik, herunder feilplassering av setningsadverbialer og manglende inversjon etter forfeltstopikalisering.
* **Morfosyntaktisk kongruens:** Verifisering av samsvarsbøying i genus, numerus og bestemt form på tvers av substantivfraser og predikativer.
* **Faglig diskursfortsettelse:** Ved syntaktisk korrekte setninger responderer systemet med et nyansert og akademisk ordforråd orientert rundt vitenskap, samfunnsdebatt og norsk arbeidslivskultur.

---

## 🏛 Arkitektur og teknologistakk

```
┌─────────────────────────┐
│     Brukergrensesnitt   │  Streamlit Web Interface
└────────────┬────────────┘
             │ (HTTP / WebSocket)
┌────────────▼────────────┐
│      Applikasjonslag    │  Python (`app.py`), session_state
└────────────┬────────────┘
             │ (Google GenAI SDK)
┌────────────▼────────────┐
│      Språkmodell        │  Google Gemini (gemini-3.5-flash-lite)
└─────────────────────────┘
```

* **Frontend & runtime:** [Streamlit](https://streamlit.io/)
* **API-grensesnitt:** `google-genai` (Google GenAI Python SDK)
* **Kjerne-modell:** Google Gemini (`gemini-3.5-flash-lite`)
* **Sikkerhet:** API-nøkler håndteres kryptert via Streamlit Cloud Secrets og eksponeres aldri i kildekoden.

---

## 📂 Prosjektstruktur

```text
├── .streamlit/
│   └── secrets.toml       # Lokale hemmeligheter (ekskludert via .gitignore)
├── app.py                 # Applikasjonslogikk, systeminstruks og UI
├── requirements.txt       # Avhengigheter (streamlit, google-genai)
└── README.md              # Prosjektdokumentasjon
```

---

## 💻 Kjøring i lokalt utviklingsmiljø

Dersom du ønsker å klone og kjøre prosjektet lokalt:

### 1. Klon repositoriet
```bash
git clone https://github.com/takumaka-ai/norsk-tutor.git
cd norsk-tutor
```

### 2. Sett opp virtuelt miljø
```bash
python3 -m venv .venv
source .venv/bin/activate   # På Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Konfigurer API-tilgang
Opprett en gratis API-nøkkel via [Google AI Studio](https://aistudio.google.com/) og sett miljøvariabelen:
```bash
export GEMINI_API_KEY="din_api_nøkkel_her"
```

Alternativt kan du opprette `.streamlit/secrets.toml`:
```toml
GEMINI_API_KEY = "din_api_nøkkel_her"
```

### 4. Start applikasjonen
```bash
streamlit run app.py
```

---

## 🔒 Personvern og sikkerhet

* Applikasjonen lagrer ingen personlige brukerdata eller chathistorikk utover den aktive nettleserøkten (`st.session_state`).
* Prosjektet benytter Googles gratis API-tier uten tilknytning til betalingskort; ingen uforutsette kostnader kan genereres.

---

## 📄 Lisens

Dette prosjektet er lisensiert under [MIT-lisensen](LICENSE).
