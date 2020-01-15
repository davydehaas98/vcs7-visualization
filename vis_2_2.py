from vtkmodules.all import (
    vtkPolyDataReader, vtkTransform,
    vtkTransformFilter, vtkPolyDataMapper,
    vtkDataSetMapper, vtkProperty,
    vtkActor, vtkStructuredPointsReader,
)

from utils.window import Window


def vtk_poly_data_visualizer(renderer, file_name, color=None, opacity=None, position=None, rotation=None):
    """Setup the VTK poly data visualizer"""

    # Initialize variables
    reader = vtkPolyDataReader()
    transform = vtkTransform()
    transform_filter = vtkTransformFilter()
    mapper = vtkPolyDataMapper()
    properties = vtkProperty()
    actor = vtkActor()

    # Set optional arguments
    color = color or (1.0, 0.0, 0.0)
    opacity = opacity or 1.0
    rotation = rotation or (0.0, 0.0, 0.0, 0.0)
    position = position or (0.0, 0.0, 0.0)

    # Set reader
    reader.SetFileName(file_name)
    reader.Update()

    # Set transform
    transform.RotateWXYZ(*rotation)
    transform.Translate(position)

    # Set transform filter
    transform_filter.SetInputConnection(reader.GetOutputPort())
    transform_filter.SetTransform(transform)
    transform_filter.Update()

    # Set mapper
    mapper.SetInputConnection(transform_filter.GetOutputPort())
    mapper.Update()

    # Set properties
    properties.SetColor(color)
    properties.SetOpacity(opacity)

    # Set actor
    actor.SetMapper(mapper)
    actor.SetProperty(properties)

    # Add reader actor to the window renderer
    renderer.AddActor(actor)


def vtk_structured_points_visualizer(renderer, file_name, color=None):
    """Create VTK structured points visualizer"""

    # Initialize variables
    reader = vtkStructuredPointsReader()
    mapper = vtkDataSetMapper()
    properties = vtkProperty()
    actor = vtkActor()

    # Set optional arguments
    color = color or (1.0, 0.0, 0.0)

    # Set reader
    reader.SetFileName(file_name)
    reader.Update()

    # Set mapper
    mapper.SetInputConnection(reader.GetOutputPort())
    mapper.Update()

    # Set properties
    properties.SetColor(color)

    # Set actor
    actor.SetMapper(mapper)
    actor.SetProperty(properties)

    # Add actor to the window renderer
    renderer.AddActor(actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    vtk_poly_data_visualizer(window.renderer, "objects/vtk/skin.vtk")
    vtk_structured_points_visualizer(window.renderer, "objects/vtk/brain.vtk")

    window.setup((0.0, 0.0, 1000.0))
