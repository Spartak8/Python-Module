import typing
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


class DataStream:
    def __init__(self) -> None:
        self.processors = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    break
            else:
                print("DataStream error - Can't process element in stream: "
                      f"{element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            name = proc.name
            total = proc._total
            remaining = len(proc._storage)
            print(f"{name}: total {total} items processed, "
                  f"remaining {remaining} on processor")


class NumericProcessor(DataProcessor):
    name = "Numeric Processor"
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
    name = "Text Processor"
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
    name = "Log Processor"
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
    print("=== Code Nexus - Data Stream ===")
    print()
    print("Initialize Data Stream...")
    d_stream = DataStream()
    d_stream.print_processors_stats()
    print()
    print("Registering Numeric Processor")
    print()
    print("Send first batch of data on stream: ['Hello world', [3.14, -1, 2.71], [{'log_level': 'WARNING', '"
          "log_message': 'Telnet access! Use ssh instead'}, {'log_level': 'INFO', 'log_message': 'User wil is"
          "connected'}], 42, ['Hi', 'five']]")
    num_p = NumericProcessor()
    text_p = TextProcessor()
    log_p = LogProcessor()
    d_stream.register_processor(num_p)
    data = ['Hello world',
            [3.14, -1, 2.71], 
            [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, 
             {'log_level': 'INFO', 'log_message': 'User wil isconnected'}],
            42, 
            ['Hi', 'five']]
    d_stream.process_stream(data)
    d_stream.print_processors_stats()
    print()
    print("Registering other data processors")
    print("Send the same batch again")
    d_stream.register_processor(text_p)
    d_stream.register_processor(log_p)
    d_stream.process_stream(data)
    d_stream.print_processors_stats()
    print()
    print("Consume some elements from the data processors: Numeric 3, Text 2, Log 1")
    for i in range(3):
        num_p.output()
    for i in range(2):
        text_p.output()
    for i in range(1):
        log_p.output()
    d_stream.print_processors_stats()