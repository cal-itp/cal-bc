import openpyxl
from xlcalculator import Evaluator, ModelCompiler, Model
import cal_bc.functions # noqa: F401


class CellValueWriter:
    def __init__(self, workbook: openpyxl.Workbook) -> None:
        self.workbook = workbook

    def write(self, cell_address: str, new_value: any) -> None:
        if cell_address in self.workbook.defined_names:
            reference = self.workbook.defined_names[cell_address]
            destinations = [
                (sheet, value.replace("$", ""))
                for (sheet, value) in reference.destinations
            ]
            sheet, cell = destinations[0]
        else:
            sheet, cell = cell_address.split("!")

        self.workbook[sheet][cell].value = new_value


class Calculator:
    def __init__(self, input_filename: str) -> None:
        self.input_filename = input_filename
        self._workbook = None

    def workbook(self) -> openpyxl.Workbook:
        if not self._workbook:
            self._workbook = openpyxl.load_workbook(
                filename=self.input_filename, keep_vba=True
            )
        return self._workbook

    def write(self, cell_values: dict[str, any]) -> None:
        writer = CellValueWriter(workbook=self.workbook())
        for cell, value in cell_values.items():
            writer.write(cell_address=cell, new_value=value)

    def save(self, output_file: str) -> None:
        self.workbook().save(output_file)

    def compile(self) -> Evaluator:
        compiler = ModelCompiler()
        model: Model = compiler.read_and_parse_archive(
            self.input_filename, build_code=True
        )
        return Evaluator(model)
