# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from lib.VideoPlayer import VideoPlayer
from numpy import ndarray

        
class QtVideoPlayer(QtWidgets.QWidget):

    
    frameUpdate = QtCore.pyqtSignal(ndarray)
        
        
    def __init__(self, filename, parent=None, refresh=int(1000/60)):
        
        QtWidgets.QWidget.__init__(self, parent)
        VideoPlayer(filename).interface(self)
        self.setupUi()
        
        self.setRefresh(refresh)
        self.timeSlider.setMaximum(int(self.videoPlayer.TIME))

    
    def setupUi(self):
        self.setObjectName("qtVideoPlayer")
        self.resize(532, 41)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.stopButton = QtWidgets.QPushButton(self)
        self.stopButton.setEnabled(True)
        self.stopButton.setObjectName("stopButton")
        self.gridLayout.addWidget(self.stopButton, 0, 2, 1, 1)
        self.playButton = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playButton.sizePolicy().hasHeightForWidth())
        self.playButton.setSizePolicy(sizePolicy)
        self.playButton.setMaximumSize(QtCore.QSize(1000, 1000))
        self.playButton.setShortcut("")
        self.playButton.setObjectName("playButton")
        self.gridLayout.addWidget(self.playButton, 0, 0, 1, 1)
        self.timeSlider = QtWidgets.QSlider(self)
        self.timeSlider.setProperty("value", 0)
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setObjectName("timeSlider")
        self.gridLayout.addWidget(self.timeSlider, 0, 3, 1, 1)
        self.pauseButton = QtWidgets.QPushButton(self)
        self.pauseButton.setEnabled(True)
        self.pauseButton.setMinimumSize(QtCore.QSize(75, 0))
        self.pauseButton.setMaximumSize(QtCore.QSize(16777215, 23))
        self.pauseButton.setObjectName("pauseButton")
        self.gridLayout.addWidget(self.pauseButton, 0, 1, 1, 1)
        self.timeLabel = QtWidgets.QLabel(self)
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.gridLayout.addWidget(self.timeLabel, 0, 4, 1, 1)

        self.retranslateUi()
        self.playButton.clicked.connect(self.play)
        self.pauseButton.clicked.connect(self.pause)
        self.stopButton.clicked.connect(self.stop)
        self.timeSlider.actionTriggered['int'].connect(self.setCurrentTime)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("qtVideoPlayer", "Form"))
        self.stopButton.setText(_translate("qtVideoPlayer", "Stop"))
        self.playButton.setText(_translate("qtVideoPlayer", "Play"))
        self.pauseButton.setText(_translate("qtVideoPlayer", "Pause"))
        self.timeLabel.setText(_translate("qtVideoPlayer", "0:00"))
        
        
    def setRefresh(self, t):
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(t)
        
        
    def update(self):
        QtWidgets.QWidget.update(self)
        _, frame = self.read()
        if _:
            self.frameUpdate.emit(frame)
            
            m, s = map(lambda n: str(n).zfill(2), self.videoPlayer.getRecordTime(mode=2))
            self.timeLabel.setText(f"{m}:{s}")
            
            v = int(self.videoPlayer.getRecordTime(mode=1))
            self.timeSlider.setValue(v)
        
        
    @staticmethod
    def test(config):
        
        import sys
        import cv2
        
        def showFrame(frame):
            
            data, width, height = frame.tobytes(), frame.shape[1], frame.shape[0]
            image = QtGui.QImage(data, width, height, QtGui.QImage.Format_BGR888)
            pixmap = QtGui.QPixmap(image)
            root.label.setPixmap(pixmap)
            
            
        def openVideo():
            
            layout.removeWidget(openButton)
            openButton.deleteLater()
            
            root.label = QtWidgets.QLabel()
            layout.addWidget(root.label)
            
            qtVideoPlayer = QtVideoPlayer(config["video"])
            qtVideoPlayer.frameUpdate.connect(showFrame)
            layout.addWidget(qtVideoPlayer)
            
        
        app = QtWidgets.QApplication(sys.argv)
        root = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        
        openButton = QtWidgets.QPushButton("Open video")
        openButton.clicked.connect(openVideo)
        layout.addWidget(openButton)
        
        root.setLayout(layout)
        root.setWindowTitle("QtVideoPlayer")
        root.show()
        sys.exit(app.exec_())
