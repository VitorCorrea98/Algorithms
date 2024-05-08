def study_schedule(permanence_period, target_time):
    if target_time is None or 0:
        return None

    counter = 0
    for schedule in permanence_period:
        if not all(
            isinstance(schedule_time, int) for schedule_time in schedule
        ):
            return None
        if schedule[0] <= target_time <= schedule[1]:
            counter += 1
    return counter
