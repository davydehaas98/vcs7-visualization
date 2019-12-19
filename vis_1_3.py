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

        self.__cylinder = vtkCylinderSource()
        self.__cylinder_property = vtkProperty()
        self.__cylinder_mapper = vtkPolyDataMapper()
        self.__cylinder_actor = vtkActor()

    def setup_cylinder(self, radius, height, resolution, center, color):
        """Setup the cylinder"""

        # Set cylinder
        self.__cylinder.SetRadius(radius)
        self.__cylinder.SetHeight(height)
        self.__cylinder.SetResolution(resolution)
        self.__cylinder.SetCenter(center)

        # Set cylinder property
        self.__cylinder_property.SetColor(color)
        self.__cylinder_property.SetDiffuse(0.7)
        self.__cylinder_property.SetSpecular(0.4)
        self.__cylinder_property.SetSpecularPower(20)

        # Set cylinder mapper
        self.__cylinder_mapper.SetInputConnection(self.__cylinder.GetOutputPort())

        # Set cylinder actor
        self.__cylinder_actor.SetProperty(self.__cylinder_property)
        self.__cylinder_actor.SetMapper(self.__cylinder_mapper)

        # Add cylinder actor to the window renderer
        self.__renderer.AddActor(self.__cylinder_actor)


# Run the program
if __name__ == '__main__':
    window_renderer = WindowRenderer()

    Cylinder(window_renderer.renderer).setup_cylinder(
        4.0, 4.0, 40,       # radius, height, resolution
        (5.0, 0.0, 0.0),    # center
        (1.0, 0.0, 0.0)     # color
    )

    Cone(window_renderer.renderer).setup_cone(
        3.0, 12.0, 120,     # radius, height, resolution
        (0.0, 0.0, 0.0),    # direction
        (0.0, 0.0, 0.0),    # center
        (0.0, 1.0, 0.0)     # color
    )

    window_renderer.setup_render_window()
    window_renderer.start_render_window()
