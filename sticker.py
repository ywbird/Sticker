import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie


class Sticker(QtWidgets.QMainWindow):
    def __init__(self, img_path, xy, size=1.0, on_top=False):
        super(Sticker, self).__init__()
        self.timer = QtCore.QTimer(self)
        self.img_path = img_path
        self.xy = xy
        self.from_xy = xy
        self.from_xy_diff = [0, 0]
        self.to_xy = xy
        self.to_xy_diff = [0, 0]
        self.speed = 60
        self.direction = [0, 0]  # x: 0(left), 1(right), y: 0(up), 1(down)
        self.size = size
        self.on_top = on_top
        self.localPos = None

        self.setupUi()
        self.show()

    # 마우스 놓았을 때
    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        if self.to_xy_diff == [0, 0] and self.from_xy_diff == [0, 0]:
            pass
        else:
            self.walk_diff(self.from_xy_diff, self.to_xy_diff,
                           self.speed, restart=True)

    # 마우스 눌렀을 때
    def mousePressEvent(self, a0: QtGui.QMouseEvent):
        self.localPos = a0.localPos()

    # 드래그 할 때
    def mouseMoveEvent(self, a0: QtGui.QMouseEvent):
        self.timer.stop()
        self.xy = [(a0.globalX() - self.localPos.x()),
                   (a0.globalY() - self.localPos.y())]
        self.move(*self.xy)

    # def walk(self, from_xy, to_xy, speed=60):
    #     self.from_xy = from_xy
    #     self.to_xy = to_xy
    #     self.speed = speed

    #     self.timer = QtCore.QTimer(self)
    #     self.timer.timeout.connect(self.__walkHandler)
    #     self.timer.start(1000 / self.speed)

    # 초기 위치로부터의 상대적 거리를 이용한 walk
    def walk_diff(self, from_xy_diff, to_xy_diff, speed=60, restart=False):
        self.from_xy_diff = from_xy_diff
        self.to_xy_diff = to_xy_diff
        self.from_xy = [self.xy[0] + self.from_xy_diff[0],
                        self.xy[1] + self.from_xy_diff[1]]
        self.to_xy = [self.xy[0] + self.to_xy_diff[0],
                      self.xy[1] + self.to_xy_diff[1]]
        self.speed = speed
        if restart:
            self.timer.start()
        else:
            self.timer.timeout.connect(self.__walkHandler)
            self.timer.start(1000 / self.speed)

    def __walkHandler(self):
        if self.xy[0] >= self.to_xy[0]:
            self.direction[0] = 0
        elif self.xy[0] < self.from_xy[0]:
            self.direction[0] = 1

        if self.direction[0] == 0:
            self.xy[0] -= 1
        else:
            self.xy[0] += 1

        if self.xy[1] >= self.to_xy[1]:
            self.direction[1] = 0
        elif self.xy[1] < self.from_xy[1]:
            self.direction[1] = 1

        if self.direction[1] == 0:
            self.xy[1] -= 1
        else:
            self.xy[1] += 1

        self.move(*self.xy)

    def setupUi(self):
        centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(centralWidget)

        flags = QtCore.Qt.WindowFlags(
            QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint if self.on_top else QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        label = QtWidgets.QLabel(centralWidget)
        movie = QMovie(self.img_path)
        label.setMovie(movie)
        movie.start()
        movie.stop()

        w = int(movie.frameRect().size().width() * self.size)
        h = int(movie.frameRect().size().height() * self.size)
        movie.setScaledSize(QtCore.QSize(w, h))
        movie.start()

        self.setGeometry(self.xy[0], self.xy[1], w, h)

    def mouseDoubleClickEvent(self, e):
        QtWidgets.qApp.quit()


def distance(x, y):
    if x >= y:
        result = x - y
    else:
        result = y - x
    return result


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    msgbox = QtWidgets.QMessageBox()
    argument = sys.argv

    # s = Sticker('gif/azzazel.gif', xy=[80, 200], size=1.0, on_top=True)
    if len(argument) >= 3:
        g = Sticker(argument[1], xy=list(map(int, argument[4].split(','))), size=float(
            argument[2]), on_top=bool(int(argument[3])))

    else:
        QtWidgets.qApp.quit()
        sys.exit()

    try:
        frm = list(map(int, argument[5].split(',')))
        to = list(map(int, argument[6].split(',')))
        g.walk_diff(from_xy_diff=frm, to_xy_diff=to, speed=int(argument[7]))

    except:
        pass

    # gif/gura.gif 0.2 1 200,180 200,200 120
    # to
    # g = Sticker('gif/gura.gif', xy=[200, 200], size=0.2, on_top=True)
    # g.walk_diff(from_xy_diff=[-100, 0], to_xy_diff=[100, 0], speed=180)

    sys.exit(app.exec_())
