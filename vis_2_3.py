from vtkmodules.all import (
    vtkUnstructuredGridReader, vtkDataSetMapper,
    vtkProperty, vtkActor,
)

from utils.window import Window


def vtk_unstructured_grid_visualizer(renderer, file_name):
    """Create VTK unstructured grid visualizer"""

    # Initialize variables
    reader = vtkUnstructuredGridReader()
    mapper = vtkDataSetMapper()
    properties = vtkProperty()
    actor = vtkActor()

    # Set reader
    reader.SetFileName(file_name)
    reader.Update()
    print(reader.GetOutput())

    # Set scalar range
    scalar_range = reader.GetOutput().GetScalarRange()

    # Set mapper
    mapper.SetInputConnection(reader.GetOutputPort())
    mapper.SetScalarRange(scalar_range)
    mapper.SetScalarModeToUsePointData()
    mapper.ScalarVisibilityOn()

    # Set properties
    properties.EdgeVisibilityOn()
    properties.SetLineWidth(2.0)

    # Set  actor
    actor.SetMapper(mapper)
    actor.SetProperty(properties)

    # Add actor to the window renderer
    renderer.AddActor(actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    vtk_unstructured_grid_visualizer(window.renderer, "files/vtk/self_made.vtk")

    window.setup((0.0, 0.0, 500.0))
