import streamlit as st
import base64

if "GOOGLE_API_KEY" in st.secrets:
    os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
else:
    st.error("GOOGLE_API_KEY is missing from Streamlit Secrets.")
    st.stop()
    
from main import run_agent


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Cooking Assistant",
    page_icon="👨‍🍳",
    layout="wide"
)


# --------------------------------------------------
# BACKGROUND IMAGE
# --------------------------------------------------

with open("images/kitchen.jpg", "rb") as image_file:
    image_base64 = base64.b64encode(image_file.read()).decode()


st.markdown(
    f"""
    <style>

    /* Full screen background */

    .stApp {{
        background-image:
            linear-gradient(
                rgba(0, 0, 0, 0.45),
                rgba(0, 0, 0, 0.45)
            ),
            url("data:image/jpeg;base64,{image_base64}");

        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }}


    /* Remove Streamlit default top space */

    .block-container {{
        padding-top: 3rem;
    }}


    /* Title */

    .cooking-title {{
        text-align: center;
        color: white;
        font-size: 55px;
        font-weight: 800;
        margin-top: 100px;
        text-shadow: 2px 2px 10px black;
    }}


    /* Subtitle */

    .cooking-subtitle {{
        text-align: center;
        color: white;
        font-size: 22px;
        margin-top: -20px;
        text-shadow: 2px 2px 8px black;
    }}


    /* Input box */

    div[data-testid="stChatInput"] {{
        background: rgba(255, 255, 255, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.5);
        border-radius: 20px;
        backdrop-filter: blur(10px);
    }}


    /* Chat messages */

    div[data-testid="stChatMessage"] {{
        background: rgba(0, 0, 0, 0.45);
        border-radius: 15px;
        color: white;
        backdrop-filter: blur(8px);
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.markdown(
    """
    <div class="cooking-title">
        👨‍🍳 COOKING ASSISTANT
    </div>

    <div class="cooking-subtitle">
        Your AI Chef for Delicious Ideas 🍃
    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# DISPLAY CHAT HISTORY
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# --------------------------------------------------
# USER INPUT
# --------------------------------------------------

user_input = st.chat_input(
    "WHAT DO YOU WANNA COOK TODAY?"
)


# --------------------------------------------------
# RUN AGENT
# --------------------------------------------------

if user_input:

    # Display user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.write(user_input)


    # Get AI response
    with st.spinner("👨‍🍳 Cooking up an answer..."):

        try:
            response = run_agent(user_input)

        except Exception as e:
            response = f"Sorry buddy, something went wrong: {e}"


    # Display AI response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    with st.chat_message("assistant"):
        st.write(response)
