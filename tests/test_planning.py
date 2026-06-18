from planning.path_planner import plan_path

def test_planning():
    assert plan_path(True) == "STOP"