from vtkmodules.all import (
    vtkOBJReader, vtkProperty,
    vtkTransform, vtkPolyDataMapper,
    vtkActor,
)

from utils.window_renderer import WindowRenderer


class ObjectReader:

    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__object_reader = vtkOBJReader()
        self.__object_reader_property = vtkProperty()
        self.__object_reader_transform = vtkTransform()
        self.__object_reader_mapper = vtkPolyDataMapper()
        self.__object_reader_actor = vtkActor()

    def setup_object_reader(self, file_name):
        """Setup the object reader"""

        # Set object reader
        self.__object_reader.SetFileName(file_name)

        # Set object reader property
        self.__object_reader_property.SetColor(1.0, 0.0, 0.0)

        # Set object reader transform
        self.__object_reader_transform.Translate(1.0, 0.0, 0.0)

        # Set object reader mapper
        self.__object_reader_mapper.SetInputConnection(self.__object_reader.GetOutputPort())

        # Set object reader actor
        self.__object_reader_actor.SetProperty(self.__object_reader_property)
        self.__object_reader_actor.SetMapper(self.__object_reader_mapper)

        # Add object reader actor to the window renderer
        self.__renderer.AddActor(self.__object_reader_actor)


# Run the program
if __name__ == '__main__':
    window_renderer = WindowRenderer()

    ObjectReader(window_renderer.renderer).setup_object_reader("objects/cactus.obj")

    window_renderer.setup_render_window()
    window_renderer.start_render_window()
