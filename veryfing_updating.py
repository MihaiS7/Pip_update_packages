def verifying(input_file):
    with open(input_file, "r+") as f:
        read = f.readlines()
        # print(len(read))
    return read


if __name__ == "__main__":
    verifying("requirements.txt")