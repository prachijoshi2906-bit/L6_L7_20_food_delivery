
import pytest
from hypothesis import given, settings, strategies as st

from processor import parse_order, delivery_eta, coupon_discount


@settings(max_examples=200)
@given(st.text() | st.none())
def test_parse_order_no_unexpected_crash(value):
    try:
        result = parse_order(value)
        assert isinstance(result, dict)
    except ValueError:
        pass


@settings(max_examples=200)
@given(st.text() | st.none())
def test_delivery_eta_no_unexpected_crash(value):
    try:
        result = delivery_eta(value)
        assert isinstance(result, int)
        assert result > 0
    except ValueError:
        pass


@settings(max_examples=200)
@given(st.text() | st.none())
def test_coupon_discount_no_unexpected_crash(value):
    try:
        result = coupon_discount(value)
        assert isinstance(result, int)
        assert result >= 0
    except ValueError:
        pass


@given(
    st.text(
        alphabet="abcdefghijklmnopqrstuvwxyz",
        min_size=1
    ),
    st.integers(min_value=1, max_value=1000)
)
def test_valid_order(name, quantity):
    result = parse_order(f"{name}:{quantity}")
    assert result == {name: quantity}


@given(st.floats(min_value=0.01, max_value=10000,
                 allow_nan=False, allow_infinity=False))
def test_valid_delivery_eta(distance):
    assert delivery_eta(distance) == int(15 + distance * 4)


@given(st.integers(min_value=0, max_value=100))
def test_valid_coupon(discount):
    assert coupon_discount(f"SAVE{discount}") == discount


@pytest.mark.parametrize("value", ["", None, "pizza", ":2", "pizza:abc",
                                   "pizza:0", "pizza:-1", "pizza:2,pizza:3"])
def test_invalid_orders(value):
    with pytest.raises(ValueError):
        parse_order(value)


@pytest.mark.parametrize("value", ["", None, "abc", "-1", "nan", "inf", "0"])
def test_invalid_distances(value):
    with pytest.raises(ValueError):
        delivery_eta(value)


@pytest.mark.parametrize("value", ["", None, "SAVE", "INVALID50",
                                   "SAVE-50", "SAVE50ABC"])
def test_invalid_coupons(value):
    with pytest.raises(ValueError):
        coupon_discount(value)
