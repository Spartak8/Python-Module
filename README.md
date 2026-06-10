# 🐍 Python Module — School 42

> A structured Python learning curriculum completed at **School 42** (login: `skhachat`).  
> Each module focuses on a distinct set of concepts, building progressively from basics to advanced patterns.

---

## 📁 Project Structure

```
Python-Module/
├── Python_Module_00/     # Python fundamentals
├── Python_Module_01/     # Functions, classes, f-strings
├── Python_Module_02/     # Exception handling
├── Python_Module_03/     # CLI args, data structures, comprehensions
├── Python_Module_04/     # File I/O
├── Python_Module_05/     # Abstract classes & OOP
├── Python_Module_06/     # Package structure & imports
├── Python_Module_07/     # Advanced OOP & design patterns
├── Python_Module_08/     # External packages & virtual environments
├── Python_Module_09/     # Data validation with Pydantic
└── Python_Module_10/     # Functional programming
```

---

## 📚 Modules Overview

### Module 00 — Python Fundamentals
> **Theme:** Garden Community

Introduction to Python syntax, variables, arithmetic, conditions, loops, and basic recursion.

| Exercise | File | Concepts |
|----------|------|----------|
| ex0 | `ft_hello_garden.py` | Hello World, functions |
| ex1 | `ft_garden_name.py` | Variables, strings |
| ex2 | `ft_plot_area.py` | Arithmetic, math |
| ex3 | `ft_harvest_total.py` | Functions, return values |
| ex4 | `ft_plant_age.py` | Conditions, logic |
| ex5 | `ft_water_reminder.py` | Control flow |
| ex6 | `ft_count_harvest_*.py` | Iteration vs recursion |
| ex7 | `ft_seed_inventory.py` | Lists, dictionaries |

---

### Module 01 — Functions, Classes & f-strings
> **Theme:** Garden Management

Deeper dive into functions with type hints, f-strings, basic OOP, and data processing.

| Exercise | File | Concepts |
|----------|------|----------|
| ex0 | `ft_garden_intro.py` | f-strings, `main()` pattern |
| ex1 | `ft_garden_data.py` | Data structures |
| ex2 | `ft_plant_growth.py` | Logic, calculations |
| ex3 | `ft_plant_factory.py` | Factory functions |
| ex4 | `ft_garden_security.py` | Validation logic |
| ex5 | `ft_plant_types.py` | Type system, OOP basics |
| ex6 | `ft_garden_analytics.py` | Data analytics, aggregations |

---

### Module 02 — Exception Handling
> **Theme:** Garden Temperature Monitor

Full coverage of Python exception mechanics.

| Exercise | File | Concepts |
|----------|------|----------|
| ex0 | `ft_first_exception.py` | `try/except`, `ValueError` |
| ex1 | `ft_raise_exception.py` | `raise`, propagation |
| ex2 | `ft_different_errors.py` | Multiple exception types |
| ex3 | `ft_custom_errors.py` | Custom exception classes |
| ex4 | `ft_finally_block.py` | `finally`, cleanup |

---

### Module 03 — CLI, Data Structures & Comprehensions
> **Theme:** Command Quest / Game Inventory

Working with the command line, Python's core data structures, and powerful one-liners.

| Exercise | File | Concepts |
|----------|------|----------|
| ex0 | `ft_command_quest.py` | `sys.argv`, CLI arguments |
| ex1 | `ft_score_analytics.py` | Lists, sorting |
| ex2 | `ft_coordinate_system.py` | Tuples |
| ex3 | `ft_achievement_tracker.py` | Dictionaries |
| ex4 | `ft_inventory_system.py` | Sets |
| ex5 | `ft_data_stream.py` | `sys.stdin` / `sys.stdout` |
| ex6 | `ft_data_alchemist.py` | List & dict comprehensions |

---

### Module 04 — File I/O
> **Theme:** Cyber Archives

Reading, writing, and safely managing files with context managers.

| Exercise | File | Concepts |
|----------|------|----------|
| ex0 | `ft_ancient_text.py` | `open()`, `read()`, `close()` |
| ex1 | `ft_archive_creation.py` | Writing files |
| ex2 | `ft_stream_management.py` | `with` statement, context managers |
| ex3 | `ft_vault_security.py` | Advanced file operations |

---

### Module 05 — Abstract Classes & OOP
> **Theme:** Code Nexus — Data Processing Pipeline

