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
        if col == 0:
            return self.data[self.ItemToObject(item)]
        return ""

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

        self.dvc.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)

        # Refresh the DataViewCtrl
        self.dvc.Refresh()

    def on_left_down(self, event):
        item, col = self.dvc.HitTest(event.GetPosition())
        print("item", item)
        print("col", col.Title)
        if item.IsOk() and col == 1:  # Assuming the button column is column index 1
            print("Single-clicked item:", self.model.GetValue(item, col))
        event.Skip()



app = wx.App(False)
frame = MyFrame(None, "Custom Button Renderer Example")
frame.Show(True)
app.MainLoop()
