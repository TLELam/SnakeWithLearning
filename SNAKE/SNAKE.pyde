#Imports
import random
import time
import math

#Setting window size and a more arcade-like framerate
def setup():
    background(255)
    size(900,900)
    frameRate(8)

#
addedFrameRate = 0
#Number of obstacles on screen
obstacle_counter = 1
#Number of obstacles that there should be
obstacles = 1
#Whether food has been created
food_exists = False
#Snake length
snake_length = 1
#A 2 dimensional array to store the x and y coordinates as well as the width and height of the obstacles
obstacle_positions = [[(random.randint(10,20)*30)],[(random.randint(10,20)*30)],[(random.randint(1,5)*30)],[(random.randint(1,5)*30)]]
#A 2 dimensional array to store the x and y coordinates of the snake
snake_positions = [[(random.randint(10,20)*30)],[(random.randint(10,20)*30)]]
#Whether the snake is currently dead
dead = False
#Whether the snake has gone through the process of dying
died = False
#How many frames it has been since the snake died
death_countdown = 0
#An int to facilitate the snakes death animation
shrink = 1
#Whether the game is paused
paused = False
#Whether the game is in the process of restarting
restarting = True
#Whether a triva question has been created
question_created = False
#Number of deaths this playthrough
deaths = 0
#The int displayed center screen when restarting or starting
countdown_timer = 3
high_score = []
sys.setrecursionlimit(1500)

#A function to resest the playing area if and when the player answers a question correctly
def resume():
    global obstacles, obstacle_counter, food_exists, snake_length, obstacle_positions, snake_positions, dead, died, death_countdown, shrink, paused, restarting, countdown_timer, addedFrameRate, question_created, rand1, rand2
    #A loop to randomly generate the snake position
    while True:
        snake_positions = [[random.randint(7,23)*30],[random.randint(7,23)*30]]
        check = 0
        #Looping through all obstacles and checking if the random position is too close to an one
        for i in range (0, obstacle_counter):
            if (obstacle_positions[0][i-1] - 90 < snake_positions[0][0] < obstacle_positions[0][i-1] + obstacle_positions[2][i-1] + 90) and (obstacle_positions[1][i-1] - 90 < snake_positions[1][0] < obstacle_positions[1][i-1] + obstacle_positions[3][i-1] + 90):
                #A boolean cannot be used to end the loop because it would end upon finding a single obstacle that the snake is not too close to, even if it is too close to other obstacles
                check += 1
                break
                
        if check == 0:
            #The snake is not too close to any obstacles so the loop is ended
            break
    
    #Reopulating the positions array with identical coordinates as the snake starts in one spot
    for i in range(1, snake_length):
        snake_positions[0].append(snake_positions[0][0])
        snake_positions[1].append(snake_positions[1][0])
    
    #Reseting necesarry variables
    dead = False
    died = False
    death_countdown = 0
    shrink = 1
    paused = False
    restarting = True
    countdown_timer = 3
    a.x = snake_positions[0][0]
    a.y = snake_positions[1][0]
    a.speed = 30
    a.direction = random.randint(1,4)
    a.turned_this_frame = False
    
