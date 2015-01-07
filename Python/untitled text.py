import random
questions = ["Are you ok?","Are you playing?","You know what I mean?","Hi"]

while True:
	ran = random.randint(0,len(questions)-1)
	print questions[ran]
	ans = raw_input()
	ans = ans.upper()
	if ans == "YES" or ans == "NO" or ans == "" or ans == "YEAH" or ans == "OK":
		n = 0
		while n < 1000000000000000000:
			print "Fail"
		break
		