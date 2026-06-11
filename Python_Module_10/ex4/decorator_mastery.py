from functools import wraps
from collections.abc import Callable
import time
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if 'power' in kwargs:
                power = kwargs['power']
            else:
                power = args[-1]

            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    attempts += 1
                    if attempts == max_attempts:
                        return (f'Spell casting failed after {max_attempts} '
                                'attempts')
                    else:
                        print(f'Spell failed, retrying... '
                              f'(attempt {attempts}/{max_attempts})')
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3 or name.replace(" ", "").isalpha() is False:
            return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Result: Fireball cast!"
    print(fireball())
    print()
    print("Testing retrying spell...")

    @retry_spell(3)
    def unstable_spell() -> str:
        raise Exception
    print(unstable_spell())
    print("Waaaaaaagh spelled !")
    print()
    print("Testing MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Gandalf"))
    print(guild.validate_mage_name("A31e"))
    print(guild.cast_spell("Lightning", power=15))
    print(guild.cast_spell("Fireball", power=5))
