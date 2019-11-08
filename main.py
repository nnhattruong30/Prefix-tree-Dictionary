import dictionary
import ui
import sys

if __name__ == '__main__':
    my_dict = dictionary.Dictionary()
    app = ui.QApplication(sys.argv)
    ex = ui.App(my_dict)
    sys.exit(app.exec_())