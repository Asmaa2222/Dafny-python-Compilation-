    test_values = [-10, 0, 15, -7, 20]

    # Applying the original Abs function to each test value
    results_original = {val: default__.Abs(val) for val in test_values}
    print(results_original)