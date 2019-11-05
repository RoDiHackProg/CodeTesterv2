#!/usr/bin/python3

from tkinter import *

import os

import json


username = 'Pepe Palotes'

with open('data.json', 'r') as f:
    file = f.read()
data = json.loads(file)

def check(n):
    probs = {1: result1}
    probs[1].set(f'Running test {n}')
    os.system('./test.sh try.py correct.py generator.py')
    with open('result', 'r') as f:
        result = f.read().replace('\n', '')

    if result == 'All tests passed' and data[str(n)] != 'All tests passed':
        data['points'] += 10
        data[str(n)] = 'All tests passed'
        points.set(data['points'])
    else:
        data[str(n)] = result
        probs[n].set(result)
    
    with open('data.json', 'w') as f:
        json.dump(data, f)


window = Tk()
window.geometry('1000x500')

#-------------------------------HEADER-------------------------------------

header = LabelFrame(window, height=80, bd=0)#bd=5
header.pack(fill=X, side=TOP)

appName = Label(header, text='CodeTester', font=('Consolas', 40))
appName.pack(side=LEFT, padx=20)

name = Label(header, text=username, bd=5, font=('Consolas', 14), anchor=E)
name.pack(side=BOTTOM, fill=BOTH, padx= 20)

pointsWord =  Label(header, text='points', font=('Consolas', 20))
pointsWord.pack(side=RIGHT, padx=20)

points = StringVar()
counter =  Label(header, textvariable=points, font=('Consolas', 40))
counter.pack(side=RIGHT)
points.set(data['points'])

#-------------------------------PROBLEMS-------------------------------------

problems = LabelFrame(window, height=900, bd=0)
problems.pack(fill=BOTH, side=TOP)

problem1 = LabelFrame(problems, text='Problem 1', font=('Consolas', 15),height=90, bd=0)#bd=5
problem1.pack(fill=X, side=TOP, padx=20, pady=10)

p1Button = Button(problem1, text='Submit', command=lambda: check(1), width=15, font='Consolas', relief=RAISED)
p1Button.pack(side=LEFT, padx=10, pady=10)

result1 = StringVar()
result1.set(data['1'])
result1Label =  Label(problem1, textvariable=result1, font=('Consolas', 10), width=100, bg='grey80', height=2, anchor=W, padx=10)
result1Label.pack(side=LEFT, padx=30)

window.mainloop()
