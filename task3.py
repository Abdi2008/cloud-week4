with open("example.log", "r") as file:
    lines = file.readlines()
    print("Total lines:", len(lines))