from manimlib.imports import *
class PlotTwoGraphsAtOnce(GraphScene):
        CONFIG = {
            "y_max" : 10,
            "y_min" : -10,
            "x_max" : 10,
            "x_min" : -10,
            "y_tick_frequency" : 2,
            "x_tick_frequency" : 2,
            "x_axis_width": 5,
            "y_axis_height": 5,
            "axes_color" : GRAY,
        }
        def construct(self):
            self.graph_origin = -0.5 * DOWN + 3 * LEFT
            self.setup_axes(animate=True)
            graph_up = self.get_graph(lambda x : x**2,
                                        color = GOLD_A,
                                        x_min = 0,
                                        x_max = 3
                                        )
            f1 = TexMobject(r"f(x) = {x}^2", color = GOLD_A)
            f1.scale(0.7)
            label_coord1 = self.input_to_graph_point(3,graph_up)
            f1.next_to(label_coord1,RIGHT+UP)
            self.graph_origin = 3.5 * DOWN + 3 * LEFT
            self.setup_axes(animate=True)
            curve1 = ParametricFunction(
                lambda u : np.array([
                np.exp(0.30635*u)*np.cos(u),
                np.exp(0.30635*u)*np.sin(u),
                u
                ]), color=ORANGE, t_min=-2*PI, t_max=2*PI
            )
            graph_down = self.add(curve1)
            #graphs=VGroup(graph_up,graph_down)
            f2 = TexMobject(r"f(x) = {x}^3", color = BLUE_D)
            f2.scale(0.7)
            label_coord2 = self.input_to_graph_point(3,graph_up)
            f2.next_to(label_coord2,RIGHT+UP)
            self.play(
                ShowCreation(graph_up),
                ShowCreation(curve1),
                run_time = 2,
            )
            self.play(ShowCreation(f1), ShowCreation(f2))
            self.wait(3)
