from vtkmodules.all import (
    vtkPlaneSource, vtkBMPReader,
    vtkTexture, vtkPolyDataMapper,
    vtkActor,
)

from utils.window import Window


def create_texture_plane_visualizer(renderer, file_name):
    """Create texture plane"""

    # Set reader
    reader = vtkBMPReader()
    reader.SetFileName(file_name)

    # Set texture
    texture = vtkTexture()
    texture.SetInputConnection(reader.GetOutputPort())

    # Set plane
    plane = vtkPlaneSource()

    # Set mapper
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(plane.GetOutputPort())

    # Set actor
    actor = vtkActor()
    actor.SetTexture(texture)
    actor.SetMapper(mapper)

    # Add actor to the window renderer
    renderer.AddActor(actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    create_texture_plane_visualizer(window.renderer, "../resources/bmp/marbles.bmp")

    window.create((0.0, 0.0, 5.0))
