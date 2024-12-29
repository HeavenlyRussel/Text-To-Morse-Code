from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QTextEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text to Morse Code Translator")
        self.show()
        
        # Set the background color using QPalette
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("black"))  # Dark color
        self.setPalette(palette)
       
        # Setting the layout(s)
        vertical_layout1 = QVBoxLayout()
        self.setLayout(vertical_layout1)
        vertical_layout1.setAlignment(Qt.AlignCenter)
        vertical_layout2 = QVBoxLayout()
        vertical_layout3 = QVBoxLayout()
        horizontal_layout1 = QHBoxLayout()
        
        # Setting the font settings for the texts
        font_settings_for_text1 = QFont()
        font_settings_for_text1.setFamily("Lucida Handwriting")
        font_settings_for_text1.setPointSize(14)
        font_settings_for_text2 = QFont()
        font_settings_for_text2.setFamily("Lucida Handwriting")
        font_settings_for_text2.setPointSize(14)
        
        # Adding the texts on the window
        text1 = QLabel("Enter here the text to be translated:")
        text1.setStyleSheet("color: white;")
        text1.setFont(font_settings_for_text1)
        text2 = QLabel("Output:")
        text2.setStyleSheet("color: white;")
        text2.setFont(font_settings_for_text2)
        text3 = QLabel("Input:")
        text3.setStyleSheet("color: white;")
        text3.setFont(font_settings_for_text2)
        
        # Adding buttons on the window
        button_settings1 = QFont()
        button_settings1.setFamily("Lucida Handwriting")
        button_settings1.setPointSize(12)
        button1 = QPushButton("Translate", clicked = lambda: self.when_button1_is_clicked())
        button1.setStyleSheet("border-style: solid; border-color: blue; border-width: 2px; border-radius: 5px; height: 35px; color: white;")
        button1.setFont(button_settings1)
        
        # Adding text boxes
        self.text_box1 = QTextEdit()
        self.text_box1.setStyleSheet("border-style: solid; border-color: blue; border-width: 4px; border-radius: 5px; font-size: 20px;")
        self.text_box2 = QTextEdit(readOnly=True)
        self.text_box2.setStyleSheet("border-style: solid; border-color: blue; border-width: 4px; border-radius: 5px; font-size: 20px;")
        self.text_box3 = QTextEdit()
        self.text_box3.setStyleSheet("border-style: solid; border-color: blue; border-width: 4px; border-radius: 5px; font-size: 20px;")
        
        # Adding widgets to vertical_layout2
        vertical_layout2.addWidget(text2)
        vertical_layout2.addWidget(self.text_box2)
        
        # Adding widgets to vertical_layout3
        vertical_layout3.addWidget(text3)
        vertical_layout3.addWidget(self.text_box3)
        
        # Adding widgets to the horizontal_layout1
        horizontal_layout1.addLayout(vertical_layout3)
        horizontal_layout1.addLayout(vertical_layout2)
        
        # Adding all to the main layout
        vertical_layout1.addWidget(text1)
        vertical_layout1.addWidget(self.text_box1)
        vertical_layout1.addWidget(button1)
        vertical_layout1.addLayout(horizontal_layout1)
        
    # Function that executes when button1 is clicked
    def when_button1_is_clicked(self):
        self.translate_text()

    # Key press event handler for Enter key
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:  # or event.key() == Qt.Key_Enter
            self.translate_text()

    # Translation function
    def translate_text(self):
        self.text_box2.clear()
        current_text = self.text_box1.toPlainText()
        lowercased_text = current_text.lower()
        turn_current_text_to_list = list(lowercased_text)
        
        self.text_box3.setText(self.text_box1.toPlainText())
        
        # Morse code dictionary
        morse_dict = {
            'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.",
            'g': "--.", 'h': "....", 'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..",
            'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 'q': "--.-", 'r': ".-.",
            's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-",
            'y': "-.--", 'z': "--..", ' ': "/"
        }
        
        # Translate each character to Morse
        for index in turn_current_text_to_list:
            if index in morse_dict:
                self.text_box2.insertPlainText(morse_dict[index] + " ")

        # Clear the input box after translation
        self.text_box1.clear()

# Run the application
app = QApplication([])
window = Window()
app.exec_()
