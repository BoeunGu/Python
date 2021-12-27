
from tkinter import*
from tkinter.filedialog import* # 파일 입출력을 위한 모듈
from tkinter.simpledialog import* # 숫자나 문자를 입력받기 위한 모듈
from wand.image import* # 이미지 처리기능을 위한 외부 라이브러리(GIF,PNG,JPG)
from wand.drawing import Drawing
from wand.image import Image
from tkinter import messagebox



#METHOD

def displayImage(img,width,height):     #이미지를 화면에 출력해주는 함수
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY

    # 이전 캔버스가 존재한다면 새 캔버스와 그 위에 새 종이를 생성하여 깨끗하게 처리한 후 처리된 이미지 출력
    # 이전 캔버스가 존재한다면 이전 캔버스를 삭제하여 기존에 이미지가 출력된 캔버스를 깨끗하게 처리
    if canvas != None :
        canvas.destroy()

        

    # 새 캔버스 생성, 처리된 이미지의 가로,세로 사이즈대로 생성
    canvas=Canvas(window, width=width, height=height, bg='#333333', highlightthickness=0)  
    paper=PhotoImage(width=width, height=height)        

    blob=img.make_blob(format='png')
    paper.put(blob)
    canvas.create_image((width/2,height/2), image=paper, state="normal")     

    
   
    canvas.place(x=(1100-width)/2,y=(820-height)/2+20)     
   

def func_open():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY
    
    readFp=askopenfilename(parent=window,filetypes=(("모든 그림 파일", "*.jpg;*.jpeg;*.bmp;*.png;*.tif;*.gif"),  ("모든 파일", "*.*") ))
    #photo는 처음 불러들인 원본 이미지
    photo=Image(filename=readFp)
    oriX=photo.width        #원본 이미지의 가로 사이즈를 oriX에 저장
    oriY=photo.height       #원본 이미지의 세로 사이즈를 oriY에 저장

    #photo2는 처리 결과를 저장할 변수
    photo2=photo.clone()        #원본 이미지의 photo를 복사하여 photo2에 저장
    newX=photo2.width
    newY=photo2.height
    string=readFp
    p=string.split('/')
    s=len(p)
    label.configure(text=str(p[s-1]))
    displayImage(photo2,newX,newY)
    fileMenu.entryconfigure("Save File", state ="normal")
    mainMenu.entryconfigure("Edit1", state ="normal")
    mainMenu.entryconfigure("Edit2", state ="normal")
    mainMenu.entryconfigure("Edit3", state ="normal")

    
    
    
                           
                                            
def func_save():
    global window,canvas,paper,photo,photo2,oriX,oriY


    if photo2==None:
        return
         #파일을 열지 않았다면 함수를 빠져나감
    saveFp=asksaveasfile(parent=window, mode="w", defaultextension=".jpg", filetypes=(("JPG 파일", "*.jpg;*.jpeg"),  ("모든 파일", "*.*") ))
    savePhoto=photo2.convert("jpg")     #결과 이미지인 photo2를 jpg로 변환
    savePhoto.save(filename=saveFp.name)    #파일저장 대화창에서 입력받은 파일 이름을 저장
def func_exit():
    window.quit()
    window.destory()

def func_zoomin():
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2==None:
        return

    scale=askinteger("확대배수", "확대할 배수를 입력하세요(2~4)", minvalue=2, maxvalue=4)    #확대할 배수 입력받음
    photo2.resize(int(newX*scale), int(newY*scale))     # 원본이미지의 가로,세로 사이즈에 배수를 곱하여크기변경
    newX=photo2.width       #변경된 값은 다시 newX에 저장
    newY=photo2.height      #변경된 값은 다시 newy에 저장
    displayImage(photo2,newX,newY)
    
def func_zoomout():
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2==None:
        return

    scale=askinteger("축소배수", "축소할 배수를 입력하세요(2~4)", minvalue=2, maxvalue=4)    #확대할 배수 입력받음
    photo2.resize(int(newX / scale), int(newY /scale))     # 원본이미지의 가로,세로 사이즈에 배수를 곱하여크기변경
    newX=photo2.width       #변경된 값은 다시 newX에 저장
    newY=photo2.height      #변경된 값은 다시 newy에 저장
    displayImage(photo2,newX,newY)
    
def func_mirror1():
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2==None:
        return

    photo2.flip()       #좌우반전
    newX=photo2.width       #변경된 값은 다시 newX에 저장
    newY=photo2.height      #변경된 값은 다시 newY에 저장
    displayImage(photo2,newX,newY)
    
