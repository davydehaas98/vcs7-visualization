from vtkmodules.all import (
    vtkRenderer, vtkCamera,
    vtkLight, vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkInteractorStyleTrackballCamera,
)


class WindowRenderer:

    def __init__(self):
        self.renderer = vtkRenderer()

        self.__camera = vtkCamera()
        self.__light = vtkLight()
        self.__render_window = vtkRenderWindow()
        self.__render_window_interactor = vtkRenderWindowInteractor()
        self.__interactor_style_trackball_camera = vtkInteractorStyleTrackballCamera()

    def setup_render_window(self, position):
        """Setup the render window"""

        # Set camera
        self.__camera.SetClippingRange(1.0, 2000.0)
        self.__camera.SetFocalPoint(0.0, 0.0, 0.0)
        self.__camera.SetPosition(position)
        self.__camera.SetViewUp(1.0, 1.0, 1.0)
        self.__camera.Zoom(1.0)
        # Divides the camera's distance from the focal point by the given dolly value
        self.__camera.Dolly(1.0)
        self.__camera.ComputeViewPlaneNormal()

        # Set light
        self.__light.SetColor(1.0, 1.0, 1.0)
        self.__light.SetFocalPoint(0.0, 0.0, 0.0)
        self.__light.SetPosition(position)
        self.__light.PositionalOn()

        # Set renderer
        self.renderer.SetActiveCamera(self.__camera)
        #self.renderer.AddLight(self.__light)
        self.renderer.SetBackground(0.5, 1.0, 1.0)

        # Set render window
        self.__render_window.AddRenderer(self.renderer)
        self.__render_window.SetSize(1000, 600)

        # Set render window interactor
        self.__render_window_interactor.SetRenderWindow(self.__render_window)
        self.__render_window_interactor.SetInteractorStyle(self.__interactor_style_trackball_camera)

    def start_render_window(self):
        """Start the render window"""

        # Initialize interactor
        self.__render_window_interactor.Initialize()

        # Start render window with interactor
        self.__render_window.Render()
        self.__render_window_interactor.Start()
