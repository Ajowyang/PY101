def get_grade(score1, score2, score3):
	avg = (score1 + score2 + score3) / 3
	if avg >= 90 and avg <= 100:
		return 'A'
	elif avg < 90 and avg >= 80:
		return 'B'
	elif avg < 80 and avg >=70:
		return 'C'
	elif avg < 70 and avg >= 60:
		return 'D'
	elif avg < 60 and avg >= 0:
		return 'F'

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True
