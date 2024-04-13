def twice_as_old(dad_years_old, son_years_old):
    # Calculate the difference in ages
    age_difference = dad_years_old - son_years_old

    # If the father is currently twice as old as his son,
    # then the difference in ages is equal to the son's age
    if age_difference == son_years_old:
        return 0

    # If the father is currently more than twice as old as his son,
    # then we need to find out how many years ago the father was twice as old
    elif age_difference > son_years_old:
        return age_difference - son_years_old

    # If the father is currently less than twice as old as his son,
    # then we need to find out how many years in the future the father will be twice as old
    else:
        return son_years_old - age_difference