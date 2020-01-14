from vtkmodules.all import (
    vtkStructuredGridReader, vtkPlane,
    vtkCutter, vtkPolyDataMapper,
    vtkActor,
)

from utils.window import Window


class CutterVisualizer:
    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__reader = vtkStructuredGridReader()
        self.__plane = vtkPlane()
        self.__cutter = vtkCutter()
        self.__mapper = vtkPolyDataMapper()
        self.__actor = vtkActor()

    def setup(self, file_name):
        """Setup cutting visualizer"""

        # Set reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()

        # Set plane
        self.__plane.SetOrigin(self.__reader.GetOutput().GetCenter())
        self.__plane.SetNormal(1.0, 1.0, 0.0)

        # Set cutter
        self.__cutter.SetCutFunction(self.__plane)
        self.__cutter.SetInputConnection(self.__reader.GetOutputPort())
        self.__cutter.Update()

        # Set mapper
        self.__mapper.SetInputConnection(self.__cutter.GetOutputPort())

        # Set actor
        self.__actor.SetMapper(self.__mapper)

        # Add actor to the window renderer
        self.__renderer.AddActor(self.__actor)


if __name__ == '__main__':
    __window = Window()

    CutterVisualizer(__window.renderer).setup("objects/density.vtk")

    __window.setup((0.0, 0.0, 200.0))