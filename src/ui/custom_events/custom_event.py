import wx

# Define a new event type
myEVT_Custom_Event = wx.NewEventType()
EVT_CUSTOM_EVENT = wx.PyEventBinder(myEVT_Custom_Event)


class ButtonClickedEvent(wx.PyCommandEvent):
    def __init__(self, event_type, id):
        super().__init__(event_type, id)
        self.data = None

    def GetData(self):
        return self.data

    def SetData(self, data):
        self.data = data


# if __name__ == "__main__":
#     class MyFrame(wx.Frame):
#         def __init__(self):
#             super(MyFrame, self).__init__(None, title="MyFrame", size=(200, 300))
#
#             self.button = wx.Button(self, label="Click Me")
#             self.Bind(wx.EVT_BUTTON, self.OnButtonClicked, self.button)
#             self.Bind(EVT_CUSTOM_EVENT, self.OnCustomButtonClicked)
#             self.Show()
#
#         def OnButtonClicked(self, event):
#             # Create a custom event
#             evt = ButtonClickedEvent(myEVT_Custom_Event, self.GetId())
#             evt.SetData("Some relevant data")
#             # Post the event to be handled by the main application or controller
#             wx.PostEvent(self, evt)
#
#         def OnCustomButtonClicked(self, event):
#             # Handle the custom event
#             data = event.GetData()
#             print(f"myEVT_Custom_Event data: {data}")
#
#
#     app = wx.App(False)
#     frame = MyFrame()
#     app.MainLoop()
