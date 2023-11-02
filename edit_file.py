def veryfing_update(input_file, output_file):
    with open(input_file, 'r') as f:
        reading_file=f.readlines()
        result = ''.join([f"pip install {x}" for x in reading_file])
    print(result)

    with open(output_file, 'w') as f:
        f.writelines(result)


veryfing_update("requirements.txt", "requirements1.txt")