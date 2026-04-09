# Absorbance Lesson for Code.org Python Lab
# Pure Python version: no streamlit, no pandas, no matplotlib
# This version uses text-based "slides," user input, calculations,
# tables, and a simple ASCII graph so it works better in Code.org.

# -----------------------------
# Helper Functions
# -----------------------------
def line():
    print("-" * 70)


def wait():
    input("\nPress Enter to continue... ")


def clear_space():
    print("\n" * 3)


def beer_lambert(epsilon, path_length, concentration):
    return epsilon * path_length * concentration


def transmittance_from_absorbance(absorbance):
    return 10 ** (-absorbance)


def print_table(concentrations, absorbances):
    print(f"{'Point':<8}{'Concentration':<18}{'Absorbance':<18}")
    line()
    for i in range(len(concentrations)):
        print(f"{i+1:<8}{concentrations[i]:<18.3f}{absorbances[i]:<18.3f}")


def ascii_graph(x_values, y_values, x_label, y_label, title):
    print("\n" + title)
    line()

    if len(x_values) == 0:
        print("No data to graph.")
        return

    max_y = max(y_values)
    if max_y == 0:
        max_y = 1

    width = 40
    for i in range(len(x_values)):
        bar_len = int((y_values[i] / max_y) * width)
        bar = "#" * bar_len
        print(f"{x_label}={x_values[i]:>6.2f} | {bar} ({y_values[i]:.3f})")

    print(f"\nX-axis: {x_label}")
    print(f"Y-axis: {y_label}")


def get_float(prompt_text):
    while True:
        try:
            return float(input(prompt_text))
        except:
            print("Please enter a valid number.")


def get_int(prompt_text):
    while True:
        try:
            return int(input(prompt_text))
        except:
            print("Please enter a whole number.")


def default_dataset(epsilon, path_length):
    concentrations = [0.00, 0.10, 0.20, 0.30, 0.40, 0.50]
    absorbances = []
    for c in concentrations:
        absorbances.append(beer_lambert(epsilon, path_length, c))
    return concentrations, absorbances


def manual_data_entry():
    print("Enter your own concentration and absorbance values.")
    print("Example: concentration = 0.2, absorbance = 0.31")
    n = get_int("How many data points do you want to enter? ")

    concentrations = []
    absorbances = []

    for i in range(n):
        print(f"\nPoint {i+1}")
        c = get_float("Concentration: ")
        a = get_float("Absorbance: ")
        concentrations.append(c)
        absorbances.append(a)

    return concentrations, absorbances


def comma_data_entry():
    print("Paste numbers separated by commas.")
    print("Example concentrations: 0.1,0.2,0.3,0.4")
    print("Example absorbances:   0.15,0.30,0.45,0.60")

    c_text = input("Concentrations: ")
    a_text = input("Absorbances: ")

    try:
        concentrations = [float(x.strip()) for x in c_text.split(",") if x.strip() != ""]
        absorbances = [float(x.strip()) for x in a_text.split(",") if x.strip() != ""]
    except:
        print("There was a problem reading the numbers.")
        return [], []

    if len(concentrations) != len(absorbances):
        print("The number of concentrations and absorbances must match.")
        return [], []

    return concentrations, absorbances


def slide_1(epsilon, path_length):
    clear_space()
    print("SLIDE 1: WHAT IS ABSORBANCE?")
    line()
    print("Absorbance tells us how much light a solution absorbs.")
    print("Usually, when concentration increases, absorbance increases too.")
    print("That means a more concentrated solution often absorbs more light.")

    print("\nMini code idea:")
    print("concentration = 0.3")
    print("epsilon = 1.5")
    print("path_length = 1.0")
    print("absorbance = epsilon * path_length * concentration")

    c, a = default_dataset(epsilon, path_length)
    ascii_graph(c, a, "Concentration", "Absorbance", "Sample Absorbance Graph")
    wait()


def slide_2(epsilon, path_length):
    clear_space()
    print("SLIDE 2: BEER-LAMBERT LAW")
    line()
    print("Formula: A = e * l * c")
    print("A = absorbance")
    print("e = molar absorptivity")
    print("l = path length")
    print("c = concentration")

    concentration = get_float("\nChoose a concentration to test: ")
    absorbance = beer_lambert(epsilon, path_length, concentration)
    transmittance = transmittance_from_absorbance(absorbance)

    print(f"\nConcentration: {concentration:.3f}")
    print(f"Absorbance:    {absorbance:.3f}")
    print(f"Transmittance: {transmittance:.3f}")

    print("\nMini code idea:")
    print("def beer_lambert(epsilon, path_length, concentration):")
    print("    return epsilon * path_length * concentration")
    wait()


def slide_3(epsilon, path_length):
    clear_space()
    print("SLIDE 3: BUILD THE GRAPH STEP BY STEP")
    line()

    concentrations, absorbances = default_dataset(epsilon, path_length)
    total_points = len(concentrations)

    step = get_int(f"How many points do you want to show? (1-{total_points}): ")
    if step < 1:
        step = 1
    if step > total_points:
        step = total_points

    shown_c = concentrations[:step]
    shown_a = absorbances[:step]

    print_table(shown_c, shown_a)
    ascii_graph(shown_c, shown_a, "Concentration", "Absorbance", "Graph So Far")

    print("\nMini code idea:")
    print("shown = data[:step]")
    print("This means: only show part of the data.")
    wait()


