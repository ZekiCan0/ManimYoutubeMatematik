#Bu kod ManimCE v0.13.1 kullanılarak hazırlanmıştır. Diğer versiyonlarında hatalar oluşabilir.


from manim import *
import manimpango


class ValueOfE(Scene):
    def construct(self):
        e = Text("e =", slant=ITALIC, font="Times New Roman", font_size=44).to_edge(UL)
        e_value = Text(
            "2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178 \n"
            "52516642742746639193200305992181741359662904357290033429526059563073813232862794349076323382 \n"
            "98807531952510190115738341879307021540891499348841675092447614606680822648001684774118537423 \n"
            "45442437107539077744992069551702761838606261331384583000752044933826560297606737113200709328 \n"
            "70912744374704723069697720931014169283681902551510865746377211127844250569536967707854499699 \n"
            "67946864454905987931636889230098793127736178215424999229576351482208269895193668033182528869 \n"
            "39849646510582093923982948879332036250944311730123819706841614039701983767932068328237646480 \n"
            "42953118023287825098194558153017567173613320698112509961818815930416903515988885193458072738 \n"
            "66738589422879228499892086805825749279610484198444363463244968487560233624827041978623209002 \n"
            "16099023530436994184914631409343173814364054625315209618369088870701676839642437814059271456 \n"
            "35490613031072085103837505101157477041718986106873969655212671546889570350354021234078498193 \n"
            "34321068170121005627880235193033224745015853904730419957777093503660416997329725088687696640 \n"
            "35557071622684471625607988265178713419512466520103059212366771943252786753985589448969709640 \n"
            "97545918569563802363701621120477427228364896134225164450781824423529486363721417402388934412 \n"
            "47963574370263755294448337998016125492278509257782562092622648326277933386566481627725164019 \n"
            "10590049164499828931505660472580277863186415519565324425869829469593080191529872117255634754 \n"
            "63964479101459040905862984967912874068705048958586717479854667757573205681288459205413340539 \n"
            "22000113786300945560688166740016984205580403363795376452030402432256613527836951177883863874 \n"
            "43966253224985065499588623428189970773327617178392803494650143455889707194258639877275471096 \n"
            "62953741521115136835062752602326484728703920764310059584116612054529703023647254929666938115 \n"
            "13732275364509888903136020572481765851180630364428123149655070475102544650117272115551948... \n",
            font_size=24, font="Times New Roman").move_to(DOWN*0.4)
        self.wait()
        self.play(AnimationGroup(
            Write(e),
            Write(e_value), lag_ratio=0.8, run_time=10
        ))
        self.wait()


class PrefaceOfNapier(Scene):
    def construct(self):
        napier_image = ImageMobject("John_Napier.jpg").scale(1.75).move_to(LEFT*3)
        napier_life_time = Text("1550 - 1617").next_to(napier_image, DOWN)
        preface_descriptio = Text(
            "Seeing there is nothing (right beloved students in the Mathematics) \n"
            "that is so troublesome to mathematical practise, nor that do more \n"
            "molest and hinder Calculators, then the multiplication,  division, \n"
            "square and cubical extractions of great numbers, which besides \n"
            "the tedious expence of time, are for the most part subject to many \n"
            "slippery errors. I began therefore to consider in my mind, by what \n "
            "certain and ready art I might remove those hindrances.",
            font_size=18, slant=ITALIC,
        ).next_to(napier_image, RIGHT*1.5)
        self.wait()
        self.play(
            AnimationGroup(
                FadeIn(napier_image),
                Write(napier_life_time), run_time=2, lag_ratio=0.8
            )
        )
        self.wait()

        self.play(Write(preface_descriptio), run_time=8)
        self.wait()


class Napiers_Books(Scene):
    def construct(self):
        descriptio = ImageMobject("descriptio.png").move_to(LEFT*2.25)
        constructio = ImageMobject("constructio.png").scale(1.44).move_to(RIGHT * 2.25)

        self.wait()
        self.play(FadeIn(descriptio), run_time=1.5)
        self.wait()

        self.play(FadeIn(constructio))
        self.wait()


