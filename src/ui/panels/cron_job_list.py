import wx
from src.utils.cron_manager import CronManager, CronJob


class CronJobList(wx.Panel):
    def __init__(self, parent):
        super(CronJobList, self).__init__(parent)
        self.parent = parent
        self.cron_jobs = []
        self.widgets = []
        # Sizer and all it's properties only needs to be defined once
        self.sizer = wx.FlexGridSizer(0, 8, 10, 10)
        # Set column proportions to make columns expand proportionally
        self.sizer.AddGrowableCol(1, 1)  # Make the second column growable
        self.sizer.AddGrowableCol(3, 1)  # Make the fourth column growable
        self.sizer.AddGrowableCol(5, 1)  # Make the sixth column growable
        self.sizer.AddGrowableCol(6, 1)  # Make the seventh column growable (progress bar column)
        wx.CallAfter(self.fetch_cron_jobs)  # Schedule fetching cron jobs after UI is fully initialized

    def fetch_cron_jobs(self):
        CM = CronManager()
        self.cron_jobs = CM.cron_jobs
        self.create_widgets()  # Add widgets to the sizer (initially empty for demonstration)
        self.grid_widgets()  # Create a FlexGridSizer with 8 columns
        self.bind_widgets()

    def create_widgets(self):
        if len(self.cron_jobs) > 0:
            for job in self.cron_jobs:
                self.widgets.append([
                    wx.CheckBox(self, label=""),
                    wx.TextCtrl(self),
                    wx.Choice(self, choices=["Option 1", "Option 2", "Option 3"]),
                    wx.TextCtrl(self),
                    wx.Choice(self, choices=["Option A", "Option B", "Option C"]),
                    wx.TextCtrl(self),
                    wx.Button(self, label="See Logs"),
                    wx.Button(self, label="...")
                ])
        else:
            # there are no cron jobs - creating fake first line.
            self.widgets.append([
                wx.CheckBox(self, label=""),
                wx.TextCtrl(self),
                wx.Choice(self, choices=["Option 1", "Option 2", "Option 3"]),
                wx.TextCtrl(self),
                wx.Choice(self, choices=["Option A", "Option B", "Option C"]),
                wx.TextCtrl(self),
                wx.Button(self, label="See Logs"),
                wx.Button(self, label="...")
            ])
            # Disable the fake widgets:
            for widget in self.widgets[0]:
                widget.Disable()

    def grid_widgets(self):
        # Add widgets to the sizer in the correct order
        print(len(self.widgets))
        for widget_group in self.widgets:
            self.sizer.Add(widget_group[0], 0, wx.EXPAND)  # checkbox
            self.sizer.Add(widget_group[1], 0, wx.EXPAND)  # text_ctrl1
            self.sizer.Add(widget_group[2], 0, wx.EXPAND)  # selection_box1
            self.sizer.Add(widget_group[3], 0, wx.EXPAND)  # text_ctrl2
            self.sizer.Add(widget_group[4], 0, wx.EXPAND)  # selection_box2
            self.sizer.Add(widget_group[5], 0, wx.EXPAND)  # text_ctrl3
            self.sizer.Add(widget_group[6], 0, wx.EXPAND)  # button
            self.sizer.Add(widget_group[7], 0, wx.EXPAND)  # button2

        # Set the sizer for the panel
        self.SetSizerAndFit(self.sizer)
        self.parent.Layout()

    def bind_widgets(self):
        pass

    def remove_widgets(self):
        self.sizer.Clear()
        for widget_group in self.widgets:
            for widget in widget_group:
                widget.Destroy()
        self.widgets = []


if __name__ == "__main__":
    class MyFrame(wx.Frame):
        def __init__(self):
            super(MyFrame, self).__init__(None, title="CronJobList", size=(800, 600))
            CronJobList(self)
            self.Show()


    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
