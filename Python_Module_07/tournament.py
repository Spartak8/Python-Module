from ex2 import BattleStrategy, NormalStrategy, AggressiveStrategy
from ex2 import DefensiveStrategy
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0 import CreatureFactory, FlameFactory, AquaFactory


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            print()
            print("* Battle *")
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]
            creature1 = factory1.create_base()
            creature2 = factory2.create_base()
            print(creature1.describe())
            print(" vs.")
            print(creature2.describe())
            print(" now fight!")
            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


print("Tournament 0 (basic)")
print(" [ (Flameling+Normal), (Healing+Defensive) ]")
opponents = [
    (FlameFactory(), NormalStrategy()),
    (HealingCreatureFactory(), DefensiveStrategy())
]
battle(opponents)
print()
print("Tournament 1 (error)")
print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
opponents = [
    (FlameFactory(), AggressiveStrategy()),
    (HealingCreatureFactory(), DefensiveStrategy())
]
battle(opponents)
print()
print("Tournament 2 (multiple)")
print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
opponents = [
    (AquaFactory(), NormalStrategy()),
    (HealingCreatureFactory(), DefensiveStrategy()),
    (TransformCreatureFactory(), AggressiveStrategy())
]
battle(opponents)