class Stifel(Scene):
    def construct(self):
        stifel_image = ImageMobject("stifel.jpeg").scale(2)
        arithmetica_integra_image = ImageMobject("arithmetica_integra.jpg").scale(1.05)
        stifel_group = Group(stifel_image, arithmetica_integra_image).arrange()
        stifel_life_time = Text("1487 - 1567").scale(0.7).next_to(stifel_image, DOWN)

        self.wait()
        self.play(FadeIn(stifel_group), Write(stifel_life_time))
        self.wait(4)

        self.play(FadeOut(stifel_group), Unwrite(stifel_life_time))
        self.wait()

        progression = MathTable(
            [[1, 2, 3, 4, 5, 6, 7, 8],
             [2, 4, 8, 16, 32, 64, 128, 256]], v_buff=1.2, h_buff=0.9,
            row_labels=[Text("Aritmetik Dizi:", font_size=30), Text("Geometrik Dizi:", font_size=30)]
            )
        progression_copy = progression.copy()
        progression_1 = MathTable(
            [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
             [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]], v_buff=1.2, h_buff=0.7,
            row_labels=[Text("Aritmetik Dizi:", font_size=30), Text("Geometrik Dizi:", font_size=30)]
        ).scale(0.7).move_to(DOWN * 1.5)

        progression_without_labels = progression.get_entries_without_labels()
        progression_1_without_labels = progression_1.get_entries_without_labels()
        self.play(Write(progression.get_entries()))
        self.wait()


        rect_2, rect_3, rect_5, rect_6, rect_8_arth,  rect_4, rect_8_geo, rect_32, rect_64, rect_256 = list(
            map(
                SurroundingRectangle, [
                    progression_without_labels[i] for i in [1, 2, 4, 5, 7, 9, 10, 12, 13, 15]
                ]
            )
        )

        upper_arrow_sum = CurvedArrow(rect_3.get_corner(UR) + SMALL_BUFF, rect_5.get_corner(UL) + SMALL_BUFF, angle=-TAU/4)
        lower_arrow_times = CurvedArrow(rect_8_geo.get_corner(DR) - SMALL_BUFF, rect_32.get_corner(DL) - SMALL_BUFF)
        upper_arrow_substract = CurvedArrow(rect_8_arth.get_corner(UL) + SMALL_BUFF, rect_6.get_corner(UR) + SMALL_BUFF)
        lower_arrow_divison = CurvedArrow(rect_256.get_corner(DL) - SMALL_BUFF, rect_64.get_corner(DR) - SMALL_BUFF,
                                          angle=-TAU/4)
        upper_arrow_3_plus_3 = CurvedArrow(rect_3.get_corner(UR) + SMALL_BUFF, rect_6.get_corner(UL) + SMALL_BUFF, angle=-TAU/4)
        lower_arrow_8_times_8 = CurvedArrow(rect_8_geo.get_corner(DR) - SMALL_BUFF, rect_64.get_corner(DL) - SMALL_BUFF)
        upper_arrow_6_divided_by_2 = CurvedArrow(rect_6.get_corner(UL) + SMALL_BUFF, rect_3.get_corner(UR) + SMALL_BUFF)
        lower_arrow_square_root_64 = CurvedArrow(rect_64.get_corner(DL) - SMALL_BUFF, rect_8_geo.get_corner(DR) - SMALL_BUFF,
                                                angle=-TAU/4)
        upper_arrow_6_divided_by_3 = CurvedArrow(rect_6.get_corner(UL) + SMALL_BUFF, rect_2.get_corner(UR) + SMALL_BUFF)
        lower_arrow_cube_root_64 = CurvedArrow(rect_64.get_corner(DL) - SMALL_BUFF, rect_4.get_corner(DR) - SMALL_BUFF,
                                                 angle=-TAU / 4)

        sum_sign = MathTex("+").next_to(upper_arrow_sum, UP)
        times_sign = MathTex("\\times").next_to(lower_arrow_times, DOWN)
        minus_sign = MathTex("-").next_to(upper_arrow_substract, UP)
        divison_sign = MathTex(":").next_to(lower_arrow_divison, DOWN)
        text_3_plus_3 = MathTex("3+3").next_to(upper_arrow_3_plus_3, UP)
        text_2_times_3 = MathTex("2 \\times 3").next_to(upper_arrow_3_plus_3, UP)
        text_8_times_8 = MathTex("8 \\times 8").next_to(lower_arrow_8_times_8, DOWN)
        text_8_to_2 = MathTex("8^2").next_to(lower_arrow_8_times_8, DOWN)
        text_6_divided_by_2 = MathTex("\\frac{6}{2}").next_to(upper_arrow_6_divided_by_2, UP)
        text_square_root_64 = MathTex("\\sqrt[2]{64}").next_to(lower_arrow_square_root_64, DOWN)
        text_6_divided_by_3 = MathTex("\\frac{6}{3}").next_to(upper_arrow_6_divided_by_3, UP)
        text_cube_root_64 = MathTex("\\sqrt[3]{64}").next_to(lower_arrow_cube_root_64, DOWN)
        self.play(*[Create(i) for i in [rect_3, rect_5, rect_8_geo, rect_32]])
        self.wait()
        self.play(
            *[Create(i) for i in [upper_arrow_sum, lower_arrow_times, sum_sign, times_sign]],
            *[
                ReplacementTransform(i, j) for i, j in zip(
                    [rect_3.copy(), rect_5.copy(), rect_8_geo.copy(), rect_32.copy()],
                    [rect_8_arth, rect_8_arth, rect_256, rect_256]
                )
            ]
        )
        self.wait(2)
        self.play(
            *[FadeOut(i, shift=UP) for i in [sum_sign, upper_arrow_sum, rect_3, rect_5, rect_8_arth]],
            *[FadeOut(i, shift=DOWN) for i in [times_sign, lower_arrow_times, rect_8_geo, rect_32, rect_256]]
        )
        self.wait()

        self.play(*[Create(i) for i in [rect_8_arth, rect_6, rect_256, rect_64]])
        self.wait(2)
        self.play(
            *[Create(i) for i in [upper_arrow_substract, lower_arrow_divison, minus_sign, divison_sign]],
            *[
                ReplacementTransform(i, j) for i, j in zip(
                    [rect_8_arth.copy(), rect_6.copy(), rect_256.copy(), rect_64.copy()],
                    [rect_2, rect_2, rect_4, rect_4]
                )
            ]
        )
        self.wait()
        self.play(
            *[FadeOut(i, shift=UP) for i in [rect_2, rect_6, rect_8_arth, upper_arrow_substract, minus_sign]],
            *[FadeOut(i, shift=DOWN) for i in [rect_4, rect_64, rect_256, lower_arrow_divison, divison_sign]]
        )
        self.wait()

        self.play(*[Create(i) for i in [rect_3, rect_8_geo, rect_6, rect_64]])
        self.play(*[Create(i) for i in [upper_arrow_3_plus_3, lower_arrow_8_times_8]],
                  *[Write(i) for i in [text_3_plus_3, text_8_times_8]])
        self.wait()
        self.play(
            ReplacementTransform(text_3_plus_3, text_2_times_3),
            ReplacementTransform(text_8_times_8, text_8_to_2)
        )
        self.wait()

        self.play(
            *[
                ReplacementTransform(i, j) for i, j in zip(
                    [upper_arrow_3_plus_3, lower_arrow_8_times_8, text_2_times_3, text_8_to_2],
                    [upper_arrow_6_divided_by_2, lower_arrow_square_root_64, text_6_divided_by_2, text_square_root_64]
                )
            ]
        )
        self.wait()

        self.play(
            *[
                ReplacementTransform(i, j) for i, j in zip(
                    [upper_arrow_6_divided_by_2, lower_arrow_square_root_64, text_6_divided_by_2, text_square_root_64,
                     rect_3, rect_8_geo],
                    [upper_arrow_6_divided_by_3, lower_arrow_cube_root_64, text_6_divided_by_3, text_cube_root_64,
                     rect_2, rect_4]
                )
            ]
        )
        self.wait()

        self.play(
            *[FadeOut(i, shift=UP) for i in [upper_arrow_6_divided_by_3, text_6_divided_by_3, rect_2, rect_6]],
            *[FadeOut(i, shift=DOWN) for i in [lower_arrow_cube_root_64, text_cube_root_64, rect_4, rect_64]],
            ReplacementTransform(progression.get_entries(), progression_1.get_entries())
        )
        self.wait()

        color_for_8192 = BLUE_D
        color_for_4096 = PURPLE_D
        color_for_1024 = GREEN_D
        color_for_32 = MAROON_C

        calculation_left = MathTex(
            "\\sqrt", "{", "{", "8192", "\\times", "4096", "}", "\\over", "{", "1024", "}", "}"

        ).move_to(UP*1.5 + LEFT*3)
        three = MathTex("3").scale(0.5).next_to(calculation_left[3], UP * 0.4 + LEFT * 0.8)
        equivalent = MathTex("\\equiv").move_to(UP*1.5)
        equality = MathTex("=").move_to(UP*1.5)
        calculation_right = MathTex("(", "13", "+", "12", "-", "10", ")", "\\frac{1}{3}").move_to(UP*1.5 + RIGHT*3)
        result_5_right = MathTex("5").move_to(UP * 1.5 + RIGHT * 1.5).set_color(color_for_32)
        result_32_right = MathTex("32").move_to(UP*1.5 + RIGHT*1.5).set_color(color_for_32)

        for tex, color in zip(["13", "12", "10"], [color_for_8192, color_for_4096, color_for_1024]):
            calculation_right.set_color_by_tex(tex, color)

        rect_calculation_8192_4096, rect_calculation_8192_4096_1024, rect_calculation = list(
            map(
                SurroundingRectangle, [
                    calculation_left[i:j] for i, j in zip([3, 3, 0], [6, 10, -1])
                ]
            )
        )

        self.play(*[ShowIncreasingSubsets(i) for i in [calculation_left, three]])
        self.wait()

        self.play(
            Write(equivalent),
            *[
                FadeToColor(calculation_left[index], color) for index, color in zip(
                    [3, 5, 9],
                    [color_for_8192, color_for_4096, color_for_1024]
                )
            ],
            *[
                FadeToColor(progression_1_without_labels[index], color) for index, color in zip(
                    [-1, -2, -4, 12, 11, 9],
                    [color_for_8192, color_for_4096, color_for_1024, color_for_8192, color_for_4096, color_for_1024]
                )
            ]
        )
        self.wait()

        self.play(Create(rect_calculation_8192_4096))
        self.wait()
        self.play(
            Write(calculation_right[2]),
            ReplacementTransform(progression_1_without_labels[12].copy(), calculation_right[1]),
            ReplacementTransform(progression_1_without_labels[11].copy(), calculation_right[3])
        )
        self.wait()

        self.play(ReplacementTransform(rect_calculation_8192_4096, rect_calculation_8192_4096_1024))
        self.play(
            Write(calculation_right[4]),
            ReplacementTransform(progression_1_without_labels[9].copy(), calculation_right[5])
        )
        self.wait()
        self.play(ReplacementTransform(rect_calculation_8192_4096_1024, rect_calculation))
        self.play(
            *[Write(calculation_right[i]) for i in [0, 6]],
            ReplacementTransform(three.copy(), calculation_right[7]),
        )
        self.wait()

        self.play(
            ReplacementTransform(progression_1_without_labels[4].copy(), result_5_right),
            ReplacementTransform(calculation_right, result_5_right),
            *[FadeToColor(i, color_for_32) for i in [progression_1_without_labels[4], progression_1_without_labels[17]]]
        )
        self.wait()

        self.play(
            ReplacementTransform(equivalent, equality),
            ReplacementTransform(result_5_right, result_32_right),
            FadeOut(rect_calculation)
        )

        self.play(FadeOut(*self.mobjects))
        self.wait()

        self.play(Write(progression_copy.get_entries()))
        self.wait()
        brace_up = BraceText(progression_copy.get_entries_without_labels(), "Yapayları", brace_direction=UP, color=ORANGE)
        brace_up_1 = BraceText(progression_copy.get_entries_without_labels(), "Logaritmaları", brace_direction=UP, color=ORANGE)
        brace_down = BraceText(progression_copy.get_entries_without_labels(), "Esas Sayılar", brace_direction=DOWN, color=ORANGE)
        self.play(Write(brace_down))
        self.wait()
        self.play(Write(brace_up))
        self.wait()
        self.play(ReplacementTransform(brace_up, brace_up_1))
        self.wait()
        self.play(FadeOut(*self.mobjects))
        self.wait()

        regiomontanus = ImageMobject("regiomontanus.jpg").scale(1.5).move_to(LEFT * 4.5)
        rheticus = ImageMobject("rheticus.jpg").scale(1.7).move_to(LEFT*0.5)
        text_regiomontanus = Text("Regiomontanus \n"
                                  "1436-1476").scale(.5).next_to(regiomontanus, DOWN)
        text_rheticus = Text("Rheticus \n"
                             "1514-1574").scale(.5).next_to(rheticus, DOWN)
        degree_vs_sinus = MathTable(
            [["90^\\circ", "10^7"], [".", "."], ["..", ".."],
             ["30^\\circ", "5.000.000"], ["...", "..."], ["0^\\circ", "0"]],
            col_labels=[Text("Derece", font_size=24), Text("Sinüs", font_size=24)],
            h_buff=0.4
        ).to_edge(RIGHT)
        sinus_vs_logarithm = MathTable(
            [
                ["0", "1", "2", "..."],
                ["10.000.000", "9.999.900", "9.999.800", "..."]
            ], row_labels=[Text("Logaritma:", font_size=30), Text("Sinüs:", font_size=30)], h_buff=1
        ).get_entries()
        brace_1_down = BraceText(sinus_vs_logarithm[7], "$10^7 - \\frac{10^7}{10^7}$", color=ORANGE,font_size=30)
        brace_1_1_down = BraceText(sinus_vs_logarithm[7], "$10^7 (1-10^{-7})^1$", color=ORANGE, font_size=30)
        brace_2_down = BraceText(sinus_vs_logarithm[8], "$9.999.900-\\frac{9.999.900}{10^7}$", color=ORANGE, font_size=30)
        brace_2_2_down = BraceText(sinus_vs_logarithm[8], "$10^7 (1-10^{-7})^2$", color=ORANGE, font_size=30)

        self.play(*[FadeIn(i) for i in [rheticus, regiomontanus]],
                  *[Write(i) for i in [text_regiomontanus, text_rheticus]])
        self.wait()
        self.play(Write(degree_vs_sinus))
        self.wait()

        self.play(
            *[FadeOut(i, shift=LEFT) for i in [regiomontanus, text_regiomontanus]],
            *[FadeOut(i, shift=UP) for i in [rheticus, text_rheticus]],
            FadeOut(degree_vs_sinus, shift=RIGHT)
        )
        self.wait()

        self.play(Write(sinus_vs_logarithm))
        self.wait()
        self.play(*[Write(i) for i in [brace_1_down, brace_2_down]])
        self.wait()
        self.play(
            ReplacementTransform(brace_1_down, brace_1_1_down),
            ReplacementTransform(brace_2_down, brace_2_2_down)
        )
        self.wait()

        self.play(
            FadeOut(sinus_vs_logarithm[0:5], shift=UP),
            FadeOut(sinus_vs_logarithm[5:10], shift=DOWN),
            *[FadeOut(i) for i in [brace_1_1_down, brace_2_2_down]]
        )
        self.wait()


