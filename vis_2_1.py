from vtkmodules.all import (
    vtkOBJReader, vtkTransform,
    vtkTransformPolyDataFilter, vtkPolyDataMapper,
    vtkProperty, vtkActor,
)

from utils.window import Window


def obj_visualizer(renderer, file_name):
    """Create obj visualizer"""

    # Initialize variables
    reader = vtkOBJReader()
    transform = vtkTransform()
    transform_filter = vtkTransformPolyDataFilter()
    mapper = vtkPolyDataMapper()
    properties = vtkProperty()
    actor = vtkActor()

    # Set reader
    reader.SetFileName(file_name)
    reader.Update()

    # Set transform
    transform.RotateWXYZ(0.0, 0.0, 0.0, 0.0)
    transform.Translate(0.0, 0.0, 0.0)

    # Set transform filter
    transform_filter.SetInputConnection(reader.GetOutputPort())
    transform_filter.SetTransform(transform)
    transform_filter.Update()

    # Set mapper
    mapper.SetInputConnection(transform_filter.GetOutputPort())

    # Set properties
    properties.SetColor(1.0, 0.0, 0.0)

    # Set actor
    actor.SetMapper(mapper)
    actor.SetProperty(properties)

    # Add actor to the window renderer
    renderer.AddActor(actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    obj_visualizer(window.renderer, "files/obj/cactus.obj")

    window.setup((0.0, 0.0, 2000.0))
