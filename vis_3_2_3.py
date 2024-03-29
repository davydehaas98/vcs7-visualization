from vtkmodules.all import (
    vtkStructuredGridReader, vtkPointSource,
    vtkRungeKutta4, vtkStreamTracer,
    vtkPolyDataMapper, vtkActor,
)

from utils.window import Window


def create_streamline_visualizer(renderer, file_name):
    """Create streamline visualizer"""

    # Set reader
    reader = vtkStructuredGridReader()
    reader.SetFileName(file_name)
    reader.Update()

    # Set points
    points = vtkPointSource()
    points.SetRadius(3.0)
    points.SetCenter(reader.GetOutput().GetCenter())
    points.SetNumberOfPoints(100)

    # Set integrator
    integrator = vtkRungeKutta4()

    # Set stream tracer
    stream_tracer = vtkStreamTracer()
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
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(stream_tracer.GetOutputPort())

    # Set actor
    actor = vtkActor()
    actor.SetMapper(mapper)

    # Add actor to the window renderer
    renderer.AddActor(actor)


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()

    create_streamline_visualizer(window.renderer, "files/vtk/density.vtk")

    window.create((0.0, 0.0, 100.0))