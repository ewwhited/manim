from manimlib.imports import *

class meme2(GraphScene):
    CONFIG = {
    "y_max" : 500,
    "y_min" : -500,
    "x_max" : 150,
    "x_min" : -150,
    "y_tick_frequency" : 125,
    "x_tick_frequency" : 25,
    "x_axis_width" : 10,
    "y_axis_height" : 6,
    "x_labeled_nums" : range(-150,151,50),
    "y_labeled_nums" : range(-500,501,250),
    "axes_color" : GRAY
    }
    def construct(self):
        self.graph_origin=0*LEFT+0*DOWN
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,x_min=-106.90455, x_max=-2.1, color=BLUE)
        func_graph_2=self.get_graph(self.func_to_graph_2,x_min=-106.90455, x_max=-2.1, color=BLUE)
        func_graph_3=self.get_graph(self.func_to_graph,x_min=0,x_max=105, color=BLUE)
        func_graph_4=self.get_graph(self.func_to_graph_2,x_min=0,x_max=105, color=BLUE)
        eqn=TextMobject("$y^2=x^3+109x^2+224x$")
        eqn.scale(0.75)
        eqn.shift(4*RIGHT+2.5*UP)
        self.play(ShowCreation(func_graph),ShowCreation(func_graph_2))
        self.play(ShowCreation(func_graph_3),ShowCreation(func_graph_4))
        self.play(Write(eqn))

        self.wait(5)
        point1=Dot(self.coords_to_point(-100,self.func_to_graph(-100)))
        p1label=TextMobject("$(-100,260)$")
        p1label.scale(0.55)
        p1label.next_to(point1,LEFT)
        self.add(point1)
        self.play(Write(p1label))
        self.wait(4)

    def func_to_graph(self,x):
        return(np.sqrt(x**3+109*x**2+224*x))
    def func_to_graph_2(self,x):
        return(-1*np.sqrt(x**3+109*x**2+224*x))
