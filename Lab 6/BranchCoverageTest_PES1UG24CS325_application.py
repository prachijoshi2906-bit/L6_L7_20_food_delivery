
import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time


# DELIVERY CHARGE - TRUE AND FALSE BRANCHES

def test_distance_zero():
    with pytest.raises(ValueError):
        delivery_charge(0, 200, False)


def test_distance_above_15():
    with pytest.raises(ValueError):
        delivery_charge(16, 200, False)


def test_distance_within_range():
    assert delivery_charge(3, 200, False) == 20


def test_distance_between_3_and_8():
    assert delivery_charge(8, 200, False) == 40


def test_distance_above_8():
    assert delivery_charge(10, 200, False) == 60


def test_free_delivery_at_500():
    assert delivery_charge(5, 500, False) == 0


def test_free_delivery_above_500():
    assert delivery_charge(5, 600, False) == 0


def test_rainy_delivery():
    assert delivery_charge(2, 200, True) == 50


def test_non_rainy_delivery():
    assert delivery_charge(2, 200, False) == 20


# COUPON - TRUE AND FALSE BRANCHES

def test_coupon_none():
    assert apply_coupon(300, None, False) == 300


def test_invalid_coupon_code():
    with pytest.raises(ValueError):
        apply_coupon(300, "INVALID", True)


def test_welcome_first_order():
    assert apply_coupon(300, "WELCOME", True) == 200


def test_welcome_not_first_order():
    with pytest.raises(ValueError):
        apply_coupon(300, "WELCOME", False)


def test_save50_valid_coupon():
    assert apply_coupon(300, "SAVE50", False) == 250


def test_order_below_200():
    assert apply_coupon(150, "SAVE50", False) == 150


def test_order_exactly_200():
    assert apply_coupon(200, "SAVE50", False) == 150


# DELIVERY ETA - TRUE AND FALSE BRANCHES

def test_normal_time():
    assert estimated_time(5, False, False) == 35


def test_peak_hour_only():
    assert estimated_time(5, True, False) == 45


def test_busy_restaurant_only():
    assert estimated_time(5, False, True) == 50


def test_peak_and_busy():
    assert estimated_time(5, True, True) == 65
