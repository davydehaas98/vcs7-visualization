from vtkmodules.all import (
    vtkStructuredGridReader, vtkPlane,
    vtkSphere, vtkClipDataSet,
    vtkDataSetMapper, vtkActor,
)

from utils.window import Window


class ClipperVisualizer:
    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__reader = vtkStructuredGridReader()
        self.__sphere = vtkSphere()
        self.__plane = vtkPlane()
        self.__clip = vtkClipDataSet()
        self.__mapper = vtkDataSetMapper()
        self.__actor = vtkActor()

    def setup(self, file_name, sphere):
        """Setup cutting visualizer"""

        # Set reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()

        # Set sphere
        if sphere:
            self.__sphere.SetCenter(self.__reader.GetOutput().GetCenter())
            self.__clip.SetClipFunction(self.__sphere)

        # Set plane
        else:
            self.__plane.SetOrigin(self.__reader.GetOutput().GetCenter())
            self.__plane.SetNormal(1.0, 1.0, 0.0)
            self.__clip.SetClipFunction(self.__plane)

        # Set cutter
        self.__clip.SetInputConnection(self.__reader.GetOutputPort())
        self.__clip.Update()

        # Set mapper
        self.__mapper.SetInputConnection(self.__clip.GetOutputPort())

        # Set actor
        self.__actor.SetMapper(self.__mapper)

        # Add actor to the window renderer
        self.__renderer.AddActor(self.__actor)


if __name__ == '__main__':
    __window = Window()

    # Clipping with a plane
    ClipperVisualizer(__window.renderer).setup("objects/density.vtk", False)

    # Clipping with a sphere
    ClipperVisualizer(__window.renderer).setup("objects/density.vtk", True)

    __window.setup((0.0, 0.0, 200.0))