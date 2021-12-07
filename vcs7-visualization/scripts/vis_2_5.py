from vtkmodules.all import (
    vtkSLCReader, vtkExtractVOI,
    vtkContourFilter, vtkPolyDataMapper,
    vtkProperty, vtkActor,
    vtkOutlineFilter,
)

from utils.window import Window


def create_contour_actor(extract_voi) -> vtkActor:

    # Set contour filter
    contour_filter = vtkContourFilter()
    contour_filter.SetInputConnection(extract_voi.GetOutputPort())
    contour_filter.SetValue(0, 80.0)

    # Set contour mapper
    contour_mapper = vtkPolyDataMapper()
    contour_mapper.SetInputConnection(contour_filter.GetOutputPort())
    contour_mapper.ScalarVisibilityOff()

    # Set contour properties
    contour_properties = vtkProperty()
    contour_properties.SetColor(1.0, 1.0, 1.0)

    # Set contour actor
    contour_actor = vtkActor()
    contour_actor.SetMapper(contour_mapper)
    contour_actor.SetProperty(contour_properties)

    return contour_actor


def create_outline_actor(extract_voi) -> vtkActor:

    # Set outline filter
    outline_filter = vtkOutlineFilter()
    outline_filter.SetInputConnection(extract_voi.GetOutputPort())

    # Set outline mapper
    outline_mapper = vtkPolyDataMapper()
    outline_mapper.SetInputConnection(outline_filter.GetOutputPort())

    # Set outline properties
    outline_properties = vtkProperty()
    outline_properties.SetColor(0.2, 0.2, 0.2)

    # Set outline actor
    outline_actor = vtkActor()
    outline_actor.SetMapper(outline_mapper)
    outline_actor.SetProperty(outline_properties)

    return outline_actor


def create_slc_visualizer(renderer, file_name, sample_rate):
    """Create SLC visualizer with contour and outline"""

    # Set reader
    reader = vtkSLCReader()
    reader.SetFileName(file_name)

    # Extract volume of interest to subsample the data for faster rendering
    extract_voi = vtkExtractVOI()
    extract_voi.SetInputConnection(reader.GetOutputPort())
    extract_voi.SetSampleRate(sample_rate, 1, 1)

    # Set contour
    contour_actor = create_contour_actor(extract_voi)

    # set outline
    outline_actor = create_outline_actor(extract_voi)

    # Add actors to the window renderer
    renderer.AddActor(contour_actor)
    renderer.AddActor(outline_actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    create_slc_visualizer(window.renderer, "../resources/slc/vw_knee.slc", 3)

    # The assignment states that you have to try a surface value of 0.5,
    # but you can only enter integers higher than 0
    create_slc_visualizer(window.renderer, "../resources/slc/neghip.slc", 2)

    window.create((700.0, 0.0, 500.0))
