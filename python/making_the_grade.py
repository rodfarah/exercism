"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    rounded_scores = []
    for nota in student_scores:
        rounded_scores.append(round(nota))

    return rounded_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    notas_reprovadas = []
    for grade in student_scores:
        if grade <= 40:
            notas_reprovadas.append(grade)
    return len(notas_reprovadas)


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    aproved_notes = []
    for note in student_scores:
        if note >= threshold:
            aproved_notes.append(note)

    return aproved_notes


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    letter_gap = ((highest - 40)/4)
    d_group = 41
    c_group = int(d_group + letter_gap)
    b_group = int(c_group + letter_gap)
    a_group = int(b_group + letter_gap)

    l_grades = [d_group, c_group, b_group, a_group]
    return l_grades


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    position_list = 1
    final_list = []
    for name, ranking in zip(student_names, student_scores):
        final_list.append(str(f'{position_list}. {name}: {ranking}'))
        position_list += 1
    return final_list


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for student in student_info:
        if student[1] == 100:
            return student
    return []
