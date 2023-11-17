"""
Goat-related utilities, including a random goat name generator.

@author GCCIS Faculty
"""
import random

__FIRST_NAMES__ = [
    'Allison', 'Beauregard', 'Bleats', 'Bleaty', 'Brad', 'Brynn', 'Charlie', 
    'Dave', 'Gerald', 'Goat', 'Goatbert', 'Goaty', 'Hairy', 'Harold', 'Harry', 
    'Jacie', 'Janet', 'Jessica', 'Jim', 'Joseph', 'Karen', 'Max', 'Randall', 
    'Reginald', 'Rob', 'Tippy'
]

__LAST_NAMES__ = [
    'Bahramewe', 'Bleater', 'Bleaterson', 'Drumpf', 'Farmington', 'Fisher', 
    'Goat', 'Goater', 'Goatson', 'Hairybutt', 'Harrison', 'Johnson', 
    'McGoatface', 'Oliver', 'Peterson', 'Reynolds', 'Sharma', 'Smith', 
    'Spiner', 'Stewart', 'Wilson', 'Winthorpe'
]

__SUFFIXES__ = [
    "Esq.", "Jr.", "Sr.", "III", "IV"
]

def make_goat_name():
    """
    Generates and returns a random goat name. There is a 25% chance of a middle
    initial. There is a 10% chance of a suffix, e.g. "Jr." There is also a 5%
    chance that the goat's last name will begin with "O'" or "Mc".
    """
    name = __FIRST_NAMES__[random.randrange(len(__FIRST_NAMES__))]
    last_name = __LAST_NAMES__[random.randrange(len(__LAST_NAMES__))]

    if random.random() < 0.25:
        middle_initial = chr(random.randint(0, 25) + 65)
        name += " " + middle_initial + "."

    o_or_mc = random.random()
    if o_or_mc < 0.05:
        last_name = "O'" + last_name
    elif o_or_mc > 0.95:
        last_name = "Mc" + last_name

    name += " " + last_name

    if random.random() < 0.10:
        name += " " + __SUFFIXES__[random.randrange(len(__SUFFIXES__))]

    return name

def main():
    for i in range(50):
        name = make_goat_name() + "\t"
        if len(name) < 14:
            name += "\t"
        name += make_goat_name()
        print(name)

if __name__ == "__main__":
    main()