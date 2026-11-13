
import math
import re


def parse_order(items_csv):
    if not isinstance(items_csv, str) or not items_csv.strip():
        raise ValueError("Order must be a non-empty string")

    order = {}

    for item in items_csv.split(','):
        if item.count(':') != 1:
            raise ValueError("Each item must have name:quantity format")

        name, qty = item.split(':')
        name = name.strip()
        qty = qty.strip()

        if not name or not qty:
            raise ValueError("Item name and quantity cannot be empty")

        try:
            quantity = int(qty)
        except ValueError:
            raise ValueError("Quantity must be an integer")

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if name in order:
            raise ValueError("Duplicate items are not allowed")

        order[name] = quantity

    return order


def delivery_eta(distance_km):
    if isinstance(distance_km, bool):
        raise ValueError("Distance must be a positive number")

    try:
        distance = float(distance_km)
    except (ValueError, TypeError):
        raise ValueError("Distance must be a valid number")

    if not math.isfinite(distance) or distance <= 0:
        raise ValueError("Distance must be positive and finite")

    return int(15 + distance * 4)


def coupon_discount(code):
    if not isinstance(code, str):
        raise ValueError("Coupon code must be a string")

    code = code.strip().upper()

    if not re.fullmatch(r"SAVE[0-9]+", code):
        raise ValueError("Invalid coupon format. Expected SAVE followed by digits")

    return int(code[4:])


def main():
    print("==== Running parse_order ====")
    items = input("Enter items (e.g. pizza:2,burger:1): ")

    try:
        print("Order:", parse_order(items))
    except ValueError as e:
        print("Invalid order:", e)

    print("\n==== Running delivery_eta ====")
    distance = input("Enter distance in km (e.g. 4.5): ")

    try:
        print("ETA in Minutes:", delivery_eta(distance))
    except ValueError as e:
        print("Invalid distance:", e)

    print("\n==== Running coupon_discount ====")
    coupon = input("Enter coupon code (e.g. SAVE50): ")

    try:
        print("Discount:", coupon_discount(coupon))
    except ValueError as e:
        print("Invalid coupon:", e)


if __name__ == "__main__":
    main()
