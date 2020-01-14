from vtkmodules.all import (
    vtkStructuredGridReader, vtkPointSource,
    vtkRungeKutta4, vtkStreamTracer,
    vtkPolyDataMapper, vtkActor,
)

from utils.window import Window


class StreamlineVisualizer:
    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__reader = vtkStructuredGridReader()
        self.__points = vtkPointSource()
        self.__integrator = vtkRungeKutta4()
        self.__stream_tracer = vtkStreamTracer()
        self.__mapper = vtkPolyDataMapper()
        self.__actor = vtkActor()

    def setup(self, file_name):
        """Setup streamline visualizer"""

        # Set reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()

        # Set points
        self.__points.SetRadius(3.0)
        self.__points.SetCenter(self.__reader.GetOutput().GetCenter())
        self.__points.SetNumberOfPoints(100)

        # Set stream tracer
        self.__stream_tracer.SetInputConnection(self.__reader.GetOutputPort())
        self.__stream_tracer.SetSourceConnection(self.__points.GetOutputPort())

        self.__stream_tracer.SetMaximumPropagation(100)
        # SetMaximumPropagationUnitToTimeUnit method does not exist in vtk 8.2.0
        #self.__stream_tracer.SetMaximumPropagationUnitToTimeUnit()

        self.__stream_tracer.SetIntegrator(self.__integrator)
        self.__stream_tracer.SetInitialIntegrationStep(0.1)
        self.__stream_tracer.SetIntegrationDirectionToBoth()
        # SetInitialIntegrationStepUnitToCellLengthUnit method does not exist in vtk 8.2.0
        #self.__stream_tracer.SetInitialIntegrationStepUnitToCellLengthUnit()
        self.__stream_tracer.Update()

        # Set mapper
        self.__mapper.SetInputConnection(self.__stream_tracer.GetOutputPort())

        # Set actor
        self.__actor.SetMapper(self.__mapper)

        # Add actor to the window renderer
        self.__renderer.AddActor(self.__actor)

if __name__ == '__main__':
    __window = Window()

    StreamlineVisualizer(__window.renderer).setup("objects/density.vtk")

    __window.setup((0.0, 0.0, 100.0))