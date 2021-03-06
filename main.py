import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from moviepy.editor import *

selected_file_path = ""
output_file_path = ""
output_file_name = ""
begin_time = 0
end_time = 0

# HH:MM:SS to seconds
def convert_time(time):
    time = time.split(":")
    return int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])

def start_subclipping():
    print("Button clicked")
    # Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
    #clip = VideoFileClip("myHolidays.mp4").subclip(50, 60)
    # Load selected_file and select the subclip begin_time - end_time
    clip = VideoFileClip(selected_file_path[0]).subclip(convert_time(begin_time), convert_time(end_time))
    video = CompositeVideoClip([clip])
    # Write the result to a file (many options available !)
    # video.write_videofile("myHolidays_edited.webm")
    video.write_videofile(output_file_path + "/" + output_file_name + ".webm")

def select_file():
    global selected_file_path
    selected_file_path = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file', '.')
    print(selected_file_path)


def select_directory():
    global output_file_path
    output_file_path = QtWidgets.QFileDialog.getExistingDirectory(None, 'Open file', '.')
    print(output_file_path)


def set_file_name(name):
    global output_file_name
    output_file_name = name
    print(output_file_name)

def set_begin_time(time):
    global begin_time
    begin_time = time
    print(begin_time)

def set_end_time(time):
    global end_time
    end_time = time
    print(end_time)


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setObjectName("MainWindow")
    win.resize(599, 305)

    btn_Start = QtWidgets.QPushButton(win)
    btn_Start.setGeometry(QtCore.QRect(280, 160, 151, 61))
    btn_Start.setObjectName("btn_Start")
    btn_Start.clicked.connect(start_subclipping)

    tbx_begin = QtWidgets.QTextEdit(win)
    tbx_begin.setGeometry(QtCore.QRect(110, 160, 141, 31))
    tbx_begin.setObjectName("tbx_begin")
    tbx_begin.textChanged.connect(lambda : set_begin_time(tbx_begin.toPlainText()))

    tbx_end = QtWidgets.QTextEdit(win)
    tbx_end.setGeometry(QtCore.QRect(110, 200, 141, 31))
    tbx_end.setObjectName("tbx_end")
    tbx_end.textChanged.connect(lambda : set_end_time(tbx_end.toPlainText()))

    btn_file = QtWidgets.QPushButton(win)
    btn_file.setGeometry(QtCore.QRect(110, 50, 151, 61))
    btn_file.setObjectName("btn_file")
    btn_file.clicked.connect(select_file)

    btn_destination = QtWidgets.QPushButton(win)
    btn_destination.setGeometry(QtCore.QRect(280, 50, 251, 61))
    btn_destination.setObjectName("btn_destination")
    btn_destination.clicked.connect(select_directory)

    tbx_name = QtWidgets.QTextEdit(win)
    tbx_name.setGeometry(QtCore.QRect(110, 120, 421, 31))
    tbx_name.setObjectName("tbx_name")
    tbx_name.textChanged.connect(lambda: set_file_name(tbx_name.toPlainText()))

    label = QtWidgets.QLabel(win)
    label.setGeometry(QtCore.QRect(10, 210, 67, 17))
    label.setObjectName("label")
    label_2 = QtWidgets.QLabel(win)
    label_2.setGeometry(QtCore.QRect(10, 170, 101, 17))
    label_2.setObjectName("label_2")
    label_3 = QtWidgets.QLabel(win)
    label_3.setGeometry(QtCore.QRect(10, 130, 101, 17))
    label_3.setObjectName("label_3")
    btn_Start.setText("Start subclip")
    btn_file.setText("Choose file")
    btn_destination.setText("Choose destination folder")
    label.setText("End time :")
    label_2.setText("Begin time :")
    label_3.setText("output name :")

    win.show()
    sys.exit(app.exec_())


# run qt app
if __name__ == "__main__":
    window()
