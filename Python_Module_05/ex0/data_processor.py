from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._total = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        rank = self._total - len(self._storage)
        first = self._storage.pop(0)
        return (rank, first)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) and not isinstance(x, bool)
                       for x in data)
        return isinstance(data, (int, float)) and not isinstance(data, bool)

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for x in data:
                self._storage.append(str(x))
                self._total += 1
        else:
            self._storage.append(str(data))
            self._total += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return isinstance(data, str)

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for x in data:
                self._storage.append(x)
                self._total += 1
        else:
            self._storage.append(data)
            self._total += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            keys_ok = all(isinstance(k, str) for k in data.keys())
            vals_ok = all(isinstance(v, str) for v in data.values())
            return keys_ok and vals_ok
        elif isinstance(data, list):
            return all(self.validate(k) for k in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for x in data:
                self._storage.append(f"{x['log_level']}: {x['log_message']}")
                self._total += 1
        else:
            self._storage.append(f"{data['log_level']}: {data['log_message']}")
            self._total += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    print()
    print("Testing Numeric Processor...")
    num_p = NumericProcessor()
    print(f"Trying to validate input '42': {num_p.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_p.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_p.ingest("foo")
    except ValueError as e:
        print(f"Got exception: {e}")
    print("Processing data: [1, 2, 3, 4, 5]")
    num_p.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for i in range(3):
        rank, value = num_p.output()
        print(f"Numeric value {rank}: {value}")
    print()
    print("Testing Text Processor...")
    text_p = TextProcessor()
    print(f"Trying to validate input '42': {text_p.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text_p.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    for i in range(1):
        rank, value = text_p.output()
        print(f"Text value {rank}: {value}")
    print()
    print("Testing Log Processor...")
    log_p = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_p.validate('hello')}")
    data_log = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {data_log}")
    log_p.ingest(data_log)
    print("Extracting 2 values...")
    for i in range(2):
        rank, value = log_p.output()
        print(f"Log entry {rank}: {value}")
