assignment_1 = [.25, 100]
assignment_2 = [.10, 95]
assignment_3 = [.50, 85]
assignment_4 = [.15, 90]
assignment_5 = [0, 0]
assignment_6 = [0, 0]
assignment_7 = [0, 0]


def grade_calculation(part_1=[0, 0], part_2=[0, 0], part_3=[0, 0], part_4=[0, 0], part_5=[0, 0], part_6=[0, 0], part_7=[0, 0]):
    total_1 = part_1[0] * part_1[-1]
    total_2 = part_2[0] * part_2[-1]
    total_3 = part_3[0] * part_3[-1]
    total_4 = part_4[0] * part_4[-1]
    total_5 = part_5[0] * part_5[-1]
    total_6 = part_6[0] * part_6[-1]
    total_7 = part_7[0] * part_7[-1]
    final_grade = total_1 + total_2 + total_3 + \
        total_4 + total_5 + total_6 + total_7
    print("Your final grade is: " + str(final_grade))
    return final_grade


grade_calculation(assignment_1, assignment_2,
                  assignment_3, assignment_4, assignment_5)
