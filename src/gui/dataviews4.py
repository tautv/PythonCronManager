import wx
import wx.dataview as dv


class ButtonRenderer(dv.DataViewCustomRenderer):
    def __init__(self):
        dv.DataViewCustomRenderer.__init__(self)

    def Render(self, rect, dc, state):
        # Draw a simple button
        dc.SetBrush(wx.Brush(wx.GREY_BRUSH))
        dc.SetPen(wx.BLACK_PEN)
        dc.DrawRectangle(rect.x, rect.y, rect.width, rect.height)
        dc.DrawLabel("Click Me", rect, alignment=wx.ALIGN_CENTER)
        return True

    def GetSize(self):
        return wx.Size(100, 30)  # Adjust the size of your button as needed

    def SetValue(self, value):
        return True  # Indicate that the value was successfully set

    def GetMode(self):
        # Enable activation for the button renderer
        return dv.DATAVIEW_CELL_ACTIVATABLE

    def ActivateCell(self, cell, model, item, col, mouseEvent):
        # Retrieve data for the clicked row
        # row_data = [model.GetValue(item, col_idx) for col_idx in range(model.GetColumnCount())]
        # row_data = model.GetValue(item, col)
        # print(f"Row Clicked: {row_data}")
        row = model.GetValue(item, col).replace("Row ", '')
        print(f"Button Click: [{col}][{row}]")
        return True


class MyModel(dv.PyDataViewModel):
    def __init__(self):
        dv.PyDataViewModel.__init__(self)
        self.data = ["Row 1", "Row 2", "Row 3"]  # Sample data

    def GetColumnCount(self):
        return 1

    def GetColumnType(self, col):
        return "string"

    def GetChildren(self, parent, children):
        if not parent:
            for row in range(len(self.data)):
                children.append(self.ObjectToItem(row))
            return len(self.data)
        return 0

    def GetValue(self, item, col):
        return self.data[self.ItemToObject(item)]

    def IsContainer(self, item):
        return False


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400, 300))

        # Create a wx.dataview.DataViewCtrl
        self.dvc = dv.DataViewCtrl(self)

        # Create a model for the DataViewCtrl
        self.model = MyModel()
        self.dvc.AssociateModel(self.model)

        # Define the columns
        self.dvc.AppendTextColumn("Text Column", 0, width=150)

        # Create and register the custom renderer for the button column
        button_renderer = ButtonRenderer()
        self.dvc.AppendColumn(dv.DataViewColumn("Button Column", button_renderer, 0, width=150))

        self.dvc.Bind(dv.EVT_DATAVIEW_ITEM_ACTIVATED, self.OnCellActivated)

        # Refresh the DataViewCtrl
        self.dvc.Refresh()

    def OnCellActivated(self, event):
        print("GetCacheFrom()", event.GetCacheFrom())
        print("GetCacheTo()", event.GetCacheTo())
        print("GetColumn()", event.GetColumn())
        print("GetDataBuffer()", event.GetDataBuffer())
        print("GetDataFormat()", event.GetDataFormat().GetType())
        print("GetDataObject()", event.GetDataObject())
        print("GetDataSize()", event.GetDataSize())
        print("GetDataViewColumn()", event.GetDataViewColumn())
        print("GetDragFlags()", event.GetDragFlags())
        print("GetDropEffect()", event.GetDropEffect())
        print("GetItem()", event.GetItem())
        print("GetModel()", event.GetModel())
        print("GetPosition()", event.GetPosition())
        print("GetProposedDropIndex()", event.GetProposedDropIndex())
        print("GetValue()", event.GetValue())
        print("")
        print(event.GetModel().GetValue(event.GetItem(), event.GetColumn))


app = wx.App(False)
frame = MyFrame(None, "Custom Button Renderer Example")
frame.Show(True)
app.MainLoop()
