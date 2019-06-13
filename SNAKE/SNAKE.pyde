import random
import time
def setup():
    background(255)
    size(900,900)
    frameRate(8)

addedFrameRate = 0
obstacle_counter = 1
obstacles = 1
obstacle_exists = False
food_exists = False
snake_length = 1
obstacle_positions = [[(random.randint(10,20)*30)],[(random.randint(10,20)*30)],[(random.randint(1,5)*30)],[(random.randint(1,5)*30)]]
snake_positions = [[(random.randint(10,20)*30)],[(random.randint(10,20)*30)]]
dead = False
died = False
death_countdown = 0
shrink = 1
paused = False
restarting = True
question_created = False
deaths = 1
countdown_timer = 3
high_score = []
sys.setrecursionlimit(1500)

def resume():
    global obstacles, obstacle_counter, food_exists, snake_length, obstacle_positions, snake_positions, dead, died, death_countdown, shrink, paused, restarting, countdown_timer, addedFrameRate, question_created, rand1, rand2
    
    overlapping = True
    while overlapping:
        snake_positions = [[random.randint(7,23)*30],[random.randint(7,23)*30]]
        
        check = 0
        
        for i in range (0, obstacle_counter):
            if (obstacle_positions[0][i-1] - 90 < snake_positions[0][0] < obstacle_positions[0][i-1] + obstacle_positions[2][i-1] + 90) and (obstacle_positions[1][i-1] - 90 < snake_positions[1][0] < obstacle_positions[1][i-1] + obstacle_positions[3][i-1] + 90):
                check += 1
                break
                
        if check == 0:
            break
    
    for i in range(1, snake_length):
        snake_positions[0].append(snake_positions[0][0])
        snake_positions[1].append(snake_positions[1][0])
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

def display_trivia():
    global dead, deaths, ans_location, answer_clicked, answer, answer_y, num1, num2, question, rand1, rand2, created
    answer_clicked = False
    if question_created:
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
        rect(50, answer_y, 25*(deaths+1),50)
        rect(50, y1, 25*(deaths+1), 50)
        rect(50, y2, 25*(deaths+1), 50)
        
        fill(255)
        text(answer, 50, answer_y + 45)
        text(rand1, 50, y1 + 45)
        text(rand2, 50, y2 + 45)
        
        fill(0,0,150)
        text(question, 50, 70)
        
        if answer_clicked:
            fill(0,0,255)
            rect (50, answer_y, 25*(deaths+1), 50)
        
        if mousePressed == True:
                if 50 < mouseX < 50 + (25*(deaths+2)) and answer_y < mouseY < answer_y + 50:
                    answer_clicked = True
                    fill(0,255,0)
                    text("Correct!", 50, answer_y)
                    fill(0,0,255)
                    rect (50, answer_y, 25*(deaths+1), 50)
                    resume()
                    
                if 50 < mouseX < 50 + (25*(deaths+1)) and y1 < mouseY < y1 + 50:
                    fill(0,0,255)
                    rect (50, y1, 25*(deaths+1), 50)
                    text ("Wrong!", 50, y1)
                    game_over()
                    
                    
                elif 50 < mouseX < 50 + (25*(deaths+2)) and y2 < mouseY < y2 + 50:
                    fill(0,0,255)
                    rect (50, y2, 25*(deaths+1), 50)
                    text ("Wrong!", 50, y2)
                    game_over()
                    
def create_trivia():
    global death_countdown, dead, deaths, question_created
    if dead == True:
        
        operation = random.randint(1,4)
        if operation == 1:
            selection = "addition"
        elif operation == 2:
            selection = "subtraction"
        elif operation == 3:
            selection = "multiplication"
        elif operation == 4:
            selection = "division"
            
        
        if selection == "division":
            num1 = random.randint(1,10**(deaths-1)-1)
            num2 = random.randint(1,10**(deaths-1)-1)
            while num1 % num2 != 0:
                num1 = random.randint(1,10**(deaths-1)-1)
                num2 = random.randint(1,10**(deaths-1)-1)
            
        else:
            num1 = random.randint(1,10**(deaths-1)-1)
            num2 = random.randint(1,10**(deaths-1)-1)
        
        
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
            
        text(question, 50, 50)
        ans_location = random.randint (1,3)
        count = 1
        count_rand = 0
        y = 150
        answer_y = 0
        y1 = 0
        y2 = 0
        
        rand1 = random.randint(int(answer) - 10, int(answer) + 10)
        rand1 = str(rand1)
        if rand1 == answer:
            while rand1 == answer:
                rand1 = random.randint(int(answer) -10 , int(answer) + 10)
                rand1 = str(rand1)

        rand2 = int(answer) + random.randint(-deaths + 1, deaths)*5
        rand2 = str(rand2)
        if rand2 == answer or rand2 == rand1:
            while rand2 == answer or rand2 == rand1:
                rand2 = random.randint(int(answer) - 10 , int(answer) + 10)
                rand2 = str(rand2)
        question_created = True
        global ans_location, answer, answer_y, num1, num2, question, rand1, rand2, question_created
    

