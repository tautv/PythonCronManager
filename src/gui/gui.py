import wx
from typing import Optional
from crontab import CronItem


class AddEditDialog(wx.Dialog):
    def __init__(self, parent, job: Optional[CronItem] = None):
        # command='python /path/to/your_script.py >> {output_path} 2>> {error_path}'
        super(AddEditDialog, self).__init__(parent,
                                            title="Edit Cron Job" if job else "Add Cron Job")
        self.panel = wx.Panel(self)
        self.job = job
        if job is None:
            self.default_minutes = 0
            self.default_hours = 0
            self.default_days = 1
            self.default_months = 1
            self.default_dow = 0  # 0 = Sunday, 1 = Monday...
            self.default_command = ""
            # Skip logging?
            # * * * * * /path/to/your/command > /dev/null 2>&1
            # * * * * * /path/to/your/command >> /path/to/logfile.log 2>&1
            # overwrite log file:
            # * * * * * /path/to/your/command > /path/to/your/output/file
            # append log file:
            # * * * * * /path/to/your/command >> /path/to/your/output/file
            self.default_comment = ""
            self.default_pre_comment = ""  # This i a description placed above the job in crontab
        else:
            self.default_minutes = job.minutes
            self.default_hours = job.hours
            self.default_days = job.day
            self.default_months = job.months
            self.default_dow = job.dow
            self.default_command = job.command
            self.default_comment = job.comment
            self.default_pre_comment = job.pre_comment
        self.create_widgets()
        self.layout_widgets()
        self.bind_widgets()

    def create_widgets(self):
        e_size = (300, -1)
        b_size = (20, -1)
        # Minutes:
        self.l_minutes = wx.StaticText(self.panel, label="Minutes")
        self.e_minutes = wx.TextCtrl(self.panel, value=f"{self.default_minutes}", size=e_size)
        self.b_minutes = wx.Button(self.panel, label="?", size=b_size)
        # Hours:
        self.l_hours = wx.StaticText(self.panel, label='Hours')
        self.e_hours = wx.TextCtrl(self.panel, value=f"{self.default_hours}", size=e_size)
        self.b_hours = wx.Button(self.panel, label="?", size=b_size)
        # Day:
        self.l_days = wx.StaticText(self.panel, label="Days")
        self.e_days = wx.TextCtrl(self.panel, value=f"{self.default_days}", size=e_size)
        self.b_days = wx.Button(self.panel, label="?", size=b_size)
        # Month:
        self.l_months = wx.StaticText(self.panel, label="Months")
        self.e_months = wx.TextCtrl(self.panel, value=f"{self.default_months}", size=e_size)
        self.b_months = wx.Button(self.panel, label="?", size=b_size)
        # Day Of Week:
        self.l_dow = wx.StaticText(self.panel, label="Day Of Week")
        self.e_dow = wx.TextCtrl(self.panel, value=f"{self.default_dow}", size=e_size)
        self.b_dow = wx.Button(self.panel, label="?", size=b_size)
        # Command:
        self.l_command = wx.StaticText(self.panel, label="Command")
        self.e_command = wx.TextCtrl(self.panel, value=f"{self.default_command}", size=e_size)
        self.b_command = wx.Button(self.panel, label="?", size=b_size)
        # Comment:
        self.l_comment = wx.StaticText(self.panel, label="Comment")
        self.e_comment = wx.TextCtrl(self.panel, value=f"{self.default_comment}", size=e_size)
        self.b_comment = wx.Button(self.panel, label="?", size=b_size)
        # Pre-Comment:
        self.l_pre_comment = wx.StaticText(self.panel, label="Pre-Comment")
        self.e_pre_comment = wx.TextCtrl(self.panel, value=f"{self.default_pre_comment}", size=e_size)
        self.b_pre_comment = wx.Button(self.panel, label="?", size=b_size)

    def layout_widgets(self):
        sizer = wx.FlexGridSizer(rows=0, cols=3, hgap=10, vgap=10)  # Adjusted gaps for padding
        # Minutes:
        sizer.Add(self.l_minutes, 0, wx.ALIGN_LEFT)
        sizer.Add(self.e_minutes, 1, wx.EXPAND)
        sizer.Add(self.b_minutes, 0, wx.ALIGN_RIGHT)
        # Hours:
        sizer.Add(self.l_hours, 0, wx.ALIGN_LEFT)
        sizer.Add(self.e_hours, 1, wx.EXPAND)
        sizer.Add(self.b_hours, 0, wx.ALIGN_RIGHT)
        # Days:
        sizer.Add(self.l_days, 0, wx.ALIGN_LEFT)
        sizer.Add(self.e_days, 1, wx.EXPAND)
        sizer.Add(self.b_days, 0, wx.ALIGN_RIGHT)
        # Month:
        sizer.Add(self.l_months, 0, wx.ALIGN_LEFT)
        sizer.Add(self.e_months, 1, wx.EXPAND)
        sizer.Add(self.b_months, 0, wx.ALIGN_RIGHT)
        # DOW (Day Of Week):
        sizer.Add(self.l_dow, 0, wx.ALIGN_LEFT)
        sizer.Add(self.e_dow, 1, wx.EXPAND)
        sizer.Add(self.b_dow, 0, wx.ALIGN_RIGHT)
        # Command:
        sizer.Add(self.l_command, 0, wx.ALIGN_LEFT)
        sizer.Add(self.e_command, 1, wx.EXPAND)
        sizer.Add(self.b_command, 0, wx.ALIGN_RIGHT)
        # Comment:
        sizer.Add(self.l_comment, 0, wx.ALIGN_LEFT)
        sizer.Add(self.e_comment, 1, wx.EXPAND)
        sizer.Add(self.b_comment, 0, wx.ALIGN_RIGHT)
        # Pre-Comment
        sizer.Add(self.l_pre_comment, 0, wx.ALIGN_LEFT)
        sizer.Add(self.e_pre_comment, 1, wx.EXPAND)
        sizer.Add(self.b_pre_comment, 0, wx.ALIGN_RIGHT)
        # Adding padding around the panel
        outer_sizer = wx.BoxSizer(wx.VERTICAL)
        outer_sizer.Add(self.panel, 1, wx.EXPAND | wx.ALL, 10)  # 10 pixels padding on all sides

        self.panel.SetSizer(sizer)
        self.SetSizerAndFit(outer_sizer)  # Set sizer for the dialog and fit it

    def bind_widgets(self):
        self.b_minutes.Bind(wx.EVT_BUTTON, self.on_minutes_help)
        self.b_hours.Bind(wx.EVT_BUTTON, self.on_hours_help)
        self.b_days.Bind(wx.EVT_BUTTON, self.on_days_help)

    def on_minutes_help(self, event):
        # Handle help for minutes
        pass

    def on_hours_help(self, event):
        # Handle help for hours
        pass

    def on_days_help(self, event):
        # Handle help for days
        pass


