import requests
import streamlit as st

#Api Code:

API_URL = "https://www.stack-inference.com/run_deployed_flow?flow_id=64e8b2790accbf029a90082b&org=a833c26e-7300-4d4c-81cb-769ae3ae4a9b"
headers = {'Authorization':
'Bearer b24fbc2b-fa65-4c13-872e-27a77c727ffa',
'Content-Type': 'application/json'
}

# Set Streamlit app title and configuration
st.set_page_config(
    page_title="Farmer Chat",
    page_icon="🌾",
    layout="wide",
)

# Set the app theme to "farmer" with green colors
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f5e0;
        color: #374d20;
    }
    .stButton button {
        background-color: #7ab648;
        color: white;
    }
    .stTextInput > div > div > input {
        background-color: #e4f0d0;
    }
    .stText p, .stMarkdown {
        color: #374d20;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create the main layout
st.title("Farmer Chat")
st.image("farmer.png", use_column_width=True)
st.subheader("Ask questions about farming!")

# Create a large chat area for input and responses

user_message = st.text_input("You:", "")
#Api Interface:
def query(payload):
 response = requests.post(API_URL, headers=headers, json=payload)
 return response.json()
output = query({"in-0":f' """{user_message}""" ', "user_id": """<USER or Conversation ID>"""})
# Define a button to submit the chat input
if st.button("Send"):
    # Process the chat input here (you can replace this with API calls or logic)
    response = "This is a response to your message."
    st.text("Response:")
    st.write(response)
    st.write(output)







