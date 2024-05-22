import wx


class Toolbar(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        # Create a box sizer for layout
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(sizer)

        # Create a menu bar
        self.menu_bar = wx.MenuBar()

        # Create File menu
        file_menu = wx.Menu()
        file_menu.Append(wx.ID_NEW, "&New\tCtrl+N", "Create a new document")
        file_menu.Append(wx.ID_OPEN, "&Open\tCtrl+O", "Open an existing document")
        file_menu.Append(wx.ID_SAVE, "&Save\tCtrl+S", "Save the current document")
        file_menu.AppendSeparator()
        file_menu.Append(wx.ID_EXIT, "&Exit\tAlt+F4", "Exit the application")
        self.menu_bar.Append(file_menu, "&File")

        # Create View menu
        view_menu = wx.Menu()
        view_menu.Append(wx.ID_ANY, "&Toolbox", "Show/hide toolbox")
        view_menu.Append(wx.ID_ANY, "&Properties", "Show/hide properties panel")
        self.menu_bar.Append(view_menu, "&View")

        # Create Window menu
        window_menu = wx.Menu()
        window_menu.Append(wx.ID_ANY, "&Cascade", "Cascade windows")
        window_menu.Append(wx.ID_ANY, "&Tile", "Tile windows")
        self.menu_bar.Append(window_menu, "&Window")

        # Add the menu bar to the parent frame
        parent.GetParent().SetMenuBar(self.menu_bar)  # Get the parent frame and set the menu bar


# # Example of usage
# class MainFrame(wx.Frame):
#     def __init__(self):
#         super().__init__(None, title="Toolbar Example", size=(600, 400))
#
#         main_panel = wx.Panel(self)
#         toolbar_panel = ToolbarPanel(main_panel)
#
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(toolbar_panel, 0, wx.EXPAND)
#         main_panel.SetSizer(sizer)
#
#         self.Show()
#
#
# if __name__ == "__main__":
#     app = wx.App(False)
#     frame = MainFrame()
#     app.MainLoop()
