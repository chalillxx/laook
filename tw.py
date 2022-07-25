"""Drop Drop"""
def main():
    """print drop"""
    grade = float(input())
    if grade < 1.00:
        print("I'm so sad.")
    elif grade < 2.00:
        grade_2 = 4.00 - grade
        print("%.2f" %grade_2)
    elif grade >= 2.00:
        print("I'm so happy.")
main()
