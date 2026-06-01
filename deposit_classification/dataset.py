from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

import pandas as pd

from deposit_classification.config import RAW_DATA_DIR, INTERIM_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    input_path: Path = RAW_DATA_DIR / "term-deposit-marketing-2020.csv",
    output_path: Path = INTERIM_DATA_DIR / "xxxx",
):
    raw_data = pd.read_csv(input_path)
    


if __name__ == "__main__":
    app()
