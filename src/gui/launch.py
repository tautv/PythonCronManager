import wx
from src.gui.frames import CrontabEditor


def launch_gui():
    app = wx.App(False)
    frame = CrontabEditor(None, "Python Cron Manager")
    frame.Show()
    app.MainLoop()
