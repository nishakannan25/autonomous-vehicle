def plan_path(object_detected):
    """
    Plans vehicle action.
    """
    if object_detected:
        return "STOP"
    return "GO"