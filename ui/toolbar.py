from PyQt5.QtWidgets import QToolBar, QAction, QColorDialog, QFontDialog, QTextEdit, QMessageBox
from PyQt5.QtCore import Qt

class Toolbar(QToolBar):
    def __init__(self, text_edit: QTextEdit, parent=None):
        super().__init__(parent)
        self.text_edit = text_edit
        self.init_toolbar()

    def init_toolbar(self):
        # Font selector
        font_action = QAction("Font", self)
        font_action.triggered.connect(self.change_font)
        self.addAction(font_action)

        # Text color
        color_action = QAction("Text Color", self)
        color_action.triggered.connect(self.change_color)
        self.addAction(color_action)

        # Alignment
        align_left = QAction("Align Left", self)
        align_left.triggered.connect(lambda: self.set_alignment(Qt.AlignLeft))
        self.addAction(align_left)

        align_center = QAction("Align Center", self)
        align_center.triggered.connect(lambda: self.set_alignment(Qt.AlignCenter))
        self.addAction(align_center)

        align_right = QAction("Align Right", self)
        align_right.triggered.connect(lambda: self.set_alignment(Qt.AlignRight))
        self.addAction(align_right)

        # Bullet points
        bullet_action = QAction("Bullet Points", self)
        bullet_action.triggered.connect(self.add_bullet_point)
        self.addAction(bullet_action)

        # Numbering
        numbering_action = QAction("Numbering", self)
        numbering_action.triggered.connect(self.add_numbering)
        self.addAction(numbering_action)

    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.text_edit.setFont(font)

    def change_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_edit.setTextColor(color)

    def set_alignment(self, alignment):
        self.text_edit.setAlignment(alignment)

    def add_bullet_point(self):
        cursor = self.text_edit.textCursor()
        cursor.insertList(1)

    def add_numbering(self):
        cursor = self.text_edit.textCursor()
        cursor.insertList(2)
