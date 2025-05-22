class DateRange:
    def __init__(self, start_date: str, end_date: str) -> None:
        self.start = start_date
        self.end = end_date
    
    def unpack(self) -> tuple[str, str]:
        return self.start, self.end