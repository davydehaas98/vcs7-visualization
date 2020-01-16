from vtkmodules.all import (
    vtkVolume16Reader, vtkContourFilter,
    vtkPolyDataMapper, vtkProperty,
    vtkActor, vtkNamedColors,
)
from utils.window import Window


def create_ct_scan_visualizer(renderer, file_prefix):
    """Visualize the CT scan"""

    # Set reader
    reader = vtkVolume16Reader()
    reader.SetFilePrefix(file_prefix)
    reader.SetDataDimensions(64, 64)
    reader.SetImageRange(1, 93)
    reader.SetDataByteOrderToLittleEndian()
    # DataSpacing is set to 3.2 mm per pixel because of changes to the resolution
    reader.SetDataSpacing(3.2, 3.2, 1.5)

    # Set bone mapper with contour filter
    bone_contour_filter = create_contour_filter(reader, 1150)

    # Set mapper
    bone_mapper = vtkPolyDataMapper()
    bone_mapper.SetInputConnection(bone_contour_filter.GetOutputPort())
    # Set scalar visibility off so we can color the result ourselves
    bone_mapper.ScalarVisibilityOff()

    # Set skin actor with properties
    bone_actor = create_bone_actor(bone_mapper)

    # Add bone actor to the renderer
    renderer.AddActor(bone_actor)

    # Set skin mapper with contour filter
    skin_contour_filter = create_contour_filter(reader, 500)

    # Set mapper
    skin_mapper = vtkPolyDataMapper()
    skin_mapper.SetInputConnection(skin_contour_filter.GetOutputPort())
    # Set scalar visibility off so we can color the result ourselves
    skin_mapper.ScalarVisibilityOff()

    # Set skin actor with properties
    skin_actor = create_skin_actor(skin_mapper)

    # Add skin actor to renderer
    renderer.AddActor(skin_actor)


def create_contour_filter(input, contour_value) -> vtkContourFilter:
    """Create isosurfaces and/or isolines from scalar values"""

    # Set contour filter
    contour_filter = vtkContourFilter()
    contour_filter.SetInputConnection(input.GetOutputPort())
    contour_filter.SetValue(0, contour_value)

    return contour_filter


def create_skin_actor(mapper) -> vtkActor:
    """Create an actor with properties for the skin"""

    # Set properties
    properties = vtkProperty()
    properties.SetColor(vtkNamedColors().GetColor3d("light_salmon"))
    properties.SetDiffuseColor(0.5, 0.5, 0.5)
    properties.SetSpecular(0.5)
    properties.SetOpacity(0.6)

    # Set actor
    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.SetProperty(properties)

    return actor


def create_bone_actor(mapper) -> vtkActor:
    """Create an actor with properties for the bone"""

    # Set properties
    properties = vtkProperty()
    properties.SetColor(vtkNamedColors().GetColor3d("wheat"))

    # Set actor
    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.SetProperty(properties)

    return actor


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    # The original 2D sliced dataset was 256² pixels, but are again sliced to 64² pixels
    # That is why the files are called quarter
    create_ct_scan_visualizer(window.renderer, "files/headsq/quarter")

    window.create((200.0, 500.0, 750.0))
