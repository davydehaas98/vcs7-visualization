from vtkmodules.all import (
    vtkConeSource, vtkProperty,
    vtkPolyDataMapper, vtkActor,
)

from utils.window import Window


def create_cone(renderer, radius, height, resolution, direction, center, color):
    """Create cone"""

    # Set cone
    cone = vtkConeSource()
    cone.SetRadius(radius)
    cone.SetHeight(height)
    cone.SetResolution(resolution)
    cone.SetDirection(direction)
    cone.SetCenter(center)

    # Set mapper
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(cone.GetOutputPort())

    # Set properties
    properties = vtkProperty()
    properties.SetColor(color)
    properties.SetDiffuse(0.7)
    properties.SetSpecular(0.4)
    properties.SetSpecularPower(20)

    # Set actor
    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.SetProperty(properties)

    # Add actor to the window renderer
    renderer.AddActor(actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    create_cone(
        window.renderer,
        1.0, 3.0, 40,  # radius, height, resolution
        (0.0, 0.0, 0.0),  # direction
        (0.0, 0.0, 0.0),  # center
        (1.0, 0.0, 0.0)  # color
    )

    create_cone(
        window.renderer,
        0.5, 2.0, 10,  # radius, height, resolution
        (1.0, 1.0, 1.0),  # direction
        (2.0, 2.0, 2.0),  # center
        (0.0, 1.0, 0.0)  # color
    )

    window.setup((0.0, 0.0, 25.0))
