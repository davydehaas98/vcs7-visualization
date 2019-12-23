from vtkmodules.all import (
    vtkOBJReader, vtkProperty,
    vtkTransform, vtkTransformPolyDataFilter,
    vtkPolyDataMapper, vtkActor,
)

from utils.window_renderer import WindowRenderer


class ObjectReader:

    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__reader = vtkOBJReader()
        self.__transform = vtkTransform()
        self.__transform_filter = vtkTransformPolyDataFilter()
        self.__property = vtkProperty()
        self.__mapper = vtkPolyDataMapper()
        self.__actor = vtkActor()

    def setup(self, file_name):
        """Setup the object reader"""

        # Set reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()

        # Set transform
        self.__transform.RotateWXYZ(0.0, 0.0, 0.0, 0.0)
        self.__transform.Translate(0.0, 0.0, 0.0)

        # Set transform filter
        self.__transform_filter.SetInputConnection(self.__reader.GetOutputPort())
        self.__transform_filter.SetTransform(self.__transform)
        self.__transform_filter.Update()

        # Set mapper
        self.__mapper.SetInputConnection(self.__transform_filter.GetOutputPort())

        # Set property
        self.__property.SetColor(1.0, 0.0, 0.0)

        # Set actor
        self.__actor.SetMapper(self.__mapper)
        self.__actor.SetProperty(self.__property)

        # Add actor to the window renderer
        self.__renderer.AddActor(self.__actor)


# Run the program
if __name__ == '__main__':
    window_renderer = WindowRenderer()

    ObjectReader(window_renderer.renderer).setup("objects/cactus.obj")

    window_renderer.setup_render_window((0.0, 0.0, 2000.0))
    window_renderer.start_render_window()
