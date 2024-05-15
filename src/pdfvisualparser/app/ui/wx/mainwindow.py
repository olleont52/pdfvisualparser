import wx

import pdfvisualparser.app.ui.common.interfaces as interfaces
from pdfvisualparser.app.ui.views.mainwindowmodel import MainWindowViewModel


class _MainWindowMeta(type(wx.Frame), type(interfaces.MainWindowViewInterface)):
    """
    A workaround for metaclass conflict resolution that disallows multiple inheritance for WX components.
    """
    pass


class MainWindow(wx.Frame, interfaces.MainWindowViewInterface, metaclass=_MainWindowMeta):
    """
    Design of the main window form.
    """

    def __init__(self,
                 parent,
                 main_view_model: MainWindowViewModel):
        super().__init__(parent=parent,
                         id=wx.ID_ANY,
                         pos=wx.DefaultPosition,
                         style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.__model = main_view_model
        self.__model.connect_view(self)

        # Add UI initialization here
        self.Layout()

    # region Interface functions

    def show_error(self, message: str) -> None:
        pass

    # endregion Interface functions