#A function to display the trivia question when needed
def display_trivia():
    global dead, deaths, ans_location, answer_clicked, answer, answer_y, num1, num2, question, rand1, rand2, created
    #Variable declaration
    answer_clicked = False
    #Making sure there is a quesion generated before trying to display one
    if question_created:
        #Getting the randomly chosen location for the answer and assigning y coordinates for the buttons accordingly
        if ans_location == 1:
            answer_y = 150
            y1 = 250
            y2 = 350
        elif ans_location == 2:
            answer_y = 250
            y1 = 150
            y2 = 350
        elif ans_location == 3:
            answer_y = 350
            y1 = 150
            y2 = 250
        
        fill(0,0,255)
        #The width of the buttons must increase with length of the answer
        #To determine the number of digits we take the base 10 log of the answer and round up
        if answer != "0" and answer != "1" and answer != "-1":
            #Log 0 will return an error
            #answer must be converted to positive to be logged
            ans_digits = math.log10(abs(int(answer)))
            ans_digits = math.ceil(ans_digits)
        else:
            ans_digits = 1
        #If the answer is negative, more space is needed for the negative sign
        if answer < 0:
            ans_digits += 1
            
        #Creating the buttons
        rect(50, answer_y, 25*ans_digits,50)
        #The wrong answers have a chance of being negative even if the answer isn't. If it is, the button must be larger to accomodate the negative sign
        if int(rand1) >= 0:
            rect(50, y1, 25*ans_digits, 50)
        else:
            rect(50, y1, 25*(ans_digits+1), 50)
        if int(rand2) >= 0:
            rect(50, y2, 25*ans_digits, 50)
        else:
            rect(50, y2, 25*(ans_digits+1), 50)
        
        #Adding the text
        fill(255)
        text(answer, 50, answer_y + 45)
        text(rand1, 50, y1 + 45)
        text(rand2, 50, y2 + 45)
        
        #Displaying the question itself
        fill(0,0,150)
        text(question, 50, 70)
        
        #Notifying the player if they clicked the answer
        if answer_clicked:
            fill(0,0,255)
            rect (50, answer_y, 25*(deaths+1), 50)
            fill(0,255,0)
            text("Correct!", 50, answer_y)
        
        #Button code
        if mousePressed == True:
                if 50 < mouseX < 50 + (25*(deaths+2)) and answer_y < mouseY < answer_y + 50:
                    #They clicked the answer
                    answer_clicked = True
                    fill(0,255,0)
                    text("Correct!", 50, answer_y)
                    fill(0,0,255)
                    rect (50, answer_y, 25*(deaths+1), 50)
                    #Resume game
                    resume()
                    
                if 50 < mouseX < 50 + (25*(deaths+1)) and y1 < mouseY < y1 + 50:
                    #They clicked the wrong one
                    fill(0,0,255)
                    rect (50, y1, 25*(deaths+1), 50)
                    text ("Wrong!", 50, y1)
                    #Game over
                    game_over()
                    
                    
                elif 50 < mouseX < 50 + (25*(deaths+2)) and y2 < mouseY < y2 + 50:
                    #They clicked the wrong one
                    fill(0,0,255)
                    rect (50, y2, 25*(deaths+1), 50)
                    text ("Wrong!", 50, y2)
                    #Game over
                    game_over()
   
#A function to create the trivia question                
def create_trivia():
    global death_countdown, dead, deaths, question_created
    #Randomly generating the operation for the math question
    operation = random.randint(1,4)
    if operation == 1:
        selection = "addition"
    elif operation == 2:
        selection = "subtraction"
    elif operation == 3:
        selection = "multiplication"
    elif operation == 4:
        selection = "division"
    
    #Randomly generates two numbers to use for the question. A digit is added each death
    num1 = random.randint(1,10**(deaths)-1)
    num2 = random.randint(1,10**(deaths)-1)
    #Checking whcih operation has been selected
    if selection == "division":
        #A loop to keep the quotients integers 
        while num1 % num2 != 0:
            num1 = random.randint(1,10**(deaths)-1)
            num2 = random.randint(1,10**(deaths)-1)
            
    #Formatting the question according to the operation
    if selection == "addition":
        question = str(num1) + "+" + str(num2)
        answer = num1 + num2
        answer = str(answer)
    elif selection == "subtraction":
        question = str (num1) + "-" + str(num2)
        answer = num1 - num2
        answer = str(answer)
    elif selection == "multiplication":
        question = str(num1) + "x" + str(num2)
        answer = num1 * num2
        answer = str(answer)
    elif selection == "division":
        question = str(num1) + "/" + str(num2)
        answer = num1 / num2
        answer = str(answer)
        
    #Randomly picking which button will have the answer
    ans_location = random.randint (1,3)
    #Y cooridinates for the buttons
    y = 150
    answer_y = 0
    y1 = 0
    y2 = 0
    
    #Randomly generating a wrong answer close to the answer
    rand1 = random.randint(int(answer) - 10, int(answer) + 10)
    rand1 = str(rand1)
    #Making sure it isn't the answer
    if rand1 == answer:
        while rand1 == answer:
            rand1 = random.randint(int(answer) -10 , int(answer) + 10)
            rand1 = str(rand1)
    
    #Randomly generating another wrong answer that is a multiple of 5 off
    #This reduces the chance of being able to guess answers solely by the last digit
    rand2 = int(answer) + random.randint(-deaths + 1, deaths)*5
    rand2 = str(rand2)
    #Making sure it's not equal to the answer or the other wrong answer
    if rand2 == answer or rand2 == rand1:
        while rand2 == answer or rand2 == rand1:
            rand2 = int(answer) + random.randint(-deaths + 1, deaths)*5
            rand2 = str(rand2)
    
    #Setting question_created to be true
    question_created = True
    #Outputting all the new variables we will use in display_trivia()
    global ans_location, answer, answer_y, num1, num2, question, rand1, rand2, question_created
    
