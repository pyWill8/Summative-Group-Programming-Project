def extract_answers_sequence(file_path): # Defines a function to extract the answer sequence from each respondent 
    """Reads answer respondent data files and creates a list to record each answer.
    Args:
        file_path: The name of the data file.
    Returns:
        A list of 100 numbers corresponding to the answer selected (1, 2, 3, 4, or 0).
    """
    answers = [] # Defines an empty list to store the answer sequence
    file = open(file_path, 'r') # Opens the file
    lines = file.readlines() # Reads all lines into a list
    file.close() # Closes the file

    for q in range(1, 101): # Initialises a loop to iterate through all 100 questions
        for i, line in enumerate(lines): # Loops through each line in the file
            if line.startswith(f"Question {q}."): # Checks to see if the line starts with 'Question {q}
                for j in range(1, 5): # Checks the next 4 lines for '[x]'
                    if lines[i + j].startswith("[x]"): # Sees if the line contains '[x]'
                        answers.append(j)  # Add 1, 2, 3 or 4 to the list of answers
                        break
                else:
                    answers.append(0)  # Adds 0 if there is no answer
                break
    return answers # Returns the list containing the answer sequence for each respondent
    
def write_answers_sequence(answers, n): # Defines a function to write the answer sequence to be saved for further use
    """Saves the list of answers to a file for a given respondent.
    Args:
        answers: The list of 100 numbers.
        n: The respondent ID number (e.g. 1 for respondent 1).
    Returns:
        Nothing however it saves the file.
    Raises:
        ValueError: if the list doesn't contain exactly 100 elements
    """
    if len(answers) != 100: # Checks if there are not 100 entries in the list of answers
        print("Error: List must contain 100 answers.") # Prints an error message
        return # Exits the function early
    file = open(f"answers_list_respondent_{n}.txt", 'w')  # Opens the file for writing
    file.write("\n".join(map(str, answers))) # Writes the answers to the file
    file.close() # Closes the file

    
for n in range(1, 26): # Loops over all 25 respondents
    file_path = f"data/answers_respondent_{n}.txt" # Creates the file path for each respondent
    answers = extract_answers_sequence(file_path) # Reads the quiz file for this respondent
    print(f"Answers for respondent {n}: {answers}") # Prints the list of 100 numbers
    write_answers_sequence(answers, n) # Saves the answers to a new file