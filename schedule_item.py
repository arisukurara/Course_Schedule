from dataclasses import dataclass

@dataclass
class ScheduleItem:
    subject: str
    catalog: str
    section: str
    component: str
    session: str
    units: int
    tot_enrl: int
    cap_enrl: int
    instructor: str

    def get_key(self):
        return self.subject + "_" + self.catalog + "_" + self.section

    def format_row(self):
        return (
            f"{self.subject:<7}"
            f"{self.catalog:<8}"
            f"{self.section:<8}"
            f"{self.component:<10}"
            f"{self.session:<8}"
            f"{self.units:>5}"
            f"{self.tot_enrl:>9}"
            f"{self.cap_enrl:>9}  "
            f"{self.instructor}"
        )

    def print(self):
        print(self.format_row())
