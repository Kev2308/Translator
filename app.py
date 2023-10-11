from pygoogletranslation import Translator
import language_check

def fix_grammar_mistakes(text):
  try:
    tool = language_check.LanguageTool('en-US')
    errors = tool.check(text)
    for error in errors:
        text = text.replace(error.word, error.suggestions[0])
    return text
  except:
     return text
translator = Translator()

def translate(text, lang, type='Direct'):
    langcode={'English':'en','Hindi':'hi','Bengali':'bn','Marathi':'mr','Tamil':'ta','Japanese':'ja'}
    if type=='Direct':
       translated = translator.translate(text, dest=langcode[lang])
       return st.text(translated.text),st.text(translated.pronunciation)
    elif type=='Double':
       eng=translator.translate(text, dest='en').text
       translated = translator.translate(eng, dest=langcode[lang])
       return st.text(translated.text),st.text(translated.pronunciation)
    else:
        eng = translator.translate(text, dest='en').text
        fixed = fix_grammar_mistakes(eng)
        translated = translator.translate(fixed, dest=langcode[lang])
        return st.text(translated.text),st.text(translated.pronunciation)

import streamlit as st
st.title('The Translation App')
lang=st.selectbox('Select Destination language', ['English','Hindi','Bengali','Marathi','Tamil','Japanese'])
text=st.text_input('Enter text')
type=st.radio('Select Method:', ['Direct','Double','Grammer'])
if st.button('Translate') == True:
   translate(text, lang, type)