def func_mirror2():
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2==None:
        return

    photo2.flop()       #상하반전
    newX=photo2.width       #변경된 값은 다시 newX에 저장
    newY=photo2.height      #변경된 값은 다시 newY에 저장
    displayImage(photo2,newX,newY)
def func_rotate():
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2==None:
        return
    degree = askinteger("회전", "회전할 각도를 입력하세요", minvalue=0, maxvalue=360)
    photo2.rotate(degree)
    newX=photo2.width       #변경된 값은 다시 newX에 저장
    newY=photo2.height      #변경된 값은 다시 newY에 저장
    displayImage(photo2,newX,newY)


def func_bright():
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2==None:
        return
    value=askinteger("밝게","값을 입력하세요(100~200)",minvalue=100,maxvalue=200)
    photo2.modulate(value,100,100)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

     
def func_dark():
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2==None:
        return
    value=askinteger("어둡게","값을 입력하세요(100~200)",minvalue=0,maxvalue=100)
    photo2.modulate(value,100,100)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)
    
def func_clear():
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2==None:
        return
    value=askinteger("밝게","값을 입력하세요(100~200)",minvalue=100,maxvalue=200)
    photo2.modulate(100,value,100)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)
    
def func_unclear():
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2==None:
        return
    value=askinteger("탁하게","값을 입력하세요(100~200)",minvalue=0,maxvalue=100)
    photo2.modulate(100,value,100)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)
    
def func_bw():
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2==None:
        return
    
    photo2.modulate(100,0,100)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

def func_defalut():
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2==None:
        return

    displayImage(photo,oriX,oriY)
    photo2=photo.clone()

def func_sup():
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2==None:
        return
    value=askinteger("밝게","값을 입력하세요(100~200)",minvalue=100,maxvalue=200)
    photo2.modulate(100,100,value)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

def func_sdown():
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2==None:
        return
    value=askinteger("어둡게","값을 입력하세요(100~200)",minvalue=100,maxvalue=200)
    photo2.modulate(100,100,value)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

def func_edge():
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2==None:
        return

    photo2.edge(radius=1)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

def func_blur():
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2==None:
        return


    value=askinteger("Blur","값을 입력하세요(0~10)",minvalue=0,maxvalue=10)
    photo2.blur(sigma=value)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

def func_text():

    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY
    if photo2==None:
        return
    
    draw = Drawing()
    draw.font_size = 20
    #draw.font_color="White"
    value=askstring("Text","Only English...")
    
    draw.text(100,100,' '+value+' ')
    draw(photo2)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

def func_watermark() :
    global window,canvas, paper, photo, photo2, photo3, oriX, oriY
    
    if photo3 == None :
        messagebox.showinfo("에러","워터 마크 이미지가 없습니다.")
    else :   
        photo3.resize( int(oriX /7) , int(oriY / 5) )
        photo2.watermark(photo3, 0.5,oriX-120, oriY-128)
        displayImage(photo2, oriX, oriY)


def func_watermarkopen():
    global window,canvas, paper, photo, photo2,photo3, oriX, oriY
    readFp = askopenfilename(parent=window, filetypes=(("모든 그림 파일", "*.jpg;*.jpeg;*.bmp;*.png;*.tif;*.gif"),  ("모든 파일", "*.*") ))
    photo3 = Image(filename=readFp)



def func_draw() :
    global pen_color,color,Colorlist,button

    canvas.bind("<B1-Motion>",paint)


def paint(event):
    global pen_color,color,Colorlist,button
    x1,y1=event.x-1,event.y-1
    x2,y2=event.x+1,event.y+1
    canvas.create_oval(x1,y1,x2,y2, fill=pen_color, outline=pen_color)
    

def func_comp() :
    global window,canvas, paper, photo, photo2, oriX, oriY, newX, newY  # 전역 변수 선언
    #photo2 = photo.clone()
    '''
    photo.transparentize(0.5) # 원본 이미지의 투명도를 50%로 설정
    photo2.composite(photo, 20, 20) # photo2의 20, 20 위치에 photo를 합성
    '''
    photo2.watermark(photo, 0.5, 20, 20)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_close():
    canvas.destroy()
    label.configure(text="")
    
def change_color(color):
    global pen_color,Colorlist,button
    Colorlist=["red","pink","lightblue","grey","magenta","lightyellow","white","cyan","green"]
    pen_color=color