class NlogProperties(Scene):
    def construct(self):
        color_for_2 = YELLOW_D
        color_for_6 = PURPLE_C
        color_for_3 = ORANGE
        color_for_5 = BLUE_D
        color_for_8 = MAROON_C

        progression = MathTable(
            [[1, 2, 3, 4, 5, 6, 7, 8],
             [2, 4, 8, 16, 32, 64, 128, 256]], v_buff=1.2, h_buff=0.9,
            row_labels=[Text("Logaritmalar:", font_size=30), Text("Esas Sayılar:", font_size=30)]
        )
        progression_without_labels = progression.get_entries_without_labels()

        Nlog_summation_property = MathTex(
            "A", "\\times", "B", "=", "C", "\\times", "D", "\\Leftrightarrow",
            "Nlog(A)", "+", "Nlog(B)", "=", "Nlog(C)", "+", "Nlog(D)",
            substrings_to_isolate=["A", "B", "C", "D"],
        ).to_edge(UP, buff=.7)
        for tex, color in zip(["A", "B", "C", "D"], [color_for_2, color_for_6, color_for_3, color_for_5]):
            Nlog_summation_property.set_color_by_tex(tex, color)
        Nlog_subtraction_property = MathTex(
            "{", "A", "\\over", "B", "}", "=", "{", "C", "\\over", "D", "}", "\\Leftrightarrow",
            "Nlog(A)", "-", "Nlog(B)", "=", "Nlog(C)", "-", "Nlog(D)",
            substrings_to_isolate=["A", "B", "C", "D"],
        ).to_edge(UP, buff=.7)
        for tex, color in zip(["A", "B", "C", "D"], [color_for_8, color_for_6, color_for_5, color_for_3]):
            Nlog_subtraction_property.set_color_by_tex(tex, color)

        tex_3_plus_5 = MathTex("3", "+", "5", "=", "8").next_to(progression, UP).shift(DOWN*.6)
        tex_8_times_32 = MathTex("8", "\\times", "32", "=", "256").next_to(progression, DOWN).shift(UP*.6)
        for index, color in zip([0, 2, 4], [color_for_3, color_for_5, color_for_8]):
            tex_3_plus_5[index].set_color(color)
            tex_8_times_32[index].set_color(color)
        tex_2_plus_6 = MathTex("2", "+", "6", "=", "8").next_to(tex_3_plus_5, UP)
        tex_4_times_64 = MathTex("4", "\\times", "64", "=", "256").next_to(tex_8_times_32, DOWN)
        for index, color in zip([0, 2, 4], [color_for_2, color_for_6, color_for_8]):
            tex_2_plus_6[index].set_color(color)
            tex_4_times_64[index].set_color(color)
        tex_8_minus_6 = MathTex("8", "-", "6", "=", "2").next_to(progression, UP).shift(DOWN*.6)
        tex_256_over_64 = MathTex("{256", "\\over", "64}", "=", "4").next_to(progression, DOWN).shift(UP*.6)
        for index, color in zip([0, 2, 4], [color_for_8, color_for_6, color_for_2]):
            tex_8_minus_6[index].set_color(color)
            tex_256_over_64[index].set_color(color)
        tex_5_minus_3 = MathTex("5", "-", "3", "=", "2").next_to(tex_8_minus_6, UP)
        tex_32_over_8 = MathTex("{32", "\\over", "8}", "=", "4").next_to(tex_256_over_64, DOWN)
        for index, color in zip([0, 2, 4], [color_for_5, color_for_3, color_for_2]):
            tex_5_minus_3[index].set_color(color)
            tex_32_over_8[index].set_color(color)

        self.wait()
        self.play(Write(progression.get_entries()), run_time=2)
        self.wait()

        self.play(
            *[FadeToColor(progression_without_labels[index], color) for index, color in zip(
                [2, 4, 7, -6, -4, -1],
                [color_for_3, color_for_5, color_for_8]*2
            )]
        )
        self.wait()

        self.play(AnimationGroup(
            *[TransformFromCopy(progression_without_labels[i], tex_8_times_32[j]) for i, j in zip(
                [-6, -4, -1],
                [0, 2, 4]
            )],
            *[Write(tex_8_times_32[i]) for i in [1, 3]], lag_ratio=0.3
        ))
        self.wait()

        self.play(AnimationGroup(
            *[TransformFromCopy(progression_without_labels[i], tex_3_plus_5[j]) for i, j in zip(
                [2, 4, 7],
                [0, 2, 4]
            )],
            *[Write(tex_3_plus_5[i]) for i in [1, 3]], lag_ratio=0.3
        ))
        self.wait()

        self.play(
            *[FadeToColor(progression_without_labels[index], color) for index, color in zip(
                [1, 5, -7, -3],
                [color_for_2, color_for_6]*2
            )]
        )
        self.wait()

        self.play(AnimationGroup(
            *[TransformFromCopy(progression_without_labels[i], tex_4_times_64[j]) for i, j in zip(
                [-7, -3, -1],
                [0, 2, 4]
            )],
            *[Write(tex_4_times_64[i]) for i in [1, 3]], lag_ratio=0.3
        ))
        self.wait()

        self.play(AnimationGroup(
            *[TransformFromCopy(progression_without_labels[i], tex_2_plus_6[j]) for i, j in zip(
                [1, 5, 7],
                [0, 2, 4]
            )],
            *[Write(tex_2_plus_6[i]) for i in [1, 3]], lag_ratio=0.3
        ))
        self.wait(2)

        self.play(
            AnimationGroup(
                *[TransformFromCopy(tex_4_times_64[i], Nlog_summation_property[j]) for i, j in zip(
                    [0, 2],
                    [0, 2]
                )],
                TransformFromCopy(tex_2_plus_6[0], Nlog_summation_property[8:11]),
                TransformFromCopy(tex_2_plus_6[2], Nlog_summation_property[12:15]),
                *[TransformFromCopy(tex_8_times_32[i], Nlog_summation_property[j]) for i, j in zip(
                    [0, 2],
                    [4, 6]
                )],
                TransformFromCopy(tex_3_plus_5[0], Nlog_summation_property[16:19]),
                TransformFromCopy(tex_3_plus_5[2], Nlog_summation_property[20:]),
                *[Write(Nlog_summation_property[i]) for i in [1, 3, 5, 7, 11, 15, 19]],
                lag_ratio=0.2
            )
        )
        self.wait()

        self.play(FadeOut(*self.mobjects),
                  FadeToColor(progression.get_entries(), WHITE))
        self.add(progression.get_entries())
        self.wait()

        self.play(
            *[FadeToColor(progression_without_labels[index], color) for index, color in zip(
                [1, 2, 4, 5, 7, -7, -6, -4, -3, -1],
                [color_for_2, color_for_3, color_for_5, color_for_6, color_for_8]*2
            )]
        )
        self.wait()

        self.play(
            *[TransformFromCopy(progression_without_labels[i], tex_256_over_64[j]) for i, j in zip(
                [-1, -3, -7],
                [0, 2, 4]
            )],
            *[TransformFromCopy(progression_without_labels[i], tex_8_minus_6[j]) for i, j in zip(
                [7, 5, 1],
                [0, 2, 4]
            )],
            *[TransformFromCopy(progression_without_labels[i], tex_32_over_8[j]) for i, j in zip(
                [-4, -6, -7],
                [0, 2, 4]
            )],
            *[TransformFromCopy(progression_without_labels[i], tex_5_minus_3[j]) for i, j in zip(
                [4, 2, 1],
                [0, 2, 4]
            )],
            *[Write(tex[index]) for tex, index in zip(
                [tex_256_over_64, tex_8_minus_6, tex_32_over_8, tex_5_minus_3]*2,
                [1, 1, 1, 1, 3, 3, 3, 3]
            )]
        )
        self.wait()

        self.play(
            AnimationGroup(
                *[TransformFromCopy(tex_256_over_64[i], Nlog_subtraction_property[j]) for i, j in zip(
                    [0, 2],
                    [1, 3]
                )],
                TransformFromCopy(tex_8_minus_6[0], Nlog_subtraction_property[12:15]),
                TransformFromCopy(tex_8_minus_6[2], Nlog_subtraction_property[16:19]),
                *[TransformFromCopy(tex_32_over_8[i], Nlog_subtraction_property[j]) for i, j in zip(
                    [0, 2],
                    [7, 9]
                )],
                TransformFromCopy(tex_5_minus_3[0], Nlog_subtraction_property[20:23]),
                TransformFromCopy(tex_5_minus_3[2], Nlog_subtraction_property[24:]),
                *[Write(Nlog_subtraction_property[i]) for i in [2, 5, 8, 11, 15, 19, 23]],
                lag_ratio=0.2
            )
        )
        self.wait(2)

        self.play(FadeOut(*self.mobjects))


