from vtkmodules.all import (
    vtkQuadric, vtkSampleFunction,
    vtkExtractVOI, vtkContourFilter,
    vtkPolyDataMapper, vtkActor,
)

from utils.window import Window


def create_extract_voi_visualizer(renderer):
    """Create volume of interest extractor visualizer"""

    # Initiate variables
    quadric = vtkQuadric()
    sample = vtkSampleFunction()
    extract_voi = vtkExtractVOI()
    contour_filter = vtkContourFilter()
    mapper = vtkPolyDataMapper()
    actor = vtkActor()

    # Set quadric
    quadric.SetCoefficients(0.5, 1.0, 0.2, 0.0, 0.1, 0.0, 0.0, 0.2, 0.0, 0.0)

    # Set sample
    sample.SetSampleDimensions(30, 30, 30)
    sample.SetImplicitFunction(quadric)
    sample.ComputeNormalsOff()

    # Set extract volume of interest
    extract_voi.SetInputConnection(sample.GetOutputPort())
    extract_voi.SetVOI(0, 29, 0, 29, 15, 15)
    extract_voi.SetSampleRate(1, 2, 3)

    # Set contour filter
    contour_filter.SetInputConnection(extract_voi.GetOutputPort())
    contour_filter.GenerateValues(13, 0.0, 1.2)

    # Set mapper
    mapper.SetInputConnection(contour_filter.GetOutputPort())
    mapper.SetScalarRange(0.0, 1.2)

    # Set actor
    actor.SetMapper(mapper)

    # Add actor to the window renderer
    renderer.AddActor(actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    create_extract_voi_visualizer(window.renderer)

    window.create((0.0, 0.0, 8.0))