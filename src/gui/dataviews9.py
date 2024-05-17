from src.utils.cron_manager import CronJob
import wx
import wx.dataview as dv
from wx._dataview import DataViewItemArray


class CronJobModel(dv.PyDataViewModel):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def GetChildren(self, parent, children):
        if not parent:
            for row in range(len(self.data)):
                children.append(self.ObjectToItem(row))
            return len(self.data)
        return 0

    def IsContainer(self, item):
        return not item.IsOk()

    def GetParent(self, item):
        return dv.DataViewItem()  # Return an invalid item to signify no parent

    def GetValue(self, item, col):
        if not item.IsOk():
            return None
        row = self.ItemToObject(item)
        cron_job = self.data[row]
        if col == 0:
            return cron_job.enabled
        elif col == 1:
            return cron_job.cron_command
        elif col == 2:
            return cron_job.output_type
        elif col == 3:
            return cron_job.output_file_path
        elif col == 4:
            return cron_job.error_type
        elif col == 5:
            return cron_job.error_file_path
        elif col == 6:
            return ""
        return None

    def SetValue(self, value, item, col):
        if not item.IsOk():
            return False
        row = self.ItemToObject(item)
        cron_job = self.data[row]
        if col == 0:
            cron_job.enabled = value
        elif col == 1:
            cron_job.cron_command = value
        elif col == 2:
            cron_job.output_type = value
        elif col == 3:
            cron_job.output_file_path = value
        elif col == 4:
            cron_job.error_type = value
        elif col == 5:
            cron_job.error_file_path = value
        self.ItemChanged(item)
        return True


class CronJobManager(wx.Frame):
    def __init__(self, parent, title):
        super(CronJobManager, self).__init__(parent, title=title, size=(800, 400))
        # Create sample data
        self.cron_jobs = [
            CronJob(enabled=False, cron_command="/path/to/command", output_file_path="/tmp/output.log"),
            CronJob(enabled=True, cron_command="/another/command", output_file_path="/tmp/another_output.log")
        ]
        # Create the DataViewCtrl
        self.dvc = dv.DataViewCtrl(self, style=wx.BORDER_THEME | dv.DV_ROW_LINES)
        self.setup_data_view()
        self.grid_widgets()
        self.bind_widgets()

    def grid_widgets(self):
        # Set up the layout sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.dvc, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Show()

    def bind_widgets(self):
        self.dvc.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)

    def setup_data_view(self):
        self.model = CronJobModel(self.cron_jobs)
        self.dvc.AssociateModel(self.model)
        # Define columns
        self.dvc.AppendToggleColumn(label="Enabled", model_column=0, mode=dv.DATAVIEW_CELL_ACTIVATABLE, width=60)

        self.dvc.AppendTextColumn(label="Cron Command", model_column=1, mode=dv.DATAVIEW_CELL_EDITABLE, width=200)

        output_renderer = dv.DataViewChoiceRenderer(
            ["Cron Default",
             "No Output",
             "Append To File",
             "Write To File"])

        self.dvc.AppendColumn(dv.DataViewColumn(title="Output Type", renderer=output_renderer, model_column=2))

        self.dvc.AppendTextColumn(label="Output File Path",
                                  model_column=3,
                                  mode=dv.DATAVIEW_CELL_EDITABLE)

        error_renderer = dv.DataViewChoiceRenderer(
            ["Cron Default", "No Output", "Append To File", "Write To File", "Append To Output", "Write To Output"])

        self.dvc.AppendColumn(dv.DataViewColumn(title="Error Type",
                                                renderer=error_renderer,
                                                model_column=4))

        self.dvc.AppendTextColumn(label="Error File Path",
                                  model_column=5,
                                  mode=dv.DATAVIEW_CELL_EDITABLE)

        self.dvc.AppendTextColumn(label="Edit Job",
                                  model_column=6,
                                  mode=dv.DATAVIEW_CELL_ACTIVATABLE)
        self.dvc.Refresh()

    def on_left_down(self, event):
        pos = event.GetPosition()
        item, col_obj = self.dvc.HitTest(pos)
        col = None
        if col_obj:
            col = col_obj.ModelColumn
        if item.IsOk() and col:
            row = self.model.ItemToObject(item)
            print(f"Row: {row}, Column: {col}")
            # Activate it right away:
            # if (col != 0) and (col != 2) and (col != 4):
            if col == 1 or col == 3 or col == 5:
                _array = DataViewItemArray()
                _array.append(item)
                self.dvc.SetSelections(_array)
                self.dvc.EditItem(item, col_obj)
            else:
                event.Skip()


if __name__ == '__main__':
    app = wx.App()
    CronJobManager(None, title="Cron Job Manager")
    app.MainLoop()