class ValueOfNlog(Scene):
    def construct(self):
        Nlog_of_proportions_in_2 = MathTex(
            r"{A \over 2A} = {5 \cdot 10^6 \over 10^7} &\Leftrightarrow \\ &Nlog(A) - Nlog(2A) =",
            "Nlog(5 \\cdot 10^6)", "-", "Nlog(10^7)",
            font_size=44
        ).to_edge(UL)
        Nlog_of_proportions_in_10 = MathTex(
            r"{A \over 10A} = {10^6 \over 10^7} &\Leftrightarrow \\ &Nlog(A) - Nlog(10A) =",
            "Nlog(10^6)", "-", "Nlog(10^7)",
            font_size=44
        ).align_to(Nlog_of_proportions_in_2, LEFT)
        cancel_2 = Arrow(
            Nlog_of_proportions_in_2[3].get_corner(DL), Nlog_of_proportions_in_2[3].get_corner(UR),
            color=RED, stroke_width=4, buff=0
        ).rotate(15*DEGREES)
        cancel_10 = Arrow(
            Nlog_of_proportions_in_10[3].get_corner(DL), Nlog_of_proportions_in_10[3].get_corner(UR),
            color=RED, stroke_width=4, buff=0
        ).rotate(15 * DEGREES)
        zero_2 = MathTex("0").next_to(cancel_2.get_end(), buff=0.1).shift(UP * 0.1)
        zero_10 = MathTex("0").next_to(cancel_10.get_end(), buff=0.1).shift(UP * 0.1)
        brace_2 = BraceText(Nlog_of_proportions_in_2[1], "= 6,931,469.22", font_size=36, color=ORANGE)
        brace_10 = BraceText(Nlog_of_proportions_in_10[1], "= 23,025,842.34", font_size=36, color=ORANGE)

        self.play(Write(Nlog_of_proportions_in_2))
        self.wait()
        self.play(AnimationGroup(
            Create(cancel_2),
            Write(zero_2),
            Create(brace_2),
            lag_ratio=0.4, run_time=2
        ))
        self.wait(2)
        self.play(
            FadeOut(*self.mobjects[-2:]),
            FadeOut(Nlog_of_proportions_in_2[-2:]),
            ReplacementTransform(Nlog_of_proportions_in_2[1],
                                 MathTex("6,931,469.22", font_size=44).next_to(Nlog_of_proportions_in_2[1], ORIGIN))
        )
        self.wait()

        self.play(Write(Nlog_of_proportions_in_10))
        self.wait()
        self.play(AnimationGroup(
            Create(cancel_10),
            Write(zero_10),
            Create(brace_10),
            lag_ratio=0.4, run_time=2
        ))
        self.wait(2)
        self.play(
            FadeOut(*self.mobjects[-2:]),
            FadeOut(Nlog_of_proportions_in_10[-2:]),
            ReplacementTransform(Nlog_of_proportions_in_10[1],
                                 MathTex("23,025,842.34", font_size=44).next_to(Nlog_of_proportions_in_10[1], ORIGIN).shift(RIGHT*0.4))
        )
        self.wait()


