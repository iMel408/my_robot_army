from datetime import datetime
from random import randrange, sample

SECONDS_PER_HOUR = 3600

file = open('robot_names.txt')
lines = file.read().splitlines()


# TODO: create dictionary to hold robot inventory. Maybe one for each status
# TODO: test all logic dependant on diff between timestamps by manually adding to the initial datetime values.

class Robot():
    """create evil robot for my army"""

    def __init__(self):

        names = sample(lines, len(lines))  # random sample the entire list

        self.unit_id = id(self)
        self.unit_name = names.pop(0)
        self.status = 'active'  # inactive
        self.date_built = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.health_capacity = 100  # TODO: move to subclass
        self.health_level = 100
        self.condition = 'good'  # critical
        self.last_health_check = datetime.now()  # .strftime("%Y-%m-%d %H:%M:%S")
        # charge capacity and level in hours
        self.charge_capacity = 12
        self.charge_level = 0

    def charge(self):
        """ charge the robot to capacity"""

        self.charge_level = self.charge_capacity
        self.last_full_charge = datetime.now()
        # print("Fully Charged. 12 hours remaining")

        # health level in units of 10/100.

    def check_charge(self):
        """ check the number of hours of charge left"""
        datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'

        diff = datetime.strptime(str(datetime.now()), datetimeFormat) \
               - datetime.strptime(str(self.last_full_charge), datetimeFormat)

        self.charge_hours_remaining = diff.seconds / 3600
        # charge_minutes_remaining = diff.seconds / 60

        self.charge_level = int(self.charge_level - self.charge_hours_remaining)

    def check_condition(self):
        """ check the robots current health status"""

        self.shots_incurred = randrange(1, 101, 10)   #TODO: move to a new class? InflictDamage maybe?
        self.health_level = self.health_level - self.shots_incurred

        if self.health_level in range(1, 31) and self.charge_level in range(1, round(self.charge_capacity / 3)):
            self.condition = 'critical'
        elif self.health_level in range(31, self.health_capacity + 1) \
                and self.charge_level in range(round(self.charge_capacity / 3), self.charge_capacity + 1):
            self.condition = 'good'
        else:
            self.condition = 'out of commission'
            self.status = 'inactive'

        self.last_health_check = datetime.now()  # .strftime("%Y-%m-%d %H:%M:%S")


print(">> Call Robot() class")
new_robot = Robot()

print("unit_id:", new_robot.unit_id)
print("unit_name:", new_robot.unit_name)
print("date_built:", new_robot.date_built)
print("[initial] status:", new_robot.status)
print("[initial] health_level:", new_robot.health_level)
print("[initial] condition:", new_robot.condition)
print("[initial] last_health_check:", new_robot.last_health_check)
print("[initial] charge_level:", new_robot.charge_level)
print()

print(">> Call charge() method")
new_robot.charge()

print("[updated] charge_level:", new_robot.charge_level)
print("[updated] last_full_charge:", new_robot.last_full_charge)
print()

print(">> Call check_charge() method")
new_robot.check_charge()

print("charge_hours_remaining:", new_robot.charge_hours_remaining)
print("[updated] charge_level:", new_robot.charge_level)
print()

print(">> Call check_condition() method")
new_robot.check_condition()

print("shots_incurred:", new_robot.shots_incurred)
print("[updsted] health_level:", new_robot.health_level)
print("[updated] charge_level:", new_robot.charge_level)
print("[updated] condition:", new_robot.condition)
print("[updated] status:", new_robot.status)
print()


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

    def check_inventory():
        """ create report on number of units cut by role/subrole/status/health_condition/
        """

    pass


class Skirmishes():
    """create battle scenarios to be applied to overall battle"""

    # def apply_damage(self):

    pass
