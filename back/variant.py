from dataclasses import dataclass
from typing import Optional


@dataclass
class Variant:
    stressed_syllable_number: int
    pre_pie_r: str
    pg_r: str
    pie_r: str

    pg_l: Optional[str] = None
    pie_l: Optional[str] = None
