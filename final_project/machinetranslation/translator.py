import os
from datetime import datetime
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

versiondate = datetime.today().strftime('%Y-%m-%d')

authenticatorKey = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=versiondate,
    authenticator=authenticatorKey
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    translate = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translate['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    translate = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translate['translations'][0]['translation']
    return english_text
