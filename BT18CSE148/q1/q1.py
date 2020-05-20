#question 1
import os,glob,re

user_input = input("Input regex:")
print("\nUser typed: '{}'. Input type: {}.".format(user_input, type(user_input)))
def is_valid_regex(regex_from_user: str, escape: bool) -> bool:
    try:
        if escape: re.compile(re.escape(regex_from_user))
        else: re.compile(regex_from_user)
        is_valid = True
    except re.error:
        is_valid = False
    return is_valid

folder_path = 'D:/python'
for filename in glob.glob(os.path.join(folder_path, '*.txt')):
    with open(filename, 'r') as file:
        
        # reading each line     
        for line in file: 
        # reading each word         
            for word in line.split():
                if is_valid_regex(user_input, escape=False):
                    regex = re.compile(user_input)
                    print("\nRegex compiled as '{}' with type {}.".format(repr(regex), type(regex)))

                    matches = regex. findall(word)
                    print('Mathces found:', matches)

                else:
                    print('\nThe regex was not valid, so no matches.')


file.close()