import win32api,win32con
import time

def valid_user():
    # 20180815 20:03기준 4시간
    print(time.time())
    now = 1534331194.42268
    terminTime = now + 60 * 60 * 4
    print("체험판 만료기간 : ", time.ctime(terminTime))
    if time.time() > terminTime:
        print('만료되었습니다.')
        exit(-1)
    else:
        print(">>>프로그램이 실행되었습니다.")

if __name__ == "__main__":
    #valid_user()
    #=== CONFIG
    EXITTIME = int( input(">>>반복 끝나는 시간 설정 (초단위)::"))
    OFFSET_G = int( input(">>>가로 몇 등분 할 것인지 설정(정수로)::"))
    OFFSET_S = int( input(">>>세로 몇 등분 할 것인지 설정(정수로)::"))

    posList = []
    new_posList = []
    # p1(x1,y1)     p2(x2,y1)
    # p3(x1,y2)     p4(x2,y2)
    p1 = input('사각형의 왼쪽 위 좌표에 커서를 둔 후 엔터키 입력::')
    posList.append(win32api.GetCursorPos())
    p4 = input('사각형의 오른쪽 아래 좌표에 커서를 둔 후 엔터키 입력::')
    posList.append(win32api.GetCursorPos()) #[p1,p4]
    p2 = (posList[1][0],posList[0][1])
    p3 = (posList[0][0],posList[1][1])
    posList.insert(1, p2)
    posList.insert(2, p3)
    p1 = posList[0]
    p4 = posList[3]
    #[p1,p2,p3,p4]

    x = round((p2[0]-p1[0])/OFFSET_G)
    y = round((p3[1]-p1[1])/OFFSET_S)

    for i in range(OFFSET_S+1):
        for j in range(OFFSET_G+1):
            pN = (p1[0]+x*j,p1[1]+y*i)
            new_posList.append(pN)
    print(new_posList)

    print(">>> 클릭 시작")
    print_format = "{:0.4f} 초 소요됨"


    now = time.time()
    #t = Thread(target=exit_timer, args=(20, time.time()))
    #t.start()

    idx = 1
    while True:

        #start = time.time()
        for pos in new_posList:
            idx +=1
            win32api.SetCursorPos(pos)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            if time.time() - now > EXITTIME:
                #end = time.time()
                print(idx)
                #print(print_format.format((end - now))
                exit(1)


