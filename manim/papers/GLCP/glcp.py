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
        left_panel = Rectangle(width=5.5, height=4, color=WHITE).to_edge(LEFT, buff=0.4).shift(DOWN*0.3)
        right_panel = Rectangle(width=5.5, height=4, color=WHITE).to_edge(RIGHT, buff=0.4).shift(DOWN*0.3)
        self.play(Create(left_panel), Create(right_panel))

        #
        # 左: predicted skeleton  \hat P_g
        #
        # スケルトンの折れ線（だいたい図と似せる）
        # 画面座標に合わせて少しずつ調整するとよい
        lp_origin = left_panel.get_center()

        # メインの折れ線（上から右へ→下へ）
        pred_path1 = VGroup(
            Line(lp_origin + LEFT*1.9 + UP*0.8, lp_origin + LEFT*0.8 + UP*0.4, color=WHITE),
            Line(lp_origin + LEFT*0.8 + UP*0.4, lp_origin + RIGHT*0.2 + UP*0.3, color=WHITE),
            Line(lp_origin + RIGHT*0.2 + UP*0.3, lp_origin + RIGHT*1.5 + UP*1.0, color=WHITE),
        )
        # 下方向の枝
        pred_branch = Line(lp_origin + RIGHT*0.2 + UP*0.3, lp_origin + RIGHT*0.2 + DOWN*1.2, color=WHITE)
        # 右上に伸びる枝
        pred_branch2 = Line(lp_origin + RIGHT*1.0 + UP*0.6, lp_origin + RIGHT*2.0 + UP*1.0, color=WHITE)

        pred_skel = VGroup(pred_path1, pred_branch, pred_branch2)
        self.play(Create(pred_skel))

        # 端点 (cyan)
        # \hat p_1, \hat p_2, \hat p_3, \hat p_4, \hat p_5
        hat_p1 = Dot(lp_origin + LEFT*1.9 + UP*0.8, color=TEAL)
        hat_p2 = Dot(lp_origin + RIGHT*0.2 + UP*0.3, color=TEAL)
        hat_p3 = Dot(lp_origin + RIGHT*2.0 + UP*1.0, color=TEAL)
        hat_p4 = Dot(lp_origin + RIGHT*1.0 + UP*0.6, color=TEAL)
        hat_p5 = Dot(lp_origin + RIGHT*0.2 + DOWN*1.2, color=TEAL)

        self.play(
            FadeIn(hat_p1),
            FadeIn(hat_p2),
            FadeIn(hat_p3),
            FadeIn(hat_p4),
            FadeIn(hat_p5),
        )

        # ラベル
        label_hat_p1 = MathTex(r"\hat p_1", color=WHITE).scale(0.6).next_to(hat_p1, LEFT, buff=0.15)
        label_hat_p2 = MathTex(r"\hat p_2", color=WHITE).scale(0.6).next_to(hat_p2, DOWN, buff=0.15)
        label_hat_p3 = MathTex(r"\hat p_3", color=WHITE).scale(0.6).next_to(hat_p3, RIGHT, buff=0.15)
        label_hat_p4 = MathTex(r"\hat p_4", color=WHITE).scale(0.6).next_to(hat_p4, DOWN, buff=0.15)
        label_hat_p5 = MathTex(r"\hat p_5", color=WHITE).scale(0.6).next_to(hat_p5, RIGHT, buff=0.15)

        self.play(
            Write(label_hat_p1),
            Write(label_hat_p2),
            Write(label_hat_p3),
            Write(label_hat_p4),
            Write(label_hat_p5),
        )

        #
        # 右: GT skeleton  P_g
        #
        rp_origin = right_panel.get_center()

        gt_main = VGroup(
            Line(rp_origin + LEFT*1.7 + UP*0.6, rp_origin + LEFT*0.5 + UP*0.2, color=WHITE),
            Line(rp_origin + LEFT*0.5 + UP*0.2, rp_origin + RIGHT*0.3 + UP*0.1, color=WHITE),
        )
        gt_vertical = Line(rp_origin + RIGHT*0.3 + UP*0.1, rp_origin + RIGHT*0.3 + DOWN*1.2, color=WHITE)
        gt_diag = Line(rp_origin + RIGHT*0.3 + UP*0.1, rp_origin + RIGHT*1.9 + UP*0.9, color=WHITE)

        gt_skel = VGroup(gt_main, gt_vertical, gt_diag)
        self.play(Create(gt_skel))

        # GT endpoints: p_1, p_2, p_3
        p1 = Dot(rp_origin + LEFT*1.7 + UP*0.6, color=TEAL)
        p2 = Dot(rp_origin + RIGHT*1.9 + UP*0.9, color=TEAL)
        p3 = Dot(rp_origin + RIGHT*0.3 + DOWN*1.2, color=TEAL)

        self.play(FadeIn(p1), FadeIn(p2), FadeIn(p3))

        label_p1 = MathTex(r"p_1", color=WHITE).scale(0.6).next_to(p1, LEFT, buff=0.15)
        label_p2 = MathTex(r"p_2", color=WHITE).scale(0.6).next_to(p2, RIGHT, buff=0.15)
        label_p3 = MathTex(r"p_3", color=WHITE).scale(0.6).next_to(p3, RIGHT, buff=0.15)

        self.play(Write(label_p1), Write(label_p2), Write(label_p3))

        self.wait(2)
