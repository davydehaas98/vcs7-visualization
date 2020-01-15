from vtkmodules.all import (
    vtkStructuredGridReader, vtkPlane,
    vtkCutter, vtkPolyDataMapper,
    vtkActor,
)

from utils.window import Window


def cutter_visualizer(renderer, file_name):
    """Create cutting visualizer"""

    # Initialize variables
    reader = vtkStructuredGridReader()
    plane = vtkPlane()
    cutter = vtkCutter()
    mapper = vtkPolyDataMapper()
    actor = vtkActor()

    # Set reader
    reader.SetFileName(file_name)
    reader.Update()

    # Set plane
    plane.SetOrigin(reader.GetOutput().GetCenter())
    plane.SetNormal(1.0, 1.0, 0.0)

    # Set cutter
    cutter.SetCutFunction(plane)
    cutter.SetInputConnection(reader.GetOutputPort())
    cutter.Update()

    # Set mapper
    mapper.SetInputConnection(cutter.GetOutputPort())

    # Set actor
    actor.SetMapper(mapper)

    # Add actor to the window renderer
    renderer.AddActor(actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    cutter_visualizer(window.renderer, "objects/density.vtk")

    window.setup((0.0, 0.0, 200.0))