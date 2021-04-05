class Element:
    def __init__(self, atomic_number,	name,	symbol,	group,	period,	element_category,	atomic_weight,	phase):
        self._atomic_number = atomic_number
        self._name = name
        self._symbol = symbol
        self._group = group
        self._period = period
        self._element_category = element_category
        self._atomic_weight = atomic_weight
        self._phase = phase


    def get_atomic_number(self):
        return self._atomic_number

    def get_name(self):
        return self._name

    def get_symbol(self):
        return self._symbol

    def get_group(self):
        if self._group is None:

            return "element has no group"
        else:
            return self._group


    def get_period(self):
        return self._period



    def get_element_category(self):
        return self._element_category

    def get_atomic_weight(self):
        return self._atomic_weight

    def get_phase(self):
        return self._phase


if __name__ == "__main__":
    main()
