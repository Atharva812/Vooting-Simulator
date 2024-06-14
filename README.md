# Voting Simulator

## Overview
The Voting Simulator is a graphical user interface (GUI) application designed to simulate a simple voting system. Users can cast their votes for a list of predefined candidates, and the application will determine and display the winner using the Boyer-Moore Majority Vote Algorithm. The application is built using Python with the Tkinter library for the GUI and Pygame for playing celebratory sounds when a winner is declared.

## Features
- **Vote Casting**: Users can select a candidate and cast their vote.
- **Winner Declaration**: The application determines the winner based on the majority of votes using the Boyer-Moore Majority Vote Algorithm.
- **User-Friendly Interface**: Easy-to-use interface with radio buttons for candidate selection and buttons for voting and declaring the winner.
- **Sound Effects**: Plays a celebratory sound when a winner is declared.

## Installation

### Prerequisites
- Python 3.x
- Tkinter (usually included with Python)
- Pygame

### Steps
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/voting-simulator.git
    cd voting-simulator
    ```

2. **Install required packages:**
    ```bash
    pip install pygame
    ```

3. **Run the application:**
    ```bash
    python voting_simulator.py
    ```

## Usage

### Launching the Application
Run the `voting_simulator.py` script using Python. The main window of the application will appear.

### Casting a Vote
1. Select a candidate by clicking on the corresponding radio button.
2. Click the "Vote" button to cast your vote.
3. A message box will appear confirming your vote.

### Declaring the Winner
1. After casting votes, click the "Declare Winner" button.
2. A message box will appear displaying the winner or stating that no candidate has a majority.

## Code Overview

### Main Components

- **VotingSimulator Class**: The main class that handles the GUI and voting logic.
  - `__init__(self, master)`: Initializes the GUI components and sets up the initial state.
  - `create_widgets(self)`: Creates and packs the GUI widgets (labels, radio buttons, buttons).
  - `cast_vote(self)`: Handles the logic for casting a vote.
  - `declare_winner(self)`: Determines the winner using the Boyer-Moore Majority Vote Algorithm and displays the result.

- **Boyer-Moore Majority Vote Algorithm**: Implemented within the `declare_winner(self)` method to find the majority element.

### Key Methods
- `cast_vote(self)`: Adds the selected candidate to the votes list and displays a confirmation message.
- `declare_winner(self)`: Determines the majority candidate using the Boyer-Moore algorithm and displays the result.

### Boyer-Moore Majority Vote Algorithm
The algorithm works in two phases:
1. **Candidate Selection Phase**: Iterates through the list of votes and identifies a potential majority candidate.
2. **Verification Phase**: Counts the occurrences of the potential majority candidate to verify if it is indeed the majority.

## Example

### Sample Output
- **Voting**: After selecting "Narendra Modi (Boss)" and clicking "Vote", a message box appears: "You voted for Narendra Modi (Boss)!".
- **Declaring Winner**: After voting, clicking "Declare Winner" might show: "The winner is Narendra Modi (Boss) with X votes!".


## Contact
For any questions or suggestions, please contact athu812talathi@gmail.com.
