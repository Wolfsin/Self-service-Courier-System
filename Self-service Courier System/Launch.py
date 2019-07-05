from UI.function_Selection import *

import sys


def launch_app():
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    function_selection_window = Ui_Function_Selection_Window()
    function_selection_window.setupUi(main)
    main.show()
    sys.exit(app.exec_())


launch_app()
