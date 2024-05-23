import wx


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()

        # File Menu
        file_menu = wx.Menu()
        file_menu.Append(wx.ID_NEW, "&New")
        file_menu.Append(wx.ID_OPEN, "&Open")
        file_menu.Append(wx.ID_SAVE, "&Save")
        file_menu.AppendSeparator()
        file_menu.Append(wx.ID_EXIT, "&Quit")
        menubar.Append(file_menu, "&File")

        # View Menu
        view_menu = wx.Menu()
        view_menu.Append(wx.ID_ANY, "&Toolbars")
        view_menu.Append(wx.ID_ANY, "&Status Bar")
        menubar.Append(view_menu, "&View")

        # Window Menu
        window_menu = wx.Menu()
        window_menu.Append(wx.ID_ANY, "&Cascade")
        window_menu.Append(wx.ID_ANY, "&Tile")
        window_menu.Append(wx.ID_ANY, "&Minimize All")
        menubar.Append(window_menu, "&Window")

        self.SetMenuBar(menubar)

        self.CreateStatusBar()

        self.SetSize((800, 600))
        self.Centre()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame(None, title="Custom Toolbar Example")
    frame.Show()
    app.MainLoop()