def slide_4(epsilon, path_length):
    clear_space()
    print("SLIDE 4: LEARN SMALL PARTS OF THE CODE")
    line()

    print("Part A: Variables")
    print("epsilon = 1.5")
    print("path_length = 1.0")
    print("concentration = 0.4")
    print("absorbance = ______")

    guess = input("Type what should go in the blank: ")
    print("Possible answer: epsilon * path_length * concentration")

    line()
    print("Part B: Loop")
    print("concentrations = [0.1, 0.2, 0.3, 0.4]")
    print("for c in concentrations:")
    print("    A = ______")
    print("    print(c, A)")
    input("Type the missing expression: ")
    print("Possible answer: epsilon * path_length * c")

    line()
    print("Part C: Why use code?")
    print("Code helps us repeat calculations, organize data, and spot patterns.")
    wait()


def slide_5(epsilon, path_length):
    clear_space()
    print("SLIDE 5: USE YOUR OWN DATA")
    line()
    print("Choose one option:")
    print("1. Use sample data")
    print("2. Enter data point-by-point")
    print("3. Paste comma-separated values")

    choice = input("Your choice: ")

    if choice == "1":
        concentrations, absorbances = default_dataset(epsilon, path_length)
    elif choice == "2":
        concentrations, absorbances = manual_data_entry()
    elif choice == "3":
        concentrations, absorbances = comma_data_entry()
    else:
        print("Invalid choice. Using sample data instead.")
        concentrations, absorbances = default_dataset(epsilon, path_length)

    if len(concentrations) == 0:
        print("No valid data was entered.")
        wait()
        return

    paired = list(zip(concentrations, absorbances))
    paired.sort()
    concentrations = [item[0] for item in paired]
    absorbances = [item[1] for item in paired]

    print("\nYour Data:")
    print_table(concentrations, absorbances)
    ascii_graph(concentrations, absorbances, "Concentration", "Absorbance", "Your Graph")

    print("\nMini code idea:")
    print("lists can store many numbers")
    print("zip() can pair x-values and y-values together")
    wait()


def slide_6(epsilon, path_length):
    clear_space()
    print("SLIDE 6: CHALLENGE + EXTENSION")
    line()
    print("Choose an extension:")
    print("1. Predict absorbance from concentration")
    print("2. Compare two substances with different e values")
    print("3. pH extension")

    choice = input("Your choice: ")

    if choice == "1":
        concentration = get_float("Enter a concentration: ")
        absorbance = beer_lambert(epsilon, path_length, concentration)
        print(f"Predicted absorbance = {absorbance:.3f}")

    elif choice == "2":
        epsilon2 = get_float("Enter a second e value: ")
        concentrations = [0.1, 0.2, 0.3, 0.4, 0.5]
        absorbance1 = []
        absorbance2 = []
        for c in concentrations:
            absorbance1.append(beer_lambert(epsilon, path_length, c))
            absorbance2.append(beer_lambert(epsilon2, path_length, c))

        print("\nSubstance 1")
        ascii_graph(concentrations, absorbance1, "Concentration", "Absorbance", "Substance 1")
        print("\nSubstance 2")
        ascii_graph(concentrations, absorbance2, "Concentration", "Absorbance", "Substance 2")

    elif choice == "3":
        print("This is a conceptual extension.")
        print("Some indicators change color and absorbance as pH changes.")
        pH_values = [1, 3, 5, 7, 9, 11, 13]
        absorbances = [0.10, 0.15, 0.25, 0.50, 0.75, 0.90, 0.95]
        print_table(pH_values, absorbances)
        ascii_graph(pH_values, absorbances, "pH", "Absorbance", "pH Extension")

    else:
        print("Invalid choice.")

    print("\nExit Ticket:")
    print("1. What variable most directly changed absorbance in this lesson?")
    print("2. Why is graphing useful in chemistry?")
    print("3. What is one thing code helped you do faster?")
    wait()


# -----------------------------
# Main Program
# -----------------------------
def main():
    print("INTERACTIVE CHEMISTRY + PYTHON LESSON: ABSORBANCE")
    line()
    print("This version is designed for Code.org Python Lab.")
    print("It uses only basic Python, user input, tables, and text graphs.")

    epsilon = 1.5
    path_length = 1.0

    while True:
        clear_space()
        print("MAIN MENU")
        line()
        print("1. Slide 1 - What is absorbance?")
        print("2. Slide 2 - Beer-Lambert Law")
        print("3. Slide 3 - Step through the graph")
        print("4. Slide 4 - Learn small code pieces")
        print("5. Slide 5 - Use your own data")
        print("6. Slide 6 - Challenge + extension")
        print("7. Change epsilon and path length")
        print("0. Quit")

        choice = input("Choose a slide: ")

        if choice == "1":
            slide_1(epsilon, path_length)
        elif choice == "2":
            slide_2(epsilon, path_length)
        elif choice == "3":
            slide_3(epsilon, path_length)
        elif choice == "4":
            slide_4(epsilon, path_length)
        elif choice == "5":
            slide_5(epsilon, path_length)
        elif choice == "6":
            slide_6(epsilon, path_length)
        elif choice == "7":
            epsilon = get_float("Enter a new epsilon value: ")
            path_length = get_float("Enter a new path length: ")
            print("Values updated.")
            wait()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
            wait()


main()
