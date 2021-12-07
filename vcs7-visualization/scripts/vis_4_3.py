from vtkmodules.all import (
    vtkSLCReader, vtkExtractVOI,
    vtkClipPolyData, vtkSphere, vtkPolyDataMapper,
    vtkProperty, vtkActor,
    vtkNamedColors,
)
from utils.window import Window
from vis_4_2 import create_contour_filter


def create_knee_visualizer(renderer, contour_value, opacity, color):
    """Visualize the vw_knee.slc"""

    # Set reader
    reader = vtkSLCReader()
    reader.SetFileName("resources/slc/vw_knee.slc")

    # Set extract volume of interest
    voi_extractor = vtkExtractVOI()
    voi_extractor.SetInputConnection(reader.GetOutputPort())
    voi_extractor.SetSampleRate(3, 1, 1)

    # Set contour filter
    contour_filter = create_contour_filter(voi_extractor, contour_value)

    # Set sphere clipper
    sphere_clipper = create_sphere_clipper(contour_filter, 100, (25.0, 25.0, 25.0))

    # Set mapper
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(sphere_clipper.GetOutputPort())
    mapper.ScalarVisibilityOff()

    # Set properties
    properties = vtkProperty()
    properties.SetColor(color)
    properties.SetOpacity(opacity)

    # Set backface properties
    backface_properties = vtkProperty()
    backface_properties.SetColor(color)
    backface_properties.SetOpacity(0.1)

    # Set actor
    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.SetProperty(properties)
    actor.SetBackfaceProperty(backface_properties)

    # Add actor to renderer
    renderer.AddActor(actor)


def create_sphere_clipper(input, radius, center) -> vtkClipPolyData:

    # Set sphere for in the clipper
    sphere = vtkSphere()
    sphere.SetRadius(radius)
    sphere.SetCenter(center)

    # Set clipper
    clipper = vtkClipPolyData()
    clipper.SetGenerateClipScalars(0)
    clipper.SetInputConnection(input.GetOutputPort())
    clipper.SetClipFunction(sphere)
    clipper.Update()

    return clipper


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()
    colors = vtkNamedColors()

    # Bone contour values are at 71 and above
    for c in range(71, 81):
        create_knee_visualizer(window.renderer, c, 1, colors.GetColor3d("wheat"))

    # Skin contour values are at 50 and below
    create_knee_visualizer(window.renderer, 40, 0.2, colors.GetColor3d("light_salmon"))
    create_knee_visualizer(window.renderer, 45, 0.3, colors.GetColor3d("light_salmon"))
    create_knee_visualizer(window.renderer, 50, 0.4, colors.GetColor3d("light_salmon"))

    window.create((200.0, 300.0, 800.0))