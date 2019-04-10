###exercise_lec06###
###10-04-19 sieun Bae###

import math
# a. sum_n(n): returns the sum of the first n natural numbers.
def sum_n(n):
	sum = 0
	for i in range(1,n+1):
		sum += i
	return sum

#b.	sum_n_cubes(n): returns the sum of the cubes of the first n natural numbers

def sum_n_cubes(n):
	sum = 0
	for i in range(1, n+1):
		sum += pow(i,3)
	return sum

#c.	sum_list(nums): nums is a list of numbers, returns the sum of the numbers in the list

def sum_list(nums):
	sum = 0
	for i in nums:
		sum += nums
	return sum

#d.	square_each(nums): nums is a list of numbers, modifies the list by squaring each entry.

def square_each(nums):
	for i in range(len(nums)):
		nums[i] = nums ** 2

#e.	to_numbers(str_list): str_list is a list of strings, each of which represents a number. Modifies each entry in the list by converting it to a number.

def to_numbers(str_list):
	for i in range(len(str_list)):
		int_list[i] = int(str_list[i])
	return int_list


#f.	A professor gives 5-point quizzes that are graded on the scale 5(A), 4(B), 3(C), 2(D), 1(E), 0(F). 
#Write a function grade(score) that accepts a quiz score as an input and prints out the corresponding grade

def grade(score):
	return "FEDCBA"[score]

def main():
	score = int(input("Please input your score (0-5)")
	print("The grade is", grade(score))
