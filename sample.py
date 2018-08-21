import win32api,win32con
import time
import threading
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
    DELAY = float( input(">>>마우스 포인터 간 딜레이를 설정(초단위)::"))
    EXITTIME = int( input(">>>반복 끝나는 시간 설정 (초단위)::"))

    posList = []

    p1 = input('사각형의 왼쪽 위 좌표에 커서를 둔 후 엔터키 입력::')
    print(win32api.GetCursorPos())
    posList.append(win32api.GetCursorPos())
    p4 = input('사각형의 오른쪽 아래 좌표에 커서를 둔 후 엔터키 입력::')
    print (win32api.GetCursorPos())
    posList.append(win32api.GetCursorPos())
    p2 = (posList[1][0],posList[0][1])
    p3 = (posList[0][0],posList[1][1])

    posList.insert(1, p2)
    posList.insert(2, p3)
    print(posList)


    print(">>> 클릭 시작")
    now = time.time()
    while True:
        for pos in posList:
            win32api.SetCursorPos(pos)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            if time.time() - now > EXITTIME:
                exit(1)
            time.sleep(DELAY)