# 변수 선언 부분(글로벌 변수)
window,canvas,paper,readFp=None,None,None,None
photo,photo2=None,None
oriX,oriY=0,0
newX,newY=0,0#이미지의 폭과 넓이
x1,y1,x2,y2=None,None,None,None
pen_color="black"


#메인코드부분
window = Tk()   #창생성
window.geometry("1355x766")
window.title("Mini Photoshop (ver 0.1)")
window.resizable(False, False)


backg=PhotoImage(file="./JPG/backgg.png")
backLabel=Label(window,image=backg)
backLabel.pack()

label = Label(window, text="file name",bg="gray")
label.place(x=38, y=62)

#메뉴생성
#1.메뉴 자체 생성

mainMenu = Menu(window)    
window.config(menu=mainMenu)       


fileMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="Open File", command=func_open)
fileMenu.add_command(label="Save File", command=func_save, state = "disable")
fileMenu.add_command(label="Open WaterMark",command=func_watermarkopen)
fileMenu.add_separator()        # 구분선 생성
fileMenu.add_command(label="Close File", command=func_close)
fileMenu.add_command(label="Exit File", command=func_exit)


imageMenu1 = Menu(mainMenu,tearoff=0)
mainMenu.add_cascade(label="Edit1", menu=imageMenu1, state = "disable")

imageMenu1.add_command(label="Zoomin", command=func_zoomin)
imageMenu1.add_command(label="Zoomout", command=func_zoomout)
imageMenu1.add_separator()        # 구분선 생성
imageMenu1.add_command(label="Mirror1", command=func_mirror1)
imageMenu1.add_command(label="Mirror2", command=func_mirror2)
imageMenu1.add_command(label="Rotate", command=func_rotate)
imageMenu1.add_separator()
imageMenu1.add_command(label="Edge", command=func_edge)
imageMenu1.add_command(label="Blur", command=func_blur)



imageMenu2 = Menu(mainMenu,tearoff=0)
imageMenu2_1 = Menu(mainMenu,tearoff=0)
imageMenu2_2= Menu(mainMenu,tearoff=0)
imageMenu2_3= Menu(mainMenu,tearoff=0)

mainMenu.add_cascade(label="Edit2", menu=imageMenu2, state = "disable")
imageMenu2.add_cascade(label="Brightness", menu=imageMenu2_1)
imageMenu2.add_cascade(label="Saturation", menu=imageMenu2_2)
imageMenu2.add_cascade(label="Clear", menu=imageMenu2_3)


imageMenu2_1.add_command(label="Brighter", command=func_bright)
imageMenu2_1.add_command(label="Darker", command=func_dark)
#imageMenu2.add_separator()        # 구분선 생성
imageMenu2_2.add_command(label="Saturation Up",command=func_sup)
imageMenu2_2.add_command(label="Saturation Down", command=func_sdown)
#imageMenu2.add_separator()        # 구분선 생성
imageMenu2_3.add_command(label="Clear", command=func_clear)
imageMenu2_3.add_command(label="Unclear", command=func_unclear)
imageMenu2.add_command(label="BW", command=func_bw)
imageMenu2.add_command(label="Text", command=func_text)


imageMenu3 = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="Edit3", menu=imageMenu3, state = "disable")

imageMenu3_1 = Menu(mainMenu, tearoff=0)
imageMenu3.add_cascade(label="Draw", menu=imageMenu3_1)

imageMenu3.add_command(label="Default", command=func_defalut)
imageMenu3.add_command(label="WaterMark",command=func_watermark)
imageMenu3.add_command(label="Erase",command=func_clear)
imageMenu3_1.add_command(label="Black",command=func_draw)
imageMenu3.add_command(label="Composite", command=func_comp)

#버튼생성

#button=Button(window, text=None, width=2,bg="",command=lambda : change_color(""))
button=[None]*9

Colorlist=["red","pink","lightblue","grey","magenta","lightyellow","white","cyan","green","purple"]
#Colorlist=["red","red","red","red","red","red","red","red","red","red"]

xpos=1200 #x 좌표값 설정
ypos=550 #y 좌표값 설정
i=0 #i 변수 설정

for y in range(0,3):
    xpos=1200
    for x in range(0,3):
        button[i]=Button(window,text=None, width=2,bg=str(Colorlist[i]),command=lambda : change_color(str(Colorlist[i])))
        button[i].place(x=xpos,y=ypos)
        xpos+=30
        i+=1
    
    ypos+=28



window.mainloop()

