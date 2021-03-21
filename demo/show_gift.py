# from pythoncode.gift import have_gift
import gift

def show_gift():
    have_gift = gift.have_gift
    if have_gift == True:
        print("收到礼物啦，好开心")
    else:
        print("等待礼物中...")
