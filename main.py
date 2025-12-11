from schedule import Schedule

def load_schedule():
    s = Schedule()
    filename = "courses.csv"
    try:
        s.load_from_csv(filename)
    except:
        print("Could not load the CSV file")
        return None
    return s

def print_menu():
    print()
    print("Course Schedule System")
    print("----------------------")
    print("1. Display all classes")
    print("2. Search by subject")
    print("3. Search by subject and catalog")
    print("4. Search by instructor last name")
    print("5. Quit")
    print()

def main():
    sched = load_schedule()
    if sched is None:
        return

    while True:
        print_menu()
        choice = input("Enter a choice: ").strip()

        if choice == "1":
            sched.print()
        elif choice == "2":
            s = input("Subject: ")
            sched.print(sched.find_by_subject(s))
        elif choice == "3":
            s = input("Subject: ")
            c = input("Catalog: ")
            sched.print(sched.find_by_subject_catalog(s, c))
        elif choice == "4":
            name = input("Instructor last name: ")
            sched.print(sched.find_by_instructor_last_name(name))
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
