import os
import wx
from wx.adv import AboutBox
from src.ui.dialogs.confirm import yes_no_dialog


class Toolbar(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.SetFocusIgnoringChildren()  # Disable focus for the panel and buttons
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))  # Set panel background color
        self.create_widgets()
        self.grid_widgets()
        self.bind_widgets()

    def customize_button(self, button):
        button.SetBackgroundColour(wx.Colour(240, 240, 240))  # Example background color
        button.SetFont(wx.Font(wx.FontInfo(10).Family(wx.FONTFAMILY_DEFAULT).FaceName("Arial")))  # Example font

    def on_show_context_menu(self, event):
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
        # File Menu:
        file_item = self.context_menu_file.FindItemById(menu_id)
        if file_item and hasattr(file_item, 'ItemLabelText'):
            if file_item.ItemLabelText == "New Job":
                self.b_File_NewJob()
            if file_item.ItemLabelText == "Export Job List":
                self.b_File_ExportJobList()
            if file_item.ItemLabelText == "Import Job List":
                self.b_File_ImportJobList()
            if file_item.ItemLabelText == "Delete Selected":
                self.b_File_DeleteSelected()
            if file_item.ItemLabelText == "Close":
                self.b_File_Close()
            # print(f"Selected: [File > {menu_id}] {file_item.ItemLabelText}")
        # Help Menu:
        help_item = self.context_menu_help.FindItemById(menu_id)
        if help_item and hasattr(help_item, 'ItemLabelText'):
            if help_item.ItemLabelText == "About":
                self.b_Help_About()
            if help_item.ItemLabelText == "Check For Updates":
                self.b_Help_CheckForUpdates()
            # print(f"Selected: [Help > {menu_id}] {help_item.ItemLabelText}")

    def create_widgets(self):
        # File Button:
        self.b_File = wx.Button(self, label='File')
        self.customize_button(self.b_File)
        # File Sub-Buttons:
        self.context_menu_file = wx.Menu()
        self.context_menu_file.Append(wx.ID_ANY, "New Job")
        self.context_menu_file.Append(wx.ID_ANY, "Export Job List")
        self.context_menu_file.Append(wx.ID_ANY, "Import Job List")
        self.context_menu_file.Append(wx.ID_ANY, "Delete Selected")
        self.context_menu_file.Append(wx.ID_ANY, "Close")
        # Help Button:
        self.b_Help = wx.Button(self, label='Help')
        self.customize_button(self.b_Help)
        # Help Sub-Buttons:
        self.context_menu_help = wx.Menu()
        self.context_menu_help.Append(wx.ID_ANY, "About")
        self.context_menu_help.Append(wx.ID_ANY, "Check For Updates")

    def grid_widgets(self):
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)  # Create a box sizer for horizontal layout
        # Add buttons to the sizer
        self.sizer.Add(self.b_File, 0, wx.ALL, 0)
        self.sizer.Add(self.b_Help, 0, wx.ALL, 0)
        # Sizer for the panel
        self.SetSizer(self.sizer)

    def bind_widgets(self):
        self.Bind(wx.EVT_MENU, self.on_context_menu_item_selected)  # Bind events for the context menu items
        self.Bind(wx.EVT_BUTTON, self.on_show_context_menu)
        self.Bind(wx.EVT_RIGHT_DOWN, self.on_show_context_menu)  # Bind right-click event to show the context menu

    def b_File_NewJob(self):
        print("b_File_NewJob")

    def b_File_ExportJobList(self):
        print("b_File_ExportJobList")
        wildcard = "JSON files (*.json)|*.json"
        initial_dir = os.getcwd()  # Get current working directory
        dialog = wx.FileDialog(self, "Save JSON File", wildcard=wildcard, style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT,
                               defaultDir=initial_dir)
        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
            print(f"Save file as: {path}")
        dialog.Destroy()

    def b_File_ImportJobList(self):
        print("b_File_ImportJobList")
        wildcard = "JSON files (*.json)|*.json"
        initial_dir = os.getcwd()  # Get current working directory
        dialog = wx.FileDialog(self, "Open JSON File", wildcard=wildcard, style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
                               defaultDir=initial_dir)
        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
            print(f"Selected file: {path}")
        dialog.Destroy()

    def b_File_Close(self):
        print("b_File_Close")
        if yes_no_dialog("Are you sure?", "Quit"):
            wx.GetApp().ExitMainLoop()

    def b_Help_About(self):
        about_info = wx.adv.AboutDialogInfo()
        about_info.SetName("Python Cron Manager")
        about_info.SetVersion("0.01")
        about_info.SetDescription("Simple wxPython based UI for cron jobs.")
        about_info.SetCopyright("(C) 2024")
        about_info.SetWebSite("https://www.github.com/tautv/PythonCronManager")
        about_info.AddDeveloper("tautv")
        wx.adv.AboutBox(about_info)

    def b_Help_CheckForUpdates(self):
        print("b_Help_CheckForUpdates")

    def b_File_DeleteSelected(self):
        print("b_File_DeleteSelected")
        if yes_no_dialog("Are you sure?\nYou cannot Undo this.\nExporting Jobs first is recommended!",
                         "Delete Selected?"):
            print("Deleting Selected Jobs")
        else:
            print("Deletion cancelled")


# Example of usage
if __name__ == "__main__":
    class MainFrame(wx.Frame):
        def __init__(self):
            super().__init__(None, title="Toolbar Example", size=(600, 400))

            main_panel = wx.Panel(self)
            toolbar_panel = Toolbar(main_panel)

            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(toolbar_panel, 0, wx.EXPAND)
            main_panel.SetSizer(sizer)

            self.Show()


    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
