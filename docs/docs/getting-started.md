# Getting Started

## Prerequisites

- Python 3.12
- A virtual environment tool (`venv` is sufficient)

## Installation

Create and activate your virtual environment, then install dependencies:

```bash
pip install -r requirements.txt
```

## Data

Place the source dataset at:

`data/raw/term-deposit-marketing-2020.csv`

## Run The Pipeline

Execute the project in this order from the repository root:

```bash
python deposit_classification/dataset.py
python deposit_classification/plots.py
python deposit_classification/features.py
python deposit_classification/modeling/train.py
python deposit_classification/modeling/predict.py
```

## Expected Outputs

- Train/test pickles in `data/interim/` and `data/processed/`
- EDA plots in `reports/figures/` from `deposit_classification/plots.py`
- Analysis tables printed to terminal from `deposit_classification/plots.py` and
	`deposit_classification/features.py`
- Trained model in `models/model_pipeline.joblib`
- Generated feature plots in `reports/figures/`

## Build Documentation

```bash
mkdocs build -f docs/mkdocs.yml
mkdocs serve -f docs/mkdocs.yml
```
