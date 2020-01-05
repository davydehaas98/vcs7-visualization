from vtkmodules.all import (
    vtkPolyDataReader, vtkTransform,
    vtkTransformFilter, vtkPolyDataMapper,
    vtkProperty, vtkActor,
    vtkStructuredPointsReader, vtkGeometryFilter,
)

from utils.window_renderer import WindowRenderer


class VTKPolyDataVisualizer:

    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__reader = vtkPolyDataReader()
        self.__transform = vtkTransform()
        self.__transform_filter = vtkTransformFilter()
        self.__mapper = vtkPolyDataMapper()
        self.__property = vtkProperty()
        self.__actor = vtkActor()

    def setup(self, file_name, color=None, opacity=None, position=None, rotation=None):
        """Setup the VTK poly data visualizer"""

        # Set optional arguments
        color = color or (1.0, 0.0, 0.0)
        opacity = opacity or 1.0
        rotation = rotation or (0.0, 0.0, 0.0, 0.0)
        position = position or (0.0, 0.0, 0.0)

        # Set reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()

        # Set transform
        self.__transform.RotateWXYZ(*rotation)
        self.__transform.Translate(position)

        # Set transform filter
        self.__transform_filter.SetInputConnection(self.__reader.GetOutputPort())
        self.__transform_filter.SetTransform(self.__transform)
        self.__transform_filter.Update()

        # Set mapper
        self.__mapper.SetInputConnection(self.__transform_filter.GetOutputPort())
        self.__mapper.Update()

        # Set property
        self.__property.SetColor(color)
        self.__property.SetOpacity(opacity)

        # Set actor
        self.__actor.SetMapper(self.__mapper)
        self.__actor.SetProperty(self.__property)

        # Add reader actor to the window renderer
        self.__renderer.AddActor(self.__actor)


class VTKStructuredPointsVisualizer:

    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__reader = vtkStructuredPointsReader()
        self.__geometry_filter = vtkGeometryFilter()
        self.__mapper = vtkPolyDataMapper()
        self.__property = vtkProperty()
        self.__actor = vtkActor()

    def setup(self, file_name, color=None):
        """Setup the VTK structured points visualizer"""

        # Set optional arguments
        color = color or (1.0, 0.0, 0.0)

        # Set reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()

        # Set geometry filter
        # This will convert the structured points data to poly data for the vtkPolyDataMapper
        self.__geometry_filter.SetInputConnection(self.__reader.GetOutputPort())
        self.__geometry_filter.Update()

        # Set mapper
        self.__mapper.SetInputConnection(self.__reader.GetOutputPort())
        self.__mapper.Update()

        # Set property
        self.__property.SetColor(color)

        # Set actor
        self.__actor.SetMapper(self.__mapper)
        self.__actor.SetProperty(self.__property)

        # Add actor to the window renderer
        self.__renderer.AddActor(self.__actor)


# Run the program
if __name__ == '__main__':
    __window_renderer = WindowRenderer()
    # VtkPolyDataReader cannot read dataset type: structured_points
    #VTKPolyDataVisualizer(__window_renderer.renderer).setup("objects/brain.vtk")
    VTKStructuredPointsVisualizer(__window_renderer.renderer).setup("objects/brain.vtk")

    __window_renderer.setup_render_window((0.0, 0.0, 1000.0))
    __window_renderer.start_render_window()
