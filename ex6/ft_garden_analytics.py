class Plant:
    class Stats:
        def __init__(self):
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0
        
        def display(self):
            print(f"Stats: {self._grow_count} grow, {self._age_count} age, {self._show_count} show")
    
    def __init__(self, name, height, age):
        self.name = name
        self._height = float(height)
        self._age = age
        self._stats = Plant.Stats()

    def show(self):
        self._stats._show_count += 1 
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def grow(self, growth_rate: float = 1.0) -> None:
        self._stats._grow_count += 1
        self._height = round(self._height + growth_rate, 1)

    def age(self, days: int = 1) -> None:
        self._stats._age_count += 1
        self._age = self._age + days

    @