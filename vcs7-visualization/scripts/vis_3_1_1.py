from vtkmodules.all import (
    vtkStructuredGridReader, vtkLookupTable,
    vtkDataSetMapper, vtkActor,
)

from utils.window import Window


def create_color_visualizer(renderer, file_name, scalar_range):
    """Create color visualizer"""

    # Initialize variables
    reader = vtkStructuredGridReader()
    mapper = vtkDataSetMapper()
    actor = vtkActor()

    # Set reader
    reader.SetFileName(file_name)

    # Set lookup table
    lookup_table = create_lookup_table(1000, (0.0, 1.0))

    # Set mapper
    mapper.SetInputConnection(reader.GetOutputPort())
    mapper.SetLookupTable(lookup_table)
    mapper.SetScalarRange(scalar_range)
    mapper.ScalarVisibilityOn()

    # Set actor
    actor.SetMapper(mapper)

    # Add actor to the window renderer
    renderer.AddActor(actor)


def create_lookup_table(colors, hue) -> vtkLookupTable:
    lookup_table = vtkLookupTable()

    lookup_table.SetNumberOfColors(colors)
    lookup_table.SetHueRange(hue)
    lookup_table.SetSaturationRange(1.0, 0.0)
    lookup_table.SetValueRange(1.0, 0.0)
    lookup_table.SetAlphaRange(1.0, 0.0)

    # Range of scalars that will be mapped
    lookup_table.SetRange(0.0, 1.0)
    lookup_table.Build()

    return lookup_table


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    create_color_visualizer(window.renderer, "../resources/vtk/density.vtk", (0.0, 1.0))

    window.create((0.0, 0.0, 100.0))
