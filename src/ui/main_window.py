import wx
from src.ui.panels.toolbar import Toolbar
from src.ui.panels.cron_job_list import CronJobList
from src.ui.panels.toolbar import myEVT_Toolbar_New, EVT_TOOLBAR_NEW


class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.SetMinSize((700, 300))

        panel = wx.Panel(self)
        toolbar = Toolbar(panel)
        cron_job_list = CronJobList(panel)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(toolbar, proportion=0, flag=wx.EXPAND, border=20)
        sizer.Add(cron_job_list, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        self.CreateStatusBar()
        self.SetStatusText("")

        panel.Fit()
        panel.SetSizer(sizer)

        self.Layout()
        self.Centre()
        self.bind_widgets()

    def bind_widgets(self):
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.Bind(EVT_TOOLBAR_NEW, self.onToolbarNew)

    def on_close(self, event):
        self.Destroy()

    def onToolbarNew(self, event):
        print('Should Create')


if __name__ == '__main__':
    app = wx.App(False)
    frame = MainWindow(None, title='MainWindow')
    frame.Show(True)
    app.MainLoop()
