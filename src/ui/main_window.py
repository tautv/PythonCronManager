import wx
from src.ui.panels.toolbar import Toolbar
from src.ui.panels.cron_job_list import CronJobList


class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        panel = wx.Panel(self)
        _toolbar = Toolbar(panel)
        _cron_job_list = CronJobList(panel)
        # self.text_ctrl = wx.TextCtrl(panel, -1, style=wx.TE_MULTILINE)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(_toolbar, proportion=0, flag=wx.EXPAND, border=20)
        sizer.Add(_cron_job_list, proportion=1, flag=wx.EXPAND, border=20)
        # sizer.Add(self.text_ctrl, 1, wx.EXPAND)
        panel.Fit()
        panel.SetSizer(sizer)

        self.Layout()

        self.Bind(wx.EVT_CLOSE, self.on_close)

    def on_close(self, event):
        self.Destroy()
#
#
# if __name__ == '__main__':
#     app = wx.App(False)
#     frame = MainWindow(None, title='MainWindow')
#     frame.Show(True)
#     app.MainLoop()
