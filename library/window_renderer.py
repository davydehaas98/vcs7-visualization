from vtkmodules.all import (
    vtkRenderer,
    vtkCamera, vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkInteractorStyleTrackballCamera,
)


class WindowRenderer:

    def __init__(self):
        self.renderer = vtkRenderer()

        self.__camera = vtkCamera()
        self.__render_window = vtkRenderWindow()
        self.__render_window_interactor = vtkRenderWindowInteractor()
        self.__interactor_style_trackball_camera = vtkInteractorStyleTrackballCamera()

    def setup_render_window(self):
        """Setup the render window"""

        # Set camera
        self.__camera.SetPosition(0.0, 0.0, 20.0)
        self.__camera.SetFocalPoint(0.0, 0.0, 0.0)

        # Set renderer
        self.renderer.SetActiveCamera(self.__camera)
        self.renderer.SetBackground(0.0, 0.0, 1.0)

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
