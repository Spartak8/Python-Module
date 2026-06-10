from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(
    mages: list[dict[str, Any]], min_power: int
) -> list[dict[str, Any]]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: '* ' + x + ' *', spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        'max_power': max(mages, key=lambda x: x['power'])['power'],
        'min_power': min(mages, key=lambda x: x['power'])['power'],
        'avg_power': round(sum(map(lambda x: x['power'], mages))/len(mages), 2)
    }


if __name__ == '__main__':
    artifacts = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'focus'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'relic'}
    ]
    mages = [
        {'name': 'Sage', 'power': 85, 'element': 'water'},
        {'name': 'Ember', 'power': 89, 'element': 'water'},
        {'name': 'Morgan', 'power': 84, 'element': 'light'},
        {'name': 'Luna', 'power': 56, 'element': 'shadow'},
        {'name': 'Sage', 'power': 99, 'element': 'wind'}
    ]
    spells = ['fireball', 'heal', 'shield']

    sorted_artifacts = artifact_sorter(artifacts)
    print("Testing artifact sorter...")
    print(
        f"{sorted_artifacts[0]['name']} "
        f"({sorted_artifacts[0]['power']} power) "
        f"comes before {sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )
    print()
    print("Testing spell transformer...")
    print(' '.join(spell_transformer(spells)))
