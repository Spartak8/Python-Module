from collections.abc import Callable


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int
) -> Callable[[str, int], str]:
    def powered(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return powered


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    def conditioned(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return conditioned


def spell_sequence(
    spells: list[Callable[[str, int], str]]
) -> Callable[[str, int], list[str]]:
    def sequenced(target: str, power: int) -> list[str]:
        results: list[str] = []
        for spell in spells:
            results.append(spell(target, power))
        return results
    return sequenced


if __name__ == '__main__':
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    target_name = "Dragon"
    base_power = 10
    multiplier = 3

    combo = spell_combiner(fireball, heal)
    first, second = combo(target_name, base_power)
    print("Testing spell combiner...")
    print(f"Combined spell result: Fireball hits {target_name}, "
          f"Heals {target_name}")
    print()
    power_up = power_amplifier(fireball, multiplier)
    amplified_result = power_up(target_name, base_power)
    print("Testing power amplifier...")
    print(f"Original: {base_power}, Amplified: {base_power * multiplier}")
