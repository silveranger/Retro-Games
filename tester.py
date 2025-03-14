import streamlit as st
import subprocess
import sys
import base64

# Function to set background
def set_bg(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    bg_image = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .title-box {{
        background-color: black;
        color: white;
        padding: 8px 20px;
        text-align: center;
        border-radius: 20px;
        display: inline-block;
    }}
    .title-container {{
        text-align: center;
    }}
    </style>
    """
    st.markdown(bg_image, unsafe_allow_html=True)

# Set background image
set_bg("C:/Users/ACER/Downloads/retro.webp")

# Define available games
games = {
    "Snake Game": "snakes3.py",
    "Tic-Tac-Toe": "Tic tac toe.py",
    "Flappy Bird": "flappy.py",
    "Car Racing": "car game.py",
}

st.markdown("""
    <div class='title-container'>
        <div class='title-box'>
            <h1>🎮 RETRO GAMES 🎮</h1>
        </div>
    </div>
""", unsafe_allow_html=True)

st.sidebar.header("GAMERS")

# Game selection
game_choice = st.sidebar.selectbox("Choose a game to play:", list(games.keys()))

if st.sidebar.button("Play Game"):
    game_script = games[game_choice]
    st.write(f"Launching {game_choice}...")
    
    # Run the selected game as a subprocess
    subprocess.run([sys.executable, game_script])
