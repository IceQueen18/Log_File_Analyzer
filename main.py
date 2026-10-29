from pathlib import Path

path = Path("log.txt")

info = 0
error = 0
warning = 0
try: 
    contents = path.read_text()
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist")
else:
    #read the contents line by line
    lines = contents.splitlines()
    for line in lines:
        #check each word in the line for the index position
        #the index position for each word I am searching is at word[2]
        
        word = line.split()
        if len(word) < 3:
            continue
        if word[2] == 'INFO':
            info += 1

        if word[2] == 'ERROR':
            error +=1

        if word[2] == 'WARNING':
            warning += 1
    
    if lines == []:
        print(f"There are 0 entries in this file")
    else:    
        print(f"There are {info} INFO in this file")
        print(f"There are {error} ERROR in this file")
        print(f"There are {warning} WARNING in this file")
