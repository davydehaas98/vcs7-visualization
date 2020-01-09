from vtkmodules.all import (
    vtkStructuredGridReader, vtkDataSetMapper,
    vtkLookupTable, vtkProperty,
    vtkActor
)

from utils.window_renderer import WindowRenderer


class ColorVisualizer:

    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__reader = vtkStructuredGridReader()
        self.__mapper = vtkDataSetMapper()
        self.__lookup_table = vtkLookupTable()
        self.__property = vtkProperty()
        self.__actor = vtkActor()

    def setup(self, file_name, scalar_range):
        """Setup the scalar visualizer"""

        # Set reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()

        # Set lookup table
        self.__setup_lookup_table(1000, (0.0, 10.0))

        # Set mapper
        self.__mapper.SetInputConnection(self.__reader.GetOutputPort())
        self.__mapper.SetLookupTable(self.__lookup_table)
        self.__mapper.SetScalarRange(scalar_range)
        self.__mapper.ScalarVisibilityOn()
        self.__mapper.Update()

        # Set actor
        self.__actor.SetMapper(self.__mapper)

        # Add actor to the window renderer
        self.__renderer.AddActor(self.__actor)

    def __setup_lookup_table(self, number_of_colors, hue_range):
        self.__lookup_table.SetNumberOfColors(number_of_colors)
        self.__lookup_table.SetHueRange(hue_range)
        self.__lookup_table.SetSaturationRange(1.0, 0.0)
        self.__lookup_table.SetValueRange(1.0, 0.0)
        self.__lookup_table.SetAlphaRange(1.0, 0.0)
        self.__lookup_table.SetRange(0.0, 1.0)
        self.__lookup_table.Build()


# Run the program
if __name__ == '__main__':
    __window_renderer = WindowRenderer()

    ColorVisualizer(__window_renderer.renderer).setup("objects/density.vtk", (0.0, 1.0))

    __window_renderer.setup_render_window((0.0, 0.0, 100.0))
    __window_renderer.start_render_window()
