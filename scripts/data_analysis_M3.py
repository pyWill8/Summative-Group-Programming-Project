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


def visualize_data(collated_answers_path,n):
    if n not in [1, 2]:
        print("Error: Please n==1 or n==2")
        return
    
    file_list = [
        "data/answers_respondent_1.txt",
        "data/answers_respondent_2.txt",
        "data/answers_respondent_3.txt",
        "data/answers_respondent_4.txt",
        "data/answers_respondent_5.txt",
        "data/answers_respondent_6.txt",
        "data/answers_respondent_7.txt",
        "data/answers_respondent_8.txt",
        "data/answers_respondent_9.txt",
        "data/answers_respondent_10.txt",
        "data/answers_respondent_11.txt",
        "data/answers_respondent_12.txt",
        "data/answers_respondent_13.txt",
        "data/answers_respondent_14.txt",
        "data/answers_respondent_15.txt",
        "data/answers_respondent_16.txt",
        "data/answers_respondent_17.txt",
        "data/answers_respondent_18.txt",
        "data/answers_respondent_19.txt",
        "data/answers_respondent_20.txt",
        "data/answers_respondent_21.txt",
        "data/answers_respondent_22.txt",
        "data/answers_respondent_23.txt",
        "data/answers_respondent_24.txt",
        "data/answers_respondent_25.txt"
    ]
    all_answers = []
    for i in file_list:
        try:
            answers = extract_answers_sequence(i)
            if len(answers) == 100:
                all_answers.append(answers)
        except:
            pass

    if n == 1:
        mean = []
        for i in range(100):
            respond_count = 0 
            sum_of_answers = 0 
            for j in all_answers: 
                if j[i] != 0: 
                    respond_count = respond_count + 1
                    sum_of_answers = sum_of_answers + j[i]
            if respond_count > 0: 
                mean.append(sum_of_answers / respond_count)

        plt.scatter(range(1, 101), mean, color="blue", s=10)
        plt.title("Mean of Answers per Question (Scatter)")
        plt.xlabel("Question Number")
        plt.ylabel("Mean Value")
        plt.ylim(1, 4)
        plt.grid(True)
        plt.savefig("output/mean_scatter_plot.png") 
        plt.show()
    
    if n ==2: 
        for j in all_answers:
            plt.plot(range(1, 101), j, alpha=0.3)
        plt.title("Answer Lines of All Respondents")
        plt.xlabel("Question Number")
        plt.ylabel("Answer (1-4)")
        plt.ylim(1, 4)
        plt.grid(True)
        plt.savefig("output/respondent_lines_plot.png")  
        plt.show()
