import turtle
myTurtle=turtle.Turtle()

#bar code array for each number 0 to 9
barCodes = ["11000",
    "00011",
    "00101",
    "00110",
    "01001",
    "01010",
    "01100",
    "10001",
    "10010",
    "10100"]
            
zipCode = input('Enter a zip code: ')

def validateInput():
    try:
        val = int(zipCode)
        barCodeString=getBarCode()
        printBarCode(barCodeString)
    except ValueError:
        print("Please enter a valid zip code")


def getBarCode():
    zipCodeString = str(zipCode)
    barCode=""
    for ch in zipCodeString:
            barCode=barCode+barCodes[int(ch)]

    ZipCodeSum=sum(int(x) for x in str(zipCode)) #To sum all digits
    barCodeLastField=(10 -(ZipCodeSum % 10)) % 10
    barCode=barCode+barCodes[int(barCodeLastField)]
    return barCode           


def printBarCode(barCodeString):
    myTurtle.lt(90)
    myTurtle.pensize(3)
    
    for ch in barCodeString:
        if(ch=="1"):
            myTurtle.pu()
            myTurtle.goto(myTurtle.xcor()+10,0)
            myTurtle.pd()
            myTurtle.forward(50)
        else:
            myTurtle.pu()
            myTurtle.goto(myTurtle.xcor()+10,0)
            myTurtle.pd()
            myTurtle.forward(20)


validateInput()
