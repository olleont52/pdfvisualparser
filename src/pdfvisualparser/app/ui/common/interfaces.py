from abc import ABC, abstractmethod
from typing import Optional


class VisualParserMainApp(ABC):
    """
    Base class of the main application, independent of the selected GUI framework.
    It will include major app components as properties, e.g. the global settings object.
    """
    pass


class MainWindowViewInterface(ABC):
    """
    Base class of the main window, defining an interface
    that the window exposes to the view model.
    """

    @abstractmethod
    def show_error(self, message: str) -> None:
        """
        Shows a modal error message.
        """
        pass


class MainWindowViewModelBase:
    """
    Base class of the main view model,
    defining the minimal possible API that the main app needs to set up the model.
    """

    def __init__(self, main_app: VisualParserMainApp):
        self.__main_app = main_app
        self.__view: Optional[MainWindowViewInterface] = None

    @property
    def main_app(self) -> VisualParserMainApp:
        return self.__main_app

    @property
    def view(self) -> MainWindowViewInterface:
        # ``connect_view`` will be called right after the object is created,
        # so there is no need to define the return type as ``Optional``.
        return self.__view

    def connect_view(self, view: MainWindowViewInterface) -> None:
        self.__view = view


class VisualParserAppUI(ABC):
    """
    Base class for the GUI application runner.

    It's not the same as the main application (``VisualParserMainApp`` defined above).
    The main app includes global logical components, while the app UI class
    defines the "application" in terms of the GUI framework.
    """

    @abstractmethod
    def run_app(self, main_view_model: MainWindowViewModelBase) -> None:
        """
        Implementation of this method must show the UI and start the main window event loop.
        """
        raise NotImplementedError()
