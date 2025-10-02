import logging
import pytest
import openpyxl
import os

from xlcalculator import Evaluator, Model, ModelCompiler
from calbc import functions

logging.basicConfig(level=logging.DEBUG)

class CellValueWriter:
    def __init__(self, workbook: openpyxl.Workbook) -> None:
        self.workbook = workbook

    def write(self, cell_address: str, new_value: any) -> None:
        if cell_address in self.workbook.defined_names:
            reference = self.workbook.defined_names[cell_address]
            destinations = [(sheet, value.replace("$", "")) for (sheet, value) in reference.destinations]
            sheet, cell = destinations[0]
        else:
            sheet, cell = cell_address.split("!")

        self.workbook[sheet][cell].value = new_value

class TestCalculation:
    @pytest.fixture
    def workbook_file(self) -> str:
        return "cal-bc-8-1-sketch-a11y.xlsm"

    @pytest.fixture
    def output_file(self) -> str:
        return "cal-bc-8-1-sketch-a11y-complete.xlsm"

    @pytest.fixture
    def workbook(self, workbook_file: str) -> openpyxl.Workbook:
        return openpyxl.load_workbook(filename=workbook_file, keep_vba=True)

    @pytest.fixture
    def model(self, output_file: str, workbook: openpyxl.Workbook) -> Model:
        writer = CellValueWriter(workbook=workbook)

        # 1) Project Information
        writer.write("ProjName", "Testing Project")
        writer.write("ProjType", "    HOV Lane Addition")
        writer.write("ProjLoc", 1)
        writer.write("Construct", 6)

        # Highway design and traffic data
        writer.write("GenLanesNB", 2)
        writer.write("GenLanesB", 2)
        writer.write("HOVLanesNB", 0)
        writer.write("HOVLanesB", 2)
        writer.write("HOVRest", 2)
        writer.write("FFSpeedNB", 65)
        writer.write("SegmentNB", 1.1)
        writer.write("ADT0", 90_000)
        writer.write("ADT1NB", 101_617)
        writer.write("ADT1B", 117_490)
        writer.write("ADT20NB", 138_405)
        writer.write("ADT20B", 148_823)
        writer.write("HOVvolNB", 0)
        writer.write("HOVvolB", 2_030)
        writer.write("PerWeaveB", 0.1)
        writer.write("TruckSpeed", 55)
        writer.write("AVONonNB", 1.38)
        writer.write("AVONonB", 1.65)
        writer.write("AVOPeakNB", 1.42)
        writer.write("AVOPeakB", 1.7)
        writer.write("AVOHovNB", 0)
        writer.write("AVOHovB", 2.15)

        writer.write("1) Project Information!P11", 150)
        writer.write("1) Project Information!P12", 3)
        writer.write("1) Project Information!P13", 34)

        writer.write("RateGroupNB", "H")
        writer.write("RateGroupB", "H")
        writer.write("AccStAvgNB", 1.14)
        writer.write("AccStAvgB", 0.64)
        writer.write("PFatStAvgNB", 0.006)
        writer.write("PFatStAvgB", 0.005)
        writer.write("PInjStAvgNB", 0.38)
        writer.write("PInjStAvgB", 0.321)

        writer.write("TAPT1NB", 1_602)
        writer.write("TAPT1B", 1_602)
        writer.write("TAPT20NB", 3_037)
        writer.write("TAPT20B", 4)

        writer.write("TVehMi1NB", 8)
        writer.write("TVehMi1B", 8)
        writer.write("TVehMi20NB", 16)
        writer.write("TVehMi20B", 16)

        writer.write("TInTimeNBN", 1)
        writer.write("TInTimeNBP", 10)

        writer.write("TPerHwy", 0)

        writer.write("1) Project Information!W15", 775)
        writer.write("1) Project Information!W16", 2_500)
        writer.write("1) Project Information!W17", 250)
        writer.write("1) Project Information!W18", 250)
        writer.write("1) Project Information!W19", 250)
        writer.write("1) Project Information!W20", 125)

        writer.write("1) Project Information!X15", 1_475)
        writer.write("1) Project Information!X16", 400)

        writer.write("1) Project Information!Y15", 5_000)
        writer.write("1) Project Information!Y16", 28_636)
        writer.write("1) Project Information!Y17", 40_000)
        writer.write("1) Project Information!Y18", 50_000)
        writer.write("1) Project Information!Y19", 10_000)
        writer.write("1) Project Information!Y20", 10_000)

        writer.write("1) Project Information!Z24", 10)
        writer.write("1) Project Information!Z25", 10)
        writer.write("1) Project Information!Z26", 10)
        writer.write("1) Project Information!Z25", 10)
        writer.write("1) Project Information!Z26", 10)
        writer.write("1) Project Information!Z27", 10)
        writer.write("1) Project Information!Z28", 10)
        writer.write("1) Project Information!Z29", 10)
        writer.write("1) Project Information!Z30", 10)
        writer.write("1) Project Information!Z31", 10)
        writer.write("1) Project Information!Z32", 10)
        writer.write("1) Project Information!Z33", 10)
        writer.write("1) Project Information!Z34", 10)
        writer.write("1) Project Information!Z35", 10)
        writer.write("1) Project Information!Z36", 10)
        writer.write("1) Project Information!Z37", 10)
        writer.write("1) Project Information!Z38", 10)
        writer.write("1) Project Information!Z39", 10)
        writer.write("1) Project Information!Z40", 10)
        writer.write("1) Project Information!Z41", 10)
        writer.write("1) Project Information!Z42", 10)
        writer.write("1) Project Information!Z43", 10)

        # 2) Model Inputs
        writer.write("2) Model Inputs!H13", 0)
        writer.write("2) Model Inputs!H32", 0)

        # 3) Results
        writer.write("VehOp", "N")
        writer.write("Emissions", "N")

        workbook.save(output_file)

        compiler = ModelCompiler()
        new_model = compiler.read_and_parse_archive(output_file, build_code=False)
        new_model.persist_to_json_file(f"{output_file}.json")

        model = Model()
        model.construct_from_json_file(f"{output_file}.json", build_code=True)
        return model

    @pytest.fixture
    def evaluator(self, model: Model) -> Evaluator:
        return Evaluator(model)

    def test_calculation(self, evaluator: Evaluator):
        # Investment Analysis
        assert round(evaluator.evaluate("3) Results!H13"), 2) == 136.65
        assert round(evaluator.evaluate("3) Results!H14"), 2) == 343.13
