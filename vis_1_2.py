from vtkmodules.all import (
    vtkTextSource, vtkPolyDataMapper,
    vtkActor,
)

from utils.window_renderer import WindowRenderer


class Text:

    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__source = vtkTextSource()
        self.__mapper = vtkPolyDataMapper()
        self.__actor = vtkActor()

    def setup(self, text):
        """Setup text"""

        # Set text
        self.__source.SetText(text)
        self.__source.SetForegroundColor(1.0, 0.0, 0.0)

        # Set mapper
        self.__mapper.SetInputConnection(self.__source.GetOutputPort())

        # Set actor
        self.__actor.SetMapper(self.__mapper)

        # Add actor to the window renderer
        self.__renderer.AddActor(self.__actor)


# Run the program
if __name__ == '__main__':
    window_renderer = WindowRenderer()

    Text(window_renderer.renderer).setup("Hello World")

    window_renderer.setup_render_window((0.0, 0.0, 500.0))
    window_renderer.start_render_window()
