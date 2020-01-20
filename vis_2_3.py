from vtkmodules.all import (
    vtkUnstructuredGridReader, vtkDataSetMapper,
    vtkProperty, vtkActor,
)

from utils.window import Window


def create_vtk_unstructured_grid_visualizer(renderer, file_name):
    """Create VTK unstructured grid visualizer"""

    # Set reader
    reader = vtkUnstructuredGridReader()
    reader.SetFileName(file_name)
    reader.Update()

    # Set mapper
    mapper = vtkDataSetMapper()
    mapper.SetInputConnection(reader.GetOutputPort())
    mapper.SetScalarRange(reader.GetOutput().GetScalarRange())
    mapper.ScalarVisibilityOn()

    # Set  actor
    actor = vtkActor()
    actor.SetMapper(mapper)

    # Add actor to the window renderer
    renderer.AddActor(actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    create_vtk_unstructured_grid_visualizer(window.renderer, "files/vtk/self_made.vtk")

    window.create((0.0, 0.0, 15.0))
