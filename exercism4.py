"""Functions to prevent a nuclear meltdown."""



def is_criticality_balanced(temperature, neutrons_emitted):
    product= temperature * neutrons_emitted
    if temperature < 800 and neutrons_emitted > 500 and product < 500000:
        return True
    else:
        return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power= voltage * current
    percentage_value= (generated_power/theoretical_max_power) * 100
    if percentage_value >= 80:
        print("green")
    if percentage_value < 80 and percentage_value >= 60:
        print("orange")
    if percentage_value < 60 and percentage_value >= 30:
        print("red")
    if percentage_value < 30:
        print("black")



def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    pass


balanced= is_criticality_balanced(625, 800)
print(balanced)