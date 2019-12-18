from vtkmodules.all import vtkTextSource, vtkPolyDataMapper, vtkActor

class Text:
    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__text = vtkTextSource()
        self.__text_mapper = vtkPolyDataMapper()
        self.__text_actor = vtkActor()

    def setup_text(self):
        """Setup text"""

        # Set text
        self.__text.SetText("Hello World")

        # Set text mapper
        self.__text_mapper.SetInputConnection(self.__text.GetOutputPort())

        # set text actor
        self.__text_actor.SetMapper(self.__text_mapper)


# Run the program
if __name__ == '__main__':
    # window_renderer = WindowRenderer()
    #
    # window_renderer.setup_render_window()
    # window_renderer.start_render_window()