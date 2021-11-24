import random,table # randint 함수를 불러오기 위한 모듈 임포트

## 전역변수 초기화
x_speed=10 #처음 공의 x속도
y_speed=0  #처음 공의 y속도

score_left=0        #왼쪽 득점판
score_right=0       #오른쪽 득점판


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
        x1 = self.x_posn            #왼쪽 위
        x2 = self.x_posn+self.width         #오른쪽 아래
        y1 = self.y_posn        #변경된 y_posn값을 y1에 반
        y2 = self.y_posn+self.height
        self.table.move_item(self.circle, x1, y1, x2, y2)


    #공이 위쪽벽에 충돌했을 때:
        if(self.y_posn<=0):
            self.y_posn=0
            self.y_speed=-self.y_speed

    #공이 아래쪽벽에 충돌했을 때:
        if(self.y_posn>=(self.table.height- self.height)):
            self.y_posn=(self.table.height- self.height)
            self.y_speed=-self.y_speed
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
                
            
        

