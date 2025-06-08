import hashlib
import io
import sys
import pandas as pd
from pathlib import Path
import shutil
import builtins

sys.path.append(str(Path(__file__).resolve().parents[1]))

from myawesomeeda.myawesomeeda import run_eda

builtins.input = lambda prompt="": "4"


def test_example():
    x = int(input())
    assert x == 4


def test_run_eda_output_hash(monkeypatch):
    df = pd.read_csv("demo_data/titanic.csv")

    buffer = io.StringIO()
    monkeypatch.setattr("sys.stdout", buffer)

    run_eda(df)

    output = buffer.getvalue()
    text_hash = hashlib.sha256(output.encode("utf-8")).hexdigest()

    expected_hash = "95b90a8093dd187eb72e5d2fae796fb3fd33413d6772c7fe12c4120bc6390f30"

    assert text_hash == expected_hash, "EDA output does not match the reference."

    current_dir = Path(__file__).resolve().parent
    pycache_dir = current_dir / "__pycache__"
    if pycache_dir.exists() and pycache_dir.is_dir():
        shutil.rmtree(pycache_dir)
