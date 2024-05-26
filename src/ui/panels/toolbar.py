import wx


class Toolbar(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        # Create a box sizer for horizontal layout
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Bind events for the context menu items
        self.Bind(wx.EVT_MENU, self.on_context_menu_item_selected)

        # Create buttons (example with 3 buttons)
        self.b_File = wx.Button(self, label='File')
        self.customize_button(self.b_File)
        self.create_context_menu_file()

        self.b_Help = wx.Button(self, label='Help')
        self.customize_button(self.b_Help)
        self.create_context_menu_help()

        # Add buttons to the sizer
        self.sizer.Add(self.b_File, 0, wx.ALL, 0)
        self.sizer.Add(self.b_Help, 0, wx.ALL, 0)

        # Set the sizer for the panel
        self.SetSizer(self.sizer)

        # Set panel background color
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        # Disable focus for the panel and buttons
        self.SetFocusIgnoringChildren()

        self.Bind(wx.EVT_BUTTON, self.on_show_context_menu)

        # Bind right-click event to show the context menu
        self.Bind(wx.EVT_RIGHT_DOWN, self.on_show_context_menu)

    def customize_button(self, button):
        # Customize button appearance here
        button.SetBackgroundColour(wx.Colour(240, 240, 240))  # Example background color
        button.SetFont(wx.Font(wx.FontInfo(12).Family(wx.FONTFAMILY_DEFAULT).FaceName("Arial")))  # Example font

    def on_show_context_menu(self, event):
        # Determine the position to show the context menu
        if isinstance(event, wx.MouseEvent):
            pos = event.GetPosition()
        else:
            pos = wx.GetMousePosition()
            pos = self.ScreenToClient(pos)
        if hasattr(event.EventObject, 'LabelText'):
            _label_text = event.EventObject.LabelText
            if _label_text == "File":
                self.PopupMenu(self.context_menu_file, pos)
            elif _label_text == "Help":
                self.PopupMenu(self.context_menu_help, pos)

    def on_context_menu_item_selected(self, event):
        menu_id = event.GetId()
        item = self.context_menu_file.FindItemById(menu_id)
        if item and hasattr(item, 'ItemLabelText'):
            print(f"Selected: [{menu_id}] {item.ItemLabelText}")

    def create_context_menu_file(self):
        # Create a right-click context menu
        self.context_menu_file = wx.Menu()
        self.context_menu_file.Append(wx.ID_ANY, "New Job")
        self.context_menu_file.Append(wx.ID_ANY, "Export Job List")
        self.context_menu_file.Append(wx.ID_ANY, "Import Job List")
        self.context_menu_file.Append(wx.ID_ANY, "Close")

    def create_context_menu_help(self):
        self.context_menu_help = wx.Menu()
        self.context_menu_help.Append(wx.ID_ANY, "About")
        self.context_menu_help.Append(wx.ID_ANY, "Check For Updates")


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
