from manim import *

class CreateCircle(Scene):
  def construct(self):
    left_square = Square()
    left_square.set_color(BLUE)
    left_square.set_fill(BLUE, opacity=0.7)
    left_square.shift(LEFT * 1.5)
    # left_square.rotate(PI / 4)

    right_square = Square()
    right_square.set_color(GREEN)
    right_square.set_fill(GREEN, opacity=0.5)
    right_square.shift(RIGHT * 1.5)

    self.play(FadeIn(left_square), FadeIn(right_square))

    self.play(Rotate(left_square, angle=PI / 2), Rotate(right_square, angle=PI), run_time=2)

    manim_text = Tex(r"\LaTeX")
    manim_text.shift(DOWN * 2)
    self.add(manim_text)
    self.play(Write(manim_text))

    self.wait(1)

    self.play(FadeOut(left_square), FadeOut(right_square), FadeOut(manim_text))
    template = TexTemplate()
    template.add_to_preamble(r"\usepackage{amsmath}")

class MatrixScene(Scene):
  def construct(self):
    mat = Matrix([
      [r"x_{11}", r"x_{12}", r"x_{13}"],
      [r"x_{21}", r"x_{22}", r"x_{23}"],
      [r"\vdots", r"\vdots", r"\vdots"],
      [r"x_{n1}", r"x_{n2}", r"x_{n3}"]
    ])

    self.add(mat)

    self.wait(1)

    # self.add(VGroup(tex, other_vector_matrix).arrange(RIGHT))

class SpecialThanks(Scene):
  def construct(self):
    special_thanks = Text("Special thanks to:")
    self.play(Write(special_thanks))

    self.wait(1)

    self.play(Unwrite(special_thanks))

    three_b1b = Tex("• Grant Sanderson (3blue1brown):\par for the wonderful animation engine, and for\par the awesome linear algebra videos\par")

    tristan = Tex("• Tristan Schulz (MrDiver):\par my new German friend in...\par")
    manim_community = Tex("• The Manim Community:\par I would not have finished this project\par were it not for your help.\par")

    group = VGroup(
      three_b1b,
      tristan,
      manim_community,
    ).arrange(DOWN)

    self.play(Write(group))

    self.wait(3)
    self.play(FadeOut(group))

    thank_you = Text("Thank you.")
    self.play(FadeIn(thank_you))
    self.wait(2)
    self.play(FadeOut(thank_you))