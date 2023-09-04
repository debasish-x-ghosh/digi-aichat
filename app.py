
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from dotenv import load_dotenv
import os

########## Remeber: enable this for DEV
# load_dotenv()
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
#     print("OPENAI_API_KEY is not set")
#     exit(1)
# else:
#     print("OPENAI_API_KEY is set")
 
########## Remeber: enable this for PROD
os.environ["OPENAI_API_KEY"] = os.environ.get('OPENAI_API_KEY')
if os.environ("OPENAI_API_KEY") is None or os.environ("OPENAI_API_KEY") == "":
    print("OPENAI_API_KEY is not set")
    exit(1)
else:
    print("OPENAI_API_KEY is set")

# From here down is all the StreamLit UI.
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("Hey, I'm your Chat GPT")

if "sessionMessages" not in st.session_state:
     st.session_state.sessionMessages = [
        SystemMessage(content="You are a helpful assistant.")
    ]


def load_answer(question):
    st.session_state.sessionMessages.append(HumanMessage(content=question))
    assistant_answer  = chat(st.session_state.sessionMessages )
    st.session_state.sessionMessages.append(AIMessage(content=assistant_answer.content))
    return assistant_answer.content


def get_text():
    input_text = st.text_input("You: ", key= input)
    return input_text


chat = ChatOpenAI(temperature=0)


user_input=get_text()
submit = st.button('Generate')  

if submit:
    response = load_answer(user_input)
    st.subheader("Answer:")
    st.write(response)

