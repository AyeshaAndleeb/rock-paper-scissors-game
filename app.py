import streamlit as st
import random

# Define choices
choices = ["Rock", "Paper", "Scissors"]

# Initialize session state for scores
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0
if "games_played" not in st.session_state:
    st.session_state.games_played = 0

# Game logic
def decide_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        st.session_state.user_score += 1
        return "You win!"
    else:
        st.session_state.computer_score += 1
        return "Computer wins!"

# Streamlit App
st.title("Rock-Paper-Scissors Game with Points System 🎮")

# Display scores
st.write(f"**Games Played:** {st.session_state.games_played}")
st.write(f"**Your Score:** {st.session_state.user_score}")
st.write(f"**Computer's Score:** {st.session_state.computer_score}")

# User selection
user_choice = st.radio("Choose your option:", choices)

if st.button("Play"):
    # Computer selection
    computer_choice = random.choice(choices)
    
    # Determine and display winner
    result = decide_winner(user_choice, computer_choice)
    st.session_state.games_played += 1
    
    # Display choices
    st.write(f"**Your choice:** {user_choice}")
    st.write(f"**Computer's choice:** {computer_choice}")
    
    # Display result
    st.subheader(result)

# Reset scores
if st.button("Reset Scores"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.games_played = 0
    st.success("Scores reset successfully!")