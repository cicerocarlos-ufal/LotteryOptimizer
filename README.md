# LotteryOptimizer

LotteryOptimizer is a Python framework for combinatorial optimization of lottery reductions.

The project was developed to generate optimized lottery reductions using heuristic and exact optimization algorithms, with an emphasis on Lotofácil.

---

## Features

- Greedy Set Cover
- GRASP
- Hill Climbing
- Genetic Algorithm
- Memetic Algorithm
- CP-SAT (OR-Tools)

Additional features:

- Coverage validation
- Automatic reporting
- CSV export
- Benchmark framework
- Configurable execution

---

## Installation

Clone the repository:

```bash
git clone https://github.com/SEU_USUARIO/LotteryOptimizer.git

cd LotteryOptimizer
```

Create a virtual environment:

```bash
python -m venv .venv
```

Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install the package

```bash
pip install -e .
```

or

```bash
pip install -r requirements.txt
```

---

## Running

Edit

```
config.py
```

Choose

- lottery
- source numbers
- algorithm
- guarantee
- number of games

Execute

```bash
python run.py
```

---

## Available algorithms

- Greedy
- GRASP
- Hill
- Genetic
- Memetic
- CP-SAT

---

## Running tests

```bash
pytest
```

or

```bash
pytest -v
```

---

## Project structure

```
lottery_optimizer/
    core/
    reduction/
    engine/
    validation/
    report/
    export/
    lotteries/
```

---

## Author

Cícero Carlos de Souza Almeida

Federal University of Alagoas (UFAL)

Brazil
