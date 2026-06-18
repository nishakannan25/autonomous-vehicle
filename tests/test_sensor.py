from sensor_drivers.lidar import get_lidar_data

def test_sensor():
    assert get_lidar_data() == 100