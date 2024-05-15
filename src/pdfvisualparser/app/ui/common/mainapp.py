from typing import Type

import pdfvisualparser.app.ui.common.interfaces as interfaces
from pdfvisualparser.app.ui.views.mainwindowmodel import MainWindowViewModel


class MainAppImpl(interfaces.VisualParserMainApp):
    """
    Implementation of the UI-independent application.
    """

    def __init__(self):
        # Initialize app components here
        pass

    def run(self, ui_app_class: Type[interfaces.VisualParserAppUI]):
        main_view_model = MainWindowViewModel(self)
        ui_app_class().run_app(main_view_model)


if __name__ == '__main__':
    # Use the AppUI class that uses a concrete UI framework
    from pdfvisualparser.app.ui.wx.wxapp import VisualParserWxGUIApp

    MainAppImpl().run(VisualParserWxGUIApp)
