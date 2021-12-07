from vtkmodules.all import (
    vtkOBJReader, vtkTransform,
    vtkTransformPolyDataFilter, vtkPolyDataMapper,
    vtkProperty, vtkActor,
)

from utils.window import Window


def create_obj_visualizer(renderer, file_name):
    """Create obj visualizer"""

    # Set reader
    reader = vtkOBJReader()
    reader.SetFileName(file_name)

    # Set transform
    transform = vtkTransform()
    transform.RotateWXYZ(0.0, 0.0, 0.0, 0.0)
    transform.Translate(0.0, 0.0, 0.0)

    # Set transform filter
    transform_filter = vtkTransformPolyDataFilter()
    transform_filter.SetInputConnection(reader.GetOutputPort())
    transform_filter.SetTransform(transform)

    # Set mapper
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(transform_filter.GetOutputPort())

    # Set properties
    properties = vtkProperty()
    properties.SetColor(1.0, 0.0, 0.0)

    # Set actor
    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.SetProperty(properties)

    # Add actor to the window renderer
    renderer.AddActor(actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    create_obj_visualizer(window.renderer, "../resources/obj/cactus.obj")

    window.create((0.0, 0.0, 2000.0))
