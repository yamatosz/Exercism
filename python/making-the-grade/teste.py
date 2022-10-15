from loops import (round_scores,
                   count_failed_students,
                   above_threshold,
                   letter_grades,
                   student_ranking,
                   perfect_score)

student_scores = [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
print(round_scores(student_scores))
print(count_failed_students(student_scores=[90,40,55,70,30,25,80,95,38,40]))
print(above_threshold(student_scores=[90,40,55,70,30,68,70,75,83,96], threshold=75))
print(letter_grades(highest=88))
student_scores = [100, 99, 90, 84, 66, 53, 47]
student_names=  ['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred']
print(student_ranking(student_scores, student_names))
print(perfect_score(student_info=[["Charles", 90], ["Tony", 80], ["Alex", 100]]))
print(perfect_score(student_info=[["Charles", 90], ["Tony", 80]]))