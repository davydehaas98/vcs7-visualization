from vtkmodules.all import (
    vtkStructuredPointsReader, vtkFixedPointVolumeRayCastMapper,
    vtkVolumeProperty, vtkVolume,
)
from utils.window import Window


def mip_volume_renderer(renderer, file_name):
    """Create Maximum Intensity Projection (MIP) volume renderer"""

    # Set reader
    reader = vtkStructuredPointsReader()
    reader.SetFileName(file_name)
    reader.Update()

    # Set fixed point volume ray cast mapper
    mapper = vtkFixedPointVolumeRayCastMapper()
    mapper.SetInputConnection(reader.GetOutputPort())
    mapper.SetBlendModeToMaximumIntensity()

    # Set properties
    properties = vtkVolumeProperty()
    properties.ShadeOn()
    properties.SetInterpolationTypeToLinear()

    # The volume holds the mapper and the property and
    # can be used to position and orientate the volume
    volume = vtkVolume()
    volume.SetMapper(mapper)
    volume.SetProperty(properties)

    # Add volume to the renderer
    renderer.AddVolume(volume)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    mip_volume_renderer(window.renderer, "files/vtk/torso.vtk")

    window.setup((0.0, 0.0, 100.0))