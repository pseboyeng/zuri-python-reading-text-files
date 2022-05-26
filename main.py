
def read_file_content(filename): 
    file = open(filename,'r')
    return file.read()

def count_words():
    text = read_file_content("./story.txt")
    encouters = dict()
    wrds = text.split()

    for w in wrds:
        if w in encouters:
            encouters[w] += 1
        else:
            encouters[w] = 1

    return encouters

print(read_file_content("./story.txt"))
print(count_words())
