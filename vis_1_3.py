from vtkmodules.all import (
    vtkCylinderSource, vtkPolyDataMapper,
    vtkProperty, vtkActor,
)

from utils.window import Window
from vis_1_1 import create_cone


def create_cylinder(renderer, radius, height, resolution, center, color):
    """Create cylinder"""

    # Initialize variables
    cylinder = vtkCylinderSource()
    mapper = vtkPolyDataMapper()
    properties = vtkProperty()
    actor = vtkActor()

    # Set cylinder
    cylinder.SetRadius(radius)
    cylinder.SetHeight(height)
    cylinder.SetResolution(resolution)
    cylinder.SetCenter(center)

    # Set mapper
    mapper.SetInputConnection(cylinder.GetOutputPort())

    # Set property
    properties.SetColor(color)
    properties.SetDiffuse(0.7)
    properties.SetSpecular(0.4)
    properties.SetSpecularPower(20)

    # Set actor
    actor.SetMapper(mapper)
    actor.SetProperty(properties)

    # Add actor to the window renderer
    renderer.AddActor(actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    create_cylinder(
        window.renderer,
        4.0, 4.0, 40,       # radius, height, resolution
        (5.0, 0.0, 0.0),    # center
        (1.0, 0.0, 0.0)     # color
    )

    create_cone(
        window.renderer,
        3.0, 12.0, 120,     # radius, height, resolution
        (0.0, 0.0, 0.0),    # direction
        (0.0, 0.0, 0.0),    # center
        (0.0, 1.0, 0.0)     # color
    )

    window.create((0.0, 0.0, 40.0))
