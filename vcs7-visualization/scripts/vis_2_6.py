from vtkmodules.all import (
    vtkNamedColors,
)
from utils.window import Window
from vis_2_2 import create_vtk_poly_data_visualizer


# Execute only if run as a script
if __name__ == '__main__':
    window = Window()
    colors = vtkNamedColors()

    create_vtk_poly_data_visualizer(window.renderer, "../resources/vtk/frog/blood.vtk", colors.GetColor3d("salmon"))
    create_vtk_poly_data_visualizer(window.renderer, "../resources/vtk/frog/brain.vtk", colors.GetColor3d("beige"))
    create_vtk_poly_data_visualizer(window.renderer, "../resources/vtk/frog/duodenum.vtk", colors.GetColor3d("orange"))
    create_vtk_poly_data_visualizer(window.renderer, "../resources/vtk/frog/eye_retina.vtk", colors.GetColor3d("misty_rose"))
    create_vtk_poly_data_visualizer(window.renderer, "../resources/vtk/frog/eye_white.vtk", colors.GetColor3d("white"))
    create_vtk_poly_data_visualizer(window.renderer, "../resources/vtk/frog/heart.vtk", colors.GetColor3d("tomato"))
    create_vtk_poly_data_visualizer(window.renderer, "../resources/vtk/frog/ileum.vtk", colors.GetColor3d("raspberry"))
    create_vtk_poly_data_visualizer(window.renderer, "../resources/vtk/frog/kidney.vtk", colors.GetColor3d("banana"))
    create_vtk_poly_data_visualizer(window.renderer, "../resources/vtk/frog/large_intestine.vtk", colors.GetColor3d("peru"))
    create_vtk_poly_data_visualizer(window.renderer, "../resources/vtk/frog/liver.vtk", colors.GetColor3d("pink"))
    create_vtk_poly_data_visualizer(window.renderer, "../resources/vtk/frog/lungs.vtk", colors.GetColor3d("powder_blue"))
    create_vtk_poly_data_visualizer(window.renderer, "../resources/vtk/frog/nerves.vtk", colors.GetColor3d("carrot"))
    create_vtk_poly_data_visualizer(window.renderer, "../resources/vtk/frog/skeleton.vtk", colors.GetColor3d("wheat"))
    create_vtk_poly_data_visualizer(
        window.renderer,
        "../resources/vtk/frog/skin.vtk",
        color=colors.GetColor3d("green"),
        opacity=0.25,
        rotation=(180.0, 0.0, 0.0, 1.0)
    )
    create_vtk_poly_data_visualizer(window.renderer, "../resources/vtk/frog/spleen.vtk", color=colors.GetColor3d("violet"))
    create_vtk_poly_data_visualizer(window.renderer, "../resources/vtk/frog/stomach.vtk", color=colors.GetColor3d("plum"))

    window.create((0.0, 0.0, 750.0))
