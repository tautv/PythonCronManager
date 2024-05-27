import wx


def yes_no_dialog(message, caption):
    dlg = wx.MessageDialog(None, message, caption, wx.YES_NO | wx.ICON_QUESTION)
    result = dlg.ShowModal() == wx.ID_YES
    dlg.Destroy()
    return result
