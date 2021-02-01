# -*- coding: utf-8 -*-


import tkinter as tk
from PIL import Image, ImageTk


############################################################################################
class VideoWidget(tk.Canvas):
    
    """
        A dedicated class for displaying frame from VideoPlayer in tkinter canvas.
    """

    ########################################################################################
    def setVideoPlayer(self, videoPlayer):
        
        """
            Bind a VideoPlayer object and start to display.
            
            @arg videoPlayer: VideoPlayer object from wich provides frames
        """

        self.videoPlayer = videoPlayer
        self.after(1, self.tick)


    ########################################################################################
    def updateImage(self):
        
        """
            Read a frame from the VideoPlayer and update the canvas.
        """

        _, frame = self.videoPlayer.read() # reading
        if _:
            width, height = int(self["width"]), int(self["height"])
            image = Image.fromarray(frame).resize((width, height))
            self.photoImage = ImageTk.PhotoImage(image)
            self.create_image(0, 0, image=self.photoImage, anchor="nw")


    ########################################################################################
    def tick(self):
        
        """
            Update frame and schedule next update.
        """
        
        self.updateImage()
        self.after(1000//30, self.tick)
        
    
    ########################################################################################
    @staticmethod
    def test():
        
        import time
        import tkinter
#         import OpenGL.GL
#         import OpenGL.GL.shaders as shaders
#         from pyopengltk import OpenGLFrame
        import numpy as np
        import ctypes as ct
        
        from lib.VideoPlayer import VideoPlayer

        vertex = """
        #version 130 
        in vec2 pos;

        void main()
        {
           gl_Position = vec4(pos.x, pos.y, 1.0, 1.0);
        }
        """

        fragment = """
        #version 130

        void main()
        {
           gl_FragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """



#         class FrameWidget(OpenGLFrame):

#             VERTICES = np.asarray([
#                 -1.0, -1.0, 1.0,
#                  1.0, -1.0, 1.0,
#                  1.0,  1.0, 1.0,
#                 -1.0,  1.0, 1.0,
#             ], dtype=np.float32)

#             TEXCOORDS = np.asarray([
#                 0, 1,
#                 1, 1,
#                 1, 0,
#                 0, 0,
#             ], dtype=np.float32)

#             COLORS = np.asarray([
#                 1, 0, 0,
#                 1, 1, 0,
#                 0, 1, 0,
#                 0, 0, 1,
#             ], dtype=np.float32)

#             VERTEX = """
#             #version 330

#             in vec3 aPos;
#             in vec3 aCol;
#             in vec2 aTexcoord;

#             out vec3 fCol;
#             out vec2 fTexcoord;

#             void main()
#             {
#                 gl_Position = vec4(aPos, 1.0);
#                 fCol = aCol;
#                 fTexcoord = aTexcoord;
#             }
#             """

#             FRAGMENT = """
#             #version 330

#             in vec3 fCol;
#             in vec2 fTexcoord;
#             uniform sampler2D uTexture;
#             uniform int uDrawmode;

#             void main()
#             {
#                 if (uDrawmode == 1)
#                     gl_FragColor = vec4(fCol, 1.0);
#                 else
#                     gl_FragColor = texture(uTexture, fTexcoord).bgra;//vec4(color, 1.0);
#             }
#             """

#             DRAWMODE_TEXTURE = 0
#             DRAWMODE_COLOR = 1


#             def initgl(self):

#                 glClearColor(0.0, 0.0, 0.0, 1.0)
#                 glViewport(0, 0, self.width, self.height)

#                 self.shader = shaders.compileProgram(
#                 shaders.compileShader(FrameWidget.VERTEX, GL_VERTEX_SHADER),
#                 shaders.compileShader(self.FRAGMENT, GL_FRAGMENT_SHADER)
#                 )
#                 glUseProgram(self.shader)
#                 self.shader.aPos = glGetAttribLocation(self.shader, "aPos")
#                 self.shader.aCol = glGetAttribLocation(self.shader, "aCol")
#                 self.shader.aTexcoord = glGetAttribLocation(self.shader, "aTexcoord")
#                 self.shader.uTexture = glGetUniformLocation(self.shader, "uTexture")
#                 self.shader.uDrawmode = glGetUniformLocation(self.shader, "uDrawmode")

#                 self.vertexBuffer = glGenBuffers(1)
#                 glBindBuffer(GL_ARRAY_BUFFER, self.vertexBuffer)
#                 glBufferData(GL_ARRAY_BUFFER, FrameWidget.VERTICES.nbytes, FrameWidget.VERTICES, GL_STATIC_DRAW)

#                 self.colorBuffer = glGenBuffers(1)
#                 glBindBuffer(GL_ARRAY_BUFFER, self.colorBuffer)
#                 glBufferData(GL_ARRAY_BUFFER, FrameWidget.COLORS.nbytes, FrameWidget.COLORS, GL_STATIC_DRAW)

#                 self.texBuffer = glGenBuffers(1)
#                 glBindBuffer(GL_ARRAY_BUFFER, self.texBuffer)
#                 glBufferData(GL_ARRAY_BUFFER, FrameWidget.TEXCOORDS.nbytes, FrameWidget.TEXCOORDS, GL_STATIC_DRAW)

#                 self.frameTexture = glGenTextures(1)
#                 glActiveTexture(GL_TEXTURE0+self.frameTexture)
#                 glBindTexture(GL_TEXTURE_2D, self.frameTexture)
#                 glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
#                 glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
#                 glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
#                 glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
#                 glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, self.frame_width, self.frame_height, 0, GL_RGB, GL_UNSIGNED_BYTE, None)
#                 glGenerateMipmap(GL_TEXTURE_2D)

#                 self.start = time.time()
#                 self.nframes = 0
#                 self.drawmode = FrameWidget.DRAWMODE_TEXTURE


#             def redraw(self):

#                 glClear(GL_COLOR_BUFFER_BIT)

#                 glUseProgram(self.shader)
#                 glUniform1i(self.shader.uDrawmode, self.drawmode)

#                 glBindBuffer(GL_ARRAY_BUFFER, self.vertexBuffer)
#                 glEnableVertexAttribArray(self.shader.aPos)
#                 glVertexAttribPointer(self.shader.aPos, 3, GL_FLOAT, False, 0, ct.c_void_p(0))

#                 glBindBuffer(GL_ARRAY_BUFFER, self.colorBuffer)
#                 glEnableVertexAttribArray(self.shader.aCol)
#                 glVertexAttribPointer(self.shader.aCol, 3, GL_FLOAT, False, 0, ct.c_void_p(0))

#                 glBindBuffer(GL_ARRAY_BUFFER, self.texBuffer)
#                 glEnableVertexAttribArray(self.shader.aTexcoord)
#                 glVertexAttribPointer(self.shader.aTexcoord, 2, GL_FLOAT, False, 0, ct.c_void_p(0))

#                 if self.frame is not None:
#                     glBindTexture(GL_TEXTURE_2D, self.frameTexture)
#                     glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, 1920, 1080, GL_RGB, GL_UNSIGNED_BYTE, self.frame)
#                     glUniform1i(self.shader.uTexture, self.frameTexture)
#                 else:
#                     glUniform1i(self.shader.uTexture, 0)

#                 glDrawArrays(GL_TRIANGLE_FAN, 0, 4)


#                 tm = time.time() - self.start
#                 self.nframes += 1
#                 print("fps",self.nframes / tm, end="\r" )


#             def settingForFrames(self, width, height, frame=None):

#                 self.frame_width = width
#                 self.frame_height = height
#                 self.frame = frame


#             def updateFrame(self, frame):

#                 self.frame = frame


#             def setDrawmode(self, drawmode):

#                 self.drawmode = drawmode


#         class VideoWidget(FrameWidget):


#             def setVideoplayer(self, videoplayer):

#                 self.videoplayer = videoplayer
#                 self.settingForFrames(videoplayer.WIDTH, videoplayer.HEIGHT)


#             def redraw(self):

#                 _, frame = self.videoplayer.read()
#                 if _ or self.videoplayer.status==VideoPlayer.STOP: self.updateFrame(frame)

#                 FrameWidget.redraw(self)



#         def colorMode():

#             videoWidget.setDrawmode(FrameWidget.DRAWMODE_COLOR)


#         def textureMode():

#             videoWidget.setDrawmode(FrameWidget.DRAWMODE_TEXTURE)
#             frame = cv2.imread("tests/test.png")
#             videoWidget.updateFrame(frame)


#         def clearTexture():

#             videoWidget.setDrawmode(FrameWidget.DRAWMODE_TEXTURE)
#             videoWidget.updateFrame(None)


        root = tkinter.Tk()

#         tk.Button(root, text="Color Mode", command=colorMode).pack()
#         tk.Button(root, text="Texture Mode", command=textureMode).pack()
#         tk.Button(root, text="Clear Texture", command=clearTexture).pack()

        videoPlayer = VideoPlayer("C:\\Users\\Anthony\\Videos\\Base Profile\\Syphon Filter - First Level.mp4")
    
        tk.Button(root, text="Play", command=videoPlayer.play).pack()
        tk.Button(root, text="Pause", command=videoPlayer.pause).pack()
        tk.Button(root, text="Stop", command=videoPlayer.stop).pack()
        tk.Button(root, text="Release", command=videoPlayer.release).pack()

        def scaleCallback(value):
            videoPlayer.setCurrentTime(var.get(), mode=Video.SECONDS)

        var = tk.DoubleVar()
        scale = tk.Scale(root, orient=tk.HORIZONTAL, variable=var, command=scaleCallback, to=videoPlayer.TIME)
        scale.pack(fill=tk.X, expand=tk.TRUE)

        label = tk.Label(root, text="0:00")
        label.pack()

        videoWidget = VideoWidget(root, width=640, height=480)
        videoWidget.setVideoPlayer(videoPlayer)
        videoWidget.pack(fill=tkinter.BOTH, expand=tkinter.YES)
        videoWidget.animate = True

        root.mainloop()


        #def colorMode():

#            videoWidget.setDrawmode(FrameWidget.DRAWMODE_COLOR)


        #def textureMode():

        #    videoWidget.setDrawmode(FrameWidget.DRAWMODE_TEXTURE)
        #    frame = cv2.imread("tests/test.png")
        #    videoWidget.updateFrame(frame)


        #def clearTexture():

        #    videoWidget.setDrawmode(FrameWidget.DRAWMODE_TEXTURE)
        #    videoWidget.updateFrame(None)


        #root = tkinter.Tk()

        #tk.Button(root, text="Color Mode", command=colorMode).pack()
        #tk.Button(root, text="Texture Mode", command=textureMode).pack()
        #tk.Button(root, text="Clear Texture", command=clearTexture).pack()

        #videoWidget = FrameWidget(root, width=640, height=480)
        #videoWidget.settingForFrames(1920, 1080)
        #videoWidget.pack(fill=tkinter.BOTH, expand=tkinter.YES)
        #videoWidget.animate = True

        #root.mainloop()

