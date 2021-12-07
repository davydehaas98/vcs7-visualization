from vtkmodules.all import (
    vtkPolyDataReader, vtkTransform,
    vtkTransformFilter, vtkPolyDataMapper,
    vtkDataSetMapper, vtkProperty,
    vtkActor, vtkStructuredPointsReader,
)

from utils.window import Window


def create_vtk_poly_data_visualizer(renderer, file_name, color=None, opacity=None, position=None, rotation=None):
    """Setup the VTK poly data visualizer"""

    # Set optional arguments
    color = color or (1.0, 0.0, 0.0)
    opacity = opacity or 1.0
    rotation = rotation or (0.0, 0.0, 0.0, 0.0)
    position = position or (0.0, 0.0, 0.0)

    # Set reader
    reader = vtkPolyDataReader()
    reader.SetFileName(file_name)
    reader.Update()

    # Set transform
    transform = vtkTransform()
    transform.RotateWXYZ(*rotation)
    transform.Translate(position)

    # Set transform filter
    transform_filter = vtkTransformFilter()
    transform_filter.SetInputConnection(reader.GetOutputPort())
    transform_filter.SetTransform(transform)
    transform_filter.Update()

    # Set mapper
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(transform_filter.GetOutputPort())

    # Set properties
    properties = vtkProperty()
    properties.SetColor(color)
    properties.SetOpacity(opacity)

    # Set actor
    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.SetProperty(properties)

    # Add reader actor to the window renderer
    renderer.AddActor(actor)


def create_vtk_structured_points_visualizer(renderer, file_name, color=None):
    """Create VTK structured points visualizer"""

    # Set optional arguments
    color = color or (1.0, 0.0, 0.0)

    # Set reader
    reader = vtkStructuredPointsReader()
    reader.SetFileName(file_name)

    # Set mapper
    mapper = vtkDataSetMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    # Set properties
    properties = vtkProperty()
    properties.SetColor(color)

    # Set actor
    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.SetProperty(properties)

    # Add actor to the window renderer
    renderer.AddActor(actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    create_vtk_poly_data_visualizer(window.renderer, "../resources/vtk/skin.vtk")
    create_vtk_structured_points_visualizer(window.renderer, "../resources/vtk/brain.vtk")

    window.create((0.0, 0.0, 1000.0))
