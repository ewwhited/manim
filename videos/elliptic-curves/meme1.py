from manimlib.imports import *

class meme1(Scene):
    def construct(self):
        title=TextMobject("Tackling the meme problem:")
        eq=TextMobject("$\\cfrac{a}{b+c}+\\cfrac{b}{a+c}+\\cfrac{c}{a+b}=4$")
        cond=TextMobject("$a,b,c\\in\\mathbb{Z}^+$")
        expand=TextMobject("$a(a+c)(a+b)+b(a+b)(b+c)+c(a+c)(b+c)=4(a+b)(b+c)(a+c)$")
        rearrange=TextMobject("$a^3+b^3+c^3-3a^2b-3ab^2-3a^2c-3b^2c-3bc^2-5abc=0$")
        transformx=TextMobject("$x=\\cfrac{-28a-28b-56c}{6a+6b-c}$")
        transformy=TextMobject("$y=\\cfrac{364a-364b}{6a+6b-c}$")
        transforma=TextMobject("$a=\\cfrac{56-x+y}{56-14x}$")
        transformb=TextMobject("$b=\\cfrac{56-x-y}{56-14x}$")
        transformc=TextMobject("$c=\\cfrac{-28-6x}{28-7x}$")
        transformed=TextMobject("\\mbox{$\\cfrac{12x^3}{49(x^3-12x^2+48x-64)}+\\cfrac{1417x^2}{49(x^3-12x^2+48x-64)}-\\cfrac{13y^2}{49(x^3-12x^2+48x-64)}+\\cfrac{416x}{7(x^3-12x^2+48x-64)}=0$}")
        transformedfactor1=TextMobject("$\\cfrac{49(x^3-12x^2+48x-64)}{13}($")
        transformedfactor2=TextMobject("$)$")
        reduced=TextMobject("$y^2=x^3+109x^2+224x$")
        badsolution=TextMobject("$a=4, b=-1, c=11$")

        title.to_edge(UP)
        eq.shift(1*UP)
        self.play(Write(title))
        self.play(Write(eq))
        cond.next_to(eq, DOWN)
        self.play(Write(cond))
        badsolution.set_color(RED_D)
        badsolution.next_to(cond,DOWN)
        self.wait(3)
        self.play(Write(badsolution))
        self.wait(3)
        self.play(FadeOut(eq),FadeOut(cond))

        self.play(ApplyMethod(badsolution.scale,0.6))
        self.play(ApplyMethod(badsolution.shift,3.2*UP+4.25*RIGHT))
        expand.scale(0.8)
        expand.shift(1*UP)
        self.play(Write(expand))
        self.wait(3)
        rearrange.shift(0.75*DOWN)
        self.play(Write(rearrange))
        self.wait(3)
        self.clear()

        title2=TextMobject("An elliptic curve in Weierstrass form:")
        title2.to_edge(UP)
        self.play(Write(title2))
        rearrange.next_to(title2,DOWN)
        self.play(Write(rearrange))
        self.wait(3)
        subtitle=TextMobject("A useful transformation:")
        subtitle.scale(0.9)
        subtitle.set_color(YELLOW)
        subtitle.next_to(rearrange,DOWN)
        subtitle.shift(0.75*DOWN)
        self.play(Write(subtitle))
        transforma.next_to(subtitle,DOWN)
        transforma.shift(3.8*LEFT)
        transformb.next_to(transforma, RIGHT)
        transformc.next_to(transformb, RIGHT)
        self.play(Write(transforma))
        self.play(Write(transformb))
        self.play(Write(transformc))
        self.wait(3)
        self.play(FadeOut(title2),FadeOut(rearrange),FadeOut(subtitle))
        self.play(ApplyMethod(transforma.scale,0.8),ApplyMethod(transformb.scale,0.8),ApplyMethod(transformc.scale,0.8))
        self.play(ApplyMethod(transforma.shift,1.5*LEFT+3*UP),ApplyMethod(transformb.shift, 4.95*LEFT+2*UP),ApplyMethod(transformc.shift,8.4*LEFT+1*UP))

        subtitle2=TextMobject("Applying the transformation:")
        subtitle2.scale(0.9)
        subtitle2.shift(3.3*UP+1.4*RIGHT)
        transformed.scale(0.4)
        transformed.next_to(subtitle2,DOWN)
        self.play(Write(subtitle2))
        self.play(Write(transformed))
        self.wait(3)
        subtitle3=TextMobject("Eliminating the denominator:")
        subtitle3.scale(0.9)
        subtitle3.next_to(transformed, DOWN)
        subtitle3.shift(0.5*DOWN)
        reduced.next_to(subtitle3, DOWN)
        self.play(Write(subtitle3))
        self.play(Write(reduced))
        self.wait(3)
        question=TextMobject("What does this even look like,")
        question2=TextMobject("and how can we find a solution?")
        question.set_color(BLUE_C)
        question2.set_color(BLUE_C)
        question.shift(1.1*DOWN)
        question2.next_to(question,DOWN)
        #self.play(Write(question))
        #self.play(Write(question2))
        #self.wait(3)

        more=TextMobject("Our ``wrong'' solution: $a=4, b=-1, c=11$")
        more2=TextMobject("corresponds with $x=-100, y=260$")
        more.scale(0.6)
        more2.scale(0.6)
        more.shift(0.8*DOWN)
        more2.next_to(more, DOWN)
        more2.shift(0.1*UP)
        self.play(Write(more),Write(more2))
        self.wait(3)