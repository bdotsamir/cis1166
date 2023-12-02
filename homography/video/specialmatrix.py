from manim import *

class SpecialMatrix(Scene):
  def construct(self):
    special_matrix = Matrix([
      ["x_{s}", "y_{s}", "1", "0", "0", "0", "- x_{d}x_{s}", "-x_{d}y_{d}", "-x_{d}"],
      [0, 0, 0, "x_{s}", "y_{s}", 1, "-y_{d}x_{s}", "-y_{d}y_{s}", "-y_{d}"],
      [r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots"]
    ], h_buff=1.5, element_alignment_corner=DOWN)

    self.play(Write(special_matrix))
    self.wait(5)

class BigMatrix(Scene):
  def construct(self):
    source_pair_coords = [
      "(0, 0)",
      "(2506, 0)",
      "(0, 675)",
      "(2506, 675)"
    ]
    dest_pair_coords = [
      "(13, 158)",
      "(247, 154)",
      "(13, 252)",
      "(247, 248)"
    ]

    source_coordinates = [MathTex(s_pair).set_color(YELLOW) for s_pair in source_pair_coords]
    
    dest_coordinates = [MathTex(d_pair).set_color(PINK) for d_pair in dest_pair_coords]
    
    s_coord_group = VGroup(*source_coordinates).arrange()
    d_coord_group = VGroup(*dest_coordinates).arrange()

    s_coord_group.shift(UP * 2 + LEFT * 2)
    d_coord_group.shift(UP * 1 + RIGHT * 2) # offset

    special_matrix = Matrix([
      ["x_{s}", "y_{s}", "1", "0", "0", "0", "- x_{d}x_{s}", "-x_{d}y_{d}", "-x_{d}"],
      [0, 0, 0, "x_{s}", "y_{s}", 1, "-y_{d}x_{s}", "-y_{d}y_{s}", "-y_{d}"]
    ], h_buff=1.5, element_alignment_corner=DOWN)

    self.play(Write(special_matrix))
    self.wait(1)

    self.play(FadeIn(s_coord_group))
    self.play(FadeIn(d_coord_group))

    self.wait(2)

    self.play(
      s_coord_group.animate.move_to(ORIGIN).scale(0.01)
    )
    self.remove(s_coord_group)
    self.play(
      d_coord_group.animate.move_to(ORIGIN).scale(0.01)
    )
    self.remove(d_coord_group)

    self.wait(5)

    composed_xy_matrix = Matrix([
      ["x_{s}^{(1)}", "y_{s}^{(1)}", "1", "0", "0", "0", "- x_{d}^{(1)}x_{s}^{(1)}", "-x_{d}^{(1)}y_{d}^{(1)}", "-x_{d}^{(1)}"],
      [0, 0, 0, "x_{s}^{(1)}", "y_{s}^{(1)}", 1, "-y_{d}^{(1)}x_{s}^{(1)}", "-y_{d}^{(1)}y_{s}^{(1)}", "-y_{d}^{(1)}"],
      [r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots"],
      ["x_{s}^{(i)}", "y_{s}^{(i)}", "1", "0", "0", "0", "- x_{d}^{(i)}x_{s}^{(i)}", "-x_{d}^{(i)}y_{d}^{(i)}", "-x_{d}^{(i)}"],
      [0, 0, 0, "x_{s}^{(i)}", "y_{s}^{(i)}", 1, "-y_{d}^{(i)}x_{s}^{(i)}", "-y_{d}^{(i)}y_{s}^{(i)}", "-y_{d}^{(i)}"],
      [r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots"],
      ["x_{s}^{(n)}", "y_{s}^{(n)}", "1", "0", "0", "0", "- x_{d}^{(n)}x_{s}^{(n)}", "-x_{d}^{(n)}y_{d}^{(n)}", "-x_{d}^{(n)}"],
      [0, 0, 0, "x_{s}^{(n)}", "y_{s}^{(n)}", 1, "-y_{d}^{(n)}x_{s}^{(n)}", "-y_{d}^{(n)}y_{s}^{(n)}", "-y_{d}^{(n)}"],
    ], h_buff=1.5, element_alignment_corner=DOWN)

    self.play(Transform(special_matrix, composed_xy_matrix))
    self.play(special_matrix.animate.shift(UP * 0.5))
    c_mat_brace = Brace(special_matrix).set_color(YELLOW)
    c_mat_brace.next_to(special_matrix, DOWN, buff=0.05)
    text_A = MathTex(r"A").set_color(YELLOW)
    t_A_copy = text_A.copy()
    text_A.next_to(c_mat_brace, DOWN, buff=0.1)

    self.play(GrowFromCenter(c_mat_brace), FadeIn(text_A))
    
    self.wait(2)

    transposed_composed_xy_matrix = Matrix([
      ["x_{s}^{(1)}", 0, r"\dots", "x_{s}^{(i)}", 0, r"\dots", "x_{s}^{(n)}", 0],
      ["y_{s}^{(1)}", 0, r"\dots", "y_{s}^{(i)}", 0, r"\dots", "y_{s}^{(n)}", 0],
      [1, 0, r"\dots", 1, 0, r"\dots", 1, 0],
      [0, "x_{s}^{(1)}", r"\dots", 0, "x_{s}^{(i)}", r"\dots", 0, "x_{s}^{(n)}"],
      [0, "y_{s}^{(1)}", r"\dots", 0, "y_{s}^{(i)}", r"\dots", 0, "y_{s}^{(n)}"],
      [0, 1, r"\dots", 0, 1, r"\dots", 0, 1],
      ["-x_{d}^{(1)}x_{s}^{(1)}", "-y_{d}^{(1)}x_{s}^{(1)}", r"\dots", "-x_{d}^{(i)}x_{s}^{(i)}", "-y_{d}^{(i)}x_{s}^{(i)}", r"\dots", "-x_{d}^{(n)}x_{s}^{(n)}", "-y_{d}^{(n)}x_{s}^{(n)}",],
      ["-x_{d}^{(1)}y_{s}^{(1)}", "-y_{d}^{(1)}y_{s}^{(1)}", r"\dots", "-x_{d}^{(i)}y_{s}^{(i)}", "-y_{d}^{(i)}y_{s}^{(i)}", r"\dots", "-x_{d}^{(n)}y_{s}^{(n)}", "-y_{d}^{(n)}y_{s}^{(n)}",],
      ["-x_{d}^{(1)}", "-y_{d}^{(1)}", r"\dots", "-x_{d}^{(i)}", "-y_{d}^{(i)}", r"\dots", "-x_{d}^{(n)}", "-y_{d}^{(n)}",]
    ], h_buff=2.1,element_alignment_corner=DOWN)

    transposed_composed_xy_matrix.scale(0.8)
    transposed_composed_xy_matrix.shift(UP * 0.3)

    text_AT = MathTex("A^{T}").set_color(YELLOW)
    text_AT.next_to(c_mat_brace, DOWN, buff=0.1),

    self.play(
      Transform(special_matrix, transposed_composed_xy_matrix),
      ReplacementTransform(text_A, text_AT),
      c_mat_brace.animate.next_to(special_matrix, DOWN, buff=0.05)
    )
    self.wait(3)

    self.play(FadeOut(special_matrix, c_mat_brace))

    mult_group = VGroup(
      text_AT.copy(),
      t_A_copy
    ).arrange()

    self.play(
      text_AT.animate.center().become(mult_group)
    )
    self.wait(3)

    self.play(FadeOut(text_AT))
    self.wait(1)

class LongAndComplicated(Scene):
  def construct(self):
    xdi = MathTex(r"""
    x_{d}^{(i)} = \frac{\tilde{x}_{d}^{(i)}}{\tilde{z}_{d}^{(i)}} = \frac{
      h_{11}x_{s}^{(i)} + h_{12}y_s^{(i)} + h_{13}
    }{
      h_{31}x_{s}^{(i)} + h_{32}y_{s}^{(i)} + h_{33}
    }
    """)

    ydi = MathTex(r"""
    y_{d}^{(i)} = \frac{\tilde{y}_{d}^{(i)}}{\tilde{z}_{d}^{(i)}} = \frac{
      h_{21}x_{s}^{(i)} + h_{22}y_s^{(i)} + h_{23}
    }{
      h_{31}x_{s}^{(i)} + h_{32}y_{s}^{(i)} + h_{33}
    }
    """)

    step1 = VGroup(xdi, ydi).arrange(DOWN, buff=1)
    
    self.play(Write(step1))
    self.wait(0.5)

    xdi_step2 = MathTex(r"""
      x_{d}^{(i)} (h_{31}x_{s}^{(i)} + h_{32}y_{s}^{(i)} + h_{33}) = h_{11}x_{s}^{(i)} + h_{12}y_{s}^{(i)} + h_{13}
    """)

    ydi_step2 = MathTex(r"""
      y_{d}^{(i)} (h_{31}x_{s}^{(i)} + h_{32}y_{s}^{(i)} + h_{33}) = h_{21}x_{s}^{(i)} + h_{22}y_{s}^{(i)} + h_{23}
    """)

    step2 = VGroup(xdi_step2, ydi_step2).arrange(DOWN, buff=1)

    self.play(Transform(step1, step2))
    self.wait(0.5)

    xy_matrix = Matrix([
      ["x_{s}^{(i)}", "y_{s}^{(i)}", "1", "0", "0", "0", "- x_{d}^{(i)}x_{s}^{(i)}", "-x_{d}^{(i)}y_{d}^{(i)}", "-x_{d}^{(i)}"],
      [0, 0, 0, "x_{s}^{(i)}", "y_{s}^{(i)}", 1, "-y_{d}^{(i)}x_{s}^{(i)}", "-y_{d}^{(i)}y_{s}^{(i)}", "-y_{d}^{(i)}"]
    ], h_buff=1.5, element_alignment_corner=DOWN)

    h_matrix = Matrix([
      ["h_{11}"],
      ["h_{12}"],
      ["h_{13}"],
      ["h_{21}"],
      ["h_{22}"],
      ["h_{23}"],
      ["h_{31}"],
      ["h_{32}"],
      ["h_{33}"]
    ], v_buff=0.5)

    t_eq = MathTex("=")
    zero_zero_matrix = Matrix([
      [0],
      [0]
    ], v_buff=0.7)

    step3 = VGroup(xy_matrix, h_matrix, t_eq, zero_zero_matrix).arrange().scale(0.7)

    self.play(Transform(step1, step3))
    self.wait(0.5)

    composed_xy_matrix = Matrix([
      ["x_{s}^{(1)}", "y_{s}^{(1)}", "1", "0", "0", "0", "- x_{d}^{(1)}x_{s}^{(1)}", "-x_{d}^{(1)}y_{d}^{(1)}", "-x_{d}^{(1)}"],
      [0, 0, 0, "x_{s}^{(1)}", "y_{s}^{(1)}", 1, "-y_{d}^{(1)}x_{s}^{(1)}", "-y_{d}^{(1)}y_{s}^{(1)}", "-y_{d}^{(1)}"],
      [r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots"],
      ["x_{s}^{(i)}", "y_{s}^{(i)}", "1", "0", "0", "0", "- x_{d}^{(i)}x_{s}^{(i)}", "-x_{d}^{(i)}y_{d}^{(i)}", "-x_{d}^{(i)}"],
      [0, 0, 0, "x_{s}^{(i)}", "y_{s}^{(i)}", 1, "-y_{d}^{(i)}x_{s}^{(i)}", "-y_{d}^{(i)}y_{s}^{(i)}", "-y_{d}^{(i)}"],
      [r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots", r"\vdots"],
      ["x_{s}^{(n)}", "y_{s}^{(n)}", "1", "0", "0", "0", "- x_{d}^{(n)}x_{s}^{(n)}", "-x_{d}^{(n)}y_{d}^{(n)}", "-x_{d}^{(n)}"],
      [0, 0, 0, "x_{s}^{(n)}", "y_{s}^{(n)}", 1, "-y_{d}^{(n)}x_{s}^{(n)}", "-y_{d}^{(n)}y_{s}^{(n)}", "-y_{d}^{(n)}"],
    ], h_buff=1.5, element_alignment_corner=DOWN)

    h_matrix_copy = h_matrix.copy()
    t_eq_copy = t_eq.copy()

    zeros_matrix = Matrix([
      ["0"],
      ["0"],
      [r"\vdots"],
      ["0"]
    ])

    step4 = VGroup(composed_xy_matrix, h_matrix_copy, t_eq_copy, zeros_matrix).arrange().scale(0.7)

    self.play(Transform(step1, step4))
    self.wait(3)