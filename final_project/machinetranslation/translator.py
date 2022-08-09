import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

authenticator = IAMAuthenticator('vZlvyp2UJVr8U8O2Njxa7kZOCjwYTGhObtNVmgV2fC4k')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/9d4dbfce-8724-40c1-93f7-5dc3e1548cac')

def english_to_french(english_text):
    french_translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    return french_translation.get('translations')[0].get('translation')

def french_to_english(french_text):
    english_translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return english_translation.get('translations')[0].get('translation')
