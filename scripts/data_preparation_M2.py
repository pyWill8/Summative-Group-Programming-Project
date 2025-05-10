import requests
import os
import gdown

urls = 'https://drive.google.com/file/d/1_hzGDdWO_wUzWJv8QyILUoATkonaKjbN/view?usp=drive_link, https://drive.google.com/file/d/1KTIqVJ-fJS0CQRsBlkrHs2shJELaDYtT/view?usp=drive_link, https://drive.google.com/file/d/1vVZFR-3Hml7K3px_kqXb6bCL8bI9Lx2z/view?usp=drive_link, https://drive.google.com/file/d/1P40bdTKG20_O6PRBrS10ttV1jDv4ISy7/view?usp=drive_link, https://drive.google.com/file/d/1wn9tZi7p0qhxaJCVlUq3HEHqfh4MwXAx/view?usp=drive_link, https://drive.google.com/file/d/1D9giruQfyi3AJpgl0Foh5nXgYvP9yihw/view?usp=drive_link, https://drive.google.com/file/d/1zgU1FzYzFahIr_eET6okTGl1vgy1928J/view?usp=drive_link, https://drive.google.com/file/d/1mNul8bOjPzHaB9-NBjqj9vz7UTtZnGrE/view?usp=drive_link, https://drive.google.com/file/d/1q_zMtU1qxSbyyNacVAjh206M9fYzGdiv/view?usp=drive_link, https://drive.google.com/file/d/1q1RJpZISGzjLHdeIm6BBxPKEHMO0B0Y9/view?usp=drive_link, https://drive.google.com/file/d/1utb3vb4WtIvaAa5yePLe6-9AsuzE-nMi/view?usp=drive_link, https://drive.google.com/file/d/1YFs4bbGcGdO-u45Yf68LQB5isPfswFCe/view?usp=drive_link, https://drive.google.com/file/d/10cxQSWZjFc6mMBtFj431pdS8dSkx3U1X/view?usp=drive_link, https://drive.google.com/file/d/1vsSrAONJvAxN2_DjRUKI9iQKR-0DP17U/view?usp=drive_link, https://drive.google.com/file/d/1NaBytU4sAbX6Jg0kjZbIwsSy6G8bWvSB/view?usp=drive_link, https://drive.google.com/file/d/1Ld4-WgSl5bVmHE3iybyhkHsWVu6xCUqz/view?usp=drive_link, https://drive.google.com/file/d/1DJE_CauzHGcmtKcRdhCRS5_1880RxBlR/view?usp=drive_link, https://drive.google.com/file/d/1LFKeHzav_4tKrdobfJfO8CSbBZ6ydJOy/view?usp=drive_link, https://drive.google.com/file/d/1UrFedwNdTKXHxXkrflfXi2luhLlB3P1M/view?usp=drive_link, https://drive.google.com/file/d/1auP2kGVwEs6Hux8b9WCv44cGzlnHxr6I/view?usp=drive_link, https://drive.google.com/file/d/19zltVSzJX7rfFal9gzZlNoPLjgJR2vTy/view?usp=drive_link, https://drive.google.com/file/d/1GOzRUEDCvQrpJV4NyivIGjLrlOqn1GgA/view?usp=drive_link, https://drive.google.com/file/d/1jG-tSvb1n60kxmWU9l1lIYqSd_kqZ608/view?usp=drive_link, https://drive.google.com/file/d/1cLEcabvp1JdY2IhkhosxAHuog1Z73vdY/view?usp=drive_link, https://drive.google.com/file/d/1wHlJNNYGvzSrtRM4g5uxt42Iitu7mQf9/view?usp=drive_link'
urls = urls.split(", ")

# As further formatting is required for the URLs, additional functions are used
# Converting Google Drive URLs to direct download links (Without it results in HTML text)
def convert_to_direct_link(url):
    # Extract the file ID from the URL
    file_id = url.split('/d/')[1].split('/view')[0]
    # Construct the direct download link
    return f"https://drive.google.com/uc?id={file_id}"

# Convert all URLs to direct download links
direct_urls = [convert_to_direct_link(url) for url in urls]

def download_answer_files(cloud_url, path_to_data_folder, respondent_index):
    # Downloading the answer files from Google Drive
    os.makedirs(path_to_data_folder, exist_ok=True)
    gdown.download(cloud_url, os.path.join(path_to_data_folder, 
                                           f"answers_respondent_{respondent_index}.txt"), quiet=False)


# Downloading all the answer files
path_to_data_folder = '/workspaces/Summative-Group-Programming-Project/data'
for i, url in enumerate(urls):
    download_answer_files(direct_urls[i], path_to_data_folder, i+1)

def collate_answer_files(data_folder_path):
    output_file = os.path.join('/workspaces/Summative-Group-Programming-Project/output', 'collated_answers.txt')
    with open(output_file, 'w') as outfile: # Open the output file in write mode
        # Iterating through all files in the data folder
        for filename in os.listdir(data_folder_path):
            if filename.startswith('answers_respondent_') and filename.endswith('.txt'): # To account for the temp files
                with open(os.path.join(data_folder_path, filename), 'r') as infile: # Open each input file
                    outfile.write(infile.read())
                    outfile.write("*\n")  # Add a separator between files

collate_answer_files(path_to_data_folder)
