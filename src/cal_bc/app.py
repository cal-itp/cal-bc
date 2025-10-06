import os
import typer

from platformdirs import user_cache_dir
from typing import List, Optional
from typing_extensions import Annotated

from cal_bc.calculator import Calculator
from cal_bc.downloader import Downloader, VERSIONS

app = typer.Typer()


@app.command()
def list():
    for id, version in VERSIONS.items():
        print(f"{id} - {version['name']}")


@app.command()
def download(
    version_id: str,
    output_dir: str = user_cache_dir("cal-bc", "caltrans"),
):
    Downloader(version_id=version_id).download(output_dir=output_dir)


@app.command()
def complete(
    input_filename: str,
    cell: Annotated[List[str], typer.Option()],
    value: Annotated[List[str], typer.Option()],
):
    if len(cell) != len(value):
        print(f"Unequal number of cells ({cell}) and values ({value})")
        raise typer.Abort()

    basename, extension = os.path.splitext(os.path.basename(input_filename))
    calculator = Calculator(input_filename)
    calculator.write(dict(zip(cell, value)))
    calculator.save(
        os.path.join(os.path.dirname(input_filename), f"{basename}-complete{extension}")
    )


@app.command()
def evaluate(
    input_filename: str,
    cell: Annotated[List[str], typer.Option()],
):
    calculator = Calculator(input_filename)
    evaluator = calculator.compile()
    for cell_address in cell:
        print(f"{cell_address} = {evaluator.evaluate(cell_address)}")
