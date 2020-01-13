from vtkmodules.all import (
    vtkConeSource, vtkProperty,
    vtkPolyDataMapper, vtkActor,
)

from utils.window import Window


class Cone:

    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__source = vtkConeSource()
        self.__property = vtkProperty()
        self.__mapper = vtkPolyDataMapper()
        self.__actor = vtkActor()

    def setup(self, radius, height, resolution, direction, center, color):
        """Setup the cone"""

        # Set cone
        self.__source.SetRadius(radius)
        self.__source.SetHeight(height)
        self.__source.SetResolution(resolution)
        self.__source.SetDirection(direction)
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
    __window = Window()

    Cone(__window.renderer).setup(
        1.0, 3.0, 40,     # radius, height, resolution
        (0.0, 0.0, 0.0),  # direction
        (0.0, 0.0, 0.0),  # center
        (1.0, 0.0, 0.0)   # color
    )

    Cone(__window.renderer).setup(
        0.5, 2.0, 10,     # radius, height, resolution
        (1.0, 1.0, 1.0),  # direction
        (2.0, 2.0, 2.0),  # center
        (0.0, 1.0, 0.0)   # color
    )

    __window.setup((0.0, 0.0, 25.0))
