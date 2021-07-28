from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
api = IAMAuthenticator("NQp3vVsdqiH1NnUVo4CdNq2IKwF6FneMSLl9FcYsNE9n")
text_2_speech= TextToSpeechV1(authenticator=api)
text_2_speech.set_service_url("https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/86fa9135-cef4-48c4-a6e7-776c81d979a6")
with open ("output.mp3", "wb") as audiofile:
    audiofile.write(
    text_2_speech.synthesize(input("please enter your message:"), accept="audio/mp3").get_result().content)
