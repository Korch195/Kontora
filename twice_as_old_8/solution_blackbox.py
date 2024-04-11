def twice_as_old(dad_years_old, son_years_old):
    if dad_years_old < son_years_old:
        return (son_years_old * 2) - dad_years_old
    else:
        result = dad_years_old - (son_years_old * 2)
        return abs(result) if result < 0 else result