import pyautogui
import time


def click_at_coordinates(x, y, interval=1, clicks=10):
    """
    在指定坐标上连续点击。

    :param x: 点击的X坐标
    :param y: 点击的Y坐标
    :param interval: 每次点击之间的时间间隔（秒）
    :param clicks: 点击次数
    """
    for _ in range(clicks):
        pyautogui.click(x, y)
        time.sleep(interval)

    # 示例：在屏幕坐标(100, 200)上每隔1秒点击一次，共点击10次


click_at_coordinates(1075, 333, interval=1, clicks=10)

# 注意：运行此脚本时，请确保你的鼠标光标不在需要自动化控制的窗口上，
# 因为pyautogui的点击是基于屏幕坐标的，而不是基于窗口的。