#All the code to run the snake game. This can be called in the draw function depending on whether the game is supposed to be running
def game_loop():
    global obstacles, obstacle_counter, obstacle_exists, food_exists, snake_length, obstacle_positions, snake_positions, dead, death_countdown, shrink, paused, restarting, countdown_timer
    #Creating the background and the borders
    background(255)
    strokeWeight(60)
    line(0,0,900,0)
    line(900,0,900,990)
    line(900,900,0,900)
    line(0,900,0,0)
    strokeWeight(1)
    #Running game related functions
    obstacle()
    food()
    display_snake()
    if dead:
        display_trivia()
    on_death()
    change_speed()
    #If the game is restarting, we display countdown_timer and reduce it every frame
    if restarting:
        a.speed = 0
        fill(0)
        textSize(40)
        text(countdown_timer,445,430)
        time.sleep(1)
        if countdown_timer == 0:
            restarting = False
        countdown_timer -= 1
        
    #Displaying the current score
    fill(0)
    text(snake_length, 810, 80)
    
    #Checking if the game has been paused
    if paused:
        fill(230,0,0)
        text("Paused",400,420)
    
    #After everything else is done, the snake moves
    a.drive()

#A function to restart the game
def restart():
    global obstacles, obstacle_counter, food_exists, snake_length,obstacle_positions, snake_positions, dead, died, death_countdown, shrink, paused, restarting, countdown_timer, addedFrameRate
    #As this is just a more intense resume, we reset a few more variables and then call the resume() function
    frameRate(8)
    addedFrameRate = 0
    obstacles = 1
    obstacle_counter = 1
    obstacle_positions = [[(random.randint(10,20)*30)],[(random.randint(10,20)*30)],[(random.randint(1,5)*30)],[(random.randint(1,5)*30)]]
    food_exists = False
    snake_length = 1
    resume()

#A function for displaying and managing the food
def food():
    global food_exists, food_x, food_y, snake_length
    #If food has been created, display; else, created it
    if food_exists:
        fill(0,255,0)
        rect(food_x, food_y, 30, 30)
    else:
        create_food()
    
    #If the head of the snake runs over the food, delete the food and grow the snake
    if food_x == a.x and food_y == a.y:
        snake_length += 1
        food_exists = False

#A function to create food
def create_food():
    global food_exists, food_x, food_y
    #Continually generates new positions until one is found that does not overlap the snake or an obstacle
    while True:
        food_x = random.randint(1,28)*30
        food_y = random.randint(1,28)*30
        notOverlappingSnake = False #Checks if food overlaps with snake
        notOverlappingObstacle = True #Checks if food overlaps with obstacle
        for i in range(snake_length):
            if food_x != snake_positions[0][i] or food_y != snake_positions[1][i]:
                notOverlappingSnake = True
        
        #Loops through all obstacles
        for i in range(obstacle_counter):
            if obstacle_positions[0][i-1] <= food_x and food_x <= (obstacle_positions[0][i-1] + obstacle_positions[2][i-1]):
                if obstacle_positions[1][i-1] <= food_y and food_y <= (obstacle_positions[1][i-1] + obstacle_positions[3][i-1]):
                    notOverlappingObstacle = False
        #while loop continues to run until food was created that does not overlap
        if notOverlappingSnake and notOverlappingObstacle:
            break 
    #Displays the food for the frame until food() takes over
    fill(0,255,0)
    rect(food_x, food_y, 30, 30)
    food_exists = True

