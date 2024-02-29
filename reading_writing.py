
def verifying(input_file):
    with open(input_file, "r") as f:
        read = f.readlines()
        if not read:
            print("You do not have any outdated package! The program will stop. ")
            exit()
    return read

def writing(output_file, lines):
    with open(output_file, "w") as f:
        f.writelines(lines)

