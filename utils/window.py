from vtkmodules.all import (
    vtkRenderer, vtkCamera,
    vtkLight, vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkInteractorStyleTrackballCamera,
)


def create_light(position) -> vtkLight:
    """Setup light"""

    # Set light
    light = vtkLight()
    light.SetColor(1.0, 1.0, 1.0)
    light.SetFocalPoint(0.0, 0.0, 0.0)
    light.SetPosition(position)
    light.PositionalOn()

    return light


def create_camera(position) -> vtkCamera:
    """Setup camera"""

    # Set camera
    camera = vtkCamera()
    camera.SetClippingRange(1.0, 2000.0)
    camera.SetFocalPoint(0.0, 0.0, 0.0)
    camera.SetPosition(position)
    camera.SetViewUp(1.0, 1.0, 1.0)
    camera.Zoom(1.0)

    # Divides the camera's distance from the focal point by the given dolly value
    camera.Dolly(1.0)
    camera.ComputeViewPlaneNormal()

    return camera


class Window:

    def __init__(self):
        self.renderer = vtkRenderer()

    def create(self, camera_position):
        """Setup the render window"""

        # Set camera
        camera = create_camera(camera_position)

        # Set light
        light = create_light(camera_position)

        # Set renderer
        self.renderer.SetActiveCamera(camera)
        #self.renderer.AddLight(light)
        self.renderer.SetBackground(0.9, 0.9, 0.9)

        # Set render window
        render_window = vtkRenderWindow()
        render_window.AddRenderer(self.renderer)
        render_window.SetSize(1000, 600)

        # Set render window interactor
        render_window_interactor = vtkRenderWindowInteractor()
        render_window_interactor.SetRenderWindow(render_window)
        render_window_interactor.SetInteractorStyle(vtkInteractorStyleTrackballCamera())
        render_window_interactor.Initialize()

        # Render the window and start the interactor
        render_window.Render()
        render_window_interactor.Start()
