from graphics import GraphWin, Rectangle, Text, Point


# Calculate the outcome
def calculate_outcome(pass_mark, defer_mark, fail_mark):
    outcomes = {
        (120, 0, 0): "Progress",
        (100, 20, 0): "Progress (module trailer)",
        (100, 0, 20): "Progress (module trailer)",
        (80, 40, 0): "Module retriever",
        (80, 20, 20): "Module retriever",
        (80, 0, 40): "Module retriever",
        (60, 60, 0): "Module retriever",
        (60, 40, 20): "Module retriever",
        (60, 20, 40): "Module retriever",
        (60, 0, 60): "Module retriever",
        (40, 80, 0): "Module retriever",
        (40, 60, 20): "Module retriever",
        (40, 40, 40): "Module retriever",
        (40, 20, 60): "Module retriever",
        (40, 0, 80): "Exclude",
        (20, 100, 0): "Module retriever",
        (20, 80, 20): "Module retriever",
        (20, 60, 40): "Module retriever",
        (20, 40, 60): "Module retriever",
        (20, 20, 80): "Exclude",
        (20, 0, 100): "Exclude",
        (0, 120, 0): "Module retriever",
        (0, 100, 20): "Module retriever",
        (0, 80, 40): "Module retriever",
        (0, 60, 60): "Module retriever",
        (0, 40, 80): "Exclude",
        (0, 20, 100): "Exclude",
        (0, 0, 120): "Exclude",
    }

    return outcomes.get((pass_mark, defer_mark, fail_mark))


# Geting the input
def get_credit_input(prompt, valid_credit_values):
    while True:
        try:
            value = int(input(prompt))
            if value in valid_credit_values:
                return value
            else:
                print("Out of range.")
        except ValueError:
            print("Integer required.")


# Creating the histogram
def create_histogram(students):
    window = GraphWin("Progression Histogram", 1200, 700)
    window.setBackground("white")

    categories = ["Progress",
                  "Progress (module trailer)", "Module retriever", "Exclude"]
    counts = [students.count(cat) for cat in categories]

    x = 300
    y = 75
    total_students = len(students)

    total_students_text = Text(
        Point(window.getWidth() / 2, 50), "Histogram Results")
    total_students_text.setSize(18)
    total_students_text.draw(window)

    total_students_text = Text(
        Point(window.getWidth() / 2, 80), f"Total Students: {total_students}")
    total_students_text.setSize(12)
    total_students_text.draw(window)

    for cat, count in zip(categories, counts):
        bar = Rectangle(Point(x, 400 - 300 * count /
                        total_students), Point(x + y, 400))
        bar.setFill("blue")
        bar.draw(window)

        label = Text(Point(x + y / 2, 430), f"{cat}\n({count} students)")

        label.draw(window)

        x += 2 * y

    window.getMouse()
    window.close()


# Main funciton
def main():
    students = []

    try:
        valid_credit_values = range(0, 121, 20)

        while True:
            pass_mark = get_credit_input("Pass: ", valid_credit_values)
            defer_mark = get_credit_input("Defer: ", valid_credit_values)
            fail_mark = get_credit_input("Fail: ", valid_credit_values)

            total_marks = pass_mark + defer_mark + fail_mark

            if total_marks != 120:
                print("Total incorrect. \n")
                continue

            outcome = calculate_outcome(pass_mark, defer_mark, fail_mark)
            print("Outcome:", outcome, "\n")

            students.append(outcome)

            choice = input(
                "Would you like to enter another set of data? Enter 'y' for yes or 'q' to quit: ").lower()
            print("")

            if choice == "q":
                break

        create_histogram(students)

    except ValueError:
        print("Integer required")


if __name__ == "__main__":
    main()
