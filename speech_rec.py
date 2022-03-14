import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)


# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# recognize speech using Google Cloud Speech
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
  "type": "service_account",
  "project_id": "speechtotext-202020",
  "private_key_id": "8d9e511d6d173266aafdabedcba567a9502bfd81",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCgFWvGst2FGnGZ\nXEZI+DoDzorZGPTqxAVVfZv92AqvS1n+9/bcGfm6E0EVVMVA4PWr+qDwTErw48/+\nM0GH3l0XPjNKwhBh33me+Kp9LGwSuOGPQAJdL45PXpB1gk50R62+v/qwlVjkIO54\nSFTWT+phhIXh4N6gtMjQIInPBA4OfBR2YBbaPyjT9p+OlVCmYoGjszpxwsz5pngG\nyFdAKdHpUKxL97O0EvFn0JMSOT3J3JpxzLfqK/LeckrKvhYEk1Rf3rFFrEojlhl0\nNXolJTWXk0pskkT1mVp0xCREFtCi5l3tXdoh1Xs+eotpMgQmrXMzi5byAwe8oMFP\nppY0QujdAgMBAAECggEACLJxOwfPqiIQJuVQ+jjmKfvIJlhJQhHpOkZLOcTJe9GL\nr6L4GegdXaMbJ5YF62rtXe0NXlC+x4yQ6b4OItwNUaxy6+5UJoUWHfFjjc5ihrfd\npUM0fayOPjikf4XXTlDwmwriC0Lp4+b4HbfMSCJqWObywR1O6ws3V7tU0VbmjpnQ\nHoZhFhbP0f+uIOH90Qxl9b4A9hZurWon6uE1+OGfk3KqaOvpwGhVsuECLwY5Dz/f\nX/SBjAnIpeuGY4pbhgYiiCnN5XfF+kcnofhjSDTQZL0b7rGue2m6t2b1tmr8vV4+\nwLHJQ0lD9awVzJSPhSDBPdfm2eO1Eu6TY8CwIxFu0QKBgQDRUFEckkBg42Oh1NlJ\n8eOqxCq8DhDU2UA6IBVTZJDFCz22Te2yA7vrQP/l3qqoMN8A3VGMb98eBMpg8hQQ\nfjRj1ZELsHAfnXWEpqqdKLYrcaFPjLRYgpA8tQF+5YEzUe+2V+hkKUKxnkfrDDIa\n2kuXE9/Bt4uxGL3I/UPowvjZiQKBgQDDyhk3JZkxW9lWDNefGCIo3XNgXVb18dH1\nyGuOnkKhJ/hL1a4R6kj+8j3HxB5g3GbaRDac7spRzDvu8lCSx+6p6bn1u12jtS0i\nXXLnAmUAniA8PukXZx726eGOAsD1eeAtW68zGUkuJX9GHerflAv8E4KDK2Ye+sRa\nekjNKwCDtQKBgHsgCsaKxXH48IempDbaIjk2cYjzoTUDosNOUh0fAAXYyfFuP89C\nYQ1Oy/jVFYAgV12z0p+QwyduW/nRDLpy8rBzVYIRxLLkNdfVDnGqHBbMHb6knwWd\nr+j19K5HpMuifCa/6UTZ/JBs8hMytlqTZHm3SB00seh4DFOpn4PRBP85AoGAXOg7\nHPMnhcebE31WmHVASHoFdPX1/RF6W5J2j5/D6GtqJLpKNtAhQXG8JV6IN9h+qhZy\nf/fEZBpxWkr8NxrOwyxZBSWbIsMnnsYPb1WwjiF7FHuZ6nQRuoNzeAsQe6wQ2BVI\nxwu5sT8z7RbnTJ8ZLM4pQYtHk23V3UVn5IwCW30CgYEApNlIQrqj6YdcUirAmujx\nzXgX7zXmM1kTZ4iAkOKN4sCZMjnDKf2eux5IqohPjh84ZpS3n86gKhDQ+cqXmIaz\nx6LdCrAGfy7uzXag+8Q297HDH46PetmNEDuxKBipc4ygzDL8dlpg4aPvbKR17b7w\n3iC/xVNuH7tt6ig19Y7+1og=\n-----END PRIVATE KEY-----\n",
  "client_email": "my-stt-sa@speechtotext-202020.iam.gserviceaccount.com",
  "client_id": "106665130235312889647",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/my-stt-sa%40speechtotext-202020.iam.gserviceaccount.com"
}
"""
try:
    print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
'''
# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))



# recognize speech using Wit.ai
WIT_AI_KEY = "INSERT WIT.AI API KEY HERE"  # Wit.ai keys are 32-character uppercase alphanumeric strings
try:
    print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
except sr.UnknownValueError:
    print("Wit.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Wit.ai service; {0}".format(e))

# recognize speech using Microsoft Bing Voice Recognition
BING_KEY = "INSERT BING API KEY HERE"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
try:
    print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

# recognize speech using Microsoft Azure Speech
AZURE_SPEECH_KEY = "INSERT AZURE SPEECH API KEY HERE"  # Microsoft Speech API keys 32-character lowercase hexadecimal strings
try:
    print("Microsoft Azure Speech thinks you said " + r.recognize_azure(audio, key=AZURE_SPEECH_KEY))
except sr.UnknownValueError:
    print("Microsoft Azure Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Azure Speech service; {0}".format(e))
x
# recognize speech using Houndify
HOUNDIFY_CLIENT_ID = "INSERT HOUNDIFY CLIENT ID HERE"  # Houndify client IDs are Base64-encoded strings
HOUNDIFY_CLIENT_KEY = "INSERT HOUNDIFY CLIENT KEY HERE"  # Houndify client keys are Base64-encoded strings
try:
    print("Houndify thinks you said " + r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))
except sr.UnknownValueError:
    print("Houndify could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Houndify service; {0}".format(e))
'''
# recognize speech using IBM Speech to Text
IBM_USERNAME = "14QXhR-0PC8gKnzv9kRPDTYFiIH_kDTT23j4W_pY0RwC"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
IBM_PASSWORD = "Gowri@2000k"  # IBM Speech to Text passwords are mixed-case alphanumeric strings
try:
    print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
except sr.UnknownValueError:
    print("IBM Speech to Text could not understand audio")
except sr.RequestError as e:
    print("Could not request results from IBM Speech to Text service; {0}".format(e))