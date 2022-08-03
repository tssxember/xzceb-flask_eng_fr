import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('u7B14Sz9byYUuaQGByxISTjLtHqARTEFdbxpQOM8hN1k')
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')

def english_to_french(english_text):
    translation= language_translator(text=english_text, model_id="en-fr").get_result()
    french_text=translation['translations'][0].get['translation']
    return french_text

def french_to_english(french_text):
    translation= language_translator(text=french_text, model_id="fr-en").get_result()
    english_text=translation['translations'][0].get['translation']
    return english_text
