import streamlit as st
from groq import Groq


client = Groq(
    api_key="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",
)

def translate_text(input_text, system_prompt):
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": input_text,
        }
    ],
    model="llama3-70b-8192",
    temperature=0.65,
    max_tokens=8192,
    stream=False,
    )
    return chat_completion.choices[0].message.content

st.title('Language Translation Assistant')

language = st.selectbox('Select Language', ['English', 'French', 'Thai', 'Vietnamese', 'Arabic', 'French', 'Portuguese', 'Chinese', 'Japanese', 'Korean', 'Hindi'])

system_prompt = f"You are an translation assistant for {language} language. only give translation of the text. don't change the any word, just translate it."

input_text = st.text_area('Enter text to translate:')

if st.button('Translate'):
    if input_text:
        translated_text = translate_text(input_text, system_prompt)
        st.text_area('Translated text:', value=translated_text, height=200)
    else:
        st.error('Please enter text to translate.')
