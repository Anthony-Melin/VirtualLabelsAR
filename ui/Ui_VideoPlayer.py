# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/VideoPlayer.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VideoPlayer(object):
    def setupUi(self, VideoPlayer):
        VideoPlayer.setObjectName("VideoPlayer")
        VideoPlayer.resize(532, 41)
        self.gridLayout = QtWidgets.QGridLayout(VideoPlayer)
        self.gridLayout.setObjectName("gridLayout")
        self.playButton = QtWidgets.QPushButton(VideoPlayer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playButton.sizePolicy().hasHeightForWidth())
        self.playButton.setSizePolicy(sizePolicy)
        self.playButton.setMaximumSize(QtCore.QSize(1000, 1000))
        self.playButton.setShortcut("")
        self.playButton.setObjectName("playButton")
        self.gridLayout.addWidget(self.playButton, 0, 0, 1, 1)
        self.timeSlider = QtWidgets.QSlider(VideoPlayer)
        self.timeSlider.setProperty("value", 0)
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setObjectName("timeSlider")
        self.gridLayout.addWidget(self.timeSlider, 0, 3, 1, 1)
        self.pauseButton = QtWidgets.QPushButton(VideoPlayer)
        self.pauseButton.setEnabled(True)
        self.pauseButton.setMinimumSize(QtCore.QSize(75, 0))
        self.pauseButton.setMaximumSize(QtCore.QSize(16777215, 23))
        self.pauseButton.setObjectName("pauseButton")
        self.gridLayout.addWidget(self.pauseButton, 0, 1, 1, 1)
        self.timeLabel = QtWidgets.QLabel(VideoPlayer)
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.gridLayout.addWidget(self.timeLabel, 0, 4, 1, 1)
        self.stopButton = QtWidgets.QPushButton(VideoPlayer)
        self.stopButton.setEnabled(True)
        self.stopButton.setObjectName("stopButton")
        self.gridLayout.addWidget(self.stopButton, 0, 2, 1, 1)

        self.retranslateUi(VideoPlayer)
        self.playButton.clicked.connect(VideoPlayer.play)
        self.pauseButton.clicked.connect(VideoPlayer.pause)
        self.timeSlider.actionTriggered['int'].connect(VideoPlayer.setCurrentTime)
        self.stopButton.clicked.connect(VideoPlayer.stop)
        QtCore.QMetaObject.connectSlotsByName(VideoPlayer)

    def retranslateUi(self, VideoPlayer):
        _translate = QtCore.QCoreApplication.translate
        VideoPlayer.setWindowTitle(_translate("VideoPlayer", "Form"))
        self.playButton.setText(_translate("VideoPlayer", "Play"))
        self.pauseButton.setText(_translate("VideoPlayer", "Pause"))
        self.timeLabel.setText(_translate("VideoPlayer", "0:00"))
        self.stopButton.setText(_translate("VideoPlayer", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VideoPlayer = QtWidgets.QWidget()
    ui = Ui_VideoPlayer()
    ui.setupUi(VideoPlayer)
    VideoPlayer.show()
    sys.exit(app.exec_())
