import csv
from array import *
with open('C:\\Users\\ADMIN\\Desktop\\exconvo.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)

    with open('C:\\Users\\ADMIN\\Desktop\\exconvo.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('name', 'msg'))
        writer.writerows(lines)
with open('C:\\Users\\ADMIN\\Desktop\\exconvo.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    ct = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        else:

            file = "C:\\Users\\ADMIN\\Desktop\\" + row[0] + ".csv"
            if ct == 0:
                ct = 1
                with open(file, 'w', newline='') as out_file:
                    writer = csv.writer(out_file)
                    writer.writerow((row[1], ''))
            else:
                with open(file, 'a', newline='') as out_file:
                    writer = csv.writer(out_file)
                    writer.writerow((row[1], ''))
line=0
cntt = array('i',[0,0,0,0,0,0])
punct= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

with open("C:\\Users\\ADMIN\\Desktop\\teen6.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        line += 1
        cntt[0] += len(row[0].split())
        x=0
        str = ""
        for val in row[0]:
            if val in punct:
                cntt[2]+=1
            else:
                str+=val
            x+=1
        cntt[1]+=int(x/len(row[0].split()))
        for word in str.split():
            with open('C:\\Users\\ADMIN\\Desktop\\slangdic.csv') as csv_file1:
                csv_reader1 = csv.reader(csv_file1, delimiter=',')
                #print("h",type(word))
                for row1 in csv_reader1:
                    #print(type(row1[0]))
                    #print(word == row1[0])
                    if word == row1[0]:
                        #print(word)
                        cntt[4] += 1

            duplicates = []
            #print(word)
            for char in word:
            ## checking whether the character have a duplicate or not
            ## str.count(char) returns the frequency of a char in the str
                if word.count(char) > 2:
                ## appending to the list if it's already not present
                    if char not in duplicates:
                        duplicates.append(char)
            cntt[3]+=len(duplicates)
            #print(duplicates)



cntt[0]=int(cntt[0]/line)
cntt[1]=int(cntt[1]/line)
#print(cntt[4])
with open("C:\\Users\\ADMIN\\Desktop\\ipclssf.csv", 'a', newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerow([cntt[0], cntt[1], cntt[2], cntt[3], cntt[4], cntt[5]])

line=0
cntt = array('i',[0,0,0,0,0,0])
punct= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

with open("C:\\Users\\ADMIN\\Desktop\\user6.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        line += 1
        print(line)
        cntt[0] += len(row[0].split())
        x=0
        str = ""
        for val in row[0]:
            if val in punct:
                cntt[2]+=1
            else:
                str+=val
            x+=1
        cntt[1]+=int(x/len(row[0].split()))
        for word in str.split():
            with open('C:\\Users\\ADMIN\\Desktop\\slangdic.csv') as csv_file1:
                csv_reader1 = csv.reader(csv_file1, delimiter=',')
                #print("h",type(word))
                for row1 in csv_reader1:
                    #print(type(row1[0]))
                    #print(word == row1[0])
                    if word == row1[0]:
                        #print(word)
                        cntt[4] += 1

            duplicates = []
            #print(word)
            for char in word:
            ## checking whether the character have a duplicate or not
            ## str.count(char) returns the frequency of a char in the str
                if word.count(char) > 2:
                ## appending to the list if it's already not present
                    if char not in duplicates:
                        duplicates.append(char)
            cntt[3]+=len(duplicates)
            #print(duplicates)



cntt[0]=int(cntt[0]/line)
cntt[1]=int(cntt[1]/line)
#print(cntt[4])
with open("C:\\Users\\ADMIN\\Desktop\\ipclssf.csv", 'a', newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerow([cntt[0], cntt[1], cntt[2], cntt[3], cntt[4], cntt[5]])

'''''
cntt[0] avg no of words per sentence
cntt[1] avg no of charac per word
cntt[2] no of punctuations used
cntt[3] occurrence of duplicate charac in word
cntt[4] slang,abbr,acronym
cntt[5] no of emoji
'''''