
# Author: <Moses Addai>


# starter file for pixelart

from graphics import *
from math import *
from button import *


class Square:
    """ A Square object appears as a (colored-in) square.
        The Square knows when it's clicked on, what color it is.
        The Square also can highlight and unhighlight itself.
    """

    def __init__(self, win, center, size, color):
        """ win: GraphWin object
            center: Point object, specifying the center of the Square
            size: int or float, specifying the length of the side of the Square
            color: string specifying color of the Square

            Creates and draws the Square in the win object.
        """
        self.win = win
        self.size = size
        self.center = center
        self.color = color

        x,y = self.center.getX(),self.center.getY()
        self.xmin, self.xmax = x - self.size/2, x + self.size/2
        self.ymin, self.ymax = y - self.size/2, y + self.size/2
        
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.square = Rectangle(p1,p2)
        self.square.setFill(color)
        self.square.draw(win)
        

    def isClicked(self, p):
        """ p: Point object
            Returns True if p is inside the Square, False otherwise.
        """
##
      
        if self.xmin <= p.getX() <= self.xmax and self.ymin <= p.getY() <= self.ymax:
            return True
        else:
            return False
        

    def getColor(self):
        return self.color

    def changeColor(self, newcolor):
        """ newcolor: string specifying color
            Changes the color of the Square
        """
        self.color = newcolor
        self.square.setFill(newcolor)
        
        

    def highlight(self):
        """ Make the outline thick and red """

      
        self.square.setOutline("red")
        #self.square.draw(self.win)
        self.square.setWidth(5)
            

    def unhighlight(self):
        """ Make the outline thin and gray """

        
        self.square.setOutline("gray")
        #self.square.draw(self.win)
        self.square.setWidth(2)

class Canvas:
    """ Object filled with rows and columns of Squares.
        Canvas knows the current color, can determine which Square is clicked on,
        and changes that Square to the current color.s
    """

    def __init__(self, win, pt, rows, columns, size, color):
        """ win: GraphWin object
            pt: Point object, specifies lower-left coordinate.
            columns, rows: int indicating number of rows and columns of Square objects
            size: int or float, size of the Square objects
            color: initial color of the Square objects

            Creates and draws the Canvas in the win object.
        """

        self.win = win
        self.win.setCoords= win.setCoords
        self.color = color
        self.rows = rows
        self.columns = columns
        #self.center = center
        self.size = size
        self.pt = pt
        
        self.grid = {}

        
        #creating and storing square grid in a dictionary 
        
        for rw in range(self.rows):
            for cm in range(self.columns):
                center = Point(cm*self.size + self.size/2,rw*self.size + self.size/2)
                self.grid[(cm,rw)] = Square(win,center,size,color)
                
        update()
                
    
        


    def getSqColor(self, i, j):
        """ Gets the color of the Square at i-th column and j-th row """
        square = self.grid[(i,j)]

        return square.getColor()
    
    def changeCurrentColor(self, newcolor):
        """ Changes current color to newcolor. """
        self.color = newcolor
        
        

    def isClicked(self, p):
        """ p: Point object
            Returns True if p is inside the Canvas, False otherwise.
        """
        pt = self.pt
        
        if pt.getX() <= p.getX() <= self.columns*self.size and pt.getY() <= p.getY() <= self.rows*self.size:
            return True
        else:
            return False


    def changeSquare(self, p):
        """ p: Point object
            Changes the Square clicked by the Point p to the current color.
        """
        for quadnom, val in self.grid.items():
            if val.isClicked(p):
                val.changeColor(self.color)
            
        

