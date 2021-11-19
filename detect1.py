from tkinter import*
import random # randint 함수를 불러오기 위한 모듈 임포트

## 전역변수 초기화
x_speed=10 #처음 공의 x속도
y_speed=0  #처음 공의 y속도

window=Tk()
window.title("MyPingPong")


'''
#캔버스 생성
canvas=Canvas(window,width=600, height=400, bg="lightpink")
canvas.pack()

#캔버스 위에 선 생성
canvas.create_line(300,0,300,400, width=2, fill="grey",dash=(15,23))        #dash는 선에 점사이의 간격

#캔버스 위에 공 만들기
canvas.create_oval(288,188,312,212,fill="coral2")

#캔버스 위에 배트 생성
canvas.create_rectangle(20,150,35,250, fill="lightblue")
canvas.create_rectangle(565,150,580,250, fill="yellow")
'''


###Table 클래스 생성(선 포함)

class Table:
    def __init__(self,window,width,height,bg_color,net_color):
        self.width=width
        self.height=height
        self.bg_color=bg_color
        self.net_color=net_color


    #Table클래스 내에서 캔버스 생성
        self.canvas=Canvas(window,width=self.width,height=self.height,bg=self.bg_color)
        #paper=PhotoImage(file="./PNG/water.png")
        #blob = png.make_blob(format='png')
       # paper.imgput(blob)
        #canvas.create_image(width,height,image=paper)
        self.canvas.pack()
        
        self.canvas.create_line(self.width/2,0,self.width/2,self.height,width=2,fill=net_color, dash=(15,23))

        ###함수부
        #Canvas(Table)에 타원을 추가하는 함수
    def draw_oval(self,oval):
        x1=oval.x_posn
        x2=oval.x_posn+oval.width
        y1=oval.y_posn
        y2=oval.y_posn+oval.height
        c=oval.color
        return self.canvas.create_oval(x1,y1,x2,y2,fill=c)

    
    #Canvas(Table)에 타원을 추가하는 함수
    def draw_rectangle(self,rectangle):

        x1=rectangle.x_posn
        x2=rectangle.x_posn+rectangle.width
        y1=rectangle.y_posn
        y2=rectangle.y_posn+rectangle.height
        c=rectangle.color
        return self.canvas.create_rectangle(x1,y1,x2,y2,fill=c)

    #coords()는 입력받은 값으로 속성값 업데이트를하는 함수
    def move_item(self, item, x1, y1, x2, y2):
        self.canvas.coords(item, x1, y1, x2, y2)

    
        
        




### Ball 클래스 생성
class Ball:
    ###생성자 만들기
    def __init__(self,table,width,height,color,x_speed,y_speed,x_posn,y_posn):
        self.width=width        #공의 가로 사이즈
        self.height=height
        self.color=color
        self.x_posn=x_posn      #공의 x좌표값
        self.y_posn=y_posn

        self.x_start=x_posn
        self.y_start=y_posn
        self.x_speed=x_speed
        self.y_speed=y_speed

        self.table=table
        self.circle=self.table.draw_oval(self)

    ##함수부
    #공이 움직이는 부분
    def move_next(self):

         
        self.x_posn = self.x_posn + self.x_speed # 현재 공의 위치에 이동할 거리 x 를 추가
        self.y_posn = self.y_posn + self.y_speed # 현재 공의 위치에 이동할 거리 x 를 추가

        #공의 변경된 위치 지정 및 이동
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn        #변경된 y_posn값을 y1에 반
        y2 = self.y_posn+self.height
        self.table.move_item(self.circle, x1, y1, x2, y2)
    #공의 초기 위치값 지정
    def start_position(self):
        self.x_posn=self.x_start
        self.y_posn=self.y_start
    #공의 변경된 위치 지정 및 이동
    def start_ball(self,x_speed,y_speed):
        self.x_speed=-x_speed if random.randint(0,1) else x_speed
        self.y_speed=-y_speed if random.randint(0,1) else y_speed
        self.start_position()
    #공을 멈춤
    def stop_ball(self):
        self.x_speed=0
        self.y_speed=0
        
                
            
        


