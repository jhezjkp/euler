#!/usr/bin/env python
#encoding=utf-8

def num2words(num):
	if num == 1:
		return "one"
	elif num == 2:
		return "two"
	elif num == 3:
		return "three"
	elif num == 4:
		return "four"
	elif num == 5:
		return "five"
	elif num == 6:
		return "six"
	elif num == 7:
		return "seven"
	elif num == 8:
		return "eight"
	elif num == 9:
		return "nine"
	elif num == 10:
		return "ten"
	elif num == 11:
		return "eleven"
	elif num == 12:
		return "twelve"
	elif num == 13:
		return "thirteen"
	elif num == 14:
		return "fourteen"
	elif num == 15:
		return "fifteen"
	elif num == 16:
		return "sixteen"
	elif num == 17:
		return "seventeen"
	elif num == 18:
		return "eighteen"
	elif num == 19:
		return "nineteen"
	elif num == 20:
		return "twenty"
	elif num == 30:
		return "thirty"
	elif num == 40:
		return "fourty"
	elif num == 50:
		return "fifty"
	elif num == 60:
		return "sixty"
	elif num == 70:
		return "seventy"
	elif num == 80:
		return "eighty"
	elif num == 90:
		return "ninety"
	elif num >20 and num < 100:
		n = num / 10 * 10
		return num2words(n) + "-" + num2words(num - n)
	elif num >= 100 and num < 1000:
		n = num / 100
		s = num2words(n) + " hundred"
		if num % 100 == 0:
			return s
		s += " and " + num2words(num - n * 100)
		return s
	elif num >= 1000 and num < 10000:
		n = num / 1000
		s = num2words(n) + " thousand"
		if num % 1000 == 0:
			return s
		s += " " + num2words(num - n * 1000)
		return s


# for i in range(1, 108):
# 	print num2words(i)
# print num2words(300)
# print num2words(304)
# print num2words(624)
# print num2words(1354)

total_letters = 0
for i in range(1, 1001):
	total_letters += len(num2words(i))
print total_letters