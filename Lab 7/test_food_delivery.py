
import pytest
from hypothesis import given, settings, strategies as st

from food_delivery import parse_order, delivery_eta, coupon_discount


# FUZZ TEST 1: PARSE ORDER

@given(st.text() | st.none())
@settings(max_examples=200)
def test_parse_order_no_crash(s):
    try:
        result = parse_order(s)
        assert isinstance(result, dict)

        for name, quantity in result.items():
            assert isinstance(name, str)
            assert name.strip() != ""
            assert isinstance(quantity, int)
            assert quantity > 0

    except ValueError:
        pass


@given(
    st.text(
        alphabet=st.characters(
            whitelist_categories=("L", "N"),
            whitelist_characters=" _-"
        ),
        min_size=1
    ).filter(lambda x: x.strip() != ""),
    st.integers(min_value=1, max_value=1000)
)
def test_parse_order_valid(name, quantity):
    result = parse_order(f"{name}:{quantity}")
    assert result == {name.strip(): quantity}


def test_parse_order_multiple_items():
    assert parse_order("pizza:2,burger:1") == {
        "pizza": 2,
        "burger": 1
    }


# FUZZ TEST 2: DELIVERY ETA

@given(st.text() | st.none())
@settings(max_examples=200)
def test_delivery_eta_no_crash(s):
    try:
        result = delivery_eta(s)
        assert isinstance(result, int)
        assert result >= 15

    except ValueError:
        pass


@given(st.floats(
    min_value=0.01,
    max_value=10000,
    allow_nan=False,
    allow_infinity=False
))
def test_delivery_eta_valid(distance):
    result = delivery_eta(distance)
    assert result == int(15 + distance * 4)


def test_delivery_eta_numeric_string():
    assert delivery_eta("4.5") == 33


# FUZZ TEST 3: COUPON DISCOUNT

@given(st.text() | st.none())
@settings(max_examples=200)
def test_coupon_discount_no_crash(s):
    try:
        result = coupon_discount(s)
        assert isinstance(result, int)
        assert result > 0

    except ValueError:
        pass


@given(st.integers(min_value=1, max_value=100000))
def test_coupon_discount_valid(amount):
    assert coupon_discount(f"SAVE{amount}") == amount


def test_coupon_discount_case_insensitive():
    assert coupon_discount("save50") == 50


# EDGE CASE TESTS

@pytest.mark.parametrize("invalid_order", [
    "",
    "pizza",
    ":2",
    "pizza:0",
    "pizza:-1",
    "pizza:abc",
    "pizza:2,",
    "pizza:2,pizza:3",
    None
])
def test_invalid_orders(invalid_order):
    with pytest.raises(ValueError):
        parse_order(invalid_order)


@pytest.mark.parametrize("invalid_distance", [
    0,
    -1,
    "abc",
    "",
    None,
    float("inf"),
    float("nan")
])
def test_invalid_distances(invalid_distance):
    with pytest.raises(ValueError):
        delivery_eta(invalid_distance)


@pytest.mark.parametrize("invalid_coupon", [
    "",
    "SAVE",
    "INVALID50",
    "SAVE-50",
    "SAVE0",
    "SAVE50ABC",
    None
])
def test_invalid_coupons(invalid_coupon):
    with pytest.raises(ValueError):
        coupon_discount(invalid_coupon)
