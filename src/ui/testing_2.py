import wx


class CustomPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        # Create a horizontal box sizer to hold the buttons
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        # Create buttons for 'File', 'View', 'Window'
        file_button = wx.Button(self, label='File')
        view_button = wx.Button(self, label='View')
        window_button = wx.Button(self, label='Window')

        # Add buttons to the sizer
        hbox.Add(file_button, proportion=1, flag=wx.EXPAND)
        hbox.Add(view_button, proportion=1, flag=wx.EXPAND)
        hbox.Add(window_button, proportion=1, flag=wx.EXPAND)

        # Bind events for buttons
        file_button.Bind(wx.EVT_BUTTON, self.on_file_button)
        view_button.Bind(wx.EVT_BUTTON, self.on_view_button)
        window_button.Bind(wx.EVT_BUTTON, self.on_window_button)

        # Set the sizer for the panel
        self.SetSizer(hbox)

    def on_file_button(self, event):
        self.show_context_menu('File', event)

    def on_view_button(self, event):
        self.show_context_menu('View', event)

    def on_window_button(self, event):
        self.show_context_menu('Window', event)

    def show_context_menu(self, menu_name, event):
        menu = wx.Menu()
        menu.Append(wx.ID_ANY, f'{menu_name} Option 1')
        menu.Append(wx.ID_ANY, f'{menu_name} Option 2')

        self.PopupMenu(menu)
        menu.Destroy()


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Custom Menu Panel Example', size=(400, 300))

        panel = CustomPanel(self)
        self.SetSizeHints(400, 300)
        self.Show()


if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
