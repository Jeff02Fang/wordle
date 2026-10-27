DataFile = open(r'C:\Users\u1040\OneDrive\桌面\Work\Project1\easy_words\easy_words.txt','r')
four = open(r'C:\Users\u1040\OneDrive\桌面\Work\Project1\easy_words\easy_4letter.txt','a')
five = open(r'C:\Users\u1040\OneDrive\桌面\Work\Project1\easy_words\easy_5letter.txt','a')
six = open(r'C:\Users\u1040\OneDrive\桌面\Work\Project1\easy_words\easy_6letter.txt','a')
line = DataFile.readline()
while line:
    length = 0
    length = len(line) - 1
    if length == 4:
        four.write(line)
    elif length == 5:
        five.write(line)
    elif length == 6:
        six.write(line)
    line = DataFile.readline()

DataFile.close()
four.close()
five.close()
six.close()