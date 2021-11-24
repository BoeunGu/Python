from tkinter import*
from table import*
from ball import*
from bat import*

## 전역변수 초기화
x_speed=10 #처음 공의 x속도
y_speed=0  #처음 공의 y속도

score_left=0        #왼쪽 득점판
score_right=0       #오른쪽 득점판


## game_flow() 함수부
def game_flow():


    global score_left
    global score_right

    
    #공을 일정시간마다 움직임
    my_ball.move_next()
    window.after(30,game_flow)      #0.3초마다 game_flow()함수 실행

     # 공이 배트에 닿았는지 충돌 확인:
    bat_L.detect_collision(my_ball)
    bat_R.detect_collision(my_ball)

    #공이 왼쪽벽과 충돌했을때
    if(my_ball.x_posn<=0):
        my_ball.stop_ball()         #공을 멈춤, x,y_speed 다시 0으로
        my_ball.start_position()     #공 위치 초기화
        bat_L.start_position()     #bat_L 위치 초기화
        bat_R.start_position()     #bat_R 위치 초기화
        my_table.move_item(bat_L.rectangle, 20, 150, 35, 250)
        my_table.move_item(bat_R.rectangle, 575, 150, 590, 250)


    #득점판 표시
        score_right= score_right+1
        if(score_right>=3):
            score_right="W"
            score_left="L"
        
        my_table.draw_score(score_left,score_right)
        
        
    #공이 오른쪽벽과 충돌했을때
    if(my_ball.x_posn+ my_ball.width >= my_table.width):
        my_ball.stop_ball()         #공을 멈춤, x,y_speed 다시 0으로
        my_ball.start_position()     #공 위치 초기화
        bat_L.start_position()     #bat_L 위치 초기화
        bat_R.start_position()     #bat_R 위치 초기화
        my_table.move_item(bat_L.rectangle, 20, 150, 35, 250)
        my_table.move_item(bat_R.rectangle, 575, 150, 590, 250)


    #득점판 표시
        score_left= score_left+1
        if(score_left>=3):
            
            score_right="L"
            score_left="W"
        my_table.draw_score(score_left,score_right)

# restart_game() 함수부   
def restart_game(event):
    global score_right
    
    my_ball.start_ball(x_speed=x_speed, y_speed=y_speed)
    
    bat_L.start_position()
    bat_R.start_position()
    
    if(score_right=="L"or"W"):
        
        score_left=0
        score_right=0
        my_table.draw_score(score_left,score_right)
    
    

    



window=Tk()
window.title("MyPingPong")


## Table클래스를 사용해서 테이블 생성
my_table = Table(window, 600, 400, "lightblue", "grey")


## 공 생성
# Ball(self,table,width,height,color,x_speed,y_speed,x_posn,y_posn)
my_ball=Ball(table=my_table,x_speed=0,y_speed=0,width=24,height=24,color="white",x_posn=288,y_posn=188)
my_ball.move_next()


# 배트 생성
# Bat 클래스로부터 배트를 주문
# Bat(self,table,width,height,x_posn,y_posn,color,x_speed=25,y_speed=25)
bat_L = Bat(table=my_table, width=15, height=100, x_posn=20, y_posn=150, color="PaleVioletRed")
          
bat_R = Bat(table=my_table, width=15, height=100, x_posn=565, y_posn=150, color="YellowGreen")




## 함수의 실행부

game_flow()
window.bind("<space>",restart_game)
## 배트를 제어하기 위한 키 이벤트
# 배트를 제어하기 위해 키보드의 키에 연결
#window.bind("<키명>", 함수명)
window.bind("<Up>", bat_R.move_up)
window.bind("<Down>", bat_R.move_down)
window.bind("<Left>", bat_R.move_left)
window.bind("<Right>", bat_R.move_right)
window.bind("w", bat_L.move_up)
window.bind("s", bat_L.move_down)
window.bind("a", bat_L.move_left)
window.bind("d", bat_L.move_right)
        

window.mainloop()
