from vtkmodules.all import (
    vtkPolyDataReader, vtkProperty,
    vtkPolyDataMapper, vtkActor,
    vtkStructuredPointsReader, vtkGeometryFilter,
)

from utils.window_renderer import WindowRenderer


class VTKPolyDataReader:

    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__reader = vtkPolyDataReader()
        self.__mapper = vtkPolyDataMapper()
        self.__property = vtkProperty()
        self.__actor = vtkActor()

    def setup(self, file_name):
        """Setup the VTK poly data reader"""

        # Set reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()

        # Set mapper
        self.__mapper.SetInputConnection(self.__reader.GetOutputPort())

        # Set property
        self.__property.SetColor(1.0, 0.0, 0.0)

        # Set actor
        self.__actor.SetMapper(self.__mapper)
        self.__actor.SetProperty(self.__property)

        # Add reader actor to the window renderer
        self.__renderer.AddActor(self.__actor)


class VTKStructuredPointsReader:

    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__reader = vtkStructuredPointsReader()
        self.__property = vtkProperty()
        self.__geometry_filter = vtkGeometryFilter()
        self.__mapper = vtkPolyDataMapper()
        self.__actor = vtkActor()

    def setup(self, file_name):
        """Setup the VTK structured points reader"""

        # Set reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()

        # Set property
        self.__property.SetColor(1.0, 0.0, 0.0)

        self.__geometry_filter.SetInputConnection(self.__reader.GetOutputPort())
        self.__geometry_filter.Update()

        # Set mapper
        self.__mapper.SetInputConnection(self.__geometry_filter.GetOutputPort())
        self.__mapper.Update()

        # Set  actor
        self.__actor.SetProperty(self.__property)
        self.__actor.SetMapper(self.__mapper)

        # Add actor to the window renderer
        self.__renderer.AddActor(self.__actor)


# Run the program
if __name__ == '__main__':
    window_renderer = WindowRenderer()

    #VTKPolyDataReader(window_renderer.renderer).setup("objects/brain.vtk")
    VTKStructuredPointsReader(window_renderer.renderer).setup("objects/brain.vtk")

    window_renderer.setup_render_window((0.0, 0.0, 100.0))
    window_renderer.start_render_window()
