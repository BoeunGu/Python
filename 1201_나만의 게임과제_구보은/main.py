from tkinter import *
from table import*
from ball import*
from bat import*
import random


window = Tk()
window.title("SavetheEarth")
my_table =Table(window)

# 배경 이미지 추가
starry_night_image = PhotoImage(file = "bgimage.gif")
my_table.canvas.create_image(0, 0, anchor=NW, image = starry_night_image, tags="bg_img")

# 이미지 스택의 맨 아래로 이미지 이동(득점판은 배경 이미지 위에서 볼 수 있습니다)
# "bg_img"로 태깅된 캔버스 객체를 lower() 메서드를 사용해 뒤로 이동시킵니다
my_table.canvas.lower("bg_img")

# 전역 변수 초기화
x_velocity = 0
y_velocity = -15
first_serve=True
direction = "right"

# Ball 클래스로부터 미사일을 주문합니다.
my_ball = Ball(table=my_table, x_speed=x_velocity, y_speed=y_velocity,
                    height=20, width=20, colour="white",outline="white")
#ball= PhotoImage(file = "ball.png")
#my_table.canvas.delete(my_ball.circle)
#my_ball.circle = my_table.canvas.create_image(my_ball.x_posn, my_ball.y_posn, anchor=None, image = ball, tags="ball_img")



# Bat 클래스로부터 수비수(탱크)를 주문합니다.
bat_B = Bat(table=my_table, width=50, height=30,
                x_posn=250, y_posn=400, colour="")

tank= PhotoImage(file = "tank.png")
my_table.canvas.delete(bat_B.rectangle)
bat_B.rectangle = my_table.canvas.create_image(bat_B.x_posn, bat_B.y_posn, anchor=NW, image = tank, tags="tank_img")


# 배트 클래스로부터 우주선을 주문하고 우주선들의 이동을 시작합니다.
invaders = []
rows=0
gap=30
colour = ("lightseagreen", "tomato", "khaki", "plum","olivedrab")
border = colour
xspace=0
while rows < 5:
    n=1
    while n < 7:
        i=80
        invader = Bat(table=my_table, width=80, height=20, x_speed=3, y_speed=15,
                          x_posn=(n*i)+xspace, y_posn=25+(rows*gap), colour=colour[(rows-1)%5],outline="")
        invaders.append(invader)
        n = n+1
        xspace=xspace+20
    rows = rows+1
    xspace=0

#### 함수:        
def game_flow():
    global first_serve
    global direction
    game_over = False
    
    # 첫번째 서브를 기다립니다:
    if(first_serve == True):
        my_ball.stop_ball()
        first_serve = False

    # 우주선이 미사일에 맞았는지 검출합니다.
    for b in invaders:
        if(b.detect_collision(my_ball, sides_sweet_spot=False) != None):
            my_table.remove_item(b.rectangle)                
            invaders.remove(b)
            hide_missile()
            
            
        if(len(invaders) == 0):
            my_table.remove_item(my_ball.circle)
            my_table.canvas.itemconfigure(my_table.scoreboard, text="WIN")
            
    # 미사일이 상단 벽에 맞았는지 검출합니다:
    if(my_ball.y_posn <= 3):
        hide_missile()
        first_serve=True
    
    my_ball.move_next()
    for i in invaders:
        my_table.change_item_colour(i.rectangle, my_table.change_bricks_colour())
       
        
    

    # 우주선들의 이동을 처리합니다
    directionChange = False;
    for b in invaders:
        directionChange = directionChange or move_brick_next(b, direction)
        game_over = detect_game_over(b, bat_B.y_posn)
    if(game_over):
        my_ball.stop_ball()
        for b in invaders:
            b.x_speed=0
            b.y_speed=0
        my_table.canvas.itemconfigure(my_table.scoreboard, text="TRY AGAIN",font=("monaco",40))
    if(directionChange):
        for b in invaders:
            b.move_down(b)
            for i in invaders:
                my_table.change_item_colour(i.rectangle, my_table.change_bricks_colour())
        if(direction == "right"):
            direction = "left"
        else:
            direction = "right" 
            
        
    window.after(40, game_flow)
    
def restart_game(master):
    first_serve=False
    my_ball.start_ball(0,0)
    my_ball.x_speed=x_velocity
    my_ball.y_speed=y_velocity
    #my_table.change_item_colour(my_ball.circle, "red")
    my_ball.x_posn = (bat_B.x_posn + bat_B.width/2)
    my_ball.y_posn = bat_B.y_posn

# 우주선이 왼쪽이나 오른쪽, 아래로 이동하고 있는지 확인합니다.
# 방향을 변경해야 하는 경우 true를 반환합니다.
def move_brick_next(brick, direction):
    if(direction == "left"):
        brick.move_left(brick)
        if(brick.x_posn < 10):  # 벽돌이 왼쪽 벽에 도달했는지 감지
            return True
        else:
            return False
    else:
        brick.move_right(brick)
        if((brick.x_posn + brick.width) > my_table.width-10):  # 벽돌이 오른쪽 벽에 도달했는지 감지
            return True
        else:
            return False

# 우주선이 아래쪽 벽에 도달했는지 감지
def detect_game_over(invader, bottom):
    if((invader.y_posn + invader.height) > bottom):
        return True
    else:
        return False

# 미사일 감춤
def hide_missile():
    my_ball.stop_ball()
    my_ball.x_posn=bat_B.x_posn
    my_ball.y_posn=bat_B.y_posn
    my_table.change_item_colour(my_ball.circle, "white")
    

# 배트를 제어할 수 있도록 키보드의 키와 연결
window.bind("<Left>", bat_B.move_left)
window.bind("<Right>", bat_B.move_right)

# 스페이스 키를 게임 재시작 기능과 연결
window.bind("<space>", restart_game)

game_flow()
window.mainloop()
