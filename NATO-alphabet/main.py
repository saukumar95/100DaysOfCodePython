import pandas as pd
df = pd.read_csv("nato_phonetic_alphabet.csv")
is_running = True
phonetic_alphabets = {row.letter: row.code for (index, row) in df.iterrows()}
while is_running:
    user_input = input("Enter your name: ")
    try:
        new_value = [phonetic_alphabets[value.upper()] for value in user_input]
    except KeyError:
        print("Sorry! Only letters in the alphabets")
    else:
        print(new_value)
        is_running = False

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# Looping through dictionaries:
# for (key, value) in student_dict.items():
# Access key and value
# pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

