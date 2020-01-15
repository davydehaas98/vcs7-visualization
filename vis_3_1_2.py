from vtkmodules.all import (
    vtkStructuredGridReader, vtkContourFilter,
    vtkPolyDataMapper, vtkActor,
)

from utils.window import Window


def contour_visualizer(renderer, file_name):
    """Create contour visualizer"""

    # Initialize variables
    reader = vtkStructuredGridReader()
    contour_filter = vtkContourFilter()
    mapper = vtkPolyDataMapper()
    actor = vtkActor()

    # Set reader
    reader.SetFileName(file_name)
    reader.Update()

    # Set contour filter that generates polygonal data
    contour_filter.SetInputConnection(reader.GetOutputPort())
    contour_filter.SetValue(0, 0.26)

    # Set mapper
    mapper.SetInputConnection(contour_filter.GetOutputPort())

    # Set actor
    actor.SetMapper(mapper)

    # Add actor to the window renderer
    renderer.AddActor(actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    contour_visualizer(window.renderer, "objects/vtk/subset.vtk")
    contour_visualizer(window.renderer, "objects/vtk/density.vtk")

    # This polygonal data vtk file does not work
    #contour_visualizer(__window.renderer, "objects/honolulu.vtk")

    window.setup((100.0, 0.0, 150.0))
