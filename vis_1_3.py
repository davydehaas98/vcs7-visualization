from vtkmodules.all import (
    vtkCylinderSource, vtkProperty,
    vtkPolyDataMapper, vtkActor,
)

from utils.window_renderer import WindowRenderer
from vis_1_1 import Cone


class Cylinder:

    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__source = vtkCylinderSource()
        self.__property = vtkProperty()
        self.__mapper = vtkPolyDataMapper()
        self.__actor = vtkActor()

    def setup(self, radius, height, resolution, center, color):
        """Setup the cylinder"""

        # Set cylinder
        self.__source.SetRadius(radius)
        self.__source.SetHeight(height)
        self.__source.SetResolution(resolution)
        self.__source.SetCenter(center)

        # Set mapper
        self.__mapper.SetInputConnection(self.__source.GetOutputPort())

        # Set property
        self.__property.SetColor(color)
        self.__property.SetDiffuse(0.7)
        self.__property.SetSpecular(0.4)
        self.__property.SetSpecularPower(20)

        # Set actor
        self.__actor.SetMapper(self.__mapper)
        self.__actor.SetProperty(self.__property)

        # Add actor to the window renderer
        self.__renderer.AddActor(self.__actor)


# Run the program
if __name__ == '__main__':
    window_renderer = WindowRenderer()

    Cylinder(window_renderer.renderer).setup(
        4.0, 4.0, 40,       # radius, height, resolution
        (5.0, 0.0, 0.0),    # center
        (1.0, 0.0, 0.0)     # color
    )

    Cone(window_renderer.renderer).setup(
        3.0, 12.0, 120,     # radius, height, resolution
        (0.0, 0.0, 0.0),    # direction
        (0.0, 0.0, 0.0),    # center
        (0.0, 1.0, 0.0)     # color
    )

    window_renderer.setup_render_window((0.0, 0.0, 40.0))
    window_renderer.start_render_window()
