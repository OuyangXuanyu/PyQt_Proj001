# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(586, 161)
        self.nPosXY_label = QLabel(Form)
        self.nPosXY_label.setObjectName(u"nPosXY_label")
        self.nPosXY_label.setGeometry(QRect(170, 120, 131, 25))
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(420, 11, 151, 141))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setAutoFillBackground(False)

        self.verticalLayout.addWidget(self.radioButton_3)

        self.posX_input_label = QLabel(Form)
        self.posX_input_label.setObjectName(u"posX_input_label")
        self.posX_input_label.setGeometry(QRect(140, 21, 54, 20))
        self.posX_input_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.posY_input_label = QLabel(Form)
        self.posY_input_label.setObjectName(u"posY_input_label")
        self.posY_input_label.setGeometry(QRect(140, 51, 54, 20))
        self.posY_input_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.posX_input_edit = QLineEdit(Form)
        self.posX_input_edit.setObjectName(u"posX_input_edit")
        self.posX_input_edit.setGeometry(QRect(200, 21, 61, 20))
        self.posX_input_edit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.posY_input_edit = QLineEdit(Form)
        self.posY_input_edit.setObjectName(u"posY_input_edit")
        self.posY_input_edit.setGeometry(QRect(200, 51, 61, 20))
        self.posY_input_edit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.nPosXY_value = QLabel(Form)
        self.nPosXY_value.setObjectName(u"nPosXY_value")
        self.nPosXY_value.setGeometry(QRect(300, 120, 91, 25))
        self.nPosXY_value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.start_button = QPushButton(Form)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(150, 81, 111, 31))
        self.times_input_edit = QLineEdit(Form)
        self.times_input_edit.setObjectName(u"times_input_edit")
        self.times_input_edit.setGeometry(QRect(340, 51, 61, 20))
        self.times_input_edit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.timeTick_input_label = QLabel(Form)
        self.timeTick_input_label.setObjectName(u"timeTick_input_label")
        self.timeTick_input_label.setGeometry(QRect(270, 21, 61, 20))
        self.timeTick_input_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timeTick_input_edit = QLineEdit(Form)
        self.timeTick_input_edit.setObjectName(u"timeTick_input_edit")
        self.timeTick_input_edit.setGeometry(QRect(340, 21, 61, 20))
        self.timeTick_input_edit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.times_input_label = QLabel(Form)
        self.times_input_label.setObjectName(u"times_input_label")
        self.times_input_label.setGeometry(QRect(270, 51, 61, 20))
        self.times_input_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fullTime_label = QLabel(Form)
        self.fullTime_label.setObjectName(u"fullTime_label")
        self.fullTime_label.setGeometry(QRect(270, 80, 61, 31))
        self.fullTime_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fullTime_value = QLabel(Form)
        self.fullTime_value.setObjectName(u"fullTime_value")
        self.fullTime_value.setGeometry(QRect(340, 80, 54, 31))
        self.fullTime_value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 20, 113, 131))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.startmode1_radiobutton = QRadioButton(self.groupBox_2)
        self.startmode1_radiobutton.setObjectName(u"startmode1_radiobutton")

        self.verticalLayout_2.addWidget(self.startmode1_radiobutton)

        self.startmode2_radiobutton = QRadioButton(self.groupBox_2)
        self.startmode2_radiobutton.setObjectName(u"startmode2_radiobutton")

        self.verticalLayout_2.addWidget(self.startmode2_radiobutton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.nPosXY_label.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u9f20\u6807\u5750\u6807\uff1a(x, y) = ", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u505c\u6b62\u6a21\u5f0f", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u66f4\u6539\u9f20\u6807\u5750\u6807\u4f4d\u7f6e", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u6309\u952e\u505c\u6b62(ESC)", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"(!!)\u7b49\u5f85\u81f3\u7ed3\u675f", None))
        self.posX_input_label.setText(QCoreApplication.translate("Form", u"X\u5750\u6807", None))
        self.posY_input_label.setText(QCoreApplication.translate("Form", u"Y\u5750\u6807", None))
        self.nPosXY_value.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.start_button.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.timeTick_input_label.setText(QCoreApplication.translate("Form", u"\u65f6\u95f4\u95f4\u9694(s)", None))
        self.times_input_label.setText(QCoreApplication.translate("Form", u"\u6b21\u6570", None))
        self.fullTime_label.setText(QCoreApplication.translate("Form", u"\u603b\u65f6\u957f(s)", None))
        self.fullTime_value.setText(QCoreApplication.translate("Form", u"NULL", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u542f\u52a8\u6a21\u5f0f", None))
        self.startmode1_radiobutton.setText(QCoreApplication.translate("Form", u"\u8ddf\u968f\u9f20\u6807\u8fde\u70b9", None))
        self.startmode2_radiobutton.setText(QCoreApplication.translate("Form", u"\u6307\u5b9a\u5750\u6807\u8fde\u70b9", None))
    # retranslateUi

