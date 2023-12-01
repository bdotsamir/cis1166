from manim import *

class MadeWithManim(Scene):
  def construct(self):
    made_with = Text("Proudly made with")
    banner = ManimBanner()
    banner.scale(0.8)

    VGroup(made_with, banner).arrange(DOWN, buff=1)

    self.play(FadeIn(made_with))
    self.play(banner.create())
    self.play(banner.expand())

    self.wait(2)
    self.play(
      FadeOut(made_with), 
      Unwrite(banner)
    )
    self.wait(1)

class IntroductionScene(Scene):
  def construct(self):
    image = ImageMobject('../images/phillies.jpg')
    image.scale(1.3)

    self.play(FadeIn(image))

    self.wait(3)

    transparent_color = ManimColor.from_rgba([0, 0, 0, 0])
    # Create a new square, position it around the logo on the left
    rect = Rectangle(
      color=transparent_color, 
      height=1, 
      width=2.3
      )
    rect.move_to([-3.2, 1, 1])

    self.play(Circumscribe(rect))
    self.wait(1)

class Homography(Scene):
  def construct(self):
    text = Text("Homography")

    self.play(Write(text))

    self.wait(2)

    self.play(text.animate.move_to([0, 2, 0]))

    matrix = Matrix([
      ["x_{11}", "x_{12}", "x_{13}"],
      ["x_{21}", "x_{22}", "x_{23}"],
      ["x_{31}", "x_{32}", "1"]
    ])
    # matrix.next_to(text, DOWN)

    self.play(Write(matrix))

    self.wait(3)

    self.play(FadeOut(text, matrix))
