#Ugyen T Jordan
# BE.1st year Instrumentation and control Engineering
# 02220249
###############################
# References
#
# How to handle file
# https://www.dataquest.io/blog/read-file-python/#:~:text=Python%20provides%20a%20built%2Din,we%20can%20manipulate%20its%20content
# https://www.w3schools.com/python/python_file_open.asp
#
# Defining a function
#https://docs.python.org/3/library/functions.html
#
###############################
# Solution
# Solution score:
#50267
##############################
# Read the input_9_cap1.txt file
# def read_input to read rounds data from a file
# def calculate_score to read rounds data from a ile
def read_input(filename='input_9_cap1.txt'):
          
    rounds = [] 
    # Initialize an empty list to store rounds data
    with open(filename, 'r') as file:
              
        for line in file:
            # Strip any leading and split the line into opponent's move and result
            opponent, result = line.strip().split()
            rounds.append((opponent, result))
    return rounds 

# Function to calculate total score based on rounds data
def calculate_score(rounds):
          
    moves_values = {'A': 1, 'B': 2, 'C': 3}  # Dict for move values
    round_scores = {'X': 0, 'Y': 3, 'Z': 6}  # Dict for round scores
    # Initialize total score to 0
    total_score = 0 
    for opponent_move, result in rounds:    
        # Check if opponent's move and result are valid
        
        if opponent_move in moves_values and result in round_scores:
            your_move = calculate_your_move(opponent_move, result)
            total_score += moves_values[your_move] + round_scores[result]
        else:
            print(f"Invalid input: '{opponent_move} {result}'")
    return total_score

# Function to calculate your move based on opponent's move and result
# Function to calculate your move based on opponent's move and result
def calculate_your_move(opponent_move, result):
    moves_mapping = {
        ('A', 'X'): 'C', ('A', 'Y'): 'A', ('A', 'Z'): 'B',
        ('B', 'X'): 'A', ('B', 'Y'): 'B', ('B', 'Z'): 'C',
        ('C', 'X'): 'B', ('C', 'Y'): 'C', ('C', 'Z'): 'A',
    }
    return moves_mapping.get((opponent_move, result), 'Invalid')


# Read rounds data from the input_9_cap1.txt
rounds_data = read_input()

# Calculate and print the total score based on the rounds data from file
if rounds_data:
    total_score = calculate_score(rounds_data)
    print(f"The total score in the end of the game: {total_score}")