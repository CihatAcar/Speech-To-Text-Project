from google.cloud import speech
import os
import io

# Creates google client
client = speech.SpeechClient()

# Full Path of the Audio file replace with your file name
file_name = os.path.join(os.path.dirname(__file__), "test.wav")

# Loads the audio file into memory
with io.open(file_name, "rb") as audio_file:
    content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(

    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    audio_channel_count=1,
    language_code="en-US",
)

# Sends the request to google to transcribe the audio
response = client.recognize(request={"config":
                                     config, "audio": audio})

# Reads the Response
for result in response.results:
    f = open('file.txt', 'w')
    f.write("Transcript: {}".format(result.alternatives[0].transcript))

f.close()

# export GOOGLE_APPLICATION_CREDENTIALS=""
