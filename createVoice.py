import pickle
#from elevenlabs import set_api_key #clone
#from elevenlabs.client import Elevenlabs

from elevenlabs.client import ElevenLabs

client = ElevenLabs(
  api_key="PUT YOURS HERE" # Defaults to ELEVEN_API_KEY
)
'''
api_key="PUT YOURS HERE"  # Eleven labs
client = Elevenlabs(api_key = api_key)
'''
try:
    with open('voice.pickle', 'rb') as f:
        voice = pickle.load(f)
except (OSError, IOError) as e:
    voice = "Greg"
    with open('voice.pickle', 'wb') as f:
        pickle.dump(voice, f)
