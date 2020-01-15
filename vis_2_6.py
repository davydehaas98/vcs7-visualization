from vtkmodules.all import (
    vtkNamedColors,
)
from utils.window import Window
from vis_2_2 import vtk_poly_data_visualizer


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()
    colors = vtkNamedColors()

    vtk_poly_data_visualizer(window.renderer, "objects/vtk/frog/blood.vtk", color=colors.GetColor3d("salmon"))
    vtk_poly_data_visualizer(window.renderer, "objects/vtk/frog/brain.vtk", color=colors.GetColor3d("beige"))
    vtk_poly_data_visualizer(window.renderer, "objects/vtk/frog/duodenum.vtk", color=colors.GetColor3d("orange"))
    vtk_poly_data_visualizer(window.renderer, "objects/vtk/frog/eye_retina.vtk", color=colors.GetColor3d("misty_rose"))
    vtk_poly_data_visualizer(window.renderer, "objects/vtk/frog/eye_white.vtk", color=colors.GetColor3d("white"))
    vtk_poly_data_visualizer(window.renderer, "objects/vtk/frog/heart.vtk", color=colors.GetColor3d("tomato"))
    vtk_poly_data_visualizer(window.renderer, "objects/vtk/frog/ileum.vtk", color=colors.GetColor3d("raspberry"))
    vtk_poly_data_visualizer(window.renderer, "objects/vtk/frog/kidney.vtk", color=colors.GetColor3d("banana"))
    vtk_poly_data_visualizer(window.renderer, "objects/vtk/frog/large_intestine.vtk", color=colors.GetColor3d("peru"))
    vtk_poly_data_visualizer(window.renderer, "objects/vtk/frog/liver.vtk", color=colors.GetColor3d("pink"))
    vtk_poly_data_visualizer(window.renderer, "objects/vtk/frog/lungs.vtk", color=colors.GetColor3d("powder_blue"))
    vtk_poly_data_visualizer(window.renderer, "objects/vtk/frog/nerves.vtk", color=colors.GetColor3d("carrot"))
    vtk_poly_data_visualizer(window.renderer, "objects/vtk/frog/skeleton.vtk", color=colors.GetColor3d("wheat"))
    vtk_poly_data_visualizer(
        window.renderer,
        "objects/vtk/frog/skin.vtk",
        color=colors.GetColor3d("green"),
        opacity=0.25,
        rotation=(180.0, 0.0, 0.0, 1.0)
    )
    vtk_poly_data_visualizer(window.renderer, "objects/vtk/frog/spleen.vtk", color=colors.GetColor3d("violet"))
    vtk_poly_data_visualizer(window.renderer, "objects/vtk/frog/stomach.vtk", color=colors.GetColor3d("plum"))

    window.setup((0.0, 0.0, 750.0))