class Briggs(Scene):
    def construct(self):
        Nlog_summation_property = MathTex(
            #0
            "A", "\\times", "B", "=", "C", "\\times", "D", r"&\Leftrightarrow \\",
            #8                                                  17
            "&Nlog", "(", "A", ")", "+", "Nlog", "(", "B", ")", "=", "Nlog", "(", "C", ")", "+", "Nlog", "(", "D", ")",
            font_size=40
        ).move_to(UP*2 + LEFT)
        Nlog_A_times_B = MathTex(
            "A", "\\times", "B", "=", "(A \\times B)", "\\times", "1", r"&\Leftrightarrow \\",
            "&Nlog", "(", "A", ")", "+", "Nlog", "(", "B", ")", "=", "Nlog", "(", "A \\times B", ")", "+", "Nlog",
            "(", "1", ")",
            font_size=40
        ).next_to(Nlog_summation_property, ORIGIN).align_to(Nlog_summation_property, LEFT)
        Nlog_A_times_B[8:].align_to(Nlog_summation_property[8], LEFT)
        Nlog_A_times_B_rearranged_terms = MathTex(
            "A", "\\times", "B", "=", "(A \\times B)", "\\times", "1", r"&\Leftrightarrow \\",
            "&Nlog", "(", "A", ")", "+", "Nlog", "(", "B", ")", "-", "Nlog", "(", "1", ")",
            "=", "Nlog", "(", "A \\times B", ")",
            font_size=40
        ).next_to(Nlog_summation_property, ORIGIN).align_to(Nlog_summation_property, LEFT)
        Nlog_A_times_B_rearranged_terms[8:].align_to(Nlog_summation_property[3], LEFT)
        Nlog_subtraction_property = MathTex(
            "{A", "\\over", "B}", "=", "{C", "\\over", "D}", r"&\Leftrightarrow \\",
            "&Nlog", "(", "A", ")", "-", "Nlog", "(", "B", ")", "=",
            "Nlog", "(", "C", ")", "-", "Nlog", "(", "D", ")",
            font_size=40
        ).move_to(UP*0.3).align_to(Nlog_summation_property[0], LEFT)
        Nlog_subtraction_property[8:].align_to(Nlog_summation_property[8], LEFT)
        Nlog_A_over_B = MathTex(
            "{A", "\\over", "B}", "=", "{{A \\over B}", "\\over", "1}", r"&\Leftrightarrow \\",
            "&Nlog", "(", "A", ")", "-", "Nlog", "(", "B", ")", "=",
            "Nlog", "(", "{A \\over B}", ")", "-", "Nlog", "(", "1", ")",
            font_size=40
        ).next_to(Nlog_subtraction_property, ORIGIN).align_to(Nlog_summation_property[0], LEFT)
        Nlog_A_over_B[8:].align_to(Nlog_summation_property[8], LEFT).shift(UP*.07)
        Nlog_A_over_B_rearranged_terms = MathTex(
            "{A", "\\over", "B}", "=", "{{A \\over B}", "\\over", "1}", r"&\Leftrightarrow \\",
            "&Nlog", "(", "A", ")", "-", "Nlog", "(", "B", ")", "+", "Nlog", "(", "1", ")",
            "=", "Nlog", "(", "{A \\over B}", ")",
            font_size=40
        ).next_to(Nlog_subtraction_property, ORIGIN).align_to(Nlog_summation_property, LEFT)
        Nlog_A_over_B_rearranged_terms[8:].align_to(Nlog_summation_property[3], LEFT)
        Nlog_subtraction_property_for_10 = MathTex(
            "{A", "\\over", "10A}", "=", "{C", "\\over", "D}", r"&\Leftrightarrow \\",
            "&Nlog", "(", "A", ")", "-", "Nlog", "(", "10A", ")", "=",
            "Nlog", "(", "C", ")", "-", "Nlog", "(", "D", ")",
            font_size=40
        ).move_to(DOWN*2.5).align_to(Nlog_summation_property, LEFT)
        Nlog_subtraction_property_for_10[8:].align_to(Nlog_summation_property[8], LEFT)
        Nlog_of_proportions_in_10 = MathTex(
            "{A", "\\over", "10A}", "=", "{10^6", "\\over", "10^7}", r"&\Leftrightarrow \\",
            "&Nlog", "(", "A", ")", "-", "Nlog", "(", "10A", ")", "=",
            "Nlog", "(", "10^6", ")", "-", "Nlog", "(", "10^7", ")",
            font_size=40
        ).next_to(Nlog_subtraction_property_for_10, ORIGIN).align_to(Nlog_summation_property, LEFT)
        Nlog_of_proportions_in_10[8:].align_to(Nlog_summation_property[8], LEFT)
        Nlog_of_proportions_in_10_rearranged_terms = MathTex(
            "{A", "\\over", "10A}", "=", "{10^6", "\\over", "10^7}", r"&\Leftrightarrow \\",
            "&Nlog", "(", "A", ")", "-", "Nlog", "(", "10^6", ")", "+", "Nlog", "(", "10^7", ")",
            "=", "Nlog", "(", "10A", ")",
            font_size=40
        ).next_to(Nlog_subtraction_property_for_10, ORIGIN).align_to(Nlog_summation_property, LEFT)
        Nlog_of_proportions_in_10_rearranged_terms[8:].align_to(Nlog_summation_property[3], LEFT)
        Nlog_of_proportions_in_1_to_10_rearranged_terms = MathTex(
            "{A", "\\over", "10A}", "=", "{1", "\\over", "10}", r"&\Leftrightarrow \\",
            "&Nlog", "(", "A", ")", "-", "Nlog", "(", "1", ")", "+", "Nlog", "(", "10", ")",
            "=", "Nlog", "(", "10A", ")",
            font_size=40
        ).next_to(Nlog_subtraction_property_for_10, ORIGIN).align_to(Nlog_summation_property, LEFT)
        Nlog_of_proportions_in_1_to_10_rearranged_terms[8:].align_to(Nlog_summation_property[3], LEFT)

        summation_and_subtraction_group = VGroup(Nlog_A_over_B, Nlog_A_times_B)
        rect_sum_subtract, rect_10_times = list(map(
            SurroundingRectangle, [summation_and_subtraction_group, Nlog_of_proportions_in_10]
        ))
        text_summation_and_subtraction = Text(
            "Toplam ve Fark Formülleri",
            font_size=24, font="Times New Roman"
        ).next_to(rect_sum_subtract, UP).align_to(rect_sum_subtract, LEFT)
        text_10_times = Text(
            "10 Katının Logaritması",
            font_size=24, font="Times New Roman"
        ).next_to(rect_10_times, UP, buff=0.1).align_to(rect_10_times, LEFT)

        text_eq_1 = Text(
            "(Eq. 1)", slant=ITALIC, font_size=24, font="Times New Roman"
        ).next_to(Nlog_A_times_B_rearranged_terms[-1], RIGHT, buff=0.7)
        text_eq_2 = Text(
            "(Eq. 2)", slant=ITALIC, font_size=24, font="Times New Roman"
        ).next_to(Nlog_A_over_B_rearranged_terms[-1], RIGHT).align_to(text_eq_1, RIGHT)
        text_eq_3 = Text(
            "(Eq. 3)", slant=ITALIC, font_size=24, font="Times New Roman"
        ).next_to(Nlog_of_proportions_in_10_rearranged_terms[-1], RIGHT).align_to(text_eq_1, RIGHT)

        Nlog_1_161_A_times_B = BraceLabel(Nlog_A_times_B_rearranged_terms[-9:-5], "= 161,180,896", DOWN, color=ORANGE, font_size=24)
        Nlog_1_161_A_over_B = Brace(Nlog_A_over_B_rearranged_terms[-9:-5], UP, color=ORANGE)
        Nlog_1_7_times_10_to_10 = BraceLabel(Nlog_A_times_B_rearranged_terms[-9:-5], "= 7 \\cdot 10^{10}", DOWN, color=ORANGE, font_size=24)
        Nlog_1_0 = BraceLabel(Nlog_A_times_B_rearranged_terms[-9:-5], "= 0", DOWN, color=ORANGE, font_size=24)
        Nlog_1_0_for_eq_3 = BraceLabel(Nlog_of_proportions_in_1_to_10_rearranged_terms[-14:-10],
                                     "= 0",
                                     UP, color=ORANGE, font_size=24)
        Nlog_10_to_7_0 = BraceLabel(Nlog_of_proportions_in_10_rearranged_terms[-9:-5], "= 0", UP, color=ORANGE, font_size=24)
        Nlog_10_to_7_10_to_10 = BraceLabel(Nlog_of_proportions_in_10_rearranged_terms[-9:-5], "= 10^{10}", UP, color=ORANGE, font_size=24)
        Nlog_10_10_to_14 = BraceLabel(Nlog_of_proportions_in_1_to_10_rearranged_terms[-9:-5], "= 10^{14}", UP, color=ORANGE, font_size=24)
        Nlog_10_to_6_23 = BraceLabel(Nlog_of_proportions_in_10_rearranged_terms[-14:-10],
                                     "= 23,025,842",
                                     UP, color=ORANGE, font_size=24)
        Nlog_10_to_6_10_to_10 = BraceLabel(Nlog_of_proportions_in_10_rearranged_terms[-14:-10],
                                     "= 10^{10}",
                                     UP, color=ORANGE, font_size=24)
        Nlog_10_to_6_6_over_7 = BraceLabel(Nlog_of_proportions_in_10_rearranged_terms[-14:-10],
                                     "= {6 \\over 7} \\cdot 10^{10}",
                                     UP, color=ORANGE, font_size=24)
        self.play(
            *[Write(i) for i in [Nlog_summation_property, Nlog_subtraction_property, Nlog_subtraction_property_for_10,
                                 text_10_times, text_summation_and_subtraction]],
            *[Create(i) for i in [rect_sum_subtract, rect_10_times]], run_time=2
        )
        self.wait(2)
        self.play(
            #A x B  for C
            *[ReplacementTransform(Nlog_summation_property[i], Nlog_A_times_B[j]) for i, j in zip(
                [4, -7],
                [4, -7]
            )],
            Nlog_summation_property[5:8].animate.next_to(Nlog_A_times_B[5:8], ORIGIN),
            Nlog_summation_property[-6:].animate.next_to(Nlog_A_times_B[-6:], ORIGIN).shift(RIGHT*0.05),

            #A / B
            *[ReplacementTransform(Nlog_subtraction_property[i], Nlog_A_over_B[j]) for i, j in zip(
                [4, -7],
                [4, -7]
            )],
            Nlog_subtraction_property[-6:].animate.next_to(Nlog_A_over_B[-6:], ORIGIN).shift(RIGHT*0.05),

            #A / 10A
            *[ReplacementTransform(Nlog_subtraction_property_for_10[i], Nlog_of_proportions_in_10[j]) for i, j in zip(
                [4, -7],
                [4, -7]
            )],
            Nlog_subtraction_property_for_10[-6:].animate.next_to(Nlog_of_proportions_in_10[-6:], ORIGIN).shift(LEFT*.1),
            run_time=1.5
        )
        Nlog_A_over_B[6].next_to(Nlog_subtraction_property[5], DOWN, buff=0.15)
        self.wait()

        self.play(
            # A x B  for D
            *[ReplacementTransform(Nlog_summation_property[i], Nlog_A_times_B[j]) for i, j in zip(
                [6, 7, -2],
                [6, 7, -2]
            )],
            Nlog_summation_property[7].animate.next_to(Nlog_A_times_B[7], ORIGIN),
            Nlog_summation_property[-1].animate.next_to(Nlog_A_times_B[-1], ORIGIN).shift(RIGHT * 0.05),

            # A / B
            *[ReplacementTransform(Nlog_subtraction_property[i], Nlog_A_over_B[j]) for i, j in zip(
                [6, -2],
                [6, -2]
            )],
            Nlog_subtraction_property[-1].animate.next_to(Nlog_A_over_B[-1], ORIGIN).shift(RIGHT * 0.05),

            # A / 10A
            *[ReplacementTransform(Nlog_subtraction_property_for_10[i], Nlog_of_proportions_in_10[j]) for i, j in zip(
                [6, 7, -2],
                [6, 7, -2]
            )],
            Nlog_subtraction_property_for_10[-1].animate.next_to(Nlog_of_proportions_in_10[-1], ORIGIN).shift(UP*0.05),
            run_time=1.5
        )
        self.remove(*self.mobjects)
        self.add(rect_sum_subtract, rect_10_times, text_10_times, text_summation_and_subtraction)
        self.play(
            #A x B   for rearranging
            ReplacementTransform(Nlog_A_times_B[:17], Nlog_A_times_B_rearranged_terms[:17]),
            ReplacementTransform(Nlog_A_times_B[17:22], Nlog_A_times_B_rearranged_terms[22:]),
            ReplacementTransform(Nlog_A_times_B[22:], Nlog_A_times_B_rearranged_terms[17:22]),

            #A / B
            ReplacementTransform(Nlog_A_over_B[:17], Nlog_A_over_B_rearranged_terms[:17]),
            ReplacementTransform(Nlog_A_over_B[17:22], Nlog_A_over_B_rearranged_terms[22:]),
            ReplacementTransform(Nlog_A_over_B[22:], Nlog_A_over_B_rearranged_terms[17:22]),

            #A / 10A
            ReplacementTransform(Nlog_of_proportions_in_10[:17], Nlog_of_proportions_in_10_rearranged_terms[:17]),
            ReplacementTransform(Nlog_of_proportions_in_10[17:22], Nlog_of_proportions_in_10_rearranged_terms[22:]),
            ReplacementTransform(Nlog_of_proportions_in_10[22:], Nlog_of_proportions_in_10_rearranged_terms[17:22]),

            run_time=1.5
        )
        self.wait()

        self.play(*[Write(i) for i in [
            Nlog_1_161_A_times_B, Nlog_1_161_A_over_B, Nlog_10_to_7_0, Nlog_10_to_6_23,
            text_eq_1, text_eq_2, text_eq_3
        ]])
        self.wait()
        self.play(ReplacementTransform(Nlog_10_to_6_23, Nlog_10_to_6_10_to_10))
        self.wait()
        self.play(ReplacementTransform(Nlog_1_161_A_times_B, Nlog_1_7_times_10_to_10))
        self.wait()
        self.play(
            ReplacementTransform(Nlog_1_7_times_10_to_10, Nlog_1_0),
            ReplacementTransform(Nlog_10_to_7_0, Nlog_10_to_7_10_to_10)
        )
        self.wait()
        self.play(ReplacementTransform(Nlog_10_to_6_10_to_10, Nlog_10_to_6_6_over_7))
        self.wait()

        self.play(
            ReplacementTransform(
                Nlog_of_proportions_in_10_rearranged_terms,
                Nlog_of_proportions_in_1_to_10_rearranged_terms
            ),
            ReplacementTransform(
                Nlog_10_to_6_6_over_7, Nlog_1_0_for_eq_3
            ),
            ReplacementTransform(
                Nlog_10_to_7_10_to_10, Nlog_10_10_to_14
            )
        )
        self.wait()


