from vtkmodules.all import (
    vtkTextSource, vtkPolyDataMapper, vtkActor,
)

from library.window_renderer import WindowRenderer


class Text:
    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__text = vtkTextSource()
        self.__text_mapper = vtkPolyDataMapper()
        self.__text_actor = vtkActor()

    def setup_text(self, text):
        """Setup text"""

        # Set text
        self.__text.SetText(text)
        self.__text.SetForegroundColor(1.0, 0.0, 0.0)

        # Set text mapper
        self.__text_mapper.SetInputConnection(self.__text.GetOutputPort())

        # set text actor
        self.__text_actor.SetMapper(self.__text_mapper)

        self.__renderer.AddActor(self.__text_actor)


# Run the program
if __name__ == '__main__':
    window_renderer = WindowRenderer()
    Text(window_renderer.renderer).setup_text("Hello World")
    window_renderer.setup_render_window()
    window_renderer.start_render_window()
