from vtkmodules.all import (
    vtkOBJReader, vtkTransform,
    vtkTransformPolyDataFilter, vtkPolyDataMapper,
    vtkProperty, vtkActor,
)

from utils.window import Window


class OBJVisualizer:

    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__reader = vtkOBJReader()
        self.__transform = vtkTransform()
        self.__transform_filter = vtkTransformPolyDataFilter()
        self.__mapper = vtkPolyDataMapper()
        self.__property = vtkProperty()
        self.__actor = vtkActor()

    def setup(self, file_name):
        """Setup the obj visualizer"""

        # Set reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()

        # Set transform
        self.__transform.RotateWXYZ(0.0, 0.0, 0.0, 0.0)
        self.__transform.Translate(0.0, 0.0, 0.0)

        # Set transform filter
        self.__transform_filter.SetInputConnection(self.__reader.GetOutputPort())
        self.__transform_filter.SetTransform(self.__transform)
        self.__transform_filter.Update()

        # Set mapper
        self.__mapper.SetInputConnection(self.__transform_filter.GetOutputPort())

        # Set property
        self.__property.SetColor(1.0, 0.0, 0.0)

        # Set actor
        self.__actor.SetMapper(self.__mapper)
        self.__actor.SetProperty(self.__property)

        # Add actor to the window renderer
        self.__renderer.AddActor(self.__actor)


# Run the program
if __name__ == '__main__':
    __window = Window()

    OBJVisualizer(__window.renderer).setup("objects/cactus.obj")

    __window.setup((0.0, 0.0, 2000.0))