class Controls:
    """ Control panel.
        Has the color palette, and the Draw button.
    """

    def __init__(self, win, P1, P2, sqsize):
        """ win: GraphWin object
            P1, P2: Point objects, lower-left and upper-right points
            sqsize : int or float, size of the squares in the color palette.
        """
        self.win = win
        self.P1 = P1
        self.P2 = P2
        self.sqsize = sqsize
        panel = Rectangle(P1,P2)
        panel.setFill("gold")
        panel.draw(self.win)
        
        #Creating buttons on panel and ensuring appropriate intervals between buttons
        self.sqlist = [ Square(win,Point(P1.getX()+sqsize+10,P1.getY()+sqsize-15),sqsize,"black"),
                        Square(win,Point(P1.getX()+sqsize+55,P1.getY()+sqsize-15),sqsize,"red"),
                        Square(win,Point(P1.getX()+sqsize+100,P1.getY()+sqsize-15),sqsize,"green"),
                        Square(win,Point(P1.getX()+sqsize+145,P1.getY()+sqsize-15),sqsize,"yellow")
                        ]
        self.selectedsquare = self.sqlist[0]
        self.selectedsquare.highlight()

        self.draw = Button(win,Point(P2.getX()-sqsize-70,P1.getY()+sqsize-15),sqsize+20, sqsize,"Draw")
        self.draw.activate()
        self.save = Button(win,Point(P2.getX()-sqsize-5,P1.getY()+sqsize-15),sqsize+20, sqsize,"Save")
        self.save.activate()
        self.fill = Button(win,Point(P2.getX()-sqsize-135,P1.getY()+sqsize-15),sqsize+20, sqsize,"Fill")
        self.fill.activate()
        self.block = Button(win,Point(P2.getX()-sqsize-200,P1.getY()+sqsize-15),sqsize+20, sqsize,"Block")
        self.block.activate()
        self.edit = Button(win,Point(P2.getX()-sqsize-265,P1.getY()+sqsize-15),sqsize+20, sqsize,"Edit Color")
        self.edit.activate()        
        


        
    def isClicked(self, p):
        """ p: Point object
            Returns True if p is inside the Controls, False otherwise
        """
        if self.P1.getX() <= p.getX() <= self.P2.getX() and self.P1.getY() <= p.getY() <= self.P2.getY():
            return True
        else:
            return False
        

    def ColorIsClicked(self, p):
        """ p: Point object
            If clicked on a color square in the color palette, return True.
            Otherwise return False.
        """        

        for square in self.sqlist:
            if square.isClicked(p):
                self.selectedsquare = square
                square.highlight()
                return True
            else:
                square.unhighlight()
        return False
    

    def getClickedColor(self, p):
        """ p: Point object inside a color square in the color palette.
            Return the color of the square.
        """
        for square in self.sqlist:
            if square.isClicked(p):
                return square.getColor()

    def DRAWClicked(self, p):
        """ True if p is inside the DRAW button, False otherwise. """
        
        return self.draw.clicked(p)
            

    def BlockClicked(self,p):
        """ True if p is inside the Block button, False otherwise. """
        return self.block.clicked(p)


    def editClicked(self,p):
        """ True if p is inside the Edit button, False otherwise. """
        return self.edit.clicked(p)

    
    def saveClicked(self,p):
        """ True if p is inside the Save button, False otherwise. """
        return self.save.clicked(p)
      
    



class PixelArt:
    """ Combines the following:
        A GraphWin object for this application
        The Canvas object
        The Controls object
        The drawing square where the pixel art will be drawn.
    """

    def __init__(self,columns):
        
        self.win = GraphWin("Pixel Art", 640, 640 + 50, autoflush = False)
        self.win.setCoords(0, 0, 640, 640+50)
        self.controls = Controls(self.win, Point(0,640), Point(640-50, 640+50), 40)
        self.drawing = Rectangle(Point(640-50, 640), Point(640, 640+50))
        self.drawing.setFill("white")
        self.drawing.draw(self.win)
        self.columns, self.rows = columns,columns
        self.canvas = Canvas(self.win, Point(0,0), self.columns, self.rows, 640/self.columns, "white")
        self.selectedcolor = "black"
        
        update()

    def drawPixelArt(self):
        """ Draws the pixel art in the center of the Drawing rectangle,
            with pixels corresponding to the squares in the Canvas.
        """
        canvas = self.canvas
        x, y = 600, 650
        for i in range(self.columns):
            for j in range(self.rows):
                p = Point(x+i*2, y+j*2)
                color = canvas.getSqColor(i,j)
                p.setOutline(color)
                p.draw(self.win)

        #self.win.getMouse()
        

    def handleClick(self, p):
        """ Handles a click, as appropriate. """

        # based on where you click, the color of a square in the panel or canvas will change, or you will obtain the pixe art

        controls = self.controls
        canvas = self.canvas
        self.columns, self.rows = 16, 16

        if canvas.isClicked(p):
            canvas.changeSquare(p)
            
        elif controls.ColorIsClicked(p):
            color = controls.getClickedColor(p)
            canvas.changeCurrentColor(color)
            self.selectedcolor = color
            

        elif controls.DRAWClicked(p):
            print("draw clicked")
            PixelArt.drawPixelArt(self)


        elif controls.BlockClicked(p):
            
            #computing the minimum x and y cordinates of the two clicks to draw colored block

            left = self.win.getMouse()
            leftx = int(left.getX()/canvas.size)
            #print(leftx)
            lefty = int(left.getY()/canvas.size)
            #print(lefty)
            
            right = self.win.getMouse()
            rightx = int(right.getX()/canvas.size)
            #print(rightx)
            righty = int(right.getY()/canvas.size)
            #print(righty)

            x1cord = min(leftx,rightx)
            #print(x1cord)
            y1cord = min(lefty,righty)
            #print(y1cord)
            x2cord = max(leftx,rightx)
            y2cord = max(lefty,righty)
