import os

def main():
    while True:
        dpath = input("Please enter the path to your dictionary: ")
        fpath = input("Please enter the path to the file to spell check: ")
        d = os.path.isfile(dpath)
        f = os.path.isfile(fpath)

        if d == True and f == True:
            misspelled_words = check_words(dpath, fpath)
            break

    print("\nThe following words were misspelled:\n----------")
    #print(misspelled_words) #comment out this line if you are using the code below

    #optional, if you want a better looking output

    for word in misspelled_words:   # erase these lines if you don't want to use them
        print(word)                 # erase these lines if you don't want to use them

    #------------------------ 


def linecheck(word, dlist):
    if word in dlist:
        return None
    else:
        return word

def check_words(dictionary, file_to_check):
    d = dictionary
    f = file_to_check
    dlist = {}  
    wrong = []  


    with open(d, 'r') as c:
        for line in c:
            (key) = line.strip()
            dlist[key] = ''

    with open(f, 'r') as i:
        for line in i:
            line = line.strip()
            fun = linecheck(line, dlist)
            if fun is not None:
                wrong.append(fun)

    return wrong

if __name__ == '__main__':
    main()