#A function to display and manage obstacles
def obstacle():
    global obstacle_x, obstacle_y, obstacle_w, obstacle_h, dead, obstacles, obstacle_counter, obstacle_positions
    #Loops through every obstacle, displays it, and checks if the snake has hit it
    for i in range (0, obstacles):
        fill(255,0,0)
        rect(obstacle_positions[0][i-1], obstacle_positions[1][i-1], obstacle_positions[2][i-1], obstacle_positions[3][i-1])
        if obstacle_positions[0][i-1] <= a.x < obstacle_positions[0][i-1] + obstacle_positions[2][i-1] and obstacle_positions[1][i-1] <= a.y < obstacle_positions[1][i-1] + obstacle_positions[3][i-1]:
            #The snake hit an obstacle, so it must die
            a.speed = 0
            dead = True
    #If there aren't enough obstacles, create one. If there are, let the game begin
    if obstacles != obstacle_counter:
        if dead != True:
            create_obstacle()
    else:
        if dead == False and paused == False:
            a.speed = 30

#A function to create obstacles
def create_obstacle():
    global obstacle_exists, obstacles, obstacle_x, obstacle_y, obstacle_h, obstacle_w
    #
    while True:
        #Randomly creates an obstacle
        obstacle_x = random.randint(2,23)*30
        obstacle_y = random.randint(2,23)*30
        obstacle_h = random.randint(1,5)*30
        obstacle_w = random.randint(1,5)*30
        
        check = 0
        #Loops through the whole snake to check if the obstacle is colliding
        for i in range (0, snake_length-1):
            if (obstacle_x - 90 < snake_positions[0][i-1] < obstacle_x + obstacle_w + 90) and (obstacle_y - 90 < snake_positions[1][i-1] < obstacle_y + obstacle_h + 90):
                #It is colliding, se we must try a new obstacle
                check += 1
                #Break to prevent unnecessary checks
                break
        #Loops through the other obstacles to check if the obstacle is colliding
        for i in range (0, obstacle_counter):    
            if (obstacle_x - 30 < obstacle_positions[0][i-1]  < obstacle_x + obstacle_w + 30) and (obstacle_y - 30 < obstacle_positions[1][i-1] < obstacle_y + obstacle_h + 30):
                #It is colliding, se we must try a new obstacle
                check += 1
                break
            
        if check == 0:
            #The obstacle is valid and we can leave the loop
            break
        
    #Adding the obstacle to the array
    obstacle_positions[0].append(obstacle_x)
    obstacle_positions[1].append(obstacle_y)
    obstacle_positions[2].append(obstacle_h)
    obstacle_positions[3].append(obstacle_w)
    #Trimming the array to only hold as many obstacles as we need
    if len(obstacle_positions[0]) > obstacle_counter:
        del obstacle_positions[0][0]
    if len(obstacle_positions[1]) > obstacle_counter:
        del obstacle_positions[1][0]
    if len(obstacle_positions[2]) > obstacle_counter:
        del obstacle_positions[2][0]
    if len(obstacle_positions[3]) > obstacle_counter:
        del obstacle_positions[3][0]

    #Increasing the obstacle count now that we added one
    obstacles += 1
    
