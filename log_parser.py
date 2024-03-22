path_file = 'logfile-normal.log'
with open(path_file, 'r') as file:
    lines = file.readline()

    for line in lines:
        l = line.script()
