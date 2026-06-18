from control.vehicle_controller import control_vehicle

def test_control():
    assert control_vehicle("GO") == "Vehicle Command: GO"