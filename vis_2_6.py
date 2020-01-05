from utils.window_renderer import WindowRenderer
from vis_2_2 import VTKPolyDataVisualizer


if __name__ == '__main__':
    __window_renderer = WindowRenderer()

    VTKPolyDataVisualizer(__window_renderer.renderer).setup("objects/frog/blood.vtk", (1.0, 0.0, 0.0))
    VTKPolyDataVisualizer(__window_renderer.renderer).setup("objects/frog/brain.vtk", (0.5, 0.0, 0.5))
    #VTKPolyDataVisualizer(__window_renderer.renderer).setup("objects/frog/brainbin.vtk", (0.0, 0.0, 0.0))
    VTKPolyDataVisualizer(__window_renderer.renderer).setup("objects/frog/duodenum.vtk", (1.0, 0.25, 0.25))
    VTKPolyDataVisualizer(__window_renderer.renderer).setup("objects/frog/eye_retina.vtk", (0.0, 1.0, 1.0))
    VTKPolyDataVisualizer(__window_renderer.renderer).setup("objects/frog/eye_white.vtk", (1.0, 1.0, 1.0))
    VTKPolyDataVisualizer(__window_renderer.renderer).setup("objects/frog/heart.vtk", (1.0, 0.0, 0.0))
    VTKPolyDataVisualizer(__window_renderer.renderer).setup("objects/frog/ileum.vtk", (1.0, 0.25, 0.25))
    VTKPolyDataVisualizer(__window_renderer.renderer).setup("objects/frog/kidney.vtk", (0.5, 0.25, 0.0))
    VTKPolyDataVisualizer(__window_renderer.renderer).setup("objects/frog/large_intestine.vtk", (0.5, 0.25, 0.0))
    VTKPolyDataVisualizer(__window_renderer.renderer).setup("objects/frog/liver.vtk", (0.5, 0.25, 0.0))
    VTKPolyDataVisualizer(__window_renderer.renderer).setup("objects/frog/lung.vtk", (1.0, 0.75, 0.75))
    VTKPolyDataVisualizer(__window_renderer.renderer).setup("objects/frog/nerves.vtk", (0.0, 1.0, 0.0))
    VTKPolyDataVisualizer(__window_renderer.renderer).setup("objects/frog/skeleton.vtk", (0.75, 0.75, 0.75))
    VTKPolyDataVisualizer(__window_renderer.renderer).setup("objects/frog/skin.vtk", (0.0, 0.5, 0.0))
    VTKPolyDataVisualizer(__window_renderer.renderer).setup("objects/frog/spleen.vtk", (0.0, 0.0, 1.0))
    VTKPolyDataVisualizer(__window_renderer.renderer).setup("objects/frog/stomach.vtk", (0.0, 0.0, 1.0))

    __window_renderer.setup_render_window((0.0, 0.0, 750.0))
    __window_renderer.start_render_window()