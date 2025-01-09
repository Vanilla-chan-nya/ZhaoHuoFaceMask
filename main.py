import sys
import time

import win32gui
import win32con
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QScreen

def get_all_hwnd(hwnd, extra):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        title = win32gui.GetWindowText(hwnd)
        if title:
            hwnd_title[hwnd] = title

hwnd_title = {}
win32gui.EnumWindows(get_all_hwnd, None)

# 筛选出所有窗口标题，打印出来
for h, t in hwnd_title.items():
    print(h, t)

# 查找特定标题的窗口
game_title = 'Mortal'
game_hwnd = None
for hwnd, title in hwnd_title.items():
    if title == game_title:
        game_hwnd = hwnd
        break

if game_hwnd:
    # 将窗口激活到前台（如果需要的话）
    # 注：如果希望程序在后台运行，则不应将窗口带到前台
    win32gui.BringWindowToTop(game_hwnd)
    win32gui.ShowWindow(game_hwnd, win32con.SW_RESTORE)
    time.sleep(3)  # 增加延时以确保窗口已经到前台

    app = QApplication(sys.argv)
    # 获取屏幕对象
    screen = QApplication.primaryScreen()
    # 截取指定窗口
    img = screen.grabWindow(game_hwnd).toImage()
    # 将图像保存到硬盘
    img.save("screenshot.jpg")
    # 清理并退出应用
    app.quit()
else:
    print("No window with the title '{}' found.".format(game_title))
    # 清理并退出应用