##            
            i = x1cord
            j = y1cord
            


            for sqname, value in self.canvas.grid.items():
                if x1cord<=sqname[0]<= x2cord and y1cord<=sqname[1]<= y2cord:
                    value.changeColor(canvas.color)

           
        elif controls.saveClicked(p):
            #creating a textbox to collect user's filename for the saved drawing.
            win = GraphWin("File Name Box",300,300)
            win.setCoords(0,0,15,15)
            win.setBackground("orange")

            notice1 = Text(Point(5,8),"Enter File Name: ")
            notice1.setSize(15)
            notice1.draw(win)

            response = Entry(Point(10,8),10)
            response.draw(win)
            response.setText("PixelArt1.ppm")
            getresp = str(response.getText())
            print(getresp)

            okbutton = Button(win,Point(7,6),2,1,"Save")
            okbutton.activate()
             
            px = win.getMouse()
            
##            getresp = str(response1.getText())
##            print(getresp)

            if okbutton.clicked(px):
                print("image saved")
                newimage = Image(Point(250,250),500,500)
                


                x,y = 250,250
                for i in range(self.rows):
                    for j in range(self.columns):
                        color = canvas.getSqColor(i, j)
                        newimage.setPixel(x+i,y+j,color)
                print("it's done")        
                newimage.save(getresp)
                print("it's done")
                win.close()
                



        elif controls.editClicked(p):
            #creating a textbox to collect user's preferred color to change color palette.
            
            win = GraphWin("Change Palette",300,300)
            win.setCoords(0,0,15,15)
            win.setBackground("lightblue")

            notice = Text(Point(5,8),"Enter color: ")
            notice.setSize(15)
            notice.draw(win)

            response = Entry(Point(10,8),10)
            response.draw(win)

            apply = Button(win,Point(7,6),2,1,"Apply")
            apply.activate()

            px = win.getMouse()
            getresp = str(response.getText())
            if apply.clicked(px):
                print("clicked")
                controls.selectedsquare.changeColor(getresp)
                win.close()
                
            

        

        
        
        update()  # End this method with an a call to update the GraphWin object
 

    def runApp(self):
        """ Runs the PixelArt app """
        
        while self.win.isOpen():
            click = self.win.checkMouse()
            if click:
                self.handleClick(click)
        
def getRows():
    win = GraphWin("Rows Builder",600,300)
    win.setCoords(0,0,15,15)
    win.setBackground("lightgreen")

    notice = Text(Point(5,8),"Enter number of rows(10-30).Integers Only!: ")
    notice.setSize(15)
    notice.draw(win)

    response = Entry(Point(10,8),10)
    response.draw(win)
    response.setText("16")

    apply = Button(win,Point(7,6),2,1,"Ok")
    apply.activate()
    


    py = win.getMouse()
    if apply.clicked(py):
        win.close()
    
    getrows = response.getText()
    return int(getrows)
    
        


def run_PixelArt():
    # This function is already written for you.

    getrows = getRows()
    app = PixelArt(int(getrows))
    app.runApp()
        
          
if __name__ == "__main__":
    run_PixelArt()

    
