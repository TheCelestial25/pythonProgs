import os

check_file = True

path_to_file = "C:/Users/spriy/Desktop/Python_horror/ichallengeyou.txt"

while check_file:
    file_exists = os.path.exists(path_to_file)
    if file_exists:
        print("Sample file exists")

        sample_file = open(path_to_file, 'r+')
        for line in sample_file:
            print(line)

        sample_file.write("\nYou may think that your system has been hijacked. \nBut...\nMake no mistakes. This PC is haunted. The work of a ghost it is...\nV^^^^^V\nAgli baar mujhe challenge mt krna!!!")
        sample_file.close

        check_file = False
