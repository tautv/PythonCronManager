import wx
from src.gui.frames import CrontabEditor
from src.utils import configs

if __name__ == '__main__':
    app = wx.App(False)
    frame = CrontabEditor(None, f"{configs.get_name()} ({configs.get_version()})")
    frame.Show()
    app.MainLoop()
