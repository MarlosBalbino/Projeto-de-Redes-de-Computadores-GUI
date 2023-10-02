from qt_core import *
import sys
from game import Game


class Colors:
    blue0 = "#3ea8e6"
    blue1 = "#1B98E0"
    blue2 = "#247BA0"
    blue3 = "#006497"
    blue4 = "#13293D"
    white1 = "#E8F1F2"


class GameInfo:
    project_name = "Projeto de Redes de Computadores"
    game_title = "Adivinhe o animal"
    slogan = "Pense em um animal e eu vou tentar adivinhar que animal é."


class Button(QPushButton):
    def __init__(self, text, font_size="30pt"):
        super().__init__(text=text)
        # self.setFixedSize(80, 20)
        # self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setStyleSheet(f"""
            QPushButton{{
                background-color: {Colors.blue1};
                border-radius: 5px;
                font-size: {font_size};
                padding: 10px;  
            }}
            QPushButton::hover{{
                background-color: {Colors.blue0}
            }}
            QPushButton::pressed{{
                background-color: {Colors.blue2}
            }}               
        """)


class Page1(QFrame):
    def __init__(self, ui_app):
        super().__init__()
        self.ui_app = ui_app
        self.setStyleSheet(f"background-color: {Colors.blue4}")
        self.main_layout = QVBoxLayout(self)

        self.title_label = QLabel(GameInfo.game_title)
        self.title_label.setStyleSheet("font-size: 30pt")

        self.slogan = QLabel(GameInfo.slogan)
        self.slogan.setStyleSheet("font-size: 15pt")

        self.play_btn = Button("Jogar")
        self.play_btn.clicked.connect(self.button_handle)

        
        self.main_layout.addWidget(self.title_label, 0, Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.slogan, 0, Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.play_btn, 0, Qt.AlignmentFlag.AlignCenter)

    def button_handle(self):
        self.ui_app.main_widget.setCurrentWidget(self.ui_app.page2)
        self.ui_app.page2.play()


class Page2(QFrame):
    def __init__(self, ui_app):
        super().__init__()
        self.game = Game()
        self.game.sinal.connect(self.setQuestion)
        self.response = None
        self.setStyleSheet(f"background-color: {Colors.blue4}")
        self.main_layout = QVBoxLayout(self)

        self.question_label = QLabel()
        self.question_label.setStyleSheet("font-size: 15pt")
        self.response_frame = QFrame()
        self.response_frame_layout = QHBoxLayout(self.response_frame)
        self.response_frame_layout.setSpacing(50)

        self.yes_btn = Button("Sim")
        self.yes_btn.clicked.connect(self.yes_handle)
        self.no_btn = Button("Não")
        self.no_btn.clicked.connect(self.no_handle)

        self.response_frame_layout.addWidget(self.yes_btn)
        self.response_frame_layout.addWidget(self.no_btn)

        self.main_layout.addWidget(self.question_label, 0, Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.response_frame, 0, Qt.AlignmentFlag.AlignCenter)

    def setQuestion(self, text):
        self.question_label.setText(text)
        self.question_label.update()

    def play(self):
        self.game.start()

    def yes_handle(self):
        self.game.setResponse('s')
        self.game.continue_running()

    def no_handle(self):
        self.game.setResponse('n')
        self.game.continue_running()


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1366, 768)
        self.setWindowTitle(GameInfo.project_name)

        self.main_widget = QStackedWidget()

        self.page1 = Page1(self)
        self.page2 = Page2(self)       
        
        self.main_widget.addWidget(self.page1)
        self.main_widget.addWidget(self.page2)
        self.main_widget.setCurrentWidget(self.page1)

        self.setCentralWidget(self.main_widget)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
