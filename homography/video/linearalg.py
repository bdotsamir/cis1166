from manim import *

class HoVec(Scene):
  def construct(self):
    homography = Text("Homography")
    self.play(Write(homography))
    self.wait(2)
      
    self.play(
      homography.animate.move_to(UP).set_color(GREY)
    )

    vectors = Text("Vector")
    self.play(Write(vectors))
    self.wait(2)
    self.play(FadeOut(homography, vectors))

class VectorIntroduction(Scene):
  def construct(self):
    def label_updater(matrix: MobjectMatrix):
      new_x, new_y, __ = vector.get_end()
      x_text.set_value(int(new_x))
      y_text.set_value(int(new_y))

    plane = NumberPlane()
    self.play(Write(plane), run_time=1.5)
    
    self.wait(7)

    vector = Vector([1, 2]).set_color(YELLOW)
    self.play(GrowArrow(vector))

    self.wait(2)

    # Create dot to follow vector path
    dot = Dot().set_color(BLUE)
    dot.scale(1.5)

    self.play(FadeIn(dot), run_time=0.5)
    self.play(MoveAlongPath(dot, vector), run_time=1)
    self.wait(2)
    # Remove dot
    self.play(Flash(dot))
    self.wait(1)
    self.play(FadeOut(dot))

    self.wait(1)

    x, y, _ = vector.get_end()
    x_text = Integer(int(x))
    y_text = Integer(int(y))
    label = MobjectMatrix([[x_text], [y_text]], bracket_h_buff=MED_LARGE_BUFF, include_background_rectangle=True)
    label.set_row_colors(GREEN, RED)
    label.next_to(vector, RIGHT)
    self.play(FadeIn(label))

    self.wait(3)

    self.play(Indicate(x_text))
    self.wait(1)
    self.play(Indicate(y_text))
    self.wait(1)

    label.add_updater(label_updater)

    v2 = Vector([-3, -1]).set_color(PINK)
    v3 = Vector([-3, 2]).set_color(BLUE)
    v4 = Vector([3, -1]).set_color(ORANGE)

    self.play(Transform(vector, v2))
    self.play(Transform(vector, v3))
    self.play(Transform(vector, v4))

    # Performance, I guess?
    label.remove_updater(label_updater)

class LinearTransformation(Scene):

  # Array of Mobjects that will be transformed
  # by the ApplyMatrix animation
  transformable_mobjects = []

  def construct(self):
    title = Text("Linear Transformation")
    self.play(Write(title))
    self.wait(2)
    self.play(title.animate.to_edge(UP))

    self.wait(0.5)

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

    i_hat = Vector([1, 0])
    i_hat.set_color(GREEN)
    i_hat_label = MathTex(r"\hat{\imath}")
    i_hat_label.set_color(GREEN)
    i_hat_label.next_to(i_hat, UP, buff=0.003)
    i_hat_label.save_state()

    j_hat = Vector([0, 1])
    j_hat.set_color(RED)
    j_hat_label = MathTex(r"\hat{\jmath}")
    j_hat_label.set_color(RED)
    j_hat_label.next_to(j_hat, LEFT, buff=0.04)
    j_hat_label.save_state()

    self.play(GrowArrow(i_hat))
    self.play(FadeIn(i_hat_label))
    self.play(GrowArrow(j_hat))
    self.play(FadeIn(j_hat_label))

    vector = Vector([1, 2])
    vector.set_color(YELLOW)
    vec_label = vector.coordinate_label(color=YELLOW)
    vec_label.next_to(vector, RIGHT)
    self.play(GrowArrow(vector))
    self.play(FadeIn(vec_label))
    vec_label.save_state()

    self.wait(1)

    self.play(
      FadeOut(plane, background_plane, i_hat, j_hat, vector)
    )

    vec_l_copy = vec_label.copy()
    t_eq = MathTex(r"=")
    t_1 = MathTex(r"1").set_color(YELLOW)
    t_star = MathTex(r"*")
    mat_i_hat = Matrix([[1], [0]]).set_color(GREEN)
    t_plus = MathTex(r"+")
    t_2 = MathTex(r"2").set_color(YELLOW)
    t_star_copy = t_star.copy()
    mat_j_hat = Matrix([[0], [1]]).set_color(RED)

    VGroup(
      vec_l_copy,
      t_eq,
      t_1,
      t_star,
      mat_i_hat,
      t_plus,
      t_2,
      t_star_copy,
      mat_j_hat
    ).arrange()

    self.play(LaggedStart(
      Transform(vec_label, vec_l_copy),
      Write(t_eq),
      Write(t_1),
      Write(t_star),
      Transform(i_hat_label, mat_i_hat),
      Write(t_plus),
      Write(t_2),
      Write(t_star_copy),
      Transform(j_hat_label, mat_j_hat),
      run_time=3,
      lag_ratio=0.25
    ))

    self.wait(3)

    self.play(
      Restore(vec_label),
      Restore(i_hat_label),
      Restore(j_hat_label),
      FadeIn(plane, background_plane, vector, i_hat, j_hat),
      FadeOut(t_eq, t_1, t_star, t_plus, t_2, t_star_copy)
    )

    self.wait(1)

    self.play(Indicate(i_hat_label))
    self.wait(1)
    self.play(Indicate(j_hat_label))
    self.wait(2)

    self.play(Indicate(vec_label))
    self.wait(2)

    # Transformation matrix
    t_mat = [
      [3, 2],
      [0, 2]
    ]
    def transform_objects(object):
      return ApplyMatrix(t_mat, object)
    
    t_ihat = Vector([t_mat[0][0], t_mat[1][0]])
    t_ihat.set_color(GREEN)
    t_jhat = Vector([t_mat[0][1], t_mat[1][1]])
    t_jhat.set_color(RED)

    t_vec = Vector([7, 4])
    t_vec.set_color(PINK)
    t_vec_label = t_vec.coordinate_label(color=PINK)
    t_vec_label.move_to([6, 2.5, 0])

    self.play(
      *map(transform_objects, self.transformable_mobjects),
      AnimationGroup(
        Transform(i_hat, t_ihat),
        Transform(j_hat, t_jhat),
        Transform(vector, t_vec),
        Transform(vec_label, t_vec_label),
        i_hat_label.animate.next_to(t_ihat, UP, buff=-1),
        j_hat_label.animate.next_to(t_jhat, LEFT, buff=0.04),
        run_time=3
      )
    )

    self.wait(2)

    t_ihat_label = t_ihat.coordinate_label(color=GREEN)
    t_jhat_label = t_jhat.coordinate_label(color=RED)

    self.play(Transform(i_hat_label, t_ihat_label))
    self.play(Transform(j_hat_label, t_jhat_label))

    self.wait(2)

    self.play(
      FadeOut(plane, background_plane, vector, i_hat, j_hat)
    )
    # Remaining: i_hat, j_hat, t_vec_label

    t_1_copy = t_1.copy()
    t_2_copy = t_2.copy()

    transformed_group = VGroup(
      t_vec_label,
      MathTex(r"="),
      t_1_copy,
      t_star.copy(),
      t_ihat_label,
      t_plus.copy(),
      t_2_copy,
      t_star.copy(),
      t_jhat_label
    ).arrange()

    self.play(Transform(
      VGroup(i_hat_label, j_hat_label, vec_label),
      transformed_group
    ))

    self.wait(2)

    original_vector_text = Text("Original vector: ", color=YELLOW)
    original_vector_matrix = Matrix([[1], [2]]).set_color(YELLOW)
    original_vector_group = VGroup(original_vector_text, original_vector_matrix)
    original_vector_group.arrange(buff=0.5)
    original_vector_group.scale(0.8)

    original_vector_group.next_to(transformed_group, DOWN, buff=0.5)

    self.play(Write(original_vector_group))
    self.wait(2)

    self.play(Circumscribe(t_ihat_label))
    self.play(Circumscribe(t_jhat_label))
    self.wait(1)

