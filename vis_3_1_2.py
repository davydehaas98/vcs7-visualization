from vtkmodules.all import (
    vtkStructuredGridReader, vtkPolyDataMapper,
    vtkContourFilter, vtkActor
)

from utils.window_renderer import WindowRenderer


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

        # Set contour filter
        # Generates polygonal data
        self.__contour_filter.SetInputConnection(self.__reader.GetOutputPort())
        self.__contour_filter.SetValue(0, 0.26)

        # Set mapper
        self.__mapper.SetInputConnection(self.__contour_filter.GetOutputPort())

        # Set actor
        self.__actor.SetMapper(self.__mapper)

        # Add actor to the window renderer
        self.__renderer.AddActor(self.__actor)


if __name__ == '__main__':
    __window_renderer = WindowRenderer()

    ContourVisualizer(__window_renderer.renderer).setup("objects/subset.vtk")
    ContourVisualizer(__window_renderer.renderer).setup("objects/density.vtk")

    __window_renderer.setup_render_window((700.0, 0.0, 500.0))
    __window_renderer.start_render_window()