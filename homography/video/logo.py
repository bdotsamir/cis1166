from manim import *

class TempleLogo(Scene):
  def construct(self):
    temple = ImageMobject('../images/temple_logo.png')
    temple.scale(0.3)
    temple.z_index = 1

    phillies = ImageMobject('../images/phillies.jpg')
    phillies.scale(1.3)

    self.play(FadeIn(temple))

    self.wait(5)

    self.play(
      temple.animate.move_to(RIGHT * 2).scale(0.7),
      FadeIn(phillies)
    )

    transparent_color = ManimColor.from_rgba([0, 0, 0, 0])
    # Create a new square, position it around the logo on the left
    rect = Rectangle(
      color=transparent_color, 
      height=0.8, 
      width=2.3
      )
    rect.move_to([-3.2, 1, 1])

    self.wait(3)
    self.play(Circumscribe(temple))
    self.play(Circumscribe(rect))

    self.wait(3)

    p_tl = UP * 1.5 + LEFT * 4.3
    p_tr = UP * 1.5 + LEFT * 2.1
    p_bl = UP * 0.65 + LEFT * 4.3
    p_br = UP * 0.7 + LEFT * 2.1

    t_tl, t_tr, t_bl, t_br = temple.points

    t_dots = [
      Dot(t_tl).set_color(YELLOW),
      Dot(t_tr).set_color(GREEN),
      Dot(t_bl).set_color(RED),
      Dot(t_br).set_color(BLUE)
    ]
    for dot in t_dots:
      dot.z_index = 10
      dot.scale(1.2)

    self.play(LaggedStart(*[
      AnimationGroup(FadeIn(dot), Flash(dot))
      for dot in t_dots
    ], lag_ratio=0.25))

    self.wait(1)

    p_dots = [
      Dot(p_tl).set_color(YELLOW),
      Dot(p_tr).set_color(GREEN),
      Dot(p_bl).set_color(RED),
      Dot(p_br).set_color(BLUE)
    ]

    self.play(LaggedStart(*[
      AnimationGroup(FadeIn(dot), Flash(dot))
      for dot in p_dots
    ], lag_ratio=0.25))

    self.wait(1)

    self.play(Circumscribe(temple))

    arrows = [
      Arrow(start=t_tl, end=p_tl).set_color(YELLOW),
      Arrow(start=t_tr, end=p_tr).set_color(GREEN),
      Arrow(start=t_bl, end=p_bl).set_color(RED),
      Arrow(start=t_br, end=p_br).set_color(BLUE)
    ]

    # "What we're doing is setting up starting and transformed vectors"
    self.play(*[
      GrowArrow(arrow)
      for arrow in arrows
    ])

    # "Now we're stuck with the same issue as before"
    self.wait(3)

    # "We have eight vectors..."
    self.play(*[
      Indicate(t_dot)
      for t_dot in t_dots
    ])

    self.wait(1)

    self.play(*[
      Indicate(p_dot)
      for p_dot in p_dots
    ])

    # "... but we don't know the transformation matrix."
    self.wait(2)

