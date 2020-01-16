from vtkmodules.all import (
    vtkPlaneSource, vtkBMPReader,
    vtkTexture, vtkPolyDataMapper,
    vtkActor,
)

from utils.window import Window


def create_texture_plane_visualizer(renderer, file_name):
    """Create texture plane"""

    # Initialize variables
    plane = vtkPlaneSource()
    reader = vtkBMPReader()
    texture = vtkTexture()
    mapper = vtkPolyDataMapper()
    actor = vtkActor()

    # Set reader
    reader.SetFileName(file_name)
    reader.Update()

    # Set texture
    texture.SetInputConnection(reader.GetOutputPort())

    # Set mapper
    mapper.SetInputConnection(plane.GetOutputPort())

    # Set actor
    actor.SetTexture(texture)
    actor.SetMapper(mapper)

    # Add actor to the window renderer
    renderer.AddActor(actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    create_texture_plane_visualizer(window.renderer, "files/bmp/marbles.bmp")

    window.create((0.0, 0.0, 5.0))
