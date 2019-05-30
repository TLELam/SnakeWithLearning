import random
import time
def setup():
    background(255)
    size(900,900)
    frameRate(8)

obstacle_counter = 10
obstacles = 1
obstacle_exists = False
food_exists = False
snake_length = 1
obstacle_positions = [[(random.randint(10,20)*30)],[(random.randint(10,20)*30)],[(random.randint(1,5)*30)],[(random.randint(1,5)*30)]]
snake_positions = [[(random.randint(10,20)*30)],[(random.randint(10,20)*30)]]
dead = False
death_countdown = 0
shrink = 1
paused = False
restarting = True
countdown_timer = 3

def game_loop():
    global obstacles, obstacle_counter, obstacle_exists, food_exists, snake_length, obstacle_positions, snake_positions, dead, death_countdown, shrink, paused, restarting, countdown_timer
    background(255)
    obstacle()
    food()
    display_snake()
    if restarting:
        a.speed = 0
        fill(0)
        textSize(40)
        text(countdown_timer,445,430)
        time.sleep(1)
        if countdown_timer == 0:
            restarting = False
            #a.speed = 30
        countdown_timer -= 1
    strokeWeight(5)
    line(0,0,900,0)
    line(900,0,900,990)
    line(900,900,0,900)
    line(0,900,0,0)
    strokeWeight(1)
    fill(0)
    text(snake_length, 840, 40)
    a.drive()
    if paused:
        fill(230,0,0)
        text("Paused",400,420)
        
def restart():
    global obstacles, obstacle_counter, food_exists, snake_length,obstacle_positions, snake_positions, dead, death_countdown, shrink, paused, restarting, countdown_timer
    obstacles = 1
    obstacle_counter =10
    food_exists = False
    snake_length = 1
    obstacle_positions = [[(random.randint(10,20)*30)],[(random.randint(10,20)*30)],[(random.randint(1,5)*30)],[(random.randint(1,5)*30)]]
    snake_positions = [[(random.randint(10,20)*30)],[(random.randint(10,20)*30)]]
    dead = False
    death_countdown = 0
    shrink = 1
    paused = False
    restarting = True
    countdown_timer = random.randint(1,4)
    a.x = snake_positions[0][0]
    a.y = snake_positions[1][0]
    a.speed = 30
    a.direction = 1
    a.turned_this_frame = False
    
def food():
    global food_exists, food_x, food_y, snake_length
    if food_exists:
        fill(0,255,0)
        rect(food_x, food_y, 30, 30)
    else:
        create_food()
    if food_x == a.x and food_y == a.y:
        snake_length += 1
        food_exists = False
        
def create_food():
    global food_exists, food_x, food_y
    while True:
        food_x = random.randint(1,28)*30
        food_y = random.randint(1,28)*30
        notOverlappingSnake = False #Checks if food overlaps with snake
        notOverlappingObstacle = True #Checks if food overlaps with obstacle
        for i in range(snake_length):
            if food_x != snake_positions[0][i] or food_y != snake_positions[1][i]:
                notOverlappingSnake = True
        
        for i in range(obstacles):
            if obstacle_positions[0][i-1] <= food_x and food_x <= (obstacle_positions[0][i-1] + obstacle_positions[2][i-1]):
                if obstacle_positions[1][i-1] <= food_y and food_y <= (obstacle_positions[1][i-1] + obstacle_positions[3][i-1]):
                    notOverlappingObstacle = False
        #while loop continues to run until food was created that does not overlap
        if notOverlappingSnake and notOverlappingObstacle:
            break 
            
    fill(0,255,0)
    rect(food_x, food_y, 30, 30)
    food_exists = True
    
def obstacle():
    global obstacle_exists, obstacle_x, obstacle_y, obstacle_w, obstacle_h, dead, obstacles, obstacle_counter, obstacle_positions
    if obstacles == obstacle_counter:
        a.speed = 30
        for i in range (0, obstacles):
            fill(255,0,0)
            rect(obstacle_positions[0][i-1], obstacle_positions[1][i-1], obstacle_positions[2][i-1], obstacle_positions[3][i-1])
            if obstacle_positions[0][i-1] <= a.x < obstacle_positions[0][i-1] + obstacle_positions[2][i-1] and obstacle_positions[1][i-1] <= a.y < obstacle_positions[1][i-1] + obstacle_positions[3][i-1]:
                a.speed = 0
                dead = True
                obstacle_exists = False
    else:
        if dead != True:
            create_obstacle()

