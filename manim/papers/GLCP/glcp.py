from manim import *

class EndpointFigure(Scene):
    def construct(self):
        # 背景を黒に
        self.camera.background_color = BLACK

        title = MathTex(
            r"\text{Endpoint-guided discontinuity mining}",
            color=WHITE
        ).to_edge(UP, buff=0.4)
        self.play(Write(title))

        # 左右パネルの枠
        left_panel = Rectangle(width=5.5, height=4, color=WHITE).to_edge(LEFT, buff=0.4).shift(DOWN*0.3+RIGHT)
        right_panel = Rectangle(width=5.5, height=4, color=WHITE).to_edge(RIGHT, buff=0.4).shift(DOWN*0.3+LEFT)
        left_title = MathTex(r"F_s").move_to(left_panel.get_top()+0.5*UP)
        right_title = MathTex(r"\hat S_g").move_to(right_panel.get_top()+0.5*UP)
        block = VGroup(left_title,left_panel, right_title, right_panel)
        self.play(FadeIn(block))

        # ===== GT Skelton ==== 
        lp_origin = left_panel.get_center()

        left_points = [
            [lp_origin+UP*1.5, lp_origin],
            [lp_origin,lp_origin+LEFT+DOWN],
            [lp_origin,lp_origin+DR*0.5],
            [lp_origin+DR*0.5, lp_origin+DR*0.5+DOWN*0.5+LEFT*0.25],
            [lp_origin+DR*0.5, lp_origin+DR*0.5+DOWN*0.5+RIGHT*0.25],
            ]

        gt_path1 = VGroup(
            Line(points[0], points[1], color=WHITE) for points in left_points
        )

        self.play(FadeIn(gt_path1))

        # ===== pi =====
        p1 = MathTex(r"p_1").move_to(left_points[0][0]+0.2*UP+0.3*LEFT).scale(0.8)
        p2 = MathTex(r"p_2").move_to(left_points[1][1]+0.3*DL).scale(0.8)
        p3 = MathTex(r"p_3").move_to(left_points[3][1]+0.3*DL).scale(0.8)
        p4 = MathTex(r"p_4").move_to(left_points[4][1]+0.3*DR).scale(0.8)
        left_ps = VGroup(p1, p2, p3, p4)

        # ===== pi points =====
        left_dots = VGroup(
            Dot(left_points[0][0], color=TEAL_A, fill_opacity=0.9, radius=0.1),
            Dot(left_points[1][1], color=TEAL_A, fill_opacity=0.9, radius=0.1),
            Dot(left_points[3][1], color=TEAL_A, fill_opacity=0.9, radius=0.1),
            Dot(left_points[4][1], color=TEAL_A, fill_opacity=0.9, radius=0.1),
        )
        self.play(FadeIn(left_dots))
        self.play(Write(left_ps))

        rp_origin = right_panel.get_center()

        right_points = [
            [rp_origin+UP*1.5, rp_origin+UP*0.6],
            [rp_origin,rp_origin+LEFT+DOWN],
            [rp_origin,rp_origin+DR*0.5],
            [rp_origin+DR*0.5, rp_origin+DR*0.5+DOWN*0.5+LEFT*0.25],
            [rp_origin+DR*0.5, rp_origin+DR*0.5+DOWN*0.5+RIGHT*0.25],
            ]

        gt_path1 = VGroup(
            Line(points[0], points[1], color=WHITE) for points in right_points
        )

        self.play(FadeIn(gt_path1))

        # ===== pi =====
        ph1 = MathTex(r"\hat p_1").move_to(right_points[0][0]+0.2*UP+0.3*LEFT).scale(0.8)
        ph2 = MathTex(r"\hat p_2").move_to(right_points[0][1]+0.5*RIGHT).scale(0.8)
        ph3 = MathTex(r"\hat p_3").move_to(right_points[1][0]+0.4*LEFT+0.1*UP).scale(0.8)
        ph4 = MathTex(r"\hat p_4").move_to(right_points[1][1]+0.3*DL).scale(0.8)
        ph5 = MathTex(r"\hat p_5").move_to(right_points[3][1]+0.3*DL).scale(0.8)
        ph6 = MathTex(r"\hat p_6").move_to(right_points[4][1]+0.3*DR).scale(0.8)
        right_ps = VGroup(ph1, ph2, ph3, ph4, ph5, ph6)

        # ===== pi points =====
        right_dots = VGroup(
            Dot(right_points[0][0], color=MAROON_A, fill_opacity=0.9, radius=0.1),
            Dot(right_points[1][1], color=MAROON_A, fill_opacity=0.9, radius=0.1),
            Dot(right_points[3][1], color=MAROON_A, fill_opacity=0.9, radius=0.1),
            Dot(right_points[4][1], color=MAROON_A, fill_opacity=0.9, radius=0.1),
            Dot(right_points[0][1], color=MAROON_A, fill_opacity=0.9, radius=0.1),
            Dot(right_points[1][0], color=MAROON_A, fill_opacity=0.9, radius=0.1),
        )
        self.play(FadeIn(right_dots))
        self.play(Write(right_ps))