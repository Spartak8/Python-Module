import operator
from functools import reduce, partial, lru_cache, singledispatch
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    def _max_op(a: int, b: int) -> int:
        return max(a, b)

    def _min_op(a: int, b: int) -> int:
        return min(a, b)
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": _max_op,
        "min": _min_op
    }

    if operation not in operations:
        raise ValueError(f"Unsupported operation: {operation}")
    if not spells:
        return 0
    op = operations[operation]
    return reduce(op, spells)


def partial_enchanter(
    base_enchantment: Callable[[int, str], str]
) -> dict[str, Callable[[str], str]]:
    fire_enchant = partial(base_enchantment, 50, "fire")
    ice_enchant = partial(base_enchantment, 50, "ice")
    light_enchant = partial(base_enchantment, 50, "light")
    return {
        "fire_enchant": fire_enchant,
        "ice_enchant": ice_enchant,
        "light_enchant": light_enchant
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register(list)
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"
    return cast


if __name__ == "__main__":
    print("Testing spell reducer...")
    sum_result = spell_reducer([30, 20, 50], "add")
    mul_result = spell_reducer([20, 20, 20, 30], "multiply")
    max_result = spell_reducer([10, 25, 5, 40, 15], "max")
    print(f"Sum: {sum_result}")
    print(f"Product: {mul_result}")
    print(f"Max: {max_result}")
    print()
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print()
    print("Testing spell dispatcher...")
    spell = spell_dispatcher()
    print(f"{spell(42)}")
    print(f"{spell('fireball')}")
    print(f"{spell([42, 50, 100])}")
    print(f"{spell(42.5)}")
