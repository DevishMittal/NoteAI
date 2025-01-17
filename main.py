import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
import warnings
warnings.filterwarnings("ignore", "You are using `torch.load` with `weights_only=False`*.")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
