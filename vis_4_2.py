from vtkmodules.all import (
    vtkVolume16Reader, vtkContourFilter,
    vtkPolyDataMapper, vtkProperty,
    vtkActor,
)
from utils.window import Window


def contour_filter_mapper(reader, contour_value) -> vtkPolyDataMapper:

    # Set contour filter
    contour_filter = vtkContourFilter()
    contour_filter.SetInputConnection(reader.GetOutputPort())
    contour_filter.SetValue(1, contour_value)

    # Set mapper
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(contour_filter.GetOutputPort())
    mapper.ScalarVisibilityOff()

    return mapper


def ct_scan_visualizer(renderer, file_prefix):
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
    bone_mapper = contour_filter_mapper(reader, 1150)

    # Set bone properties
    bone_properties = vtkProperty()
    bone_properties.SetColor(0.8, 0.8, 0.8)

    # Set actor
    bone_actor = vtkActor()
    bone_actor.SetMapper(bone_mapper)
    bone_actor.SetProperty(bone_properties)

    # Add bone actor to the renderer
    renderer.AddActor(bone_actor)

    # Set skin mapper with contour filter
    skin_mapper = contour_filter_mapper(reader, 500)

    # Set skin properties
    skin_properties = vtkProperty()
    skin_properties.SetColor(0.7, 0.6, 0.4)
    skin_properties.SetDiffuseColor(0.5, 0.5, 0.5)
    skin_properties.SetSpecular(0.5)
    skin_properties.SetOpacity(0.6)

    # Set skin actor
    skin_actor = vtkActor()
    skin_actor.SetMapper(skin_mapper)
    skin_actor.SetProperty(skin_properties)

    # Add skin actor to renderer
    renderer.AddActor(skin_actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    # The original 2D sliced dataset was 256² pixels, but are again sliced to 64² pixels
    # That is why the files are called quarter
    ct_scan_visualizer(window.renderer, "files/headsq/quarter")

    window.setup((200.0, 500.0, 750.0))
