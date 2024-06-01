import pickle
#from elevenlabs import set_api_key #clone
#from elevenlabs.client import Elevenlabs

from elevenlabs.client import ElevenLabs

client = ElevenLabs(
  api_key="d3062c42b47c5c88010b0a8a7af21188" # Defaults to ELEVEN_API_KEY
)
'''
api_key="d3062c42b47c5c88010b0a8a7af21188"  # Eleven labs
client = Elevenlabs(api_key = api_key)
'''
try:
    with open('voice.pickle', 'rb') as f:
        voice = pickle.load(f)
except (OSError, IOError) as e:
    voice = "Greg"
    with open('voice.pickle', 'wb') as f:
        pickle.dump(voice, f)
