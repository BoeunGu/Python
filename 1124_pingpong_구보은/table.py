from tkinter import*

## 전역변수 초기화
x_speed=10 #처음 공의 x속도
y_speed=0  #처음 공의 y속도

score_left=0        #왼쪽 득점판
score_right=0       #오른쪽 득점판

###Table 클래스 생성(선 포함)


class Table:

    global score_left
    global score_right

    ## 생성자
    def __init__(self,window,width,height,bg_color,net_color):
        
        self.width=width
        self.height=height
        self.bg_color=bg_color
        self.net_color=net_color


    #Table클래스 내에서 캔버스 생성
        self.canvas=Canvas(window,width=self.width,height=self.height,bg=self.bg_color)
        self.canvas.pack()
                
        self.image=PhotoImage(file="./gif/dog.gif")       
        self.canvas.create_image(self.width/2,self.height/2,image=self.image)
    
        self.canvas.create_line(self.width/2,0,self.width/2,self.height,width=2,fill=net_color, dash=(15,23))

     # Table 클래스 내에서 득점판 생성
        font=("monaco",60)
        self.scoreboard=self.canvas.create_text(self.width/2,66,font=font,fill="Lightpink", text=str(score_left)+ " " +str(score_right))
     

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


    # Canvas(Table)에 득점판을 갱신하는 함수
    def draw_score(self,left,right):
        scores=str(left)+" "+str(right)
        self.canvas.itemconfigure(self.scoreboard,text=scores)

    
        
        




