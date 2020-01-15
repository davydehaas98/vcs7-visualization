from numpy import loadtxt
from vtkmodules.util.numpy_support import numpy_to_vtk
from vtkmodules.all import (
    vtkUnstructuredGrid, vtkPoints,
    vtkDoubleArray, vtkArrowSource,
    vtkSphereSource, vtkGlyph3D,
    vtkPolyDataMapper, vtkActor,
)

from utils.window import Window


class RawDataVisualizer:
    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__points = vtkPoints()
        self.__vectors = vtkDoubleArray()
        self.__unstructured_grid = vtkUnstructuredGrid()
        self.__arrow = vtkArrowSource()
        self.__sphere = vtkSphereSource()
        self.__sphere_glyph_3d = vtkGlyph3D()
        self.__arrow_glyph_3d = vtkGlyph3D()
        self.__sphere_mapper = vtkPolyDataMapper()
        self.__arrow_mapper = vtkPolyDataMapper()
        self.__sphere_actor = vtkActor()
        self.__arrow_actor = vtkActor()

    def setup(self, coordinates_text_file, vectors_text_file):
        """Setup Raw data visualizer"""

        # Set coordinates numpy array
        __coordinates = loadtxt(fname=coordinates_text_file)

        # Set points as vtkPoints from coordinates numpy array
        self.__points.SetData(numpy_to_vtk(__coordinates, deep=True))

        # Set values numpy array
        __values = loadtxt(fname=vectors_text_file)

        # Set vectors as vtkDoubleArray from values numpy array
        self.__vectors = numpy_to_vtk(__values, deep=True)

        # Set unstructured grid
        self.__unstructured_grid.SetPoints(self.__points)
        self.__unstructured_grid.GetPointData().SetVectors(self.__vectors)

        print(self.__points)
        print(self.__unstructured_grid)

        # Set sphere glyph 3D
        self.__sphere.SetRadius(0.1)
        self.__sphere_glyph_3d.SetSourceConnection(self.__sphere.GetOutputPort())
        self.__sphere_glyph_3d.SetVectorModeToUseVector()
        self.__sphere_glyph_3d.OrientOn()
        self.__sphere_glyph_3d.SetScaleFactor(0.2)

        # Set arrow glyph 3D
        self.__arrow.SetTipLength(5)
        self.__arrow.SetTipRadius(1)
        self.__arrow.SetTipResolution(10)
        self.__arrow_glyph_3d.SetSourceConnection(self.__arrow.GetOutputPort())
        self.__sphere_glyph_3d.SetVectorModeToUseVector()
        self.__sphere_glyph_3d.OrientOn()
        self.__sphere_glyph_3d.SetScaleFactor(0.2)

        # Set mapper
        self.__sphere_mapper.SetInputConnection(self.__sphere_glyph_3d.GetOutputPort())
        self.__arrow_mapper.SetInputConnection(self.__arrow_glyph_3d.GetOutputPort())

        # Set actor
        self.__sphere_actor.SetMapper(self.__sphere_mapper)
        self.__arrow_actor.SetMapper(self.__arrow_mapper)

        # Add actor to the window renderer
        self.__renderer.AddActor(self.__sphere_actor)
        self.__renderer.AddActor(self.__arrow_actor)


if __name__ == '__main__':
    __window = Window()

    RawDataVisualizer(__window.renderer).setup("objects/coordinates.txt", "objects/vectors.txt")

    __window.setup((0.0, 0.0, 300.0))