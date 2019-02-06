from graphics import *
def main():
    win = GraphWin()
    previous = Rectangle(Point(0,0), Point(20,20))
    color = color_rgb(255, 0, 100)
    previous.setFill(color)
    previous.draw(win)
    for i in range(9):
        new = previous#.clone()
        new.move(20,20)
        new.draw(win)

        previous = new

main()
