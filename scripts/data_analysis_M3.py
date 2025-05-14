from data_extraction_M1 import extract_answers_sequence
import os
import re
import matplotlib.pyplot as plt

def generate_means_sequence(collated_answers_path):
    with open(collated_answers_path, "r") as f:
        pieces = re.split(r'\n\s*\*\s*\n', f.read().strip())
    
    total_answers = []
    for i in range(len(pieces)):
        clear_answer_script = pieces[i].strip()
        line_count = len(clear_answer_script.splitlines())
        with open(f"temp_{i}.txt", "w") as f:
            f.write(clear_answer_script)

        answers = extract_answers_sequence(f"temp_{i}.txt")
        total_answers.append(answers)
        os.remove(f"temp_{i}.txt")

    mean = []
    for i in range(100):
        respond_count = 0
        sum_of_answers = 0
        for j in total_answers:
            if j[i] != 0:
                respond_count = respond_count + 1
                sum_of_answers = sum_of_answers + j[i]
        if respond_count > 0: 
            mean.append(sum_of_answers / respond_count)
        else:
            mean.append(0)

    return mean
    
print(generate_means_sequence("output/collated_answers.txt"))
