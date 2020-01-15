from vtkmodules.all import (
    vtkSLCReader, vtkExtractVOI,
    vtkContourFilter, vtkPolyDataMapper,
    vtkProperty, vtkActor,
    vtkOutlineFilter,
)

from utils.window import Window


def slc_visualizer(renderer, file_name, sample_rate):
    """Create SLC visualizer"""

    # Initialize variables
    reader = vtkSLCReader()
    extract_voi = vtkExtractVOI()

    contour_filter = vtkContourFilter()
    contour_mapper = vtkPolyDataMapper()
    contour_properties = vtkProperty()
    contour_actor = vtkActor()

    outline_filter = vtkOutlineFilter()
    outline_mapper = vtkPolyDataMapper()
    outline_properties = vtkProperty()
    outline_actor = vtkActor()

    # Set reader
    reader.SetFileName(file_name)
    reader.Update()

    # Extract volume of interest to subsample the data for faster rendering
    extract_voi.SetInputConnection(reader.GetOutputPort())
    extract_voi.SetSampleRate(sample_rate, 1, 1)

    # Set contour filter
    contour_filter.SetInputConnection(extract_voi.GetOutputPort())
    contour_filter.SetValue(0, 80.0)

    # Set contour mapper
    contour_mapper.SetInputConnection(contour_filter.GetOutputPort())
    contour_mapper.ScalarVisibilityOff()

    # Set contour properties
    contour_properties.SetColor(1.0, 1.0, 1.0)

    # Set contour actor
    contour_actor.SetMapper(contour_mapper)
    contour_actor.SetProperty(contour_properties)

    # Set outline filter
    outline_filter.SetInputConnection(extract_voi.GetOutputPort())

    # Set outline mapper
    outline_mapper.SetInputConnection(outline_filter.GetOutputPort())

    # Set outline properties
    outline_properties.SetColor(0.2, 0.2, 0.2)

    # Set outline actor
    outline_actor.SetMapper(outline_mapper)
    outline_actor.SetProperty(outline_properties)

    # Add actor to the window renderer
    renderer.AddActor(contour_actor)
    renderer.AddActor(outline_actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    slc_visualizer(window.renderer, "files/slc/vw_knee.slc", 3)

    # The assignment states that you have to try a surface value of 0.5,
    # but you can only enter integers higher than 0
    slc_visualizer(window.renderer, "files/slc/neghip.slc", 2)

    window.setup((700.0, 0.0, 500.0))
