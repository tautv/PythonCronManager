import wx
from src.utils.cron_manager import CronManager
import time  # Placeholder for demo purposes, replace with your cron_manager import


class CronJobList(wx.Panel):
    def __init__(self, parent):
        super(CronJobList, self).__init__(parent)

        # Create a FlexGridSizer with 8 columns
        sizer = wx.FlexGridSizer(0, 8, 10, 10)

        # Add widgets to the sizer (initially empty for demonstration)
        for _ in range(5):  # Add 5 rows as an example
            checkbox = wx.CheckBox(self, label="")
            text_ctrl1 = wx.TextCtrl(self)
            selection_box1 = wx.Choice(self, choices=["Option 1", "Option 2", "Option 3"])
            text_ctrl2 = wx.TextCtrl(self)
            selection_box2 = wx.Choice(self, choices=["Option A", "Option B", "Option C"])
            text_ctrl3 = wx.TextCtrl(self)
            button = wx.Button(self, label="See Logs")
            button2 = wx.Button(self, label="...")

            # Add widgets to the sizer in the correct order
            sizer.Add(checkbox, 0, wx.EXPAND)
            sizer.Add(text_ctrl1, 0, wx.EXPAND)
            sizer.Add(selection_box1, 0, wx.EXPAND)
            sizer.Add(text_ctrl2, 0, wx.EXPAND)
            sizer.Add(selection_box2, 0, wx.EXPAND)
            sizer.Add(text_ctrl3, 0, wx.EXPAND)
            sizer.Add(button, 0, wx.EXPAND)
            sizer.Add(button2, 0, wx.EXPAND)

        # Set column proportions to make columns expand proportionally
        sizer.AddGrowableCol(1, 1)  # Make the second column growable
        sizer.AddGrowableCol(3, 1)  # Make the fourth column growable
        sizer.AddGrowableCol(5, 1)  # Make the sixth column growable
        sizer.AddGrowableCol(6, 1)  # Make the seventh column growable (progress bar column)

        # Set the sizer for the panel
        self.SetSizer(sizer)

        # Disable the panel initially
        self.Disable()

        # Schedule fetching cron jobs after UI is fully initialized
        wx.CallAfter(self.fetch_cron_jobs)

    def fetch_cron_jobs(self):
        # Simulate fetching cron jobs (replace with your actual code)
        CM = CronManager()
        cron_jobs = CM.cron_jobs

        # Enable the panel now that initialization is complete
        self.Enable()

        # Populate widgets based on cron jobs (example)
        self.populate_widgets(cron_jobs)

    def populate_widgets(self, cron_jobs):
        # Example: Populate widgets based on cron jobs data
        for job in cron_jobs:
            # Example: Create widgets dynamically based on job details
            checkbox = wx.CheckBox(self, label=job.enabled)
            text_ctrl1 = wx.TextCtrl(self, value=job.cron_command)
            selection_box1 = wx.Choice(self, choices=job.output_type)
            # Add more widgets as needed and add them to the sizer

            # Add to sizer or layout accordingly
            # Example: self.sizer.Add(checkbox, 0, wx.EXPAND)

        # Optionally refresh layout after adding new widgets
        self.Layout()
#
#
# class MyFrame(wx.Frame):
#     def __init__(self):
#         super(MyFrame, self).__init__(None, title="FlexGridSizer Example", size=(800, 600))
#         panel = CronJobList(self)
#         self.Show()
#
#
# if __name__ == "__main__":
#     app = wx.App(False)
#     frame = MyFrame()
#     app.MainLoop()
