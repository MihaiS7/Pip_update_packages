
def verifying(input_file):
    with open(input_file, "r") as f:
        read = f.readlines()
        # print(len(read))
        
    return read

def writing(output_file, lines):
    with open(output_file, "w") as f:
        f.writelines(lines)

