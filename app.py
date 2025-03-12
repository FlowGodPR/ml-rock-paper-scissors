import random  # Import random for the computer's choice
import gradio as gr  # Import Gradio for the web interface (installed using uv)

# TODO: Define the game logic function
def play(player_choice):
    """
    Rock, Paper, Scissors game logic.
    - The user selects Rock, Paper, or Scissors.
    - The computer randomly picks a choice.
    - The winner is determined based on the standard game rules.
    - Returns the game result.
    """
    
    options = ["Rock", "Paper", "Scissors"]  # Choices for both player and computer
    computer_choice = random.choice(options)  # Random choice for AI

    # Game rules: Determine winner
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win! 🎉"
    else:
        result = "Computer wins! 🤖"

    # Return formatted game output
    return f"You chose: {player_choice}\nComputer chose: {computer_choice}\n\n{result}"

# TODO: Set up the Gradio UI interface
ui = gr.Interface(
    fn=play,  # Calls the play function
    inputs=gr.Radio(["Rock", "Paper", "Scissors"], label="Choose your move"),  # User selects input
    outputs="text",  # Display result as text
    title="Rock, Paper, Scissors Game",  # Title of the app
    description="Play Rock, Paper, Scissors against an AI opponent."  # Short description
)

# TODO: Launch the app when script runs
if __name__ == "__main__":
    ui.launch()  # Start the web app
