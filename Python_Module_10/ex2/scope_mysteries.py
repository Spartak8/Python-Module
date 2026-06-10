from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total_power = initial_power

    def power_up(add: int) -> int:
        nonlocal total_power
        total_power += add
        return total_power
    return power_up


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def apply_enchantment(name: str) -> str:
        return f"{enchantment_type} {name}"
    return apply_enchantment


def memory_vault() -> dict[str, Callable[..., Any]]:
    storage = {}

    def store(key: str, value: Any) -> None:
        storage[key] = value

    def recall(key: str) -> Any:
        if key in storage:
            return storage[key]
        else:
            return "Memory not found"

    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    a = mage_counter()
    b = mage_counter()

    print("Testing mage_counter...")
    print(f"counter_a call 1: {a()}")
    print(f"counter_a call 2: {a()}")
    print(f"counter_b call 1: {b()}")
    print()
    print("Testing spell_accumulator...")
    power = spell_accumulator(100)
    print(f"Base power: {power(0)}, add 20: {power(20)}")
    print(f"Base power: {power(0)}, add 30: {power(30)}")
    print()
    print("Testing enchantment factory...")
    item1 = enchantment_factory("Flaming")
    item2 = enchantment_factory("Frozen")
    print(item1("Sword"))
    print(item2("Shield"))
    print()
    print("Testing memory vault...")
    vault = memory_vault()
    vault['store']('secret', 42)
    print("Stored 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
