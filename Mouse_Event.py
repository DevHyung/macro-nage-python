import win32api,win32con
import time

def valid_user():
    # 20180815 20:03기준 4시간
    # print(time.time())
    now = 1534902170.077185
    terminTime = now + 60 * 60 * 6
    print("체험판 만료기간 : ", time.ctime(terminTime))
    if time.time() > terminTime:
        print('만료되었습니다.')
        exit(-1)
    else:
        print(">>>프로그램이 실행되었습니다.")

if __name__ == "__main__":
    valid_user()
    #=== CONFIG
    print("\n__________ 매크로 환경설정 __________")
    EXITTIME = int( input(">>>반복 끝나는 시간 설정  (초단위)   ::"))
    OFFSET_G = int( input(">>>가로 몇 등분 할 것인지 설정(정수로)::"))
    OFFSET_S = int( input(">>>세로 몇 등분 할 것인지 설정(정수로)::"))
    print("\n__________ 마우스 커서 설정 __________")
    MOUSE_DELAY = float(input(">>>네모 영역안의 좌표간 이동 딜레이(0.001 기본)::"))
    AREA_DELAY  = float(input(">>>네모 영역간 클릭 딜레이(기본 0)::"))
    posList = []
    new_posList = []
    # p1(x1,y1)     p2(x2,y1)
    # p3(x1,y2)     p4(x2,y2)
    print("\n__________ 영역 설정 __________")
    p1 = input('>>>사각형의 왼쪽 위 좌표에 커서를 둔 후 엔터키 입력::')
    posList.append(win32api.GetCursorPos())
    p4 = input('>>>사각형의 오른쪽 아래 좌표에 커서를 둔 후 엔터키 입력::')
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
    print(">>> 클릭 시작")


    now = time.time()
    while True:
        for pos in new_posList:
            win32api.SetCursorPos(pos)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            time.sleep(MOUSE_DELAY)
            if time.time() - now > EXITTIME:
                exit(1)