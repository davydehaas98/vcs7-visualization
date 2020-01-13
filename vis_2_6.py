from vtkmodules.all import (
    vtkNamedColors,
)
from utils.window import Window
from vis_2_2 import VTKPolyDataVisualizer

if __name__ == '__main__':
    __window = Window()
    __colors = vtkNamedColors()

    VTKPolyDataVisualizer(__window.renderer).setup("objects/frog/blood.vtk", color=__colors.GetColor3d("salmon"))
    VTKPolyDataVisualizer(__window.renderer).setup("objects/frog/brain.vtk", color=__colors.GetColor3d("beige"))
    VTKPolyDataVisualizer(__window.renderer).setup("objects/frog/duodenum.vtk", color=__colors.GetColor3d("orange"))
    VTKPolyDataVisualizer(__window.renderer).setup("objects/frog/eye_retina.vtk", color=__colors.GetColor3d("misty_rose"))
    VTKPolyDataVisualizer(__window.renderer).setup("objects/frog/eye_white.vtk", color=__colors.GetColor3d("white"))
    VTKPolyDataVisualizer(__window.renderer).setup("objects/frog/heart.vtk", color=__colors.GetColor3d("tomato"))
    VTKPolyDataVisualizer(__window.renderer).setup("objects/frog/ileum.vtk", color=__colors.GetColor3d("raspberry"))
    VTKPolyDataVisualizer(__window.renderer).setup("objects/frog/kidney.vtk", color=__colors.GetColor3d("banana"))
    VTKPolyDataVisualizer(__window.renderer).setup("objects/frog/large_intestine.vtk", color=__colors.GetColor3d("peru"))
    VTKPolyDataVisualizer(__window.renderer).setup("objects/frog/liver.vtk", color=__colors.GetColor3d("pink"))
    VTKPolyDataVisualizer(__window.renderer).setup("objects/frog/lungs.vtk", color=__colors.GetColor3d("powder_blue"))
    VTKPolyDataVisualizer(__window.renderer).setup("objects/frog/nerves.vtk", color=__colors.GetColor3d("carrot"))
    VTKPolyDataVisualizer(__window.renderer).setup("objects/frog/skeleton.vtk", color=__colors.GetColor3d("wheat"))
    VTKPolyDataVisualizer(__window.renderer).setup(
        "objects/frog/skin.vtk",
        color=__colors.GetColor3d("green"),
        opacity=0.4,
        rotation=(180.0, 0.0, 0.0, 1.0)
    )
    VTKPolyDataVisualizer(__window.renderer).setup("objects/frog/spleen.vtk", color=__colors.GetColor3d("violet"))
    VTKPolyDataVisualizer(__window.renderer).setup("objects/frog/stomach.vtk", color=__colors.GetColor3d("plum"))

    __window.setup((0.0, 0.0, 750.0))
