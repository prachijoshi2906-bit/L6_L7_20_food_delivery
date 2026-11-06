
import math
import re


def parse_order(items_csv):
    if not isinstance(items_csv, str) or not items_csv.strip():
        raise ValueError("Order must be a non-empty string")

    order = {}

    for item in items_csv.split(','):
        if item.count(':') != 1:
            raise ValueError("Each item must have the format name:quantity")

        name, qty = item.split(':')
        name = name.strip()

        if not name:
            raise ValueError("Item name cannot be empty")

        if name in order:
            raise ValueError("Duplicate item names are not allowed")

        try:
            quantity = int(qty.strip())
        except (ValueError, AttributeError):
            raise ValueError("Quantity must be an integer")

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        order[name] = quantity

    return order


def delivery_eta(distance_km):
    if isinstance(distance_km, bool) or distance_km is None:
        raise ValueError("Distance must be a positive number")

    try:
        distance = float(distance_km)
    except (ValueError, TypeError):
        raise ValueError("Distance must be a positive number")

    if not math.isfinite(distance) or distance <= 0:
        raise ValueError("Distance must be a positive number")

    return int(15 + distance * 4)


def coupon_discount(code):
    if not isinstance(code, str):
        raise ValueError("Coupon code must be a string")

    match = re.fullmatch(r"SAVE([0-9]+)", code.strip().upper())

    if not match:
        raise ValueError("Invalid coupon code")

    discount = int(match.group(1))

    if discount <= 0:
        raise ValueError("Discount must be positive")

    return discount


def main():
    print("==== Running parse_order ====")
    user_input = input("Enter items as name:qty CSV (e.g. pizza:2,burger:1): ")
    result = parse_order(user_input)
    print("Order:", result)

    print("\n==== Running delivery_eta ====")
    user_input = input("Enter distance in km (e.g. 4.5): ")
    result = delivery_eta(user_input)
    print("ETA in Minutes:", result)

    print("\n==== Running coupon_discount ====")
    user_input = input("Enter a coupon code (e.g. SAVE50): ")
    result = coupon_discount(user_input)
    print("Discount:", result)


if __name__ == "__main__":
    main()
