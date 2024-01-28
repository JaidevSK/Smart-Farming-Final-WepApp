import streamlit as st
import openai
from streamlit_chat import message

def api_calling(prompt):
	completions = openai.Completion.create(
		engine="text-davinci-003",
		prompt=prompt,
		max_tokens=1024,
		n=1,
		stop=None,
		temperature=0.5,
	)
	message = completions.choices[0].text
	return message

st.title("Smart Farming Chatbot for Cotton")
if 'user_input' not in st.session_state:
	st.session_state['user_input'] = []

if 'openai_response' not in st.session_state:
	st.session_state['openai_response'] = []

apikey = st.text_input("Enter Your API Key")
openai.api_key = apikey

def get_text():
	input_text = st.text_input("How can I help you?", key="input")
	return input_text

user_input = get_text()

if user_input:
	output = api_calling(user_input)
	output = output.lstrip("\n")

	# Store the output
	st.session_state.openai_response.append(user_input)
	st.session_state.user_input.append(output)

message_history = st.empty()

if st.session_state['user_input']:
	for i in range(len(st.session_state['user_input']) - 1, -1, -1):
		# This function displays user input
		message(st.session_state["user_input"][i], 
				key=str(i),avatar_style="🦖")
		# This function displays OpenAI response
		message(st.session_state['openai_response'][i], 
				avatar_style="🤖",is_user=True,
				key=str(i) + 'data_by_user')