class PampletOfBriggs(Scene):
    def construct(self):
        prima = ImageMobject("LogarithmorumChiliasPrima.png").move_to(DOWN / 2)
        text_prima = Text("Logarithmorum Chilias Prima", font_size=36,
                          font="Times New Roman").next_to(prima, UP)
        arithmetica = ImageMobject("Arithmetica_Logarithmica.jpg").scale(1.3).move_to(DOWN/2)
        text_arithmetica = Text("Arithmetica Logarithmica", font_size=36,
                          font="Times New Roman").next_to(arithmetica, UP)

        self.play(FadeIn(prima), Write(text_prima))
        self.wait()

        self.play(FadeOut(prima), Unwrite(text_prima))
        self.play(FadeIn(arithmetica), Write(text_arithmetica))
        self.wait()

        self.play(FadeOut(arithmetica), Unwrite(text_arithmetica))
        self.wait()


class NapierVsBriggs(Scene):
    def construct(self):
        napier_vs_birggsian_logarithm = MathTable(
            [
                ["Nlog(10^7) = 0", "Blog(1) = 0"],
                ["Nlog(9,999,900) = 1", "Blog(10^{14}) = 1"],
                ["Nlog(1) = 161,180,896", "Blog(1) = 0"],
                ["Nlog(2) = 6,931,469.22", "Blog(2) = 0.30102999566398"],
                ["Nlog(A) + Nlog(B) - Nlog(1) = Nlog(A \\times B)", "Blog(A) + Blog(B) = Blog(A \\times B)"],
                ["Nlog(A) - Nlog(B) + Nlog(1) = Nlog({A \\over B})", "Blog(A) - Blog(B) = Blog({A \\over B})"]
            ], col_labels=[Text("Napierian Logaritma", font_size=36), Text("Briggsian Logaritma", font_size=36)],
            line_config={"stroke_width": 2, "color": YELLOW}
        ).scale(0.65)
        napier_vs_birggsian_logarithm_get_entries = napier_vs_birggsian_logarithm.get_entries()
        b = MathTex("Blog(10) = 1").next_to(napier_vs_birggsian_logarithm_get_entries[5], ORIGIN).scale(0.65)

        self.play(
            *[Write(napier_vs_birggsian_logarithm_get_entries[i]) for i in [0, 1]],
            *[Create(napier_vs_birggsian_logarithm[i]) for i in [1, -1]]
        )
        self.wait()

        self.play(
            Write(napier_vs_birggsian_logarithm_get_entries[2:4]),
            Create(napier_vs_birggsian_logarithm[2])
        )
        self.wait()

        self.play(
            Write(napier_vs_birggsian_logarithm_get_entries[4:6]),
            Create(napier_vs_birggsian_logarithm[3])
        )
        self.wait()
        self.play(Transform(napier_vs_birggsian_logarithm_get_entries[5], b))
        self.wait()

        self.play(
            Write(napier_vs_birggsian_logarithm_get_entries[6:8]),
            Create(napier_vs_birggsian_logarithm[4])
        )
        self.wait()

        self.play(
            Write(napier_vs_birggsian_logarithm_get_entries[8:10]),
            Create(napier_vs_birggsian_logarithm[5])
        )
        self.wait()

        self.play(
            Write(napier_vs_birggsian_logarithm_get_entries[10:12]),
            Create(napier_vs_birggsian_logarithm[6])
        )
        self.wait()

        self.play(Write(napier_vs_birggsian_logarithm_get_entries[12:14]))
        self.wait()

        self.play(FadeOut(napier_vs_birggsian_logarithm))
        self.wait()


