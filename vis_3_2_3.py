from vtkmodules.all import (
    vtkStructuredGridReader, vtkPointSource,
    vtkRungeKutta4, vtkStreamTracer,
    vtkPolyDataMapper, vtkActor,
)

from utils.window import Window


def streamline_visualizer(renderer, file_name):
    """Create streamline visualizer"""

    # Initialize variables
    reader = vtkStructuredGridReader()
    points = vtkPointSource()
    integrator = vtkRungeKutta4()
    stream_tracer = vtkStreamTracer()
    mapper = vtkPolyDataMapper()
    actor = vtkActor()

    # Set reader
    reader.SetFileName(file_name)
    reader.Update()

    # Set points
    points.SetRadius(3.0)
    points.SetCenter(reader.GetOutput().GetCenter())
    points.SetNumberOfPoints(100)

    # Set stream tracer
    stream_tracer.SetInputConnection(reader.GetOutputPort())
    stream_tracer.SetSourceConnection(points.GetOutputPort())

    stream_tracer.SetMaximumPropagation(100)
    # SetMaximumPropagationUnitToTimeUnit method does not exist in vtk 8.2.0
    #stream_tracer.SetMaximumPropagationUnitToTimeUnit()

    stream_tracer.SetIntegrator(integrator)
    stream_tracer.SetInitialIntegrationStep(0.1)
    stream_tracer.SetIntegrationDirectionToBoth()
    # SetInitialIntegrationStepUnitToCellLengthUnit method does not exist in vtk 8.2.0
    #stream_tracer.SetInitialIntegrationStepUnitToCellLengthUnit()
    stream_tracer.Update()

    # Set mapper
    mapper.SetInputConnection(stream_tracer.GetOutputPort())

    # Set actor
    actor.SetMapper(mapper)

    # Add actor to the window renderer
    renderer.AddActor(actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    streamline_visualizer(window.renderer, "objects/density.vtk")

    window.setup((0.0, 0.0, 100.0))