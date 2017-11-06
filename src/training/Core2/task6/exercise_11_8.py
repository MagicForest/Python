def is_leap_year(year):
    return (year % 4 ==0 and year % 100 != 0) or (year % 400 == 0)


def filter_leap_year(year_list):
    return filter(lambda year : is_leap_year(year), year_list)


def filter_leap_year_by_list_comprehension(year_list):
    return [year_list[i] for i in range(len(year_list)) if is_leap_year(year_list[i])]
