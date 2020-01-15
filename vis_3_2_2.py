from vtkmodules.all import (
    vtkStructuredGridReader, vtkArrowSource,
    vtkGlyph3D, vtkPolyDataMapper,
    vtkActor,
)

from utils.window import Window


def glyph_3d_visualizer(renderer, file_name):
    """Create glyph 3D visualizer"""

    # Initialize variables
    reader = vtkStructuredGridReader()
    arrow = vtkArrowSource()
    glyph_3d = vtkGlyph3D()
    mapper = vtkPolyDataMapper()
    actor = vtkActor()

    # Set reader
    reader.SetFileName(file_name)
    reader.Update()

    # Set arrow
    arrow.SetTipLength(0.25)
    arrow.SetTipRadius(0.1)
    arrow.SetTipResolution(10)

    # Set glyph 3D
    glyph_3d.SetInputConnection(reader.GetOutputPort())
    glyph_3d.SetSourceConnection(arrow.GetOutputPort())
    glyph_3d.SetVectorModeToUseVector()
    glyph_3d.SetColorModeToColorByScalar()

    # Uncomment one of the three methods below to set the scale mode
    glyph_3d.SetScaleModeToDataScalingOff()
    #glyph_3d.SetScaleModeToScaleByScalar()
    #glyph_3d.SetScaleModeToScaleByVector()

    glyph_3d.OrientOn()
    glyph_3d.SetScaleFactor(0.2)

    # Set mapper
    mapper.SetInputConnection(glyph_3d.GetOutputPort())

    # Set actor
    actor.SetMapper(mapper)

    # Add actor to the window renderer
    renderer.AddActor(actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    glyph_3d_visualizer(window.renderer, "files/vtk/density.vtk")

    window.setup((0.0, 0.0, 300.0))