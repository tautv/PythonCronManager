import wx
import wx.dataview as dv


class MyDataModel(dv.DataViewVirtualListModel):
    def __init__(self, data):
        super().__init__(len(data))
        self.data = data

    def GetColumnType(self, col):
        return "string"

    def GetValueByRow(self, row, col):
        value = self.data[row][col]
        # Convert the age (column 2) to string before returning
        if col == 2:
            value = str(value)
        return value

    def SetValueByRow(self, value, row, col):
        self.data[row][col] = value


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(400, 300))

        self.data = [
            ["John", "Doe", 30],
            ["Jane", "Smith", 25],
            ["Bob", "Brown", 40]
        ]

        self.dvc = dv.DataViewCtrl(self, style=wx.BORDER_THEME | dv.DV_ROW_LINES | dv.DV_VERT_RULES)
        self.model = MyDataModel(self.data)
        self.dvc.AssociateModel(self.model)

        self.dvc.AppendTextColumn("First Name", 0)
        self.dvc.AppendTextColumn("Last Name", 1)
        self.dvc.AppendTextColumn("Age", 2)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.dvc, 1, wx.EXPAND)

        self.SetSizer(sizer)
        self.Center()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, "DataViewCtrl Example")
    frame.Show()
    app.MainLoop()
