from cows_and_bulls import cows_and_bulls

def run_tests():
    # secret, guess, expected (cows, bulls)
    cases = [
        ("1038", "1234", (2, 0)),  # digits 1 & 3 in right position
        ("1038", "1038", (4, 0)),  # exact match
        ("1234", "4321", (0, 4)),  # all digits present but misplaced
        ("1212", "2112", (2, 2)),  # repeated digits
        ("9876", "9870", (3, 0)),  # three correct, last wrong
        ("0000", "0000", (4, 0)),  # all zeroes
    ]
    for i, (s, g, exp) in enumerate(cases, start=1):
        out = cows_and_bulls(s, g)
        assert out == exp, f"Case {i} failed: {s=}, {g=}, expected {exp}, got {out}"
    print("✅ All tests passed!")

if __name__ == "__main__":
    run_tests()
