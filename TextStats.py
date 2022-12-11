
# Author: <Moses Addai>

# A program that reads a text file and produces stats such as number lines, words per line etc. You can read the sonnet18.txt file
#which is in the repository

def main():
    fname = input("what file do you want to open? ")

    fileobj = open(fname, 'r')

       
    totw = 0
    totc = 0
    totl = 0
    for line in fileobj:
        totl = totl + 1
        splrt = line.split()
        lenrt = len(splrt)
        totw = totw + lenrt
        for j in splrt:
            lens2 = len(j)
            totc = totc + lens2


    numlines = totl
    avgwordspl = totw/totl
    avgchpw = totc/totw
       


    print("Total number of lines:",numlines,"Average words per line:",round(avgwordspl,ndigits =2), "Average characters per word",round(avgchpw,ndigits = 2))



        

   









main()
