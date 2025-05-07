from data_extraction_M1 import extract_answers_sequence, write_answers_sequence # Imports the functions for extracting and writing answer sequences

for n in range(1, 26):  # Loops over all 25 respondents
    file_path = f"data/answers_respondent_{n}.txt" # Creates the file path for each respondent
    answers = extract_answers_sequence(file_path) # Reads the quiz file for this respondent
    print(f"Answers for respondent {n}: {answers}")  # Prints the list of 100 numbers
    write_answers_sequence(answers, n)     # Saves the answers to a new file