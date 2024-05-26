import wx
from src.utils.cron_manager import CronManager


class CronJobList(wx.Panel):
    def __init__(self, parent):
        super(CronJobList, self).__init__(parent)
        self.create_widgets()  # Add widgets to the sizer (initially empty for demonstration)
        self.grid_widgets()  # Create a FlexGridSizer with 8 columns
        self.bind_widgets()
        self.cron_jobs = []
        wx.CallAfter(self.fetch_cron_jobs)  # Schedule fetching cron jobs after UI is fully initialized

    def fetch_cron_jobs(self):
        CM = CronManager()
        self.cron_jobs = CM.cron_jobs

    def create_widgets(self):

        self.checkbox = wx.CheckBox(self, label="")
        self.text_ctrl1 = wx.TextCtrl(self)
        self.selection_box1 = wx.Choice(self, choices=["Option 1", "Option 2", "Option 3"])
        self.text_ctrl2 = wx.TextCtrl(self)
        self.selection_box2 = wx.Choice(self, choices=["Option A", "Option B", "Option C"])
        self.text_ctrl3 = wx.TextCtrl(self)
        self.button = wx.Button(self, label="See Logs")
        self.button2 = wx.Button(self, label="...")

    def grid_widgets(self):
        self.sizer = wx.FlexGridSizer(0, 8, 10, 10)
        # Add widgets to the sizer in the correct order
        self.sizer.Add(self.checkbox, 0, wx.EXPAND)
        self.sizer.Add(self.text_ctrl1, 0, wx.EXPAND)
        self.sizer.Add(self.selection_box1, 0, wx.EXPAND)
        self.sizer.Add(self.text_ctrl2, 0, wx.EXPAND)
        self.sizer.Add(self.selection_box2, 0, wx.EXPAND)
        self.sizer.Add(self.text_ctrl3, 0, wx.EXPAND)
        self.sizer.Add(self.button, 0, wx.EXPAND)
        self.sizer.Add(self.button2, 0, wx.EXPAND)

        # Set column proportions to make columns expand proportionally
        self.sizer.AddGrowableCol(1, 1)  # Make the second column growable
        self.sizer.AddGrowableCol(3, 1)  # Make the fourth column growable
        self.sizer.AddGrowableCol(5, 1)  # Make the sixth column growable
        self.sizer.AddGrowableCol(6, 1)  # Make the seventh column growable (progress bar column)

        # Set the sizer for the panel
        self.SetSizer(self.sizer)

    def bind_widgets(self):
        pass


if __name__ == "__main__":
    class MyFrame(wx.Frame):
        def __init__(self):
            super(MyFrame, self).__init__(None, title="CronJobList", size=(800, 600))
            panel = CronJobList(self)
            self.Show()

    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
