from schedule import Schedule

def load_schedule(use_avl=False):
    s = Schedule(use_avl=use_avl)
    filename = "courses_2023.csv"
    try:
        s.load_from_csv(filename)
        print(f"Loaded {len(s.get_all_items())} records into {s.tree_type} tree")
    except Exception as e:
        print(f"Could not load the CSV file: {e}")
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
    print("5. Display tree height")
    print("6. Quit")
    print()

def main():
    print("Choose tree type:")
    print("1. BST (Binary Search Tree)")
    print("2. AVL (Balanced Tree)")
    tree_choice = input("Enter choice: ").strip()
    
    use_avl = (tree_choice == "2")
    sched = load_schedule(use_avl=use_avl)
    
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
            height = sched.get_height()
            print(f"{sched.tree_type} tree height: {height}")
        elif choice == "6":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()