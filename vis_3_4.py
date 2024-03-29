from numpy import loadtxt
from utils.window import Window
from vtkmodules.util.numpy_support import numpy_to_vtk
from vtkmodules.all import (
    vtkUnstructuredGrid, vtkPoints,
    vtkArrowSource, vtkSphereSource,
    vtkGlyph3D, vtkPolyDataMapper,
    vtkActor,
)


def create_raw_data_visualizer(renderer, coordinates_text_file, vectors_text_file):
    """Create Raw data visualizer"""

    # Set unstructured grid
    unstructured_grid = create_unstructured_grid(coordinates_text_file, vectors_text_file)

    # Set sphere actor
    sphere_actor = create_sphere_actor(unstructured_grid)

    # Set arrow actor
    arrow_actor = create_arrow_actor(unstructured_grid)

    # Add actors to the window renderer
    renderer.AddActor(sphere_actor)
    renderer.AddActor(arrow_actor)


def create_unstructured_grid(coordinates_text_file, vectors_text_file) -> vtkUnstructuredGrid:
    """Read out .txt files with coordinates and vectors and create a vtkUnstructuredGrid object"""

    # Set points as vtkPoints from coordinates numpy array
    points = vtkPoints()
    points.SetData(numpy_to_vtk(loadtxt(fname=coordinates_text_file), deep=True))

    # Set vectors as vtkDoubleArray from vectors numpy array
    vectors = numpy_to_vtk(loadtxt(fname=vectors_text_file), deep=True)

    # Set unstructured grid
    unstructured_grid = vtkUnstructuredGrid()
    unstructured_grid.SetPoints(points)
    unstructured_grid.GetPointData().SetVectors(vectors)

    return unstructured_grid


def create_sphere_actor(unstructured_grid) -> vtkActor:
    """Create a sphere within a vtkActor"""

    # Set sphere
    sphere = vtkSphereSource()
    sphere.SetRadius(0.1)

    # Set sphere glyph 3D
    glyph = create_glyph_3d(unstructured_grid, sphere)

    # Set sphere mapper
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(glyph.GetOutputPort())

    # Set sphere actor
    actor = vtkActor()
    actor.SetMapper(mapper)

    return actor


def create_arrow_actor(unstructured_grid) -> vtkActor:
    """Create an arrow within a vtkActor"""

    # Set arrow
    arrow = vtkArrowSource()
    arrow.SetTipLength(0.4)
    arrow.SetTipRadius(0.2)
    arrow.SetTipResolution(50)

    # Set arrow glyph 3D
    glyph = create_glyph_3d(unstructured_grid, arrow)

    # Set arrow mapper
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(glyph.GetOutputPort())

    # Set arrow actor
    actor = vtkActor()
    actor.SetMapper(mapper)

    return actor


def create_glyph_3d(input_data, source) -> vtkGlyph3D:
    glyph = vtkGlyph3D()
    glyph.SetInputData(input_data)
    glyph.SetSourceConnection(source.GetOutputPort())
    glyph.SetVectorModeToUseVector()
    glyph.OrientOn()
    glyph.SetScaleFactor(0.2)

    return glyph


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    create_raw_data_visualizer(window.renderer, "files/txt/coordinates.txt", "files/txt/vectors.txt")

    window.create((0.0, 0.0, 5.0))