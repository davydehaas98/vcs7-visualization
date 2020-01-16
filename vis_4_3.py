from vtkmodules.all import (
    vtkSLCReader, vtkExtractVOI,
    vtkContourFilter, vtkPolyDataMapper,
    vtkProperty, vtkActor,
)
from utils.window import Window
from vis_4_2 import contour_filter_mapper


def create_knee_visualizer(renderer, file_name):
    """Visualize the vw_knee.slc"""

    # Set reader
    reader = vtkSLCReader()
    reader.SetFileName(file_name)

    # Set extract volume of interest
    extract_voi = vtkExtractVOI()
    extract_voi.SetInputConnection(reader.GetOutputPort())
    extract_voi.SetSampleRate(2, 1, 1)

    # Set skin mapper with contour filter
    skin_mapper = contour_filter_mapper(extract_voi, 50)

    # Set skin properties
    skin_properties = vtkProperty()
    skin_properties.SetColor(0.9, 0.8, 0.8)
    skin_properties.SetOpacity(0.5)

    # Set skin actor
    skin_actor = vtkActor()
    skin_actor.SetMapper(skin_mapper)
    skin_actor.SetProperty(skin_properties)

    # Add skin actor to renderer
    renderer.AddActor(skin_actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    create_knee_visualizer(window.renderer, "files/slc/vw_knee.slc")

    window.setup((0.0, 0.0, 200.0))