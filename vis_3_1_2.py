from vtkmodules.all import (
    vtkStructuredGridReader, vtkContourFilter,
    vtkPolyDataMapper, vtkActor,
)

from utils.window import Window


class ContourVisualizer:

    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__reader = vtkStructuredGridReader()
        self.__contour_filter = vtkContourFilter()
        self.__mapper = vtkPolyDataMapper()
        self.__actor = vtkActor()

    def setup(self, file_name):
        """Setup the contour visualizer"""

        # Set reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()

        # Set contour filter that generates polygonal data
        self.__contour_filter.SetInputConnection(self.__reader.GetOutputPort())
        self.__contour_filter.SetValue(0, 0.26)

        # Set mapper
        self.__mapper.SetInputConnection(self.__contour_filter.GetOutputPort())

        # Set actor
        self.__actor.SetMapper(self.__mapper)

        # Add actor to the window renderer
        self.__renderer.AddActor(self.__actor)


if __name__ == '__main__':
    __window = Window()

    ContourVisualizer(__window.renderer).setup("objects/subset.vtk")
    ContourVisualizer(__window.renderer).setup("objects/density.vtk")

    # This polygonal data vtk file does not work
    #ContourVisualizer(__window.renderer).setup("objects/honolulu.vtk")

    __window.setup((700.0, 0.0, 500.0))
