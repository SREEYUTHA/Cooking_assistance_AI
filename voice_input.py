import streamlit as st
import streamlit.components.v1 as components


# =========================================================
# HTML
# =========================================================

HTML = """
<!DOCTYPE html>

<html>

<head>

<style>

body {
    margin: 0;
    padding: 0;
    background: transparent;
    font-family: Arial, sans-serif;
}

.input-wrapper {

    display: flex;
    align-items: center;

    width: 100%;
    height: 52px;

    box-sizing: border-box;

    padding: 6px 10px;

    border: 1px solid #555;
    border-radius: 16px;

    background: #1f1f1f;
}


/* -----------------------------------------
   Text input
----------------------------------------- */

#message {

    flex: 1;

    border: none;
    outline: none;

    background: transparent;

    color: white;

    font-size: 16px;

    padding: 8px;
}


/* -----------------------------------------
   Buttons
----------------------------------------- */

.icon-button {

    border: none;

    background: transparent;

    color: white;

    font-size: 20px;

    cursor: pointer;

    width: 40px;
    height: 40px;

    border-radius: 50%;
}


.icon-button:hover {

    background: #333;

}


/* -----------------------------------------
   Language menu
----------------------------------------- */

.language-menu {

    position: absolute;

    right: 55px;
    bottom: 60px;

    display: none;

    flex-direction: column;

    width: 150px;

    background: #222;

    border: 1px solid #555;

    border-radius: 10px;

    padding: 6px;

    box-shadow: 0 4px 15px rgba(0,0,0,0.4);

}


.language-menu.show {

    display: flex;

}


.language-option {

    border: none;

    background: transparent;

    color: white;

    text-align: left;

    padding: 10px;

    border-radius: 7px;

    cursor: pointer;

    font-size: 14px;

}


.language-option:hover {

    background: #333;

}


</style>

</head>


<body>


<div class="input-container">


    <!-- Language menu -->

    <div id="languageMenu" class="language-menu">

        <button
            class="language-option"
            onclick="selectLanguage('English')">
            🇬🇧 English
        </button>

        <button
            class="language-option"
            onclick="selectLanguage('Telugu')">
            🇮🇳 Telugu
        </button>

        <button
            class="language-option"
            onclick="selectLanguage('Hindi')">
            🇮🇳 Hindi
        </button>

        <button
            class="language-option"
            onclick="selectLanguage('Tamil')">
            🇮🇳 Tamil
        </button>

        <button
            class="language-option"
            onclick="selectLanguage('Kannada')">
            🇮🇳 Kannada
        </button>

    </div>


    <!-- Input bar -->

    <div class="input-wrapper">


        <input
            id="message"
            type="text"
            placeholder="WHAT DO YOU WANNA COOK TODAY?"
        />


        <!-- Speaker -->

        <button
            id="voiceButton"
            class="icon-button"
            title="Choose voice language">

            🔊

        </button>


        <!-- Send -->

        <button
            id="sendButton"
            class="icon-button"
            title="Send">

            ➤

        </button>


    </div>


</div>


<script>


let selectedLanguage = "English";


/* -----------------------------------------
   Speaker button
----------------------------------------- */

document
    .getElementById("voiceButton")
    .addEventListener("click", function() {

        const menu =
            document.getElementById("languageMenu");

        menu.classList.toggle("show");

    });


/* -----------------------------------------
   Language selection
----------------------------------------- */

function selectLanguage(language) {

    selectedLanguage = language;

    const menu =
        document.getElementById("languageMenu");

    menu.classList.remove("show");

}


/* -----------------------------------------
   Send button
----------------------------------------- */

document
    .getElementById("sendButton")
    .addEventListener("click", function() {

        sendMessage();

    });


/* -----------------------------------------
   Enter key
----------------------------------------- */

document
    .getElementById("message")
    .addEventListener("keydown", function(event) {

        if (event.key === "Enter") {

            event.preventDefault();

            sendMessage();

        }

    });


/* -----------------------------------------
   Send message to Streamlit
----------------------------------------- */

function sendMessage() {

    const message =
        document.getElementById("message").value;


    if (!message.trim()) {

        return;

    }


    const data = {

        text: message,

        language: selectedLanguage

    };


    // Send data to Streamlit

    window.parent.postMessage(

        {
            type: "cooking_input",
            data: data
        },

        "*"

    );


    // Clear input

    document.getElementById("message").value = "";

}


</script>


</body>

</html>
"""


# =========================================================
# Streamlit Component
# =========================================================

cooking_input = components.declare_component(
    "cooking_voice_input",
    html=HTML
)


# =========================================================
# Component Function
# =========================================================

def cooking_input_component():

    result = cooking_input(
        default=None,
        height=70
    )

    return result