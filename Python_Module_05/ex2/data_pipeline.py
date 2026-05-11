import typing
from abc import ABC, abstractmethod
from typing import Any, Protocol


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass

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
            
    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            result = []
            for i in range(nb):
                if len(proc._storage) == 0:
                    break
                result.append(proc.output())
            plugin.process_output(result)


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


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        result = []
        for element in data:
            rank, value = element
            result.append(value)
        print("CSV Output:")
        print(",".join(result))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        result = {}
        for element in data:
            rank, value = element
            result[f"item_{rank}"] = value
        print("JSON Output:")
        pairs = []
        for k, v in result.items():
            pairs.append(f'"{k}": "{v}"')
        print("{" + ",".join(pairs) + "}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print()
    print("Initialize Data Stream...")
    print()
    d_stream = DataStream()
    num_p = NumericProcessor()
    text_p = TextProcessor()
    log_p = LogProcessor()
    d_stream.print_processors_stats()
    print("Registering Processors")
    d_stream.register_processor(num_p)
    d_stream.register_processor(text_p)
    d_stream.register_processor(log_p)
    print()
    print("Send first batch of data on stream: ['Hello world', [3.14, -1, 2.71], [{'log_level': 'WARNING', '"
          "log_message': 'Telnet access! Use ssh instead'}, {'log_level': 'INFO', 'log_message': 'User wil is"
          "connected'}], 42, ['Hi', 'five']]")
    data = ['Hello world',
            [3.14, -1, 2.71], 
            [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, 
             {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
            42, 
            ['Hi', 'five']]
    d_stream.process_stream(data)
    d_stream.print_processors_stats()
    print()
    print("Send 3 processed data from each processor to a CSV plugin:")
    csv = CSVExportPlugin()
    d_stream.output_pipeline(3, csv)
    print()
    d_stream.print_processors_stats()
    print()
    print("Send another batch of data: [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'], [{'log_level': '"
          "ERROR', 'log_message': '500 server crash'}, {'log_level': 'NOTICE', 'log_message': 'Certificate"
          "expires in 10 days'}], [32, 42, 64, 84, 128, 168], 'World hello']")
    print()
    data1 =  [21,
               ['I love AI', 'LLMs are wonderful', 'Stay healthy'], 
               [{'log_level': 'ERROR', 'log_message': '500 server crash'}, 
                {'log_level': 'NOTICE', 'log_message': 'Certificate expires in 10 days'}],
               [32, 42, 64, 84, 128, 168],
               'World hello']
    d_stream.process_stream(data1)
    d_stream.print_processors_stats()
    print("Send 5 processed data from each processor to a JSON plugin:")
    json = JSONExportPlugin()
    d_stream.output_pipeline(5, json)
    print()
    d_stream.print_processors_stats()