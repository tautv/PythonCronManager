import wx
from src.utils.cron_manager import CronManager, CronJob
from src.utils.cron_manager import DEFAULT_OUTPUT_CHOICES, DEFAULT_ERROR_CHOICES


class CronJobList(wx.Panel):
    def __init__(self, parent):
        super(CronJobList, self).__init__(parent)
        self.parent = parent
        self.cron_jobs_found = False
        self.cron_jobs = []
        self.widgets = []
        # Sizer and all it's properties only needs to be defined once
        self.sizer = wx.FlexGridSizer(0, 8, 10, 10)
        # Set column proportions to make columns expand proportionally
        self.sizer.AddGrowableCol(1, 1)
        self.sizer.AddGrowableCol(3, 1)
        self.sizer.AddGrowableCol(5, 1)
        self.sizer.AddGrowableCol(6, 1)
        wx.CallAfter(self.fetch_cron_jobs)  # Schedule fetching cron jobs after UI is fully initialized
        wx.CallLater(2000, self.test)  # Schedule fetching cron jobs after UI is fully initialized

    def test(self):
        self.cron_jobs = [CronJob(), CronJob(), CronJob(), CronJob()]
        self.remove_widgets()
        self.create_widgets()
        self.grid_widgets()
        self.bind_widgets()

    def fetch_cron_jobs(self):
        self.CM = CronManager()
        self.cron_jobs = self.CM.get_all_cron_jobs()
        self.create_widgets()  # Add widgets to the sizer (initially empty for demonstration)
        self.grid_widgets()  # Create a FlexGridSizer with 8 columns
        self.bind_widgets()

    def create_widgets(self):
        if len(self.cron_jobs) > 0:
            self.cron_jobs_found = True
            for index, job in enumerate(self.cron_jobs):
                widgets_row = [
                    wx.CheckBox(self, label="Enabled"),
                    wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER),
                    wx.Choice(self, choices=DEFAULT_OUTPUT_CHOICES),
                    wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER),
                    wx.Choice(self, choices=DEFAULT_ERROR_CHOICES),
                    wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER),
                    wx.Button(self, label="See Logs"),
                    wx.Button(self, label="...")
                ]
                self.widgets.append(widgets_row)
                # Bind the event handlers
                widgets_row[5].Bind(wx.EVT_TEXT_ENTER,
                                    lambda event, idx=len(self.widgets) - 1: self.on_error_path_confirmed(event, idx))
                widgets_row[5].Bind(wx.EVT_TEXT,
                                    lambda event, idx=len(self.widgets) - 1: self.on_error_path_changed(event, idx))
                widgets_row[6].Bind(wx.EVT_BUTTON,
                                    lambda event, idx=len(self.widgets) - 1: self.on_see_logs(event, idx))
                widgets_row[7].Bind(wx.EVT_BUTTON,
                                    lambda event, idx=len(self.widgets) - 1: self.on_edit_job(event, idx))
        else:
            self.cron_jobs_found = False
            for _ in range(2):  # Creating two fake lines
                widgets_row = [
                    wx.CheckBox(self, label=""),
                    wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER),
                    wx.Choice(self, choices=DEFAULT_OUTPUT_CHOICES),
                    wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER),
                    wx.Choice(self, choices=DEFAULT_ERROR_CHOICES),
                    wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER),
                    wx.Button(self, label="See Logs"),
                    wx.Button(self, label="...", size=(25, -1))
                ]
                self.widgets.append(widgets_row)
                # Bind the event handlers
                widgets_row[5].Bind(wx.EVT_TEXT_ENTER,
                                    lambda event, idx=len(self.widgets) - 1: self.on_error_path_confirmed(event, idx))
                widgets_row[5].Bind(wx.EVT_TEXT,
                                    lambda event, idx=len(self.widgets) - 1: self.on_error_path_changed(event, idx))
                widgets_row[6].Bind(wx.EVT_BUTTON,
                                    lambda event, idx=len(self.widgets) - 1: self.on_see_logs(event, idx))
                widgets_row[7].Bind(wx.EVT_BUTTON,
                                    lambda event, idx=len(self.widgets) - 1: self.on_edit_job(event, idx))
                # Disable the fake widgets:
                for widget in widgets_row:
                    widget.Disable()

    def grid_widgets(self):
        # Add widgets to the sizer in the correct order
        for widget_group in self.widgets:
            self.sizer.Add(widget_group[0], 0, wx.EXPAND)  # checkbox
            self.sizer.Add(widget_group[1], 0, wx.EXPAND)  # text_ctrl1 [command]
            self.sizer.Add(widget_group[2], 0, wx.EXPAND)  # selection_box1 [output type]
            self.sizer.Add(widget_group[3], 0, wx.EXPAND)  # text_ctrl2 [output path]
            self.sizer.Add(widget_group[4], 0, wx.EXPAND)  # selection_box2 [error type]
            self.sizer.Add(widget_group[5], 0, wx.EXPAND)  # text_ctrl3 [error path]
            self.sizer.Add(widget_group[6], 0, wx.EXPAND)  # button [see logs]
            self.sizer.Add(widget_group[7], 0, wx.EXPAND)  # button2 [edit ...]
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

    def on_command_changed(self, event, index):
        pass
    
    def on_command_confirmed(self, event, index):
        pass

    def on_output_path_changed(self, event, index):
        pass

    def on_output_path_confirmed(self, event, intex):
        pass

    def on_error_path_changed(self, event, index):
        widget_group = self.widgets[index]
        widget_group[5].SetBackgroundColour(wx.Colour(255, 255, 150))
        widget_group[5].Refresh()  # This ensures the color change is applied immediately
        print(f"[error path changed] - row {index}")

    def on_error_path_confirmed(self, event, index):
        widget_group = self.widgets[index]
        widget_group[5].SetBackgroundColour(wx.Colour(255, 255, 255))
        widget_group[5].Refresh()  # This ensures the color change is applied immediately
        print(f"[error path confirm] - row {index}")

    def on_see_logs(self, event, index):
        # Event handler for the "See Logs" button
        print(f"[See Logs] - row {index}")

    def on_edit_job(self, event, index):
        print(f"[...] - row {index}")


if __name__ == "__main__":
    class MyFrame(wx.Frame):
        def __init__(self):
            super(MyFrame, self).__init__(None, title="CronJobList", size=(800, 600))
            CronJobList(self)
            self.Show()


    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
