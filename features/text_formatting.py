class TextFormatting:
    @staticmethod
    def set_font(text_edit, font_family, font_size):
        font = text_edit.font()
        font.setFamily(font_family)
        font.setPointSize(font_size)
        text_edit.setFont(font)

    @staticmethod
    def set_text_color(text_edit, color):
        text_edit.setTextColor(color)

    @staticmethod
    def set_alignment(text_edit, alignment):
        text_edit.setAlignment(alignment)

    @staticmethod
    def add_bullet_point(text_edit):
        cursor = text_edit.textCursor()
        cursor.insertList(1)  # QTextListFormat::ListDisc for bullet points

    @staticmethod
    def add_numbering(text_edit):
        cursor = text_edit.textCursor()
        cursor.insertList(2)  # QTextListFormat::ListDecimal for numbered list
