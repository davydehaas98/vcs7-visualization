from vtkmodules.all import (
    vtkStructuredGridReader, vtkPlane,
    vtkCutter, vtkPolyDataMapper,
    vtkActor,
)

from utils.window import Window


def create_cutter_visualizer(renderer, file_name):
    """Create cutting visualizer"""

    # Set reader
    reader = vtkStructuredGridReader()
    reader.SetFileName(file_name)
    reader.Update()

    # Set plane
    plane = vtkPlane()
    plane.SetOrigin(reader.GetOutput().GetCenter())
    plane.SetNormal(1.0, 1.0, 0.0)

    # Set cutter
    cutter = vtkCutter()
    cutter.SetCutFunction(plane)
    cutter.SetInputConnection(reader.GetOutputPort())
    cutter.Update()

    # Set mapper
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(cutter.GetOutputPort())

    # Set actor
    actor = vtkActor()
    actor.SetMapper(mapper)

    # Add actor to the window renderer
    renderer.AddActor(actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    create_cutter_visualizer(window.renderer, "../resources/vtk/density.vtk")

    window.create((0.0, 0.0, 200.0))