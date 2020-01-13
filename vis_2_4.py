from vtkmodules.all import (
    vtkPlaneSource, vtkBMPReader,
    vtkTexture, vtkPolyDataMapper,
    vtkActor,
)

from utils.window import Window


class TextureVisualizer:

    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__plane = vtkPlaneSource()
        self.__reader = vtkBMPReader()
        self.__texture = vtkTexture()
        self.__mapper = vtkPolyDataMapper()
        self.__actor = vtkActor()

    def setup(self, file_name):
        """Setup the texture plane"""

        # Set reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()

        # Set texture
        self.__texture.SetInputConnection(self.__reader.GetOutputPort())

        # Set mapper
        self.__mapper.SetInputConnection(self.__plane.GetOutputPort())

        # Set actor
        self.__actor.SetTexture(self.__texture)
        self.__actor.SetMapper(self.__mapper)

        # Add actor to the window renderer
        self.__renderer.AddActor(self.__actor)


# Run the program
if __name__ == '__main__':
    __window = Window()

    TextureVisualizer(__window.renderer).setup("images/marbles.bmp")

    __window.setup((0.0, 0.0, 5.0))
