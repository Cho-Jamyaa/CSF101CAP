################################
# Jamyang Choden
# 1ME
# 02230262
################################
# REFERENCES
#https://www.geeksforgeeks.org/how-to-read-from-a-file-in-python/
#https://pythonspot.com/read-file/
#https://youtu.be/yY-ILvG4uCo?feature=shared
################################
# SOLUTION
# Your Solution Score:49801
# Put your number here: 2
################################
def read_input():
    f = open('input_2_cap1.txt', 'r')
    print(f.read())
    f.close()

def pusher():
    return open('input_2_cap1.txt', 'r')

def calculate_score(docs):
    score=0
    marksboard={'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7} 
    for line in docs:
        code= line.strip()
        if code in marksboard:
            score+= marksboard[code]
    print("your overall marks:",score)


read_input()
calculate_score(pusher()) 