"""
Main entry point for the wx GUI application.
"""
import wx

import pdfvisualparser.app.ui.common.interfaces as interfaces
from pdfvisualparser.app.ui.views.mainwindowmodel import MainWindowViewModel
from pdfvisualparser.app.ui.wx.mainwindow import MainWindow


class VisualParserWxGUIApp(interfaces.VisualParserAppUI):
    """
    A specific implementation of the main GUI app runner using wxPython.
    """

    def run_app(self, main_view_model: MainWindowViewModel) -> None:
        """
        App launcher.
        """
        app = wx.App(False)
        MainWindow(parent=None, main_view_model=main_view_model).Show()
        app.MainLoop()
