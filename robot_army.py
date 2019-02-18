from datetime import datetime, timedelta
from random import randrange, sample
import decimal


from math import ceil

SECONDS_PER_HOUR = 3600

file = open('robot_names_samp.txt')
# names_list = file.readlines()
lines = file.read().splitlines()

    #TODO: create dictionary to hold robot inventory. Maybe one for each status

class Robot():
    """create evil robot for my army"""

    def __init__(self):

        self.unit_id = id(self)
        print("self.unit_id:", self.unit_id)
        names = sample(lines, len(lines))
        self.unit_name = names.pop(0)
        print("self.unit_name:", self.unit_name)
        self.status = 'active' #inactive
        print("self.status:", self.status)
        self.date_built = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("self.date_built:", self.date_built)
        self.health_level = 100
        self.health_capacity = 100 #TODO: move to subclass
        print("self.health_level (initial):", self.health_level)
        self.condition = 'good'  #critical
        print("self.condition:", self.condition)
        self.last_health_check = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("self.last_health_check:", self.last_health_check)
        # charge capacity and level in hours
        self.charge_capacity = 12
        print("self.charge_capacity:", self.charge_capacity)
        self.charge_level = 0
        print("charge_level (initial):", self.charge_level)


    def charge(self):
        """ charge the robot to capacity"""

        self.charge_level = self.charge_capacity
        self.last_full_charge = datetime.now()
        print("charge_level (after):", self.charge_level)
        # print("Fully Charged. 12 hours remaining")

        # health level in units of 10/100.

    def check_condition(self):
        """ check the robots current health status"""

        self.last_health_check = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.shots_incurred = randrange(1,101,10)
        self.health_level = self.health_level - self.shots_incurred


        if self.health_level in range(1,31) and self.charge_level in range(1,round(self.charge_capacity/3)):
            self.condition = 'critical'
        elif self.health_level in range(31,self.health_capacity + 1) \
                and self.charge_level in range(round(self.charge_capacity/3),self.charge_capacity):
            self.condition = 'good'
        else:
            self.condition = 'out of commission'
            self.status = 'inactive'



        # self.current_health = diff(self.last_health_check, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("self.health_level:", self.health_level)
        print("self.shots_incurred:", self.shots_incurred)
        print("self.condition:", self.condition)
        print("self.status:", self.status)
        print("self.last_health_check:", self.last_health_check)
        # print("self.current_health:", self.current_health)

    def check_charge(self):
        """ check the number of hours of charge left"""

        charge_remaining = round((datetime.now() - self.last_full_charge).total_seconds() / SECONDS_PER_HOUR)

        print("self.charge_remaining:", charge_remaining)


# decimal.Decimal('3.5').quantize(decimal.Decimal('1'),
#     rounding=decimal.ROUND_HALF_DOWN)

new_robot = Robot()
new_robot.charge()
new_robot.check_condition()
new_robot.check_charge()


class Role(Robot):
    """ assign robot a role from the following categories
    tank/damage/support based on what the current needs are
    """
    pass

class SubRole(Role):
    """ assign robot a subrole from the following categories
    sniper/builder/healer based on what the current needs are
    """
    pass

def check_battle_inventory():
    """ create report on number of units cut by role/subrole/status/health_condition/
    """
    pass

class Skirmishes():
    """create battle scenarios to be applied to overall battle"""

    #
    # def apply_damage(self):

    pass




