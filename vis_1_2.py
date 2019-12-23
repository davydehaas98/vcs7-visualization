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
        self.__source_mapper = vtkPolyDataMapper()
        self.__source_actor = vtkActor()

    def setup(self, text):
        """Setup text"""

        # Set text
        self.__source.SetText(text)
        self.__source.SetForegroundColor(1.0, 0.0, 0.0)

        # Set text mapper
        self.__source_mapper.SetInputConnection(self.__source.GetOutputPort())

        # Set text actor
        self.__source_actor.SetMapper(self.__source_mapper)

        # Add text actor to the window renderer
        self.__renderer.AddActor(self.__source_actor)


# Run the program
if __name__ == '__main__':
    window_renderer = WindowRenderer()

    Text(window_renderer.renderer).setup("Hello World")

    window_renderer.setup_render_window()
    window_renderer.start_render_window()
