# Test Python Project

Een simpel Python project voor de claude-dev VM met OrbStack.

## Structuur

```
test-python/
├── main.py           # Hoofdprogramma
├── calculator.py     # Calculator class met basis operaties
├── utils.py          # Utility functies
└── test_calculator.py # Unit tests
```

## Installatie

```bash
git clone https://github.com/Matthi-code/test-python.git
cd test-python
```

## Gebruik

```bash
# Run het hoofdprogramma
python3 main.py

# Run de tests
python3 -m unittest test_calculator -v
```

## Features

### Calculator
- Basis operaties: `add`, `subtract`, `multiply`, `divide`
- Priemgetal check: `is_prime`

### Utils
- `greet(name)` - Begroeting functie
- `reverse_string(s)` - String omkeren
- `fibonacci(n)` - Fibonacci reeks genereren

## Tests

```bash
python3 -m unittest test_calculator -v
```

Alle 6 tests slagen:
- test_add
- test_subtract
- test_multiply
- test_divide
- test_divide_by_zero
- test_is_prime

## Licentie

MIT
