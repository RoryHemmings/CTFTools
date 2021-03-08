'''

Flag extraction script
 - Searches files for brace pairs
 - Prints out flags in order of score which is the percentage of alphanumberic characters
 - padding is how far in front of each flag it checks

'''

import sys
import math

def create_flag(line, i, j):
    global padding
    numAlNumChars = 0
    begin = max(i - padding, 0) 
    flag = line[begin:j+1]
    for c in flag:
        if c.isalnum() or c == '_' or c == '{' or c=='}':
            numAlNumChars += 1

    score = numAlNumChars / len(flag) # will rank based on percentage of alphanumberic characters
    return (flag, score)

def search_file(path):
    ret = []
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            i = 0
            while i < len(line):
                if line[i] == '{':
                    j = i
                    while j < len(line) and line[j] != '}':
                        j += 1

                    if j != len(line):
                        ret.append(create_flag(line, i, j))
                    i = j
                i += 1

    return ret
                

def main():
    global padding
    if len(sys.argv) <= 1:
        print('Usage: py flagex.py <path> <padding:optional>')
        return

    path = sys.argv[1]
    if len(sys.argv) > 2:
        padding = int(sys.argv[2])
    else:
        padding = 10

    flags = search_file(path)
    flags = sorted(flags, key=lambda x: x[1])

    for flag in flags:
        print('score: {}%    {}'.format(round(flag[1]*100), flag[0]))

    print('Flags found: ' + str(len(flags)))

if __name__ == '__main__':
    main()