def game_loop():
    global obstacles, obstacle_counter, obstacle_exists, food_exists, snake_length, obstacle_positions, snake_positions, dead, death_countdown, shrink, paused, restarting, countdown_timer
    background(255)
    strokeWeight(60)
    line(0,0,900,0)
    line(900,0,900,990)
    line(900,900,0,900)
    line(0,900,0,0)
    strokeWeight(1)
    obstacle()
    food()
    display_snake()
    on_death()
    change_speed()
    if restarting:
        a.speed = 0
        fill(0)
        textSize(40)
        text(countdown_timer,445,430)
        time.sleep(1)
        if countdown_timer == 0:
            restarting = False
        countdown_timer -= 1
    fill(0)
    text(snake_length, 810, 80)
    a.drive()
    if paused:
        fill(230,0,0)
        text("Paused",400,420)
        
def restart():
    global obstacles, obstacle_counter, food_exists, snake_length,obstacle_positions, snake_positions, dead, died, death_countdown, shrink, paused, restarting, countdown_timer, addedFrameRate
    frameRate(8)
    addedFrameRate = 0
    obstacles = 1
    obstacle_counter = 3
    obstacle_counter =1
    food_exists = False
    snake_length = 1
    obstacle_positions = [[(random.randint(10,20)*30)],[(random.randint(10,20)*30)],[(random.randint(1,5)*30)],[(random.randint(1,5)*30)]]
    snake_positions = [[(random.randint(10,20)*30)],[(random.randint(10,20)*30)]]
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
        if dead == False and paused == False:
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
    overlapping = True
    while overlapping:
        obstacle_x = random.randint(2,23)*30
        obstacle_y = random.randint(2,23)*30
        obstacle_h = random.randint(1,5)*30
        obstacle_w = random.randint(1,5)*30
        
        check = 0
        
        for i in range (0, snake_length-1):
            if (obstacle_x - 90 < snake_positions[0][i-1] < obstacle_x + obstacle_w + 90) and (obstacle_y - 90 < snake_positions[1][i-1] < obstacle_y + obstacle_h + 90):
                check += 1
                break
        for i in range (0, obstacle_counter):    
            if (obstacle_x - 30 < obstacle_positions[0][i-1]  < obstacle_x + obstacle_w + 30) and (obstacle_y - 30 < obstacle_positions[1][i-1] < obstacle_y + obstacle_h + 30):
                check += 1
                
        if check == 0:
            break
        
    
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
        display_trivia()
    for i in range(0, snake_length):
        fill(60,180,180)
        if dead:
            if death_countdown > snake_length:
                shrink = shrink*0.7
                rect(snake_positions[0][0]+(shrink-shrink*15)+10.5, snake_positions[1][0]+(shrink-shrink*15)+10.5, shrink*30, shrink*30)
            else:
                rect(snake_positions[0][i-1], snake_positions[1][i-1], 30, 30)
        else:
            rect(snake_positions[0][i-1], snake_positions[1][i-1], 30, 30)

def change_speed():
    global addedFrameRate, obstacle_counter
    defaultFramerate = 8
    if (snake_length % 5) == 0:
        addedFrameRate = (snake_length / 5)
        frameRate((defaultFramerate + addedFrameRate))
        obstacle_counter = 1 + addedFrameRate


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
        
        if (self.x >= width-30 and self.direction == 2) or (self.x < 30 and self.direction == 4):
            self.speed = 0
            dead = True
        if (self.y >= height-30 and self.direction == 3) or (self.y < 30 and self.direction == 1):
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
        
def on_death():
    global dead, died, deaths
    if dead and died == False:
        died = True
        deaths += 1
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
