import wx


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        # Create a right-click context menu
        self.context_menu = wx.Menu()
        self.context_menu.Append(wx.ID_ANY, "Option 1")
        self.context_menu.Append(wx.ID_ANY, "Option 2")
        self.context_menu.Append(wx.ID_ANY, "Option 3")

        # Bind events for the context menu items
        self.Bind(wx.EVT_MENU, self.on_context_menu_item_selected)

        # Create other widgets on the panel
        self.button = wx.Button(self, label="Show Context Menu", pos=(10, 10))
        self.Bind(wx.EVT_BUTTON, self.on_show_context_menu, self.button)

        # Bind right-click event to show the context menu
        self.Bind(wx.EVT_RIGHT_DOWN, self.on_show_context_menu)

        # Layout the panel
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.button, 0, wx.ALL, 10)
        self.SetSizer(sizer)

    def on_show_context_menu(self, event):
        # Determine the position to show the context menu
        if isinstance(event, wx.MouseEvent):
            pos = event.GetPosition()
        else:
            pos = wx.GetMousePosition()
            pos = self.ScreenToClient(pos)

        self.PopupMenu(self.context_menu, pos)

    def on_context_menu_item_selected(self, event):
        menu_id = event.GetId()
        item = self.context_menu.FindItemById(menu_id)
        if item and hasattr(item, 'ItemLabelText'):
            print(f"Selected: [{menu_id}] {item.ItemLabelText}")


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        # Create the main panel
        self.panel = MyPanel(self)

        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, "Panel with Context Menu Example")
    app.MainLoop()
