import time
from pynput import mouse,keyboard

time.sleep(5)

m_mouse=mouse.Controller()                  #创建一个鼠标
m_keyboard=keyboard.Controller()            #创建一个键盘
m_mouse.click(mouse.Button.left)            #点击鼠标左键

while True:
    m_keyboard.type('大咩！')                #输入轰炸信息
    m_keyboard.press(keyboard.Key.enter)    #按下Enter
    m_keyboard.release(keyboard.Key.enter)  #松开
    time.sleep(0.1)

