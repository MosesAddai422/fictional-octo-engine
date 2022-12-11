# Author: <Moses Addai>
# I chose this code because it shows a key backbone of linear regressions. Given different models can incorporate a multitude of data points,
#it is essential to identify important patterns that best describe the relationship between two or more variables in the model. Please run this file on my github(already there)as
#I import some graphic functions from an external graphics file

from math import *
from graphics import *

def window():
    win = GraphWin("Line of Best Fit", 600, 600)
    win.setBackground("white")
    # Lower-left corner coordinates are (0,0), upper-right coordinates are (10,10)
    win.setCoords(0, 0, 10, 10)
    return win

def backg(win):  
    bx = Rectangle(Point(0.7,0.5),Point(2.2,1.5))
    bx.setOutline("white")
    bx.setFill("white")
    bx.draw(win)
    
    button = Text(Point(1.5,1),"Done")
    button.draw(win)
    box = Rectangle(Point(1,0.7),Point(2,1.3))
    box.draw(win)
          
    num = 0
    xtot = 0
    ytot = 0
    count = 0
    xsqr = 0
    ysqr = 0
    xy = 0
            
    p1 = win.getMouse()
    p1.draw(win)
    
    x1 = p1.getX()
    y1 = p1.getY()
  
        # draws the points unless the user clicks on the Done button
        
    while not ((1 <= x1 <= 2) and (0.7 <= y1 <= 1.3)):   
        p2 = win.getMouse()
        p2.draw(win)
        
        
        x2 = p2.getX()
        y2 = p2.getY()

        #calulating summation of x,y,xy, xsquare and ysquare
        xtot = xtot + x1
        xsqr = xsqr + (x1*x1)
        ytot = ytot + y1 
        ysqr = ysqr + (y1*y1)
        
        xy = xy + (x1*y1)
        count = count + 1   
        p1 = p2
        x1 = p1.getX()
        y1 = p1.getY()
                      
    xavg = xtot/count
    yavg = ytot/count
    m = (xy - count*xavg*yavg)/(xsqr-count*(xavg**2))
    ygen = yavg + m*(0 - xavg)
    pnuevo = Point(0,ygen)

    ygen1 = yavg + m*(10 - xavg)
    pnuevo1 = Point(10,ygen1)

  
    #plots line if done button is clicked
    if ((1 <= x1 <= 2) and (0.7 <= y1 <= 1.3)):
        button.undraw()
        box.undraw()
        regyline = Line(pnuevo,pnuevo1)
        regyline.draw(win)
   
def main():
    k=window()
    instr = Text(Point(5,9),"Click on the spots to draw lines and when you are satisfied click Done!")
    instr.draw(k)
    m = 1
    if m > 0 :
        backg(k)
    input("Press <Enter> to quit.")
    k.close()
    
main()
    

