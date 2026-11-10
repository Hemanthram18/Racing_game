import turtle

track = turtle.Screen()
track.bgcolor("cyan")


car_1 = turtle.Turtle()
car_2 = turtle.Turtle()
car_1.color("red")
car_2.color("yellow")

grass_1 = turtle.Turtle()
grass_2 = turtle.Turtle()
grass_1.speed("fastest")
grass_2.speed("fastest")

track_1 = turtle.Turtle()
track_2 = turtle.Turtle()
track_1.speed("fastest")
track_2.speed("fastest")




grass_1.fillcolor("green")
grass_1.begin_fill()
grass_1.penup()
grass_1.goto(-390,200)
grass_1.pendown()
for _ in range(4):
    grass_1.forward(800)
    grass_1.left(90)
grass_1.end_fill()



grass_2.fillcolor("green")
grass_2.begin_fill()
grass_2.penup()
grass_2.goto(-390,-200)
grass_2.pendown()
for _ in range(4):
    grass_2.forward(800)
    grass_2.right(90)
grass_2.end_fill()


track_1.seth(-45)
track_1.penup()
track_1.fillcolor("black")
track_1.begin_fill()
track_1.goto(-350,-80)
track_1.pendown()
for _ in range(2):
    
    track_1.circle(500, 90)  
    track_1.circle(100, 90)
track_1.end_fill() 
track_1.hideturtle()





track_2.seth(-45)
track_2.penup()
track_2.fillcolor("cyan")
track_2.begin_fill()
points = []


    
track_2.goto(-100,0)
track_2.pendown()
for _ in range(2):
    for _ in range(90):
        track_2.forward(2)
        track_2.left(1)
        points.append(track_2.pos())
    for _ in range(90):
            track_2.forward(1)
            track_2.left(1)
            points.append(track_2.pos())
 
   
track_2.end_fill() 
    
track_2.hideturtle()

track_2.penup()
track_2.goto(0,0)
print(points)


car_1.goto(-200,0)
car_2.goto(-300,0)

def out_of_track(car):
    for pt in points:
        if car.distance(pt)< 10:
            return True
    return False


car_1.penup()
car_2.penup()

def forward_1():
   
    car_1.forward(20)
    if out_of_track(car_1):
        car_1.goto(-200, 0)

def backward_1():
    
    car_1.backward(20)
    if out_of_track(car_1):
            car_1.goto(-200, 0)

def left_1():

    car_1.left(45)
    if out_of_track(car_1):
            car_1.goto(-200, 0)

def right_1():

    car_1.right(45)
    if out_of_track(car_1):
            car_1.goto(-200, 0)


track.onkey(forward_1,"w")
track.onkey(backward_1,"s")
track.onkey(right_1,"a")
track.onkey(left_1,"d")
turtle.listen()


def forward_2():
    car_2.forward(20)
    if out_of_track(car_2):
        car_2.goto(-300, 0)
    

def backward_2():
    car_2.backward(20)
    if out_of_track(car_2):
        car_2.goto(-300, 0)
        

def left_2():
    car_2.left(45)
    if out_of_track(car_2):
        car_2.goto(-300, 0)
        

def right_2():
    car_2.right(45)
    if out_of_track(car_2):
        car_2.goto(-300, 0)
        


track.onkey(forward_2,"i")
track.onkey(backward_2,"k")
track.onkey(right_2,"l")
track.onkey(left_2,"j")
turtle.listen()



turtle.done()
