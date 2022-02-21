# tests/test_lib.py
from mlproject.distance import haversine

def haversine(lon1, lat1, lon2, lat2):
    assert haversine(48.865070, 2.380009, 47.865071, 1.380009) == 133.4960462817939
