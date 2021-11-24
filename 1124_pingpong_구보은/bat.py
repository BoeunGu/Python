import table

## 전역변수 초기화
x_speed=10 #처음 공의 x속도
y_speed=0  #처음 공의 y속도

score_left=0        #왼쪽 득점판
score_right=0       #오른쪽 득점판

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
        if(self.x_posn<=0):
            self.x_posn=0

        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn        #변경된 y_posn값을 y1에 반
        y2 = self.y_posn+self.height

        #변경된 값으로 아이템을 옮김
        #Table클래스의 move_item() 함수를 실행
        self.table.move_item(self.rectangle, x1, y1, x2, y2)        

    def move_right(self,master):
        self.x_posn=self.x_posn+self.x_speed
        if(self.x_posn>=self.table.width-self.width):
            self.x_posn=self.table.width-self.width

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
        v_center = top + (self.height/2)        #배트의 top에서 배트의 높이를 2로 나눈 값 더하면 세로중간
        h_center = left + (self.width/2)

        # 공변
        top_b = ball.y_posn
        bottom_b = ball.y_posn + ball.height
        left_b = ball.x_posn
        right_b = ball.x_posn + ball.width
        r = (right_b - left_b)/2         #반지름
        v_center_b = top_b + r      #공의 탑에서 반지름 더하면 세로 중간
        h_center_b = left_b + r     #공의 왼쪽에서 반지름 더하면 가로중간

            
             
        if((bottom_b > top) and (top_b < bottom) and (right_b > left) and (left_b < right)):
            collision = True
            print("BOMB!")

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
               

