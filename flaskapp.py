import pickle
from flask import Flask, request, send_file, render_template
import openai
from elevenlabs import play
from elevenlabs.client import ElevenLabs

app = Flask(__name__)

API_KEY = "PUT YOURS HERE"  # Eleven labs
OPENAI_API_KEY = "PUT YOURS HERE"
MODEL_NAME = "gpt-3.5-turbo"
VOICE_PICKLE_FILE = 'voice.pickle'
RESPONSE_AUDIO_FILE = 'response_elevenlabs.mp3'
messages = [{"role": "system", "content": "I want you to act as a british detective."}]

def get_voice_from_pickle(file_path):
    # Loads and returns a voice object from a pickle file
    # Your code here
    with open(file_path, 'rb') as f:
        voice = pickle.load(f)
    return voice

def get_response_text_from_model(messages):
    # Sends the messages to the OpenAI model and returns the generated response
    # Your code here
    response = openai.Completion.create(
        engine="davinci",
        prompt=messages,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n", " Human:"]
    )
    return response["choices"][0]["text"]

def write_audio_to_file(response_text, voice, file_path):
    # Writes the audio version of the response_text to the file_path
    # Your code here
    with open(file_path, 'wb') as f:
        f.write(response_text)
    return file_path

@app.route('/')
def home():
    # Returns the homepage
    # Your code here
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def process_message():
    # Processes the user message and returns an audio file with the response
    # This function calls the other functions in this file
    # Your code here
    # Extract the user message from the request
    user_message = request.form['message']
    
    # Generate response text based on the user message
    response_text = get_response_text_from_model(user_message)
    
    # Retrieve the voice object from the pickle file
    voice = get_voice_from_pickle(VOICE_PICKLE_FILE)
    
    # Convert the response text into audio using the retrieved voice object
    audio_file_path = write_audio_to_file(response_text, voice, RESPONSE_AUDIO_FILE)
    
    return send_file(audio_file_path, mimetype='audio/mp3')

def main():
    # Sets the API keys and starts the server
    #elevenlabs.set_api_key(API_KEY)
    client = ElevenLabs(api_key = API_KEY)
    openai.api_key = OPENAI_API_KEY
    
    #audio = client.generate(text="Hello World", voice="xmmt10aCxujz9S28zFcH", model="eleven_multilingual_v2")
    #play(audio)

    app.run(host='0.0.0.0', port=5001, debug=True)

if __name__ == '__main__':
    main()