#A function to display the snake
def display_snake():
    global positions, snake_length, shrink, dead, death_countdown, paused
    #Counting the number of frames since death
    if dead:
        death_countdown += 1
    #looping through and displaying each segment of the snake
    for i in range(0, snake_length):
        fill(60,180,180)
        #Once the death_countdown is greater than snake length, that means all segments have 'caught up' to the place where it died
        #Once all the segments have caught up we display the snake using the shrink value to add our death animation
        if dead:
            if death_countdown > snake_length:
                shrink = shrink*0.7
                rect(snake_positions[0][0]+(shrink-shrink*15)+10.5, snake_positions[1][0]+(shrink-shrink*15)+10.5, shrink*30, shrink*30)
            else:
                rect(snake_positions[0][i-1], snake_positions[1][i-1], 30, 30)
        else:
            #If the snake isn't dead, we display it normally
            rect(snake_positions[0][i-1], snake_positions[1][i-1], 30, 30)

def change_speed():
    global addedFrameRate, obstacle_counter
    defaultFramerate = 8
    if (snake_length % 5) == 0:
        addedFrameRate = (snake_length / 5)
        frameRate((defaultFramerate + addedFrameRate))
        #Increasing the number of obstacles every 5 length
        obstacle_counter = 1 + addedFrameRate

#Initializing our snake head
class Snake_head():
    #Populating the variables
    def __init__(self):
        global snake_positions
        self.x = snake_positions[0][0]
        self.y = snake_positions[1][0]
        self.speed = 30
        #Randomly choosing a direction
        self.direction = random.randint(1,4)
        #A boolean to keep track of whether the snake has turned this frame. This is used later to prevent turning multiple times a frame
        self.turned_this_frame = False
        
    #Driving the snake head    
    def drive(self):
        global positions, snake_length, dead, paused
        #Changing the position based on speed and direction
        if self.direction == 1:
            self.y -= self.speed
        elif self.direction == 2:
            self.x += self.speed
        elif self.direction == 3:
            self.y += self.speed
        elif self.direction == 4:
            self.x -= self.speed
        self.turned_this_frame = False
        
        #Checking to see if it ran into itself or a wall
        for i in range (snake_length):
            if self.x == snake_positions[0][i-1] and self.y == snake_positions[1][i-1] and self.speed != 0:
                dead = True
                self.speed = 0
        
        if (self.x >= width-30 and self.direction == 2) or (self.x < 30 and self.direction == 4):
            self.speed = 0
            dead = True
        if (self.y >= height-30 and self.direction == 3) or (self.y < 30 and self.direction == 1):
            self.speed = 0
            dead = True
            
        #Managing the array of positions
        if paused == False:   
            #Adding the position of the snake's head to the array
            snake_positions[0].append(self.x)
            snake_positions[1].append(self.y)
            #Deleting the oldest position to keep the array trimmed to the snake's length
            if len(snake_positions[0]) > snake_length:
                del snake_positions[0][0]
            if len(snake_positions[1]) > snake_length:
                del snake_positions[1][0]
                
#Initializing our snake head
a = Snake_head()

#Managing user input
def keyPressed():
    global turns, paused
    #Checking which key was pressed
    #Direction related keys change the direction
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
    
    #Spacebar will pause or unpause
    elif key == " ":
        if a.speed == 0:
            a.speed = 30
            paused = False
        elif a.speed == 30:
            a.speed = 0
            paused = True
            
    #R will restart the game
    elif key == "r":
        restart()
        
def save_old_high_scores():
    global snake_length, high_score
    highScoreFile = open("high_scores.txt", "r")
    for i in range(10):
        high_score.append(int(highScoreFile.readline()))
    highScoreFile.close
save_old_high_scores()

def check_high_scores():
    global snake_length, high_score
    check = False
    highScoreFile = open("high_scores.txt", "r")
    for i in range(len(high_score)):
        if snake_length > high_score[i]:
            check = True
    highScoreFile.close    
    return check

def save_new_high_scores():
    global snake_length, high_score
    highScoreFile = open("high_scores.txt", "w")
    high_score.sort(reverse = True)
    for i in range(len(high_score)):
        highScoreFile.writelines(str(high_score[i]) + "\n") 
    highScoreFile.close
    
def replace_high_scores():
    global snake_length, high_score    
    high_score.sort(reverse = True)
    del high_score[-1]
    high_score.append(snake_length)
    save_new_high_scores()

    
