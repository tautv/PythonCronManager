import wx

# Define a new event type
myEVT_BUTTON_CLICKED = wx.NewEventType()
EVT_BUTTON_CLICKED = wx.PyEventBinder(myEVT_BUTTON_CLICKED, 1)


class ButtonClickedEvent(wx.PyCommandEvent):
    def __init__(self, event_type, id):
        wx.PyCommandEvent.__init__(self, event_type, id)
        self.data = None

    def GetData(self):
        return self.data


# import wx
# from .custom_events.py import ButtonClickedEvent, myEVT_BUTTON_CLICKED
#
# class MyPanel(wx.Panel):
#     def __init__(self, parent):
#         super(MyPanel, self).__init__(parent)
#
#         self.button = wx.Button(self, label="Click Me")
#         self.Bind(wx.EVT_BUTTON, self.OnButtonClicked, self.button)
#
#     def OnButtonClicked(self, event):
#         # Create a custom event
#         evt = ButtonClickedEvent(myEVT_BUTTON_CLICKED, self.GetId())
#         evt.SetData("Some relevant data")
#         # Post the event to be handled by the main application or controller
#         wx.PostEvent(self.GetParent(), evt)
