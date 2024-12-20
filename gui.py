# Form implementation generated from reading ui file 'spotify_snapshot.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_spotify_snapshot_window(object):
    def setupUi(self, spotify_snapshot_window):
        spotify_snapshot_window.setObjectName("spotify_snapshot_window")
        spotify_snapshot_window.resize(800, 443)
        spotify_snapshot_window.setMinimumSize(QtCore.QSize(800, 443))
        spotify_snapshot_window.setMaximumSize(QtCore.QSize(800, 443))
        self.widget = QtWidgets.QWidget(parent=spotify_snapshot_window)
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(460, 0, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.doc_link = QtWidgets.QLineEdit(parent=self.widget)
        self.doc_link.setGeometry(QtCore.QRect(340, 70, 421, 21))
        self.doc_link.setObjectName("doc_link")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.widget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 30, 281, 331))
        self.textBrowser.setObjectName("textBrowser")
        self.start_date = QtWidgets.QDateEdit(parent=self.widget)
        self.start_date.setGeometry(QtCore.QRect(360, 140, 110, 24))
        self.start_date.setCurrentSection(QtWidgets.QDateTimeEdit.Section.DaySection)
        self.start_date.setCalendarPopup(True)
        self.start_date.setDate(QtCore.QDate(2024, 12, 1))
        self.start_date.setObjectName("start_date")
        self.end_date = QtWidgets.QDateEdit(parent=self.widget)
        self.end_date.setGeometry(QtCore.QRect(620, 140, 110, 24))
        self.end_date.setCurrentSection(QtWidgets.QDateTimeEdit.Section.DaySection)
        self.end_date.setCalendarPopup(True)
        self.end_date.setDate(QtCore.QDate(2025, 1, 1))
        self.end_date.setObjectName("end_date")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(360, 110, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(620, 110, 101, 16))
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(parent=self.widget)
        self.line.setGeometry(QtCore.QRect(480, 110, 121, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(parent=self.widget)
        self.line_2.setGeometry(QtCore.QRect(530, 170, 20, 151))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setGeometry(QtCore.QRect(350, 200, 151, 20))
        self.label_4.setObjectName("label_4")
        self.songs_to_load = QtWidgets.QSpinBox(parent=self.widget)
        self.songs_to_load.setGeometry(QtCore.QRect(410, 200, 48, 20))
        self.songs_to_load.setObjectName("songs_to_load")
        self.artists_to_load = QtWidgets.QSpinBox(parent=self.widget)
        self.artists_to_load.setGeometry(QtCore.QRect(660, 200, 48, 20))
        self.artists_to_load.setObjectName("artists_to_load")
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        self.label_6.setGeometry(QtCore.QRect(600, 200, 161, 20))
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setGeometry(QtCore.QRect(330, 260, 191, 16))
        self.label_5.setObjectName("label_5")
        self.specific_song = QtWidgets.QLineEdit(parent=self.widget)
        self.specific_song.setGeometry(QtCore.QRect(350, 280, 131, 21))
        self.specific_song.setObjectName("specific_song")
        self.specific_artist = QtWidgets.QLineEdit(parent=self.widget)
        self.specific_artist.setGeometry(QtCore.QRect(600, 280, 131, 21))
        self.specific_artist.setObjectName("specific_artist")
        self.label_7 = QtWidgets.QLabel(parent=self.widget)
        self.label_7.setGeometry(QtCore.QRect(580, 260, 191, 16))
        self.label_7.setObjectName("label_7")
        self.submit_button = QtWidgets.QPushButton(parent=self.widget)
        self.submit_button.setGeometry(QtCore.QRect(362, 340, 381, 32))
        self.submit_button.setObjectName("submit_button")
        self.label.raise_()
        self.doc_link.raise_()
        self.textBrowser.raise_()
        self.start_date.raise_()
        self.end_date.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.label_4.raise_()
        self.songs_to_load.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.specific_song.raise_()
        self.specific_artist.raise_()
        self.label_7.raise_()
        self.artists_to_load.raise_()
        self.submit_button.raise_()
        spotify_snapshot_window.setCentralWidget(self.widget)
        self.menubar = QtWidgets.QMenuBar(parent=spotify_snapshot_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 36))
        self.menubar.setObjectName("menubar")
        spotify_snapshot_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=spotify_snapshot_window)
        self.statusbar.setObjectName("statusbar")
        spotify_snapshot_window.setStatusBar(self.statusbar)

        self.retranslateUi(spotify_snapshot_window)
        QtCore.QMetaObject.connectSlotsByName(spotify_snapshot_window)

    def retranslateUi(self, spotify_snapshot_window):
        _translate = QtCore.QCoreApplication.translate
        spotify_snapshot_window.setWindowTitle(_translate("spotify_snapshot_window", "Spotify Snapshot"))
        self.label.setText(_translate("spotify_snapshot_window", "Spotify Snapshot"))
        self.doc_link.setPlaceholderText(_translate("spotify_snapshot_window", "Paste Doc Link"))
        self.textBrowser.setHtml(_translate("spotify_snapshot_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15pt;\">You will need </span><a href=\"https://ifttt.com/applets/nin7BxVm-keep-a-log-of-your-recently-played-tracks\"><span style=\" font-size:14pt; text-decoration: underline; color:#0000ff;\">this IFTTTT</span></a><span style=\" font-size:15pt;\"> applet and connect it to an account with Google Sheets</span></li>\n"
"<li style=\" font-size:15pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Wait for your data to roll in as you listen to songs!</li>\n"
"<li style=\" font-size:15pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Make sure the Google Sheet that is created is open for viewing for anyone with a link</li>\n"
"<li style=\" font-size:15pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copy the Google Sheet link <span style=\" font-weight:600;\">from the browser</span>, Paste in in the first text box.</li>\n"
"<li style=\" font-size:15pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select the dates you want to find data between.</li>\n"
"<li style=\" font-size:15pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choose how many top songs &amp; artists you want to load.</li>\n"
"<li style=\" font-size:15pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pick a specific song or artist to see how many times you listened!</li></ol></body></html>"))
        self.label_2.setText(_translate("spotify_snapshot_window", "Select Start Date"))
        self.label_3.setText(_translate("spotify_snapshot_window", "Select End Date"))
        self.label_4.setText(_translate("spotify_snapshot_window", "Load top                songs"))
        self.label_6.setText(_translate("spotify_snapshot_window", "Load top                artists"))
        self.label_5.setText(_translate("spotify_snapshot_window", "How many times did I listen to"))
        self.specific_song.setPlaceholderText(_translate("spotify_snapshot_window", "Enter name of song"))
        self.specific_artist.setPlaceholderText(_translate("spotify_snapshot_window", "Enter name of artist"))
        self.label_7.setText(_translate("spotify_snapshot_window", "How many times did I listen to"))
        self.submit_button.setText(_translate("spotify_snapshot_window", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    spotify_snapshot_window = QtWidgets.QMainWindow()
    ui = Ui_spotify_snapshot_window()
    ui.setupUi(spotify_snapshot_window)
    spotify_snapshot_window.show()
    sys.exit(app.exec())
