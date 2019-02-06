from graphics import *
def main():
    x = 0
    y = 0
    win = GraphWin("Stair Case", 400, 400)
    while (x < win.getWidth()):
        p = Rectangle(Point(x,y), Point(x + 20, y + 20))
        p.draw(win)
        p.setFill("red")
        x = x + 20
        y = y + 20
        
    win.getMouse()
    win.close()

main()
