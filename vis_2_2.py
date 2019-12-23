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
        self.__reader_property = vtkProperty()
        self.__reader_mapper = vtkPolyDataMapper()
        self.__reader_actor = vtkActor()

    def setup(self, file_name):
        """Setup the VTK poly data reader"""

        # Set reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()

        # Set reader property
        self.__reader_property.SetColor(1.0, 0.0, 0.0)

        # Set mapper
        self.__reader_mapper.SetInputConnection(self.__reader.GetOutputPort())

        # Set actor
        self.__reader_actor.SetProperty(self.__reader_property)
        self.__reader_actor.SetMapper(self.__reader_mapper)

        # Add reader actor to the window renderer
        self.__renderer.AddActor(self.__reader_actor)


class VTKStructuredPointsReader:

    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__reader = vtkStructuredPointsReader()
        self.__reader_property = vtkProperty()
        self.__geometry_filter = vtkGeometryFilter()
        self.__mapper = vtkPolyDataMapper()
        self.__actor = vtkActor()

    def setup(self, file_name):
        """Setup the VTK structured points reader"""

        # Set object reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()

        # Set object reader property
        self.__reader_property.SetColor(1.0, 0.0, 0.0)

        self.__geometry_filter.SetInputConnection(self.__reader.GetOutputPort())
        self.__geometry_filter.Update()

        # Set object reader mapper
        self.__mapper.SetInputConnection(self.__geometry_filter.GetOutputPort())
        self.__mapper.Update()

        # Set object reader actor
        self.__actor.SetProperty(self.__reader_property)
        self.__actor.SetMapper(self.__mapper)

        # Add object reader actor to the window renderer
        self.__renderer.AddActor(self.__actor)


# Run the program
if __name__ == '__main__':
    window_renderer = WindowRenderer()

    #VTKPolyDataReader(window_renderer.renderer).setup("objects/brain.vtk")
    VTKStructuredPointsReader(window_renderer.renderer).setup("objects/brain.vtk")

    window_renderer.setup_render_window()
    window_renderer.start_render_window()
