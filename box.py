from dataclasses import dataclass


@dataclass()
class Box:
    id: str
    name: str
    age_days: int
    make_date: str