def display_high_scores():
    global high_score
    text("High scores:", 350, 150)
    for i in range(len(high_score)):
        text(high_score[i], 425, 200 + i*50)

#A function for doing things once and only once upon death of the snake        
def on_death():
    global dead, died, deaths
    #If the snake is dead but has not died yet, it runs
    if dead and died == False:
        #Setting died to True to prevent the code from running again
        died = True
        #Adding a death
        deaths += 1
        #Creating our trivia question
        create_trivia()

def game_over():
    global start_game
    if check_high_scores():
        replace_high_scores()
    start_game = False
    restart()
    
start_game = False
display_high_score = False
display_instructions = False

def main_menu():
    global shrink, restarting, countdown_timer, start_game, display_high_score, display_instructions

    fill("#00aaaa")
    rect(0,0,900,900) #creates a turqoise background to "hide" what isn't the menu
    
    fill("#aaaaaa")
    rect(350,150,200,50)
    fill("#000000")
    textSize(18)
    text("Start", 420, 180)
    #similar if statement to the previous one
    if (mouseX >= 350) and (mouseX <= 550) and (mouseY >= 150) and (mouseY <= 200) and mousePressed:
        start_game = True
        
    fill("#aaaaaa")
    rect(350,300,200,50)
    fill("#000000")
    text("Instructions",400,330)
    if (mouseX >= 350) and (mouseX <= 550) and (mouseY >= 300) and (mouseY <= 350) and mousePressed:
        display_instructions = True
    
    fill("#aaaaaa")
    rect(350,450,200,50)
    fill("#000000")
    text("High Scores", 400, 480)
    if (mouseX >= 350) and (mouseX <= 550) and (mouseY >= 450) and (mouseY <= 500) and mousePressed:
        display_high_score = True
            
    fill("#aaaaaa")
    rect(350,600,200,50)
    fill("#000000")
    text("Quit", 420, 630)
    if (mouseX >= 350) and (mouseX <= 550) and (mouseY >= 600) and (mouseY <= 650) and mousePressed:
        exit()    
    
def instructions_screen():
    global display_instructions
    fill("#aaaaff")
    rect(0,0,900,900) #A new "background" for the instructions screen
    
    fill("#aaaaaa")
    rect(350,700,200,50)
    fill("#000000")
    text("Back", 430, 730)
    text ("Snake with Learning is an educational game by the legendary Team 4 Star", 20, 100)
    text ("This game plays like traditional snake where the objective is to move the snake to get food", 20, 150)
    text ("(Green Boxes)", 20, 200)
    text ("'d' right, 's' down, 'a' left, 'w' up", 20, 250)
    text ("The user must avoid the border and the various objects that will appear on screen", 20, 300)
    text ("When the food is 'eaten' the snake grows larger and the user must avoid running into themselves", 20, 350)
    text ("However, when the user runs into the border, an object, or themselves a math question will appear.", 20, 400)
    text ("If the user selects the correct answer, they will be able to continue and if not, the game is over", 20, 450)
    text ("The questions get progressively harder the more the user dies", 20, 500)
    if (mouseX >= 350) and (mouseX <= 550) and (mouseY >= 700) and (mouseY <= 750) and mousePressed:
        display_instructions = False
        
def high_scores_screen():
    global display_high_score
    fill("#aa0000")
    rect(0,0,900,900) #A new "background" for the high scores screen
    
    fill("#ffffff")
    display_high_scores()
    
    fill("#aaaaaa")
    rect(350,700,200,50)
    fill("#000000")
    text("Back", 430, 730)
    if (mouseX >= 350) and (mouseX <= 550) and (mouseY >= 700) and (mouseY <= 750) and mousePressed:
        display_high_score = False
   
def draw():
    global shrink, restarting, countdown_timer, start_game, display_high_score, display_instructions

    background("#ffffff")
    if (start_game == False) and (display_high_score == False) and (display_instructions == False):
        main_menu()
    if (start_game == False) and (display_high_score == True):
        high_scores_screen()
    if (start_game == False) and (display_instructions == True):
        instructions_screen()
    if start_game == True:
        game_loop()
