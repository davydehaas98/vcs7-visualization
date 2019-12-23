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
        self.__reader_transform = vtkTransform()
        self.__reader_transform_filter = vtkTransformPolyDataFilter()
        self.__reader_property = vtkProperty()
        self.__reader_mapper = vtkPolyDataMapper()
        self.__reader_actor = vtkActor()

    def setup(self, file_name):
        """Setup the object reader"""

        # Set reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()

        # Set reader transform
        self.__reader_transform.RotateWXYZ(0.0, 0.0, 0.0, 0.0)
        self.__reader_transform.Translate(0.0, 0.0, 0.0)

        # Set reader transform filter
        self.__reader_transform_filter.SetInputConnection(self.__reader.GetOutputPort())
        self.__reader_transform_filter.SetTransform(self.__reader_transform)
        self.__reader_transform_filter.Update()

        # Set reader property
        self.__reader_property.SetColor(1.0, 0.0, 0.0)

        # Set mapper
        self.__reader_mapper.SetInputConnection(self.__reader_transform_filter.GetOutputPort())

        # Set actor
        self.__reader_actor.SetProperty(self.__reader_property)
        self.__reader_actor.SetMapper(self.__reader_mapper)

        # Add actor to the window renderer
        self.__renderer.AddActor(self.__reader_actor)


# Run the program
if __name__ == '__main__':
    window_renderer = WindowRenderer()

    ObjectReader(window_renderer.renderer).setup("objects/cactus.obj")

    window_renderer.setup_render_window()
    window_renderer.start_render_window()