def create_obstacle():
    global obstacle_exists, obstacles, obstacle_x, obstacle_y, obstacle_h, obstacle_w
    obstacle_x = random.randint(1,28)*30
    obstacle_y = random.randint(1,28)*30
    obstacle_h = random.randint(1,5)*30
    obstacle_w = random.randint(1,5)*30
    
    obstacle_positions[0].append(obstacle_x)
    obstacle_positions[1].append(obstacle_y)
    obstacle_positions[2].append(obstacle_h)
    obstacle_positions[3].append(obstacle_w)
    if len(obstacle_positions[0]) > obstacle_counter:
        del obstacle_positions[0][0]
    if len(obstacle_positions[1]) > obstacle_counter:
        del obstacle_positions[1][0]
    if len(obstacle_positions[2]) > obstacle_counter:
        del obstacle_positions[2][0]
    if len(obstacle_positions[3]) > obstacle_counter:
        del obstacle_positions[3][0]

    obstacle_exists = True
    obstacles += 1
    
def display_snake():
    global positions, snake_length, shrink, dead, death_countdown, paused
    if dead:
        death_countdown += 1
    for i in range(0, snake_length):
        fill(60,180,180)
        if dead:
            if death_countdown > snake_length:
                snake_length = 1
                shrink = shrink*0.7
                rect(snake_positions[0][0]+(shrink-shrink*15)+10.5, snake_positions[1][0]+(shrink-shrink*15)+10.5, shrink*30, shrink*30)
            else:
                rect(snake_positions[0][i-1], snake_positions[1][i-1], 30, 30)
        else:
            rect(snake_positions[0][i-1], snake_positions[1][i-1], 30, 30)

class Snake_head():
    def __init__(self):
        global snake_positions
        self.x = snake_positions[0][0]
        self.y = snake_positions[1][0]
        self.speed = 30
        self.direction = random.randint(1,4)
        self.turned_this_frame = False
        
    def drive(self):
        global positions, snake_length, dead, paused
        if self.direction == 1:
            self.y -= self.speed
        elif self.direction == 2:
            self.x += self.speed
        elif self.direction == 3:
            self.y += self.speed
        elif self.direction == 4:
            self.x -= self.speed
        self.turned_this_frame = False
        
        for i in range (snake_length):
            if self.x == snake_positions[0][i-1] and self.y == snake_positions[1][i-1] and self.speed != 0:
                dead = True
                self.speed = 0
        
        if self.x >= width-30 or self.x <= 0:
            self.speed = 0
            dead = True
        if self.y >= height-30 or self.y <= 0:
            self.speed = 0
            dead = True
            
        if paused == False:    
            snake_positions[0].append(self.x)
            snake_positions[1].append(self.y)
            if len(snake_positions[0]) > snake_length:
                del snake_positions[0][0]
            if len(snake_positions[1]) > snake_length:
                del snake_positions[1][0]

a = Snake_head()

def keyPressed():
    global turns, paused
    #Checking which key was pressed
    if key == "w" and a.direction != 3 and a.turned_this_frame == False and paused == False:
        a.direction = 1
        a.turned_this_frame = True
    elif key == "d" and a.direction != 4 and a.turned_this_frame == False and paused == False:
        a.direction = 2
        a.turned_this_frame = True
    elif key == "s" and a.direction != 1 and a.turned_this_frame == False and paused == False:
        a.direction = 3
        a.turned_this_frame = True
    elif key == "a" and a.direction != 2 and a.turned_this_frame == False and paused == False:
        a.direction = 4
        a.turned_this_frame = True
    elif key == " ":
        if a.speed == 0:
            a.speed = 30
            paused = False
        elif a.speed == 30:
            a.speed = 0
            paused = True
    elif key == "r":
        restart()
        
def draw():
    global shrink, restarting, countdown_timer
    game_loop()
        
    