##Bat 클래스 생성
class Bat:
    ###생성자
    def __init__(self,table,width,height,x_posn,y_posn,color,x_speed=9,y_speed=23):

        self.width=width        
        self.height=height
        self.color=color
        self.x_posn=x_posn      
        self.y_posn=y_posn

        self.x_start=x_posn
        self.y_start=y_posn
        self.x_speed=x_speed
        self.y_speed=y_speed
        # Table의 draw_rectangle()함수실행
        self.table=table
        self.rectangle=self.table.draw_rectangle(self)

    ### 함수부 /  배트를 위로 움직이는 함수

    def move_up(self,master):
        self.y_posn=self.y_posn-self.y_speed
        if(self.y_posn<=0):
            self.y_posn=0

        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn        #변경된 y_posn값을 y1에 반
        y2 = self.y_posn+self.height

        #변경된 값으로 아이템을 옮김
        #Table클래스의 move_item() 함수를 실행
        self.table.move_item(self.rectangle, x1, y1, x2, y2)

    def move_down(self,master):
        self.y_posn=self.y_posn + self.y_speed
        if(self.y_posn>=300):
            self.y_posn=300

        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn        #변경된 y_posn값을 y1에 반
        y2 = self.y_posn+self.height

        #변경된 값으로 아이템을 옮김
        #Table클래스의 move_item() 함수를 실행
        self.table.move_item(self.rectangle, x1, y1, x2, y2)        


    def move_left(self,master):
        self.x_posn=self.x_posn-self.x_speed
        #if(self.x_posn<=0):
            #self.x_posn=0

        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn        #변경된 y_posn값을 y1에 반
        y2 = self.y_posn+self.height

        #변경된 값으로 아이템을 옮김
        #Table클래스의 move_item() 함수를 실행
        self.table.move_item(self.rectangle, x1, y1, x2, y2)        

    def move_right(self,master):
        self.x_posn=self.x_posn+self.x_speed
        #if(self.x_posn<=0):
            #self.x_posn=0

        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn        #변경된 y_posn값을 y1에 반
        y2 = self.y_posn+self.height

        #변경된 값으로 아이템을 옮김
        #Table클래스의 move_item() 함수를 실행
        self.table.move_item(self.rectangle, x1, y1, x2, y2)

    def detect_collision(self,ball):

        collision_direction = ""  # 충돌 방향 저장
        collision = False           # 충돌이 감지되면 True 로 바뀜
        feel = 5 

        #배트변수
        top=self.y_posn
        bottom= self.y_posn + self.height
        left = self.x_posn
        right = self.x_posn + self.width
        v_center = top + (self.height/2)        #배트의 답에서 배트의 높이를 2로 나눈 값 더하면 세로중간
        h_center = left + (self.width/2)

        # 공변
        top_b = ball.y_posn
        bottom_b = ball.y_posn + ball.height
        left_b = ball.x_posn
        right_b = ball.x_posn + ball.width
        r = (right_b - left_b)/2         #반지름
        v_center_b = top_b + r      #공의 탑에서 반지름 더하면 새로 중상
        h_center_b = left_b + r     #공의 왼쪽에서 반지름 더하면 가로중간

            
             
        if((bottom_b > top) and (top_b < bottom) and (right_b > left) and (left_b < right)):
            collision = True
            print("충돌")

        # 만약 충돌했다면 어느 방향으로 충돌했는지 collision_direction에 저장        
        if(collision):
            if((top_b > top-r) and (bottom_b < bottom+r) and (right_b > right) and (left_b <= right)):
                collision_direction = "E"
               # abs() 함수는 숫자의 부호를 제거하는 함수, 속도 값을 얻는데 사용
                # abs() 함수는 공이 배트의 어느 부분에 충돌했는지에 따라 공이 튀는 방향 바꿈
                ball.x_speed = abs(ball.x_speed)


                # 공의 중심이 배트의 중심에서 얼마나 먼 거리에서 충돌이  발생했는지 계산하여 y좌표값에 적용
                adjustment = (-(v_center-v_center_b))/(self.height/2)
                print(adjustment)
                ball.y_speed=feel*adjustment

            

            elif((top_b > top-r) and (bottom_b < bottom+r) and (left_b < left) and (right_b >= left)):
                collision_direction = "W"
                ball.x_speed = -abs(ball.x_speed)

                adjustment = (-(v_center-v_center_b))/(self.height/2)
                print(adjustment)
                ball.y_speed=feel*adjustment

            return (collision, collision_direction)

        #배트의 초기 위치값 지정
    def start_position(self):
        self.x_posn=self.x_start
        self.y_posn=self.y_start
               


# game_flow() 함수부
def game_flow():
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
        
    #공이 왼쪽벽과 충돌했을때
    if(my_ball.x_posn+ my_ball.width >= my_table.width):
        my_ball.stop_ball()         #공을 멈춤, x,y_speed 다시 0으로
        my_ball.start_position()     #공 위치 초기화
        bat_L.start_position()     #bat_L 위치 초기화
        bat_R.start_position()     #bat_R 위치 초기화
        my_table.move_item(bat_L.rectangle, 20, 150, 35, 250)
        my_table.move_item(bat_R.rectangle, 575, 150, 590, 250)

# restart_game() 함수부   
def restart_game(event):
    my_ball.start_ball(x_speed=x_speed, y_speed=y_speed)

    



## Table클래스를 사용해서 테이블 생성
my_table = Table(window, 600, 400, "Lavender", "BlueViolet")


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
