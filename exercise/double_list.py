
kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
student_score = [0,0,0,0,0]

score = list(zip(kor_score, math_score, eng_score))
for i, s in enumerate(score):
    student_score[i] = int(sum(s)/3)

print(student_score)