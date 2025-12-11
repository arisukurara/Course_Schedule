import csv
from schedule_item import ScheduleItem

class Schedule:
    def __init__(self):
        self.items = {}

    def add_entry(self, item):
        key = item.get_key()
        self.items[key] = item

    def load_from_csv(self, filename):
        with open(filename, encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("Subject") is None:
                    continue

                units = row.get("Units", "").strip()
                tot = row.get("TotEnrl", "").strip()
                cap = row.get("CapEnrl", "").strip()

                if units == "":
                    units = 0
                else:
                    units = int(units)

                if tot == "":
                    tot = 0
                else:
                    tot = int(tot)

                if cap == "":
                    cap = 0
                else:
                    cap = int(cap)

                item = ScheduleItem(
                    row["Subject"].strip(),
                    row["Catalog"].strip(),
                    row["Section"].strip(),
                    row["Component"].strip(),
                    row["Session"].strip(),
                    units,
                    tot,
                    cap,
                    row["Instructor"].strip()
                )

                self.add_entry(item)

    def print_header(self):
        print(
            f"{'Subject':<7}"
            f"{'Catalog':<8}"
            f"{'Section':<8}"
            f"{'Component':<10}"
            f"{'Session':<8}"
            f"{'Units':>5}"
            f"{'TotEnrl':>9}"
            f"{'CapEnrl':>9}  "
            f"Instructor"
        )

    def print(self, items=None):
        if items is None:
            items = list(self.items.values())

        if len(items) == 0:
            print("No matching classes found.")
            return

        self.print_header()
        for i in items:
            i.print()

    def find_by_subject(self, subject):
        subject = subject.upper().strip()
        return [item for item in self.items.values() if item.subject.upper() == subject]

    def find_by_subject_catalog(self, subject, catalog):
        subject = subject.upper().strip()
        catalog = catalog.strip()
        return [item for item in self.items.values() 
                if item.subject.upper() == subject and item.catalog == catalog]

    def find_by_instructor_last_name(self, last):
        last = last.lower().strip()
        return [item for item in self.items.values() 
                if item.instructor and last in item.instructor.split(",")[0].strip().lower()]