class CrontabEditor(wx.Frame):
    def __init__(self, parent, title):
        super(CrontabEditor, self).__init__(parent, title=title, size=(600, 400))

        self.panel = wx.Panel(self)
        self.jobs_list = wx.ListBox(self.panel, style=wx.LB_SINGLE | wx.LB_SORT)

        self.add_button = wx.Button(self.panel, label="Add Job")
        self.edit_button = wx.Button(self.panel, label="Edit Job")
        self.delete_button = wx.Button(self.panel, label="Delete Job")

        self.Bind(wx.EVT_BUTTON, self.on_add_job, self.add_button)
        self.Bind(wx.EVT_BUTTON, self.on_edit_job, self.edit_button)
        self.Bind(wx.EVT_BUTTON, self.on_delete_job, self.delete_button)

        self.create_layout()

    def create_layout(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        main_sizer.Add(self.jobs_list, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        button_sizer.Add(self.add_button, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        button_sizer.Add(self.edit_button, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        button_sizer.Add(self.delete_button, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        main_sizer.Add(button_sizer, flag=wx.EXPAND | wx.ALL, border=10)

        self.panel.SetSizer(main_sizer)
        self.Layout()

    def on_add_job(self, _event):
        dialog = AddEditDialog(self, job=None)
        dialog.ShowModal()
        dialog.Destroy()

    def on_edit_job(self, _event):
        print("on_edit_job")

    def on_delete_job(self, _event):
        print("on_delete_job")
