# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-02-13 21:14:28
# @Last Modified by:   Administrator
# @Last Modified time: 2018-02-24 16:18:06
import random

class Creature():
	def __init__(self, name, hp):
		self.name = name
		self.hp   = hp

	def not_dead(self):
		if self.hp <= 0:
			return False
		else:
			return True

	def attack(self):
		return random.randint(0,50)

	def being_attack(self,attack_point):
		self.hp -= attack_point

	def show_status(self):
		print("{0}'s HP is {1}.".format(self.name,self.hp))


player = Creature("李狗蛋",100)
enemy  = Creature("小怪",80)


while player.not_dead() and enemy.not_dead():
	player.show_status()
	enemy.show_status()
	user_input = input("Attack or Defence(A/D)\n")

	if user_input == "A":
		player_attack_value = player.attack()
		enemy.being_attack(player_attack_value)

		enemy_attack_value = enemy.attack()
		player.being_attack(enemy_attack_value)
	elif user_input == "D":
		enemy_attack_value = enemy.attack()
		player.being_attack(0.2*enemy_attack_value)
	else:
		print("Wrong input")


if player.not_dead():
	print("You win!")
else:
	print("You loss.")