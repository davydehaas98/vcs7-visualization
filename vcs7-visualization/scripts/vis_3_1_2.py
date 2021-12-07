from vtkmodules.all import (
    vtkStructuredGridReader, vtkContourFilter,
    vtkPolyDataMapper, vtkActor,
)

from utils.window import Window


def create_contour_visualizer(renderer, file_name):
    """Create contour visualizer"""

    # Set reader
    reader = vtkStructuredGridReader()
    reader.SetFileName(file_name)

    # Set contour filter that generates polygonal data
    contour_filter = vtkContourFilter()
    contour_filter.SetInputConnection(reader.GetOutputPort())
    contour_filter.SetValue(0, 0.26)

    # Set mapper
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(contour_filter.GetOutputPort())

    # Set actor
    actor = vtkActor()
    actor.SetMapper(mapper)

    # Add actor to the window renderer
    renderer.AddActor(actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    create_contour_visualizer(window.renderer, "../resources/vtk/subset.vtk")
    create_contour_visualizer(window.renderer, "../resources/vtk/density.vtk")

    # This polygonal data vtk file does not work
    #create_contour_visualizer(__window.renderer, "resources/honolulu.vtk")

    window.create((100.0, 0.0, 150.0))
