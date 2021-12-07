from vtkmodules.all import (
    vtkTextSource, vtkPolyDataMapper,
    vtkActor,
)

from utils.window import Window


def create_text(renderer, text):
    """Create text"""

    # Set text
    source = vtkTextSource()
    source.SetText(text)
    source.SetForegroundColor(1.0, 0.0, 0.0)

    # Set mapper
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(source.GetOutputPort())

    # Set actor
    actor = vtkActor()
    actor.SetMapper(mapper)

    # Add actor to the window renderer
    renderer.AddActor(actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    create_text(window.renderer, "Hello World")

    window.create((0.0, 0.0, 500.0))
