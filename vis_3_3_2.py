from vtkmodules.all import (
    vtkStructuredGridReader, vtkPlane,
    vtkSphere, vtkClipDataSet,
    vtkDataSetMapper, vtkActor,
)

from utils.window import Window


def create_clipper_visualizer(renderer, file_name, sphere):
    """Create cutting visualizer"""

    # Initialize variables
    reader = vtkStructuredGridReader()
    clip_data_set = vtkClipDataSet()
    mapper = vtkDataSetMapper()
    actor = vtkActor()

    # Set reader
    reader.SetFileName(file_name)
    reader.Update()

    # Set sphere or plane
    if sphere:
        clip_function = create_sphere_clip_function(reader)
    else:
        clip_function = create_plane_clip_function(reader)

    # Set cutter
    clip_data_set.SetClipFunction(clip_function)
    clip_data_set.SetInputConnection(reader.GetOutputPort())
    clip_data_set.Update()

    # Set mapper
    mapper.SetInputConnection(clip_data_set.GetOutputPort())

    # Set actor
    actor.SetMapper(mapper)

    # Add actor to the window renderer
    renderer.AddActor(actor)


def create_plane_clip_function(reader) -> vtkPlane:
    # To use the vtkClipDataSet().SetClipFunction we have to use implicit vtkPlane
    # instead of PolyDataAlgorithm object vtkPlaneSource
    plane = vtkPlane()
    plane.SetOrigin(reader.GetOutput().GetCenter())
    plane.SetNormal(1.0, 1.0, 0.0)

    return plane


def create_sphere_clip_function(reader) -> vtkSphere:
    # To use the vtkClipDataSet().SetClipFunction we have to use implicit vtkSphere
    # instead of PolyDataAlgorithm object vtkSphereSource
    sphere = vtkSphere()
    sphere.SetCenter(reader.GetOutput().GetCenter())

    return sphere


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    # Clipping with a plane
    create_clipper_visualizer(window.renderer, "files/vtk/density.vtk", False)

    # Clipping with a sphere
    #create_clipper_visualizer(window.renderer, "files/density.vtk", True)

    window.create((0.0, 0.0, 200.0))