class OtherLogarithms(Scene):
    def construct(self):
        table = MathTable(
            [
                ["10^7(1-10^{-7})^n", "n"],
                ["10^n", "n"],
                ["10^7(1-10^{-7})^n", "(10^8-n) \\over 10^2"],
                ["10^8(1+10^{-4})^n", "10n"],
                ["10^5(1-10^{-5})^n", "n"],
                ["10^n", "10+n"],
                ["10^n", "10-n"]
            ],
            col_labels=[
                Text("Geometrik Dizi", font="Times New Roman", font_size=36),
                Text("Aritmetik Dizi", font="Times New Roman", font_size=36)
            ],
            row_labels=[
                Text("Napier, 1614", font="Times New Roman", font_size=36),
                Text("Briggs, 1617", font="Times New Roman", font_size=36),
                Text("Speidell, 1619", font="Times New Roman", font_size=36),
                Text("Bürgi, 1620", font="Times New Roman", font_size=36),
                Text("Kepler, 1624", font="Times New Roman", font_size=36),
                Text("Cavalieri, 1632", font="Times New Roman", font_size=36),
                Text("Caramuel, 1670", font="Times New Roman", font_size=36),
            ],v_buff=0.6, h_buff=3
        ).scale(0.7)

        self.play(Write(table), run_time=5)

        self.wait()

        self.play(FadeOut(table))
        self.wait()

