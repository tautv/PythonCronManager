import wx
from src.gui.dialogs import AddEditDialog


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
