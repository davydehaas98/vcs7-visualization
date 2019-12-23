from vtkmodules.all import (
    vtkSLCReader, vtkExtractVOI,
    vtkContourFilter, vtkPolyDataMapper,
    vtkProperty, vtkActor,
    vtkOutlineFilter,
)

from utils.window_renderer import WindowRenderer


class SLCReader:

    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__reader = vtkSLCReader()
        self.__extract_voi = vtkExtractVOI()

        self.__contour_filter = vtkContourFilter()
        self.__mapper = vtkPolyDataMapper()
        self.__property = vtkProperty()
        self.__actor = vtkActor()

        self.__outline_filter = vtkOutlineFilter()
        self.__outline_mapper = vtkPolyDataMapper()
        self.__outline_property = vtkProperty()
        self.__outline_actor = vtkActor()

    def setup(self, file_name, sample_rate):
        """Setup the SLC reader"""

        # Set reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()

        # Extract volume of interest to subsample the data for faster rendering
        self.__extract_voi.SetInputConnection(self.__reader.GetOutputPort())
        self.__extract_voi.SetSampleRate(sample_rate, 1, 1)

        # Set contour filter
        self.__contour_filter.SetInputConnection(self.__extract_voi.GetOutputPort())
        self.__contour_filter.SetValue(0, 80.0)

        # Set mapper
        self.__mapper.SetInputConnection(self.__contour_filter.GetOutputPort())
        self.__mapper.ScalarVisibilityOff()

        # Set property
        self.__property.SetColor(1.0, 1.0, 1.0)

        # Set actor
        self.__actor.SetMapper(self.__mapper)
        self.__actor.SetProperty(self.__property)

        # Set outline filter
        self.__outline_filter.SetInputConnection(self.__extract_voi.GetOutputPort())

        # Set outline mapper
        self.__outline_mapper.SetInputConnection(self.__outline_filter.GetOutputPort())

        # Set property
        self.__outline_property.SetColor(0.2, 0.2, 0.2)

        # Set outline actor
        self.__outline_actor.SetMapper(self.__outline_mapper)
        self.__outline_actor.SetProperty(self.__outline_property)

        # Add actor to the window renderer
        self.__renderer.AddActor(self.__actor)
        self.__renderer.AddActor(self.__outline_actor)


# Run the program
if __name__ == '__main__':
    window_renderer = WindowRenderer()

    SLCReader(window_renderer.renderer).setup("objects/vw_knee.slc", 3)

    # The assignment states that you have to try a surface value of 0.0, but you can only enter integers
    SLCReader(window_renderer.renderer).setup("objects/neghip.slc", 2)

    window_renderer.setup_render_window((700.0, 0.0, 500.0))
    window_renderer.start_render_window()
