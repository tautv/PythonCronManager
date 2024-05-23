import wx


class TestFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(TestFrame, self).__init__(*args, **kwargs)

        # Create a main panel
        main_panel = wx.Panel(self)

        # Create a toolbar and embed it in a panel
        toolbar_panel = wx.Panel(main_panel)
        toolbar = wx.ToolBar(toolbar_panel, style=wx.TB_HORIZONTAL | wx.NO_BORDER | wx.TB_FLAT)

        # Add tools to the toolbar
        toolbar.AddTool(wx.ID_ANY, 'New', wx.ArtProvider.GetBitmap(wx.ART_NEW))
        toolbar.AddTool(wx.ID_ANY, 'Open', wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN))
        toolbar.AddTool(wx.ID_ANY, 'Save', wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE))

        # Realize the toolbar to prepare it for display
        toolbar.Realize()

        # Add toolbar to a sizer in the toolbar panel
        toolbar_sizer = wx.BoxSizer(wx.HORIZONTAL)
        toolbar_sizer.Add(toolbar, 1, wx.EXPAND)
        toolbar_panel.SetSizer(toolbar_sizer)

        # Create a sample text control to show in the main window
        text_ctrl = wx.TextCtrl(main_panel, style=wx.TE_MULTILINE)

        # Create a vertical box sizer to manage the layout
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Add the custom toolbar panel and the text control to the sizer
        main_sizer.Add(toolbar_panel, 0, wx.EXPAND)
        main_sizer.Add(text_ctrl, 1, wx.EXPAND | wx.ALL, 5)

        # Set the sizer for the main panel
        main_panel.SetSizer(main_sizer)

        # Set the main panel as the frame's content
        self.SetSize((800, 600))
        self.Centre()


if __name__ == "__main__":
    app = wx.App(False)
    frame = TestFrame(None, title="Embedded Toolbar Example")
    frame.Show()
    app.MainLoop()
