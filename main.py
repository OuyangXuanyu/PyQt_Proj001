import sys
import pyautogui
import time
from pynput import keyboard

from PySide6.QtCore import (QDateTime, QTimer)
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import (QLabel, QMessageBox, QLineEdit)
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import QTimer, Qt, QThread, Signal
from PySide6.QtGui import QCursor

from UI_Main.main_ import Ui_Form


class KeyListenerThread(QThread):
    key_pressed_signal = Signal(str)

    def __init__(self, parent=None):
        super(KeyListenerThread, self).__init__(parent)
        self.listener = None

    def run(self):
        # 阻塞方式
        # with keyboard.Listener(on_press=self.on_press) as listener:
        #     listener.join()
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()  # 使用非阻塞方式启动监听器
        self.listener.join()

    def on_press(self, key):
        try:
            self.key_pressed_signal.emit(f'{key.char}')
        except AttributeError:
            self.key_pressed_signal.emit(f'{key}')

    def stop(self):
        if self.listener:
            self.listener.stop()


class MyStartForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyStartForm, self).__init__(parent)
        self.X_POS = 0
        self.Y_POS = 0
        self.TIMES = 0
        self.TIME_TICK = 0.0
        self.n_pos_y = None
        self.n_pos_x = None
        self.setupUi(self)

        self.start_mode = None
        self.exit_mode = None

        self.start_time = None
        self.end_time = None

        self.click_count = 0

        self.running_state = False

        self.start_button.clicked.connect(self.start_button_clicked)

        # 实时更新鼠标坐标（QTimer）
        self.timer_nPosXY = QTimer(self)
        self.timer_nPosXY.timeout.connect(self.update_nPosXY)
        self.timer_nPosXY.start(20)

        # 鼠标点击动作（QTimer）
        self.timer_click = QTimer(self)
        self.timer_click.timeout.connect(self.click_fun)

        # 点击总时间（QTimer）  # 要不要->要！通过它来实现中断的操作，开个循环（self.timer.start(0)）不断去判断是否达特定值
        self.full_timer = QTimer(self)
        self.full_timer.timeout.connect(self.fulltime_fun)

        # start mode radio button toggled function
        self.startmode1_radiobutton.toggled.connect(self.startmode1_fun)
        self.startmode2_radiobutton.toggled.connect(self.startmode2_fun)

        # 启动时默认的运行方式
        self.startmode1_radiobutton.setChecked(True)

        # 选择默认的退出方式
        # self.radioButton.setChecked(True)  # 移动鼠标实现退出

        # 创建并启动键盘监听线程
        self.key_listener_thread = KeyListenerThread()
        self.key_listener_thread.key_pressed_signal.connect(self.key_to_cancel)
        self.key_listener_thread.start()

    def startmode1_fun(self):
        self.start_mode = 0
        self.posX_input_edit.setEnabled(False)
        self.posY_input_edit.setEnabled(False)
        self.radioButton.setEnabled(False)
        self.radioButton_2.setChecked(True)

    def startmode2_fun(self):
        self.start_mode = 1
        self.posX_input_edit.setEnabled(True)
        self.posY_input_edit.setEnabled(True)
        self.radioButton.setEnabled(True)
        self.radioButton.setChecked(True)

    def update_nPosXY(self):  # 更新实时鼠标坐标函数
        self.n_pos_x, self.n_pos_y = pyautogui.position()
        self.nPosXY_value.setText(f'({self.n_pos_x}, {self.n_pos_y})')

        # 使用下面函数与显示器和DPI调节有关，由于连点器是根据pyautogui库实现，因此不考虑自带函数
        # pos = QCursor.pos()
        # self.nPosXY_value.setText(f'({pos.x()}, {pos.y()})')

    def start_button_clicked(self):  # 点击开始工作的函数
        self.start_time = time.time()
        # 判断选择的运行模式
        """
        self.start_mode = 0
        try:
            if self.startmode1_radiobutton.isChecked():
                self.start_mode = 0
            elif self.startmode2_radiobutton.isChecked():
                self.start_mode = 1
            else:
                self.start_mode = -1
                msgbox = QMessageBox(self)
                msgbox.setWindowTitle('提示')
                msgbox.setText('非法！')
                msgbox.exec()
                return
        except Exception as ex:
            print(ex)
            msgbox = QMessageBox(self)
            msgbox.setWindowTitle('提示')
            msgbox.setText(f'{ex}\n非法！')
            msgbox.exec()
            return
        """

        # 判断选择的退出模式

        self.exit_mode = 0
        try:
            if self.radioButton.isChecked():
                self.exit_mode = 0
            elif self.radioButton_2.isChecked():
                self.exit_mode = 1
            elif self.radioButton_3.isChecked():
                self.exit_mode = 2
            else:
                self.exit_mode = -1
                msgbox = QMessageBox(self)
                msgbox.setWindowTitle('提示')
                msgbox.setText('非法！')
                msgbox.exec()
                return
        except Exception as ex:
            print(ex)
            msgbox = QMessageBox(self)
            msgbox.setWindowTitle('提示')
            msgbox.setText(f'{ex}\n非法！')
            msgbox.exec()
            return

        # 判断输入的值是否非法->类型转换
        try:
            if self.start_mode == 1:
                x_pos = int(self.posX_input_edit.text())
                y_pos = int(self.posY_input_edit.text())
            time_tick = float(self.timeTick_input_edit.text())
            times = int(self.times_input_edit.text())

            # 在（移动鼠标退出和）ESC按键退出时可设置按键的次数为无穷（-1）
            print((times > 0 and self.exit_mode == 2))
            print(times >= -1 and times != 0 and self.exit_mode == 1)
            if (times <= 0 and self.exit_mode == 2) or ((times < -1 or times == 0) and (self.exit_mode == 1 or self.exit_mode == 0)):
                msgbox = QMessageBox(self)
                msgbox.setWindowTitle('提示')
                msgbox.setText(f'数据非法！')
                msgbox.exec()
                return
            self.fullTime_value.setText(str(times * time_tick))
        except Exception as ex:
            print(ex)
            msgbox = QMessageBox(self)
            msgbox.setWindowTitle('提示')
            msgbox.setText(f'{ex}\n非法！')
            msgbox.exec()
            return

        # 确定当前输入的全部数值并赋值给全局变量
        if self.start_mode == 1:
            self.X_POS = x_pos
            self.Y_POS = y_pos
            print(x_pos, y_pos, end=' ')
        self.TIMES = times
        self.TIME_TICK = time_tick

        print(time_tick, times, self.start_mode, self.exit_mode)

        # 运行模式 0
        if self.start_mode == 0:
            # 直接点击
            self.timer_click.start(int(1000 * self.TIME_TICK))
            self.full_timer.start(int((1000 * self.TIME_TICK) / 2))
            self.running_state = True
            self.startmode1_radiobutton.setEnabled(False)
            self.startmode2_radiobutton.setEnabled(False)
            self.radioButton_2.setEnabled(False)
            self.radioButton_3.setEnabled(False)
            self.start_button.setEnabled(False)

            return

        # TODO 运行模式 1

        # 记录先前的鼠标坐标位置
        bef_x_pos = self.n_pos_x
        bef_y_pos = self.n_pos_y
        # 判断输入的坐标是否有效->是否存在该坐标

        pyautogui.moveTo(x_pos, y_pos)
        self.n_pos_x, self.n_pos_y = pyautogui.position()
        if x_pos != self.n_pos_x or y_pos != self.n_pos_y:
            # 返回之前的鼠标位置
            pyautogui.moveTo(bef_x_pos, bef_y_pos)
            msgbox = QMessageBox(self)
            msgbox.setWindowTitle('提示')
            msgbox.setText('坐标无效！')
            msgbox.exec()
            return

        # 开始连点操作
        self.timer_click.start(int(1000 * self.TIME_TICK))
        self.full_timer.start(int((1000 * self.TIME_TICK) / 2))

        self.running_state = True

        self.startmode1_radiobutton.setEnabled(False)
        self.startmode2_radiobutton.setEnabled(False)
        self.radioButton_2.setEnabled(False)
        self.radioButton_3.setEnabled(False)
        self.start_button.setEnabled(False)

    def click_fun(self):
        if self.start_mode == 0:
            pyautogui.click()
        elif self.start_mode == 1:
            if (self.exit_mode == 0 and (self.X_POS, self.Y_POS) == (self.n_pos_x, self.n_pos_y)) or self.exit_mode:
                pyautogui.click(self.X_POS, self.Y_POS)
            else:
                self.stop_fun()
                return
        self.click_count += 1
        print(self.click_count, self.TIMES)

    def fulltime_fun(self):
        if self.click_count >= self.TIMES:
            self.stop_fun()
            self.end_time = time.time()
            print(self.start_time, self.end_time)
            print(self.start_time - self.end_time)
            self.running_state = False
        else:
            pass

    # def keyPressEvent(self, event):
    #     if self.exit_mode == 1 and event.key() == Qt.Key_Escape and self.running_state and True == False:
    #         self.stop_fun()
    #         print("ESC was pressed")
    #     else:
    #         # 如果不是ESC键，可以选择调用父类的keyPressEvent方法
    #         super().keyPressEvent(event)

    def stop_fun(self):
        self.timer_click.stop()
        self.full_timer.stop()
        self.click_count = 0
        if self.start_mode == 1:
            self.radioButton.setEnabled(True)

        self.radioButton_2.setEnabled(True)
        self.radioButton_3.setEnabled(True)

        self.startmode1_radiobutton.setEnabled(True)
        self.startmode2_radiobutton.setEnabled(True)

        self.start_button.setEnabled(True)

        self.running_state = False

    def key_to_cancel(self, key_info):
        # print(key_info)
        if key_info == "Key.esc":
            # todo
            print("ESC")
            if self.exit_mode == 1 and self.running_state:
                self.stop_fun()
                print("ESC was pressed")

    def closeEvent(self, event):
        self.key_listener_thread.stop()
        self.key_listener_thread.quit()
        self.key_listener_thread.wait()
        event.accept()
        # 这个调用父类无所谓
        # super().closeEvent(event)


if __name__ == "__main__":
    app_start = QApplication(sys.argv)
    # 初始化窗口
    my_start = MyStartForm()
    my_start.show()
    # app_start.exec()
    sys.exit(app_start.exec())
