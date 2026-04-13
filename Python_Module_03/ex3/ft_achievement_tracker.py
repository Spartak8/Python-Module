import random

ACHIEVEMENTS = [
    "First Steps", "Boss Slayer", "Speed Runner",
    "Collector Supreme", "Untouchable", "Sharp Mind",
    "Strategist", "Survivor", "Treasure Hunter",
    "Master Explorer", "World Savior", "Crafting Genius",
    "Unstoppable", "Hidden Path Finder"
]


def gen_player_achievements() -> set:
    count = random.randint(5, 9)
    return set(random.sample(ACHIEVEMENTS, count))


print("=== Achievement Tracker System ===")
print()
alice = gen_player_achievements()
bob = gen_player_achievements()
charlie = gen_player_achievements()
dylan = gen_player_achievements()
print(f"Player Alice: {alice}")
print(f"Player Bob: {bob}")
print(f"Player Charlie: {charlie}")
print(f"Player Dylan: {dylan}")
print()
all1 = alice.union(bob).union(charlie).union(dylan)
print(f"All distinct achievements: {all1}")
print()
common = alice.intersection(bob).intersection(charlie).intersection(dylan)
print(f"Common achievements: {common}")
print()
o_alice = alice.difference(bob).difference(charlie).difference(dylan)
o_bob = bob.difference(alice).difference(charlie).difference(dylan)
o_charlie = charlie.difference(bob).difference(alice).difference(dylan)
o_dylan = dylan.difference(bob).difference(charlie).difference(alice)
print(f"Only Alice has: {o_alice}")
print(f"Only Bob has: {o_bob}")
print(f"Only Charlie has: {o_charlie}")
print(f"Only Dylan has: {o_dylan}")
print()
m_alice = all1.difference(alice)
m_bob = all1.difference(bob)
m_charlie = all1.difference(charlie)
m_dylan = all1.difference(dylan)
print(f"Alice is missing: {m_alice}")
print(f"Bob is missing: {m_bob}")
print(f"Charlie is missing: {m_charlie}")
print(f"Dylan is missing: {m_dylan}")
