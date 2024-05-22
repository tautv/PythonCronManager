import wx
from src.ui.main_window import MainWindow


def main():
    app = wx.App(False)
    frame = MainWindow(None, title='Python Cron Manager', size=(800, 600))
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main()

# python setup.py py2exe
# python setup.py py2app
