from vtkmodules.all import (
    vtkStructuredGridReader, vtkArrowSource,
    vtkGlyph3D, vtkPolyDataMapper,
    vtkActor,
)

from utils.window import Window


class Glyph3DVisualizer:
    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__reader = vtkStructuredGridReader()
        self.__arrow = vtkArrowSource()
        self.__glyph_3d = vtkGlyph3D()
        self.__mapper = vtkPolyDataMapper()
        self.__actor = vtkActor()

    def setup(self, file_name):
        """Setup the glyph 3D visualizer"""

        # Set reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()

        # Set arrow
        self.__arrow.SetTipLength(0.25)
        self.__arrow.SetTipRadius(0.1)
        self.__arrow.SetTipResolution(10)

        # Set glyph 3D
        self.__glyph_3d.SetInputConnection(self.__reader.GetOutputPort())
        self.__glyph_3d.SetSourceConnection(self.__arrow.GetOutputPort())
        self.__glyph_3d.SetVectorModeToUseVector()
        self.__glyph_3d.SetColorModeToColorByScalar()

        # Uncomment one of the three methods below to set the scale mode
        self.__glyph_3d.SetScaleModeToDataScalingOff()
        #self.__glyph_3d.SetScaleModeToScaleByScalar()
        #self.__glyph_3d.SetScaleModeToScaleByVector()

        self.__glyph_3d.OrientOn()
        self.__glyph_3d.SetScaleFactor(0.2)

        # Set mapper
        self.__mapper.SetInputConnection(self.__glyph_3d.GetOutputPort())

        # Set actor
        self.__actor.SetMapper(self.__mapper)

        # Add actor to the window renderer
        self.__renderer.AddActor(self.__actor)

if __name__ == '__main__':
    __window = Window()

    Glyph3DVisualizer(__window.renderer).setup("objects/density.vtk")

    __window.setup((0.0, 0.0, 300.0))