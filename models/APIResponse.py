from dataclasses import dataclass


@dataclass
class APIResponse:
    total : int
    skip: int
    limit : int