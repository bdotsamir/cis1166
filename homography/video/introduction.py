from manim import *

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
      [1, 2], 
      [-1, -1]
      ]).set_column_colors(GREEN, RED)
    # matrix.next_to(text, DOWN)

    self.play(Write(matrix))

    self.wait(3)
