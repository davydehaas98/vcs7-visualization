from vtkmodules.all import (
    vtkQuadric, vtkSampleFunction,
    vtkExtractVOI, vtkContourFilter,
    vtkPolyDataMapper, vtkActor,
)

from utils.window import Window


class ExtractVOIVisualizer:
    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__quadric = vtkQuadric()
        self.__sample = vtkSampleFunction()
        self.__extract_voi = vtkExtractVOI()
        self.__contour_filter = vtkContourFilter()
        self.__mapper = vtkPolyDataMapper()
        self.__actor = vtkActor()

    def setup(self):
        """Setup volume of interest extractor visualizer"""

        # Set quadric
        self.__quadric.SetCoefficients(0.5, 1.0, 0.2, 0.0, 0.1, 0.0, 0.0, 0.2, 0.0, 0.0)

        # Set sample
        self.__sample.SetSampleDimensions(30, 30, 30)
        self.__sample.SetImplicitFunction(self.__quadric)
        self.__sample.ComputeNormalsOff()

        # Set extract volume of interest
        self.__extract_voi.SetInputConnection(self.__sample.GetOutputPort())
        self.__extract_voi.SetVOI(0, 29, 0, 29, 15, 15)
        self.__extract_voi.SetSampleRate(1, 2, 3)

        # Set contour filter
        self.__contour_filter.SetInputConnection(self.__extract_voi.GetOutputPort())
        self.__contour_filter.GenerateValues(13, 0.0, 1.2)

        # Set mapper
        self.__mapper.SetInputConnection(self.__contour_filter.GetOutputPort())
        self.__mapper.SetScalarRange(0.0, 1.2)

        # Set actor
        self.__actor.SetMapper(self.__mapper)

        # Add actor to the window renderer
        self.__renderer.AddActor(self.__actor)


if __name__ == '__main__':
    __window = Window()

    ExtractVOIVisualizer(__window.renderer).setup()

    __window.setup((0.0, 0.0, 300.0))