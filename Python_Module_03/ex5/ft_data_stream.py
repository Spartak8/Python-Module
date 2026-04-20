import random
import typing


PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "jump", "eat", "sleep", "move", 
           "climb", "swim", "grab", "use", "release"]


def gen_event() -> typing.Generator:
    while True:   
        yield(random.choice(PLAYERS), random.choice(ACTIONS))

print("=== Game Data Stream Processor ===")
gen = gen_event()
for i in range(1000):
    ev = next(gen)
    print(f"Event {i}: Player {ev[0]} did action {ev[1]}")
my_list = []
for i in range(10):
    l = next(gen)
    my_list.append(l)
print(f"Built list of 10 events: {my_list}")


def consume_event(my_list: list) -> typing.Generator:
    while len(my_list) > 0:
        element = random.choice(my_list)
        my_list.remove(element)
        yield element

for event in consume_event(my_list):
    print(f"Got event from list: {event}")
    print(f"Remains in list: {my_list}")