class LinTransPatch(Scene):
  def construct(self):
    title = Text("Linear Transformation")
    title.to_edge(UP)
    self.add(title)

    t_vec = Matrix([[7], [4]]).set_color(PINK)
    mt_eq = MathTex(r"=")
    mt_1 = MathTex(r"1").set_color(YELLOW)
    mt_star = MathTex(r"*")
    t_ihat = Matrix([[3], [0]]).set_color(GREEN)
    mt_plus = MathTex(r"+")
    mt_2 = MathTex(r"2").set_color(YELLOW)
    mt_star_copy = mt_star.copy()
    t_jhat = Matrix([[2], [2]]).set_color(RED)

    step1 = VGroup(
      # t_vec,
      # mt_eq,
      mt_1,
      mt_star,
      t_ihat,
      mt_plus,
      mt_2,
      mt_star_copy,
      t_jhat
    ).arrange()

    self.add(step1)

    self.wait(2)

    self.play(Indicate(mt_1))
    self.wait(2)
    self.play(Indicate(t_ihat))
    self.wait(1)
    self.play(Indicate(mt_2))
    self.wait(2)
    self.play(Indicate(t_jhat))

    step2 = VGroup(
      Matrix([[3], [0]]).set_color(GREEN),
      mt_plus,
      Matrix([[4], [4]]).set_color(RED)
    ).arrange()

    self.play(Transform(step1, step2))

    final_vec = Matrix([[7], [4]]).set_color(PINK)

    self.wait(1)

    self.play(Transform(step1, final_vec))

    self.wait(5)

class JustTheCoordinates(Scene):
  def construct(self):
    matrix = Matrix([
      ["x", "x"],
      ["y", "y"]
    ]).set_column_colors(GREEN, RED)

    self.play(Write(matrix))

    self.wait(3)
    self.play(Unwrite(matrix))
    self.wait(1)

class WhatAboutTheOpposite(Scene):
  def construct(self):
    title = Text("What about the opposite?")
    self.play(FadeIn(title))

    self.wait(2)

    self.play(title.animate.move_to(UP * 2))

    vector_label = Matrix([[7], [-4]]).set_color(PINK)
    i_hat = Matrix([
      [3], 
      [0]
      ]).set_color(GREEN)
    m_star = MathTex(r"*")
    j_hat = Matrix([
      [2],
      [2]
    ]).set_color(RED)
    m_star_copy = m_star.copy()
    group = VGroup(
      vector_label,
      MathTex(r"="),
      MathTex(r"1").set_color(YELLOW),
      m_star,
      i_hat,
      MathTex(r"+"),
      MathTex(r"2").set_color(YELLOW),
      m_star_copy,
      j_hat
    ).arrange()

    self.play(FadeIn(group))

    self.wait(2)

    # There's gotta be a better way to do this?
    i_unknown = Matrix([["x"], ["y"]]).set_color(GREEN)
    i_unknown.next_to(m_star, RIGHT)
    j_unknown = Matrix([["x"], ["y"]]).set_color(RED)
    j_unknown.next_to(m_star_copy, RIGHT)

    self.play(
      Transform(i_hat, i_unknown), 
      Transform(j_hat, j_unknown)
    )

    self.wait(2)

    self.play(
      Circumscribe(i_unknown), 
      Circumscribe(j_unknown)
    )

    self.wait(1)

    self.play(
      FadeOut(title, group, i_unknown, j_unknown)
    )

    self.wait(2)

    homography = Text("Homography").set_color(YELLOW)
    self.play(Write(homography))

    self.wait(1)