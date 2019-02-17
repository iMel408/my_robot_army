from datetime import datetime
import random

file = open('robot_names_samp.txt')
line = file.readlines()

def line_split(line,index):
    return line.split("\n")[index]

print(line_split(line,0))
# class Robot(object):
#
#     def __init__(self):
#
#     self.unit_id = id(object)
#     self.unit_name = random.rand(names_list).pop()
#     self.status = "Active"
#     self.date_built = datetime.now()
#     self.health_level = 100
#     self.last_health_check = datetime.now()
#
#     # charge capacity and level hours
#     self.charge_capacity = 12
#     self.charge_level = 0
#
#     # health level in units of 10/100.
#
#     def check_health(self):
#
#         self.last_health_check = datetime.now()
#         self.shots_absorbed = random.randrange(1,101,10)
#         self.current_health =
#
#
#     def charge(self):
#
#         self.charge_level = self.charge_capacity
#         self.last_full_charge = datetime.now()
#         print("Fully Charged. 12 hours remaining")
#
#
#     def check_charge(self):
#         """ check the number of hours of charge left"""
#
#         charge_remaining = diff.total_seconds(self.last_full_charge  - datetime.now()) / 3600
#
#         return charge_remaining
#
#
#     def check_battle_inventory(self):
#
