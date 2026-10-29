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
    words = contents.splitlines()
    for word in words:
        fields = word.split()
        if fields[2] == 'INFO' in word:
            info += 1

        if fields[2] == 'ERROR' in word:
            error +=1

        if fields[2] == 'WARNING' in word:
            warning += 1
    
    if words == []:
        print(f"There are 0 entries in this file")
    else:    
        print(f"There are {info} INFO in this file")
        print(f"There are {error} ERROR in this file")
        print(f"There are {warning} WARNING in this file")
