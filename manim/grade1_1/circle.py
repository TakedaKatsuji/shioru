from manim import *
import numpy as np

class ArcAnimation(Scene):
    def construct(self):
        r = 1/(2*np.pi) * 20  # 半径
        O = ORIGIN
        A = np.array([r, 0, 0])

        # 円
        circle = Circle(radius=r, color=WHITE).move_to(O)
        self.add(circle)

        # 点O, A
        dot_O = Dot(O, color=WHITE)
        dot_A = Dot(A, color=RED)
        label_O = Text("O", font_size=24).next_to(dot_O, DOWN+LEFT*0.2)
        label_A = Text("A", font_size=24).next_to(dot_A, RIGHT)
        self.play(FadeIn(dot_O), FadeIn(dot_A), Write(label_O), Write(label_A))

        # ValueTrackerで角度uを動かす
        u = ValueTracker(PI/6)

        def get_B():
            return np.array([r*np.cos(u.get_value()), r*np.sin(u.get_value()), 0])
        def get_label_B():
            B = get_B()
            # ベクトルを正規化して外向き方向を作る
            v = B / np.linalg.norm(B)
            return Text("B", font_size=24).move_to(B + 0.3*v)

        dot_B = always_redraw(lambda: Dot(get_B(), color=GREEN))
        label_B = always_redraw(get_label_B)

        line_OA = Line(O, A, color=BLUE)
        line_OB = always_redraw(lambda: Line(O, get_B(), color=BLUE))
        
        arc_short = always_redraw(
            lambda: Arc(
                start_angle=0 if u.get_value() <= PI else u.get_value(),
                angle=u.get_value() if u.get_value() <= PI else 2*PI - u.get_value(),
                radius=r,
                arc_center=O,
                color=RED
            )
)

        # 長い弧
        arc_long = always_redraw(
            lambda: Arc(
                start_angle=u.get_value() if u.get_value() <= PI else 0,
                angle=2*PI - (u.get_value() if u.get_value() <= PI else 2*PI - u.get_value()),
                radius=r,
                arc_center=O,
                color=BLUE,
                stroke_opacity=0.4
            )
        )

        def get_arc_midpoint(is_short=True):
            if is_short:
                arc = ArcBetweenPoints(A, get_B(), radius=r) if u.get_value() <= PI else ArcBetweenPoints(get_B(), A, radius=r)
            else:
                arc = ArcBetweenPoints(get_B(), A, radius=r) if u.get_value() <= PI else ArcBetweenPoints(A, get_B(), radius=r)
            return arc.point_from_proportion(0.5)

        label_X = always_redraw(
            lambda: Text("X", font_size=24).move_to(
                get_arc_midpoint(is_short=True) +
                0.3 * (get_arc_midpoint(is_short=True) / np.linalg.norm(get_arc_midpoint(is_short=True)))
            )
        )
        # ラベルY（長い弧の中点）
        label_Y = always_redraw(
            lambda: Text("Y", font_size=24).move_to(
                -get_arc_midpoint(is_short=True) +
                0.3 * (-get_arc_midpoint(is_short=True)) / np.linalg.norm(get_arc_midpoint(is_short=True))
            )
        )
        label_u = always_redraw(
            lambda: Text("u", font_size=24).move_to(
                0.6 * get_arc_midpoint(is_short=True) / np.linalg.norm(get_arc_midpoint(is_short=True))
            )
        )


        self.play(Create(line_OA), Create(line_OB))
        self.play(FadeIn(dot_B), Write(label_B))
        self.add(arc_short, arc_long, label_X, label_Y, label_u)

        # Bを回転
        self.play(u.animate.set_value(5*PI/3), run_time=6, rate_func=linear)
        self.wait()
