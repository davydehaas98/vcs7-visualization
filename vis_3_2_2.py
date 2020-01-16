from vtkmodules.all import (
    vtkStructuredGridReader, vtkArrowSource,
    vtkGlyph3D, vtkPolyDataMapper,
    vtkActor,
)

from utils.window import Window


def create_glyph_visualizer(renderer, file_name):
    """Create glyph 3D visualizer"""

    # Initialize variables
    reader = vtkStructuredGridReader()
    arrow = vtkArrowSource()
    glyph = vtkGlyph3D()
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
    glyph.SetInputConnection(reader.GetOutputPort())
    glyph.SetSourceConnection(arrow.GetOutputPort())
    glyph.SetVectorModeToUseVector()
    glyph.SetColorModeToColorByScalar()

    # Uncomment one of the three methods below to set the scale mode
    glyph.SetScaleModeToDataScalingOff()
    #glyph.SetScaleModeToScaleByScalar()
    #glyph.SetScaleModeToScaleByVector()

    glyph.OrientOn()
    glyph.SetScaleFactor(0.2)

    # Set mapper
    mapper.SetInputConnection(glyph.GetOutputPort())

    # Set actor
    actor.SetMapper(mapper)

    # Add actor to the window renderer
    renderer.AddActor(actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    create_glyph_visualizer(window.renderer, "files/vtk/density.vtk")

    window.setup((0.0, 0.0, 300.0))