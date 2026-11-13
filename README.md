# Software Engineering – Testing Labs 6 & 7

**Student Name:** Prachi Ganesh Joshi  
**SRN:** PES1UG24CS325  
**Course:** Software Engineering / Testing Labs

## Project Overview

This repository contains the implementation and testing work for Lab 6 and Lab 7 using Python-based applications.

The two labs focus on different software testing techniques:

- **Lab 6 – Code and Branch Coverage Analysis:** Evaluating application logic using pytest and measuring code and branch coverage.
- **Lab 7 – Fuzz Testing:** Testing application functions with automatically generated inputs using the Hypothesis property-based testing framework.

---

# Lab 6 – Code and Branch Coverage Analysis

## Objective

The objective of Lab 6 is to analyse the effectiveness of test cases by measuring code coverage and branch coverage of the Food Delivery Application.

## Application Description

The application contains three main functions:

### `delivery_charge(distance_km, order_value, is_raining)`

- Calculates delivery charges based on distance and order value.
- Provides free delivery for orders worth ₹500 or more.
- Applies additional charges during rainy conditions.
- Validates the delivery distance.

### `apply_coupon(order_value, code, is_first_order)`

- Applies valid coupon discounts.
- Checks coupon validity and first-order eligibility.
- Handles orders below the minimum discount threshold.

### `estimated_time(distance_km, is_peak_hour, restaurant_busy)`

- Estimates delivery time based on distance.
- Adds extra time during peak hours and when the restaurant is busy.

## Testing Approach

Pytest was used to write test cases covering normal inputs, boundary conditions, and exceptional scenarios.

Two separate test files were created:

- `CodeCoverageTest_PES1UG24CS325_application.py`
- `BranchCoverageTest_PES1UG24CS325_application.py`

## Code Coverage

Code coverage measures the percentage of executable statements that are executed by the test cases.

The test suite covers:

- Valid delivery charge calculations.
- Invalid delivery distances.
- Coupon application and validation.
- Free delivery conditions.
- Delivery time calculations.
- Peak-hour and restaurant-busy conditions.

## Branch Coverage

Branch coverage measures whether each possible decision outcome in the application has been executed.

The tests cover both true and false outcomes of conditional statements, including nested conditions and exception-handling paths.

## Results

| Metric | Result |
|---|---:|
| Code Coverage Tests | 16 passed |
| Code Coverage | 100% |
| Branch Coverage Tests | 20 passed |
| Branch Coverage | 100% |
| Total Statements | 33 |
| Total Branches | 24 |
| Partial Branches | 0 |

Both code coverage and branch coverage achieved 100%.

## Commands to Run

Navigate to the Lab 6 directory:

```bash
cd "Lab 6"
```

Install dependencies:

```bash
py -m pip install pytest pytest-cov
```

Run code coverage tests:

```bash
py -m pytest CodeCoverageTest_PES1UG24CS325_application.py --cov=food_delivery --cov-report=term-missing
```

Run branch coverage tests:

```bash
py -m pytest BranchCoverageTest_PES1UG24CS325_application.py --cov=food_delivery --cov-branch --cov-report=term-missing
```

---

# Lab 7 – Fuzz Testing

## Objective

The objective of Lab 7 is to test application robustness using fuzz testing and automatically generated inputs.

Hypothesis is used to generate different input values, including unexpected, invalid, and boundary-case inputs, to identify potential failures.

## Application Description

The application contains three main functions:

### `parse_order(items_csv)`

- Parses comma-separated order items.
- Extracts item names and quantities.
- Validates the input format and quantities.
- Handles malformed order inputs and invalid quantities.

### `delivery_eta(distance_km)`

- Calculates estimated delivery time based on distance.
- Converts the input into a numeric value.
- Validates invalid, non-finite, and non-positive distance values.

### `coupon_discount(code)`

- Extracts the discount value from a coupon code.
- Validates coupon code formatting.
- Handles invalid coupon inputs.

## Testing Approach

The Hypothesis library was used along with pytest to perform property-based and fuzz testing.

The test file is:

- `test_processor.py`

The testing strategy includes:

- Generating random text inputs.
- Testing empty and invalid inputs.
- Testing `None` values.
- Checking valid order parsing.
- Testing different delivery distances.
- Testing valid and invalid coupon codes.
- Checking expected output properties.
- Testing boundary conditions and malformed inputs.
- Using parameterized tests for specific invalid inputs.

## Bug Identification and Fixing

The initial implementation was tested using automatically generated inputs.

Fuzz testing identified input-handling issues such as:

- Invalid order formats.
- Missing or malformed quantities.
- Invalid distance values.
- Empty or incorrectly formatted coupon codes.
- Unexpected input types.

The application was then updated with input validation and appropriate exception handling to prevent unexpected failures when invalid inputs are provided.

## Results

| Metric | Result |
|---|---:|
| Total Tests | 27 |
| Passed | 27 |
| Failed | 0 |
| Testing Framework | Pytest |
| Input Generation | Hypothesis |

All 27 tests passed successfully after fixing the identified input-validation issues.

## Commands to Run

Navigate to the Lab 7 directory:

```bash
cd "Lab 7"
```

Install dependencies:

```bash
py -m pip install pytest hypothesis
```

Run the application:

```bash
py processor.py
```

Run the fuzz tests:

```bash
py -m pytest test_processor.py -v
```

---

# Technologies Used

- **Python:** Application implementation.
- **Pytest:** Automated testing framework.
- **pytest-cov:** Code and branch coverage measurement.
- **Hypothesis:** Property-based testing and automatic input generation.
- **Git & GitHub:** Version control and repository management.

---

# Repository Structure

```text
L6_L7_20_food_delivery/
│
├── Lab 6/
│   ├── food_delivery.py
│   ├── test_food_delivery.py
│   ├── CodeCoverageTest_PES1UG24CS325_application.py
│   ├── BranchCoverageTest_PES1UG24CS325_application.py
│   ├── CodeCoverage_PES1UG24CS325_1.png
│   ├── CodeCoverage_PES1UG24CS325_2.png
│   ├── BranchCoverage_PES1UG24CS325_1.png
│   └── BranchCoverage_PES1UG24CS325_2.png
│
├── Lab 7/
│   ├── processor.py
│   └── test_processor.py
│
└── README.md
```

---

# Conclusion

Lab 6 demonstrated how code coverage and branch coverage can be used to evaluate the effectiveness and completeness of software testing.

Lab 7 demonstrated how fuzz testing and property-based testing can help identify unexpected input scenarios and improve application robustness.

Together, these labs provide practical experience with automated testing, input validation, test coverage analysis, and software quality assurance.
