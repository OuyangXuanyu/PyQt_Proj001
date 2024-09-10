import sys
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import QThread
from PySide6.QtCore import Signal
from pynput import keyboard


# 定义一个线程来处理全局键盘监听
class KeyListenerThread(QThread):
    key_pressed_signal = Signal(str)  # 定义一个信号来发送按键信息

    def __init__(self):
        super().__init__()
        self.listener = None

    def run(self):
        # 创建键盘监听器
        # with keyboard.Listener(on_press=self.on_press) as listener:
        #     listener.join()
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()  # 使用非阻塞方式启动监听器
        self.listener.join()

    def on_press(self, key):
        try:
            self.key_pressed_signal.emit(f'{key.char}')  # 发送按键字符
        except AttributeError:
            self.key_pressed_signal.emit(f'{key}')  # 发送特殊按键

    def stop(self):
        if self.listener:
            self.listener.stop()


# 创建 PyQt 应用程序
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt + Pynput Example")
        self.resize(300, 200)

        # 创建标签来显示按键信息
        self.label = QLabel("Press any key...")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        # 创建并启动键盘监听线程
        self.key_listener_thread = KeyListenerThread()
        self.key_listener_thread.key_pressed_signal.connect(self.update_label)  # 连接信号到槽
        self.key_listener_thread.start()

    def update_label(self, key_info):
        self.label.setText(key_info)  # 更新标签显示

    def closeEvent(self, event):
        self.key_listener_thread.stop()
        self.key_listener_thread.quit()
        self.key_listener_thread.wait()
        event.accept()
        # 这个调用父类无所谓
        # super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
