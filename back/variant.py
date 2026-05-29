from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Variant:
    stressed_syllable_number: int
    minoan: str
    minoan_search: str
    cognates: List[Dict[str, str]]
