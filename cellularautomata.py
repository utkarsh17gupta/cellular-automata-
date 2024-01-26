import turtle
import math 

'''
Turtle set up for the canvas
'''
t = turtle.Turtle()
t.speed("fastest")
turtle.setup(1000,800)
t.penup()  # Lift the pen to move without drawing
t.goto(-turtle.window_width() / 2, turtle.window_height() / 2)
t.pendown()  # Lower the pen to start drawing

wn = turtle.Screen()



'''
creating the rule set by putting in the number
'''
rule = 195
rule = bin(rule)[2:]

while(len(rule) < 8):
    rule = '0'+rule

rule= [int(bit) for bit in rule]

print(rule)



'''
creating starter cells and setting size
'''
cells = [0 for _ in range(51)]
cells[math.ceil(len(cells)/2)] = 1
generation = 1

s = turtle.window_width() / len(cells)


'''
draws the generation given to it
'''
def drawGen(input):
    wn.tracer(0)
    for x in input:
        if(x == 1):
            t.begin_fill()

        for i in range(4):
            # drawing first side
            t.forward(s)  # Forward turtle by s units
            t.right(90)  # Turn turtle by 90 degree
        t.forward(s)

        t.end_fill()

    wn.update() 
    t.penup()  # Lift the pen to move without drawing
    t.goto((-turtle.window_width() / 2), (turtle.window_height() / 2)-s*generation)
    t.pendown()


def calcNewGen(cells):
    newcells = cells
    for i in range(len(cells)):
        if i == 0:
            curr = cells[i]
            next = cells[i+1]
            neighborhood = '0'+str(curr)+str(next)
        elif i == (len(cells)-1):
            prev = cells[i-1]
            curr = cells[i]
            neighborhood = str(prev)+str(curr)+'0'
        else:
            prev = cells[i-1]
            curr = cells[i]
            next = cells[i+1]
            neighborhood = str(prev)+str(curr)+str(next)
        
        newcells[i] = rule[int(neighborhood, 2)]
    
    return newcells


'''
driver
'''
while(True):
    drawGen(cells)
    generation += 1
    cells = calcNewGen(cells)