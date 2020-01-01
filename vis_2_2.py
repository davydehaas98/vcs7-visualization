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
        self.__geometry_filter = vtkGeometryFilter()
        self.__mapper = vtkPolyDataMapper()
        self.__property = vtkProperty()
        self.__actor = vtkActor()

    def setup(self, file_name):
        """Setup the VTK poly data reader"""

        # Set reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()

        # Set geometry filter
        self.__geometry_filter.SetInputConnection(self.__reader.GetOutputPort())
        self.__geometry_filter.Update()

        # Set mapper
        self.__mapper.SetInputConnection(self.__geometry_filter.GetOutputPort())
        self.__mapper.Update()

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
        self.__geometry_filter = vtkGeometryFilter()
        self.__mapper = vtkPolyDataMapper()
        self.__property = vtkProperty()
        self.__actor = vtkActor()

    def setup(self, file_name):
        """Setup the VTK structured points reader"""

        # Set reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()

        # Set geometry filter
        self.__geometry_filter.SetInputConnection(self.__reader.GetOutputPort())
        self.__geometry_filter.Update()

        # Set mapper
        self.__mapper.SetInputConnection(self.__geometry_filter.GetOutputPort())
        self.__mapper.Update()

        # Set property
        self.__property.SetColor(1.0, 0.0, 0.0)

        # Set  actor
        self.__actor.SetMapper(self.__mapper)
        self.__actor.SetProperty(self.__property)

        # Add actor to the window renderer
        self.__renderer.AddActor(self.__actor)


# Run the program
if __name__ == '__main__':
    __window_renderer = WindowRenderer()
    # VtkPolyDataReader cannot read dataset type: structured_points
    #VTKPolyDataReader(window_renderer.renderer).setup("objects/brain.vtk")
    VTKStructuredPointsReader(__window_renderer.renderer).setup("objects/brain.vtk")

    __window_renderer.setup_render_window((0.0, 0.0, 1000.0))
    __window_renderer.start_render_window()
