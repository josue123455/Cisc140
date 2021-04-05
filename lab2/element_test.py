from element import Element
import sys
import stdio


def main():
    atomic_number = 1
    name = 'Hydrogen'
    symbol = 'H'
    group = 1
    period = 1
    element_category = 'nonmetal'
    atomic_weight = 1.008
    phase = 'gas'





    a = Element(atomic_number,	name,	symbol,	group,	period,	element_category,	atomic_weight,	phase)

    stdio.writeln('Atomic_number:'+ str(a.get_atomic_number()))
    stdio.writeln('Name:' + str(a.get_name()))
    stdio.writeln('Symbol:' + str(a.get_symbol()))
    stdio.writeln('Group:' + str(a.get_group()))
    stdio.writeln('Period:' + str(a.get_period()))
    stdio.writeln('element_category:' + str(a.get_element_category()))
    stdio.writeln('Atomic_weight:' + str(a.get_atomic_weight()))
    stdio.writeln('Phase:' + str(a.get_phase()))


if __name__ == '__main__':
    main()
#python element_test.py
