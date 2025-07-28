# 🕵️‍♂️ OpenAI Voice Response – British Detective Edition

My first attempt at a web-based AI assistant that role-plays as a clever British detective. Ask it anything through the browser, and hear its response spoken aloud using ultra-realistic voice synthesis via **ElevenLabs**.

---
## 🎩 Features

- 🌐 Simple web interface for user input  
- 🧠 OpenAI-powered text generation  
- 🔊 ElevenLabs API for lifelike speech in a British accent  
- 🧑‍💻 Built with Flask + HTML/CSS/JavaScript  

---
## 🗂️ Project Structure

```
OpenAI-Voice-Response
├── flaskapp.py         # Flask server: handles requests, prompts OpenAI, calls ElevenLabs
├── createVoice.py      # Uses ElevenLabs API to convert text to audio
├── index.html          # Frontend UI
├── main.js             # JS for input/output handling
├── styles.css          # Styling for the page
├── voice.pickle        # (Optional) Cached voice data
├── LICENSE
└── README.md
```

---
## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/danielpul101/OpenAI-Voice-Response.git
cd OpenAI-Voice-Response
```

### 2. Install dependencies

You can manually install packages or generate a requirements.txt later.

```bash
pip install flask openai requests
```

> ⚠️ **Note:** You may also need to install other packages depending on your ElevenLabs integration (e.g., pydub, ffmpeg).

## 🔑 API Setup

You will need two API keys:

### OpenAI API Key
- Get it from: https://platform.openai.com/account/api-keys

### ElevenLabs API Key
- Sign up at: https://www.elevenlabs.io/

Add them securely to your environment (recommended):

```bash
export OPENAI_API_KEY="your-openai-key"
export ELEVENLABS_API_KEY="your-elevenlabs-key"
```

Or set them in a `.env` file and load via `python-dotenv`.

## ▶️ Running the App

Start the Flask server:

```bash
python flaskapp.py
```

Then open your browser and go to:
```
http://localhost:5000
```

## 🧠 How It Works

1. You enter a question or prompt into the web form.
2. Flask sends it to OpenAI with this system message: *"I want you to act as a British detective."*
3. The AI generates a detective-style reply.
4. The reply is passed to ElevenLabs, which returns a British-accented audio file.
5. The response plays back in your browser.

## 🗣️ Example Interaction

**User Input:**
> "Detective, what do you make of the blood on the candlestick?"

**AI Voice Reply:**
> "Ah, a classic diversion. The blood's fresh—but not the weapon. Someone's framing the butler again, I daresay."

## 💡 Customization

- Change the prompt inside `flaskapp.py` to roleplay as a different persona.
- Swap the ElevenLabs voice ID for a different British voice.
- Add audio download buttons or conversation history.

## 📦 Optional: Create requirements.txt

If you'd like to generate a requirements file:

```bash
pip freeze > requirements.txt
```

## 📜 License

MIT License

## 🕵️ Closing Words

*"Now then, let's unravel your little mystery, shall we?"*
