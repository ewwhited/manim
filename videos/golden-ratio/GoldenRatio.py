from manimlib.imports import *

class GoldenRatio(GraphScene):
    CONFIG = {
        "y_max" : 10,
        "y_min" : -10,
        "x_max" : 20,
        "x_min" : -20,
        "y_tick_frequency" : 2,
        "x_tick_frequency" : 2,
        "x_axis_width": 12,
        "y_axis_height": 6,
        "axes_color" : GRAY,
        }
    def construct(self):
        title1 = TextMobject("The")
        title2 = TextMobject("Golden")
        title3 = TextMobject("Ratio")
        title1.shift(3*UP+4*LEFT)
        title2.next_to(title1,DOWN)
        title3.next_to(title2,DOWN)
        title2.set_color(GOLD)
        title=VGroup(title1,title2,title3)
        self.play(Write(title))

        self.graph_origin = 0 * DOWN + 0 * LEFT
        self.setup_axes(animate=True)

        curve1 = ParametricFunction(
            lambda u : np.array([
            0.5*np.exp(0.30635*u)*np.cos(u),
            0.5*np.exp(0.30635*u)*np.sin(u),
            u
            ]), color=MAROON_D, t_min=-2*PI, t_max=2*PI
        )

        self.play(ShowCreation(curve1), run_time=2)

        time=TextMobject("$\\theta \\in [-\\tau , \\tau]$")
        time.scale(0.7)
        func=TextMobject("$r=\\varphi^{\\theta\\frac{2}{\\pi}}$")
        func.scale(0.7)
        func.shift(1*UP+1.5*RIGHT)
        time.next_to(func)
        legend=VGroup(func,time)
        self.play(Write(legend))
        self.wait(0.5)

        text1=TextMobject("$\\varphi = \\frac{1+\\sqrt{5}}{2} \\approx$")
        text1.shift(3*UP + 3.6*RIGHT)
        text2=TextMobject("1.618")
        text2.set_color(BLUE_C)
        text2.next_to(text1)
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(2)

        self.clear()

        head=TextMobject("\\textbf{Where do we get $\\varphi$?}")
        head.scale(1.25)
        head.to_edge(UP)
        self.play(Write(head))
        self.wait(.5)

        subhead=TextMobject("Consider the following infinite continued fraction:")
        subhead.next_to(head,DOWN)
        line1=TextMobject("Let $n = 1+\\cfrac{1}{1+\\cfrac{1}{1+\\cfrac{1}{1+\\cfrac{1}{1+\\cfrac{1}{1+\\cfrac{1}{1+\\cdots}}}}}}$")
        line1.next_to(subhead,DOWN)
        line1.shift(0.3*UP)
        line1.scale(0.67)
        rectangle=Rectangle(height=2.8,width=4.5,color=RED)
        rectangle.shift(0.36*DOWN+1*RIGHT)
        sideline=TextMobject("This is")
        sideline.next_to(rectangle)
        sideline.scale(0.8)
        sideline2=TextMobject("exactly $n$")
        sideline2.scale(0.8)
        sideline3=TextMobject("itself!")
        sideline3.scale(0.8)
        sideline2.next_to(sideline,DOWN)
        sideline3.next_to(sideline2,DOWN)
        sidelines=VGroup(sideline,sideline2,sideline3)
        botline1=TextMobject("This means we can simplify to $n = 1+\\frac{1}{n}$")
        botline1.shift(3*DOWN)

        self.play(Write(subhead),run_time=2)
        self.play(Write(line1),run_time=3.5)
        self.wait(3.5)
        self.play(ShowCreation(rectangle),run_time=2)
        self.play(Write(sidelines), run_time=1.5)
        self.wait(2)
        self.play(Write(botline1),run_time=2.5)
        self.wait(2)
        self.remove(rectangle)

        newline1=TextMobject("So, we consider $n = 1 + \\frac{1}{n}$")
        newline1.next_to(head,DOWN)
        grouping=VGroup(sidelines,line1,botline1,subhead)
        self.play(Transform(grouping,newline1), run_time=2)
        self.wait(2)

        solving1=TextMobject("$n = 1 + \\frac{1}{n}$")
        solving1.scale(1.5)
        solving1.next_to(newline1,DOWN)
        self.play(Write(solving1),run_time=1.5)

        solving2=TextMobject("$n^2=n+1$")
        solving2.scale(1.5)
        solving2.next_to(solving1,DOWN)
        self.play(Write(solving2),run_time=1.5)

        solving3=TextMobject("$n^2-n-1=0$")
        solving3.scale(1.5)
        solving3.next_to(solving2,DOWN)
        self.play(Write(solving3),run_time=1.5)

        solving4=TextMobject("$n=\\frac{1\\pm\\sqrt{1-(-4)}}{2}$")
        solving4.scale(1.5)
        solving4.next_to(solving3,DOWN)
        self.play(Write(solving4),run_time=1.5)

        solving5=TextMobject("$n=\\frac{1+\\sqrt{5}}{2}$")
        solving5.scale(1.5)
        solving5.next_to(solving4,DOWN)
        self.play(Write(solving5),run_time=1.5)
        addon=TextMobject("$=\\varphi$")
        addon.scale(1.5)
        addon.next_to(solving5)
        self.play(Write(addon),run_time=2)
        self.wait(3)
        self.clear()

        penult1=TextMobject("$\\varphi =$")
        penult1.set_color(GOLD)
        penult2=TextMobject("$\\frac{1+\\sqrt{5}}{2}$")
        penult1.scale(1.5)
        penult1.to_edge(UP)
        penult1.shift(2*DOWN+2.5*LEFT)
        penult2.scale(1.5)
        penult2.next_to(penult1)
        self.play(Write(penult1),run_time=1.5)
        self.play(Write(penult2),run_time=1.5)
        self.wait(3)
        finalline=TextMobject("$ 1+\\cfrac{1}{1+\\cfrac{1}{1+\\cfrac{1}{1+\\cfrac{1}{1+\\cfrac{1}{1+\\cfrac{1}{1+\\cdots}}}}}}$")
        finalline.scale(1.15)
        finalline.next_to(penult1)
        finalline.shift(2*DOWN)
        self.play(Transform(penult2,finalline),run_time=1.5)
        sig=TextMobject("\\textit{Evan Whited}")
        sig.scale(0.4)
        sig.to_edge(DOWN)
        sig.shift(6*LEFT)
        self.play(Write(sig))
        self.wait(3)
