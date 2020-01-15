from vtkmodules.all import (
    vtkUnstructuredGridReader, vtkDataSetMapper,
    vtkProperty, vtkActor,
)

from utils.window import Window


class VTKUnstructuredGridVisualizer:

    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__reader = vtkUnstructuredGridReader()
        self.__mapper = vtkDataSetMapper()
        self.__property = vtkProperty()
        self.__actor = vtkActor()

    def setup(self, file_name):
        """Setup the VTK unstructured grid visualizer"""

        # Set reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()
        print(self.__reader.GetOutput())

        # Set scalar range
        __scalar_range = self.__reader.GetOutput().GetScalarRange()

        # Set mapper
        self.__mapper.SetInputConnection(self.__reader.GetOutputPort())
        self.__mapper.SetScalarRange(__scalar_range)
        self.__mapper.SetScalarModeToUsePointData()
        self.__mapper.ScalarVisibilityOn()

        # Set property
        self.__property.EdgeVisibilityOn()
        self.__property.SetLineWidth(2.0)

        # Set  actor
        self.__actor.SetMapper(self.__mapper)
        self.__actor.SetProperty(self.__property)

        # Add actor to the window renderer
        self.__renderer.AddActor(self.__actor)


if __name__ == '__main__':
    __window = Window()

    VTKUnstructuredGridVisualizer(__window.renderer).setup("objects/self_made.vtk")

    __window.setup((0.0, 0.0, 500.0))