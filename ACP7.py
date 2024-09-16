def series_resistance(resistances):
    return sum(resistances)

def parallel_resistance(resistances):
    inverse_sum = sum(1/r for r in resistances)
    return 1 / inverse_sum

def total_resistance(series_resistances, parallel_resistances):
    return series_resistance(series_resistances) + parallel_resistance(parallel_resistances)

def main():
    # Example values
    series_resistances = [10, 20]  # Resistors in series
    parallel_resistances = [30, 60]  # Resistors in parallel
    voltage_source = 12  # Voltage source in volts

    # Calculate total resistance
    R_total = total_resistance(series_resistances, parallel_resistances)
    print(f"Total Resistance: {R_total} ohms")

    # Calculate total current using Ohm's Law (V = IR)
    total_current = voltage_source / R_total
    print(f"Total Current: {total_current} A")

if __name__ == "__main__":
    main()
