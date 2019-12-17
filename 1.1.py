from vtkmodules.all import \
    vtkRenderWindow, vtkRenderer, vtkCamera, \
    vtkRenderWindowInteractor, vtkInteractorStyleTrackballCamera, \
    vtkConeSource, vtkPolyDataMapper, vtkActor


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


class Cone:

    def __init__(self, renderer):
        # Renderer variable is needed to add the cone actor
        self.__renderer = renderer
        
        self.__cone = vtkConeSource()
        self.__cone_mapper = vtkPolyDataMapper()
        self.__cone_actor = vtkActor()

    def setup_cone(self, position):
        """Setup the cone"""

        # Set cone properties
        self.__cone.SetRadius(1.0)
        self.__cone.SetHeight(2.0)
        self.__cone.SetResolution(50)
        self.__cone.SetCenter(position)

        # Set cone mapper
        self.__cone_mapper.SetInputConnection(self.__cone.GetOutputPort())

        # Set cone actor
        self.__cone_actor.SetMapper(self.__cone_mapper)
        self.__cone_actor.GetProperty().SetColor(1.0, 0.0, 0.0)

        # Add cone actor to the window renderer
        self.__renderer.AddActor(self.__cone_actor)


# Run the program
if __name__ == '__main__':
    window_renderer = WindowRenderer()
    Cone(window_renderer.renderer).setup_cone((2.0, 2.0, 2.0))
    Cone(window_renderer.renderer).setup_cone((0.0, 0.0, 0.0))

    window_renderer.setup_render_window()
    window_renderer.start_render_window()
