from vtkmodules.all import (
    vtkStructuredGridReader, vtkPolyDataMapper,
    vtkHedgeHog, vtkActor,
)

from utils.window import Window
from vis_3_1_1 import create_lookup_table


def create_hedgehog_visualizer(renderer, file_name, scale):
    """Create hedgehog visualizer"""

    # Set reader
    reader = vtkStructuredGridReader()
    reader.SetFileName(file_name)

    # Set lookup table
    lookup_table = create_lookup_table(1000, (1.0, 0.0))

    # Set hedgehog
    hedgehog = vtkHedgeHog()
    hedgehog.SetInputConnection(reader.GetOutputPort())
    hedgehog.SetScaleFactor(scale)

    # Set mapper
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(hedgehog.GetOutputPort())
    mapper.SetLookupTable(lookup_table)
    mapper.SetScalarRange(0.0, 1.0)
    mapper.ScalarVisibilityOn()

    # Set actor
    actor = vtkActor()
    actor.SetMapper(mapper)

    # Add actor to the window renderer
    renderer.AddActor(actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    create_hedgehog_visualizer(window.renderer, "../resources/vtk/density.vtk", 0.01)

    window.create((0.0, 0.0, 100.0))