Abstract base classes, polymorphism, and a real data processing pipeline.

| Exercise | File | Concepts |
|----------|------|----------|
| ex0 | `data_processor.py` | `ABC`, `@abstractmethod`, `NumericProcessor`, `TextProcessor`, `LogProcessor` |
| ex1 | `data_stream.py` | Dispatcher pattern, stream routing |
| ex2 | `data_pipeline.py` | Full pipeline with CSV/JSON export |

---

### Module 06 — Package Structure & Imports
> **Theme:** The Alchemy Lab

Building a multi-level Python package from scratch and mastering the import system.

```
alchemy/
├── __init__.py
├── elements.py
├── potions.py
├── transmutation/
│   ├── __init__.py
│   └── recipes.py
└── grimoire/
    ├── __init__.py
    ├── light_spellbook.py
    ├── dark_spellbook.py
    ├── light_validator.py
    └── dark_validator.py
```

Key concepts: absolute vs relative imports, `__init__.py`, circular import patterns, intentional `AttributeError` design, `noqa` directives.

Scripts: `ft_alembic_0..5.py`, `ft_distillation_0..1.py`, `ft_transmutation_0..2.py`, `ft_kaboom_0..1.py`

---

### Module 07 — Advanced OOP & Design Patterns
> **Theme:** Creature Battle Arena

Multiple inheritance, capability mixins, and the Strategy design pattern.

| Exercise | Contents | Concepts |
|----------|----------|----------|
| ex0 | `Creature` ABC, `Flameling`, `Pyrodon`, `Aquabub`, `Torragon` | Abstract classes, polymorphism |
| ex1 | `HealCapability`, `TransformCapability`, new creatures | Multiple inheritance, mixins |
| ex2 | `BattleStrategy`, `NormalStrategy`, `AggressiveStrategy`, `HealingStrategy` | Strategy pattern |

Support scripts: `battle.py`, `tournament.py`, `capacitor.py`

---

### Module 08 — External Packages & Virtual Environments
> **Theme:** The Matrix

Package management, dependency checking, and environment variable configuration.

| Exercise | File | Concepts |
|----------|------|----------|
| ex0 | `construct.py` | venv detection, `sys.prefix`, `site.getsitepackages()` |
| ex1 | `loading.py` | `importlib`, package checking, `pandas` / `numpy` / `matplotlib` |
| ex2 | `oracle.py` | `python-dotenv`, `os.environ`, `.env` files |

---

### Module 09 — Data Validation with Pydantic
> **Theme:** Space Station Command

Runtime data validation using Pydantic v2 models.

| Exercise | File | Concepts |
|----------|------|----------|
| ex0 | `space_station.py` | `BaseModel`, `Field`, `ValidationError` |
| ex1 | `alien_contact.py` | `Enum`, `model_validator`, cross-field validation |
| ex2 | `space_crew.py` | Nested models (`SpaceMission` → `CrewMember`), `Rank` enum |

---

### Module 10 — Functional Programming
> **Theme:** Arcane Magic

Lambdas, higher-order functions, and closures with `nonlocal`.

| Exercise | File | Concepts |
|----------|------|----------|
| ex0 | `lambda_spells.py` | `lambda`, `sorted`, `filter`, `map`, `max`, `min` |
| ex1 | `higher_magic.py` | Higher-order functions: `spell_combiner`, `power_amplifier`, `conditional_caster` |
| ex2 | `scope_mysteries.py` | Closures, `nonlocal`, counter & accumulator factories |

Support script: `data_generator.py` — test data generator for all exercises.

---

## 🚀 Running the Exercises

Each exercise is a standalone script. To run one:

```bash
# Navigate to the exercise folder
cd Python_Module_XX/exN/

# Run directly
python3 script_name.py

# Some exercises expect CLI arguments
python3 ft_command_quest.py arg1 arg2

# Some exercises require a virtual environment (Module 08+)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 script_name.py
```

---

## 🛠️ Requirements

- Python **3.10+**
- Some modules require third-party packages (see individual `requirements.txt` or `pyproject.toml`):
  - `numpy`, `matplotlib`, `pandas` — Module 08
  - `python-dotenv` — Module 08
  - `pydantic` — Module 09

---

## 👤 Author

**skhachat** — School 42  
GitHub: [@Spartak8](https://github.com/Spartak8)
