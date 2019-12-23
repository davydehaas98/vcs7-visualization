from vtkmodules.all import (
    vtkConeSource, vtkProperty,
    vtkPolyDataMapper, vtkActor,
)

from utils.window_renderer import WindowRenderer


class Cone:

    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__source = vtkConeSource()
        self.__source_property = vtkProperty()
        self.__source_mapper = vtkPolyDataMapper()
        self.__source_actor = vtkActor()

    def setup(self, radius, height, resolution, direction, center, color):
        """Setup the cone"""

        # Set cone
        self.__source.SetRadius(radius)
        self.__source.SetHeight(height)
        self.__source.SetResolution(resolution)
        self.__source.SetDirection(direction)
        self.__source.SetCenter(center)

        # Set cone property
        self.__source_property.SetColor(color)
        self.__source_property.SetDiffuse(0.7)
        self.__source_property.SetSpecular(0.4)
        self.__source_property.SetSpecularPower(20)

        # Set cone mapper
        self.__source_mapper.SetInputConnection(self.__source.GetOutputPort())

        # Set cone actor
        self.__source_actor.SetMapper(self.__source_mapper)
        self.__source_actor.SetProperty(self.__source_property)

        # Add cone actor to the window renderer
        self.__renderer.AddActor(self.__source_actor)


# Run the program
if __name__ == '__main__':
    window_renderer = WindowRenderer()

    Cone(window_renderer.renderer).setup(
        1.0, 3.0, 40,     # radius, height, resolution
        (0.0, 0.0, 0.0),  # direction
        (0.0, 0.0, 0.0),  # center
        (1.0, 0.0, 0.0)   # color
    )

    Cone(window_renderer.renderer).setup(
        0.5, 2.0, 10,     # radius, height, resolution
        (1.0, 1.0, 1.0),  # direction
        (2.0, 2.0, 2.0),  # center
        (0.0, 1.0, 0.0)   # color
    )

    window_renderer.setup_render_window()
    window_renderer.start_render_window()
