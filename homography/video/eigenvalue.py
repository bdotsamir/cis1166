from math import *
from manim import *

class EigenIntro(Scene):

  # Array of Mobjects that will be transformed
  # by the ApplyMatrix animation
  transformable_mobjects = []

  def construct(self):
    plane = NumberPlane()
    background_plane = NumberPlane(
      faded_line_style={
      "stroke_color": DARK_GREY,
      "stroke_opacity": 0.01
    })
    background_plane.z_index = -10
    background_plane.fade()
    self.add(background_plane)
    self.play(FadeIn(plane), FadeIn(background_plane))
    self.transformable_mobjects.append(plane)

    # self.wait(2)

    scalar = 2
    arr = VGroup(*[Arrow(
      start=ORIGIN, 
      end=[scalar * np.cos(theta), scalar * np.sin(theta), 0]).set_color(YELLOW)
      for theta in np.arange(0, 2 * PI, PI / 4)]
    )
    for arrow in arr:
      arrow.z_index = 10

    spans = VGroup(*[
      Line(
        start=ORIGIN, 
        end=[7 * np.cos(theta), 7 * np.sin(theta), 0]
      ).set_color(PURPLE)
      for theta in np.arange(0, 2 * PI, PI / 4)]
    )

    self.play(*[
      GrowArrow(arrow)
      for arrow in arr
    ], *[
      Create(line)
      for line in spans
    ])

    span_1_brace = Brace(spans[0]).set_color(PURPLE)
    span_text = Text("Span")
    span_text.next_to(span_1_brace, DOWN)
    self.play(FadeIn(span_text), GrowFromCenter(span_1_brace))

    self.wait(1)

    t_mat = np.array([
      [3, 1],
      [0, 2]
    ])
    t_arrows = VGroup()
    # print(t_mat)
    for arrow in arr.submobjects:
      arrow_x, arrow_y, _ = arrow.get_end()
      vector = np.array([arrow_x, arrow_y])
      mult = np.dot(t_mat, vector)
      # print(mult)
      t_arrows += Arrow(start=ORIGIN, end=[*mult, 0]).set_color(PINK)

    self.play(
      ApplyMatrix(t_mat, plane),
      AnimationGroup(*[
        ReplacementTransform(o_arrow, t_arrow)
        for o_arrow, t_arrow in zip(arr, t_arrows)
      ], run_time=3),
      FadeOut(span_1_brace, span_text)
    )

    def is_eigenvector(arrow: Arrow):
      arrow_x, arrow_y, _ = arrow.get_end()
      return abs(arrow_x) == 5 or abs(int(arrow_x)) == 2
    
    def is_not_eigenvector(arrow: Arrow):
      arrow_x, arrow_y, _ = arrow.get_end()
      return abs(arrow_x) != 5 and abs(int(arrow_x)) != 2

    # Horrible. I know.
    eigenvectors = filter(is_eigenvector, t_arrows)
    not_eigenvectors = filter(is_not_eigenvector, t_arrows)
    # Is there a np.difference that I can use?
    #np.setdiff1d

    self.play(*[
      FadeOut(vector)
      for vector in not_eigenvectors
    ])

    self.wait(2)

    self.play(*[
      Indicate(eigenvector)
      for eigenvector in eigenvectors
    ])

    self.wait(5)

    eigenvector_brace = Brace(
      next(x for x in t_arrows if is_eigenvector(x)),
      color=YELLOW,
      direction=UP
      )
    eigenvector_text = Text("Eigenvector", color=YELLOW)
    eigenvector_text.next_to(eigenvector_brace, UP)

    self.play(FadeIn(eigenvector_text), GrowFromCenter(eigenvector_brace))

    self.wait(3)

    text_3 = Text("3", color=YELLOW)
    text_3.next_to(eigenvector_brace, UP)
    self.play(ReplacementTransform(eigenvector_text, text_3))

    self.wait(2)

    self.play(*[
      FadeOut(vector)
      for vector in list(t_arrows) if is_eigenvector(vector)
    ], 
    FadeOut(eigenvector_brace, text_3),
    *[
      FadeOut(span)
      for span in spans
    ]
    )

    i_hat = Vector([3, 0], color=GREEN)
    j_hat = Vector([1, 2], color=RED)

    self.play(GrowArrow(i_hat))
    self.play(GrowArrow(j_hat))

    self.wait(2)

    i_hat_label = i_hat.coordinate_label(include_background_rectangle=True)
    i_hat_label.set_column_colors(GREEN)
    i_hat_label.next_to(i_hat, RIGHT)
    j_hat_label = j_hat.coordinate_label(include_background_rectangle=True)
    j_hat_label.next_to(j_hat.get_end(), RIGHT)
    j_hat_label.set_column_colors(RED)
    self.play(Write(i_hat_label))
    self.play(Write(j_hat_label))

    self.wait(5)

    self.play(Circumscribe(i_hat_label))
    self.wait(1)
    self.play(Circumscribe(j_hat_label))
    self.wait(2)

    self.play(Indicate(i_hat))

    i_hat_brace = Brace(i_hat, color=GREEN)
    i_hat_brace.next_to(i_hat, DOWN)
    i_hat_brace_text = Text("3", color=GREEN)
    i_hat_brace_text.next_to(i_hat_brace, DOWN)
    self.play(GrowFromCenter(i_hat_brace), FadeIn(i_hat_brace_text))

    self.wait(5)

    self.play(Wiggle(i_hat))
    self.wait(4)

    self.play(Indicate(i_hat_brace_text))

    self.wait(2)

    sneaky_vector = Vector([-2, 2], color=YELLOW)
    self.play(GrowArrow(sneaky_vector))
    self.wait(1)

    sneaky_vector_brace = Brace(sneaky_vector,
                                direction=sneaky_vector.copy().rotate(PI / 2).get_unit_vector(),
                                color=YELLOW)
    sneaky_vector_brace.align_to(sneaky_vector)
    sneaky_vector_text = Text("2", color=YELLOW)
    sneaky_vector_text.next_to(sneaky_vector_brace, direction=DOWN * 0.0025 + LEFT, buff=0.0025)

    self.play(GrowFromCenter(sneaky_vector_brace))
    self.wait(1)
    self.play(Write(sneaky_vector_text))
    self.wait(1)