import pdfvisualparser.app.ui.common.interfaces as interfaces


class MainWindowViewModel(interfaces.MainWindowViewModelBase):
    """
    Part of behavior of the main window that does not rely on concrete UI widgets.
    """

    def __init__(self, main_app: interfaces.VisualParserMainApp):
        """
        Initialization of the view model.

        :param main_app: Reference to the main app.
        """
        super().__init__(main_app)
