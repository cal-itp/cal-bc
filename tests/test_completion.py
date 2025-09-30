import logging
import pytest
import os

import openpyxl

logging.basicConfig(level=logging.DEBUG)

class CellValueWriter:
    def __init__(self, workbook: openpyxl.Workbook) -> None:
        self.workbook = workbook

    def write(self, cell_address: str, new_value: any) -> None:
        sheet, cell = cell_address.split("!")
        reference = self.workbook[sheet][cell]
        self.workbook[sheet][cell].value = new_value

    def named_write(self, cell_name: str, new_value: any) -> None:
        reference = self.workbook.defined_names[cell_name]
        destinations = [(sheet, value.replace("$", "")) for (sheet, value) in reference.destinations]
        sheet, cell = destinations[0]
        self.workbook[sheet][cell].value = new_value


class TestCompletion:
    @pytest.fixture
    def workbook_file(self) -> str:
        return "cal-bc-8-1-sketch-a11y.xlsm"

    @pytest.fixture
    def output_file(self) -> str:
        return "cal-bc-8-1-sketch-a11y-complete.xlsm"

    @pytest.fixture
    def workbook(self, workbook_file: str) -> openpyxl.Workbook:
        return openpyxl.load_workbook(filename=workbook_file, keep_vba=True)

    def test_completion(self, workbook: openpyxl.Workbook, output_file: str) -> None:
        writer = CellValueWriter(workbook=workbook)

        # 1) Project Information
        writer.named_write(cell_name="ProjName", new_value="Testing Project")
        writer.named_write(cell_name="ProjType", new_value="    HOV Lane Addition")
        writer.named_write(cell_name="ProjLoc", new_value=1)
        writer.named_write(cell_name="Construct", new_value=6)

        # Highway design and traffic data
        writer.named_write(cell_name="GenLanesNB", new_value=2)
        writer.named_write(cell_name="GenLanesB", new_value=2)
        writer.named_write(cell_name="HOVLanesNB", new_value=0)
        writer.named_write(cell_name="HOVLanesB", new_value=2)
        writer.named_write(cell_name="HOVRest", new_value=2)
        writer.named_write(cell_name="FFSpeedNB", new_value=65)
        writer.named_write(cell_name="SegmentNB", new_value=1.1)
        writer.named_write(cell_name="ADT0", new_value=90_000)
        writer.named_write(cell_name="ADT1NB", new_value=101_617)
        writer.named_write(cell_name="ADT1B", new_value=117_490)
        writer.named_write(cell_name="ADT20NB", new_value=138_405)
        writer.named_write(cell_name="ADT20B", new_value=148_823)
        writer.named_write(cell_name="HOVvolNB", new_value=0)
        writer.named_write(cell_name="HOVvolB", new_value=2_030)
        writer.named_write(cell_name="PerWeaveB", new_value=0.1)
        writer.named_write(cell_name="TruckSpeed", new_value=55)
        writer.named_write(cell_name="AVONonNB", new_value=1.38)
        writer.named_write(cell_name="AVONonB", new_value=1.65)
        writer.named_write(cell_name="AVOPeakNB", new_value=1.42)
        writer.named_write(cell_name="AVOPeakB", new_value=1.7)
        writer.named_write(cell_name="AVOHovNB", new_value=0)
        writer.named_write(cell_name="AVOHovB", new_value=2.15)

        writer.write(cell_address="1) Project Information!P11", new_value=150)
        writer.write(cell_address="1) Project Information!P12", new_value=3)
        writer.write(cell_address="1) Project Information!P13", new_value=34)

        writer.named_write(cell_name="RateGroupNB", new_value="H")
        writer.named_write(cell_name="RateGroupB", new_value="H")
        writer.named_write(cell_name="AccStAvgNB", new_value=1.14)
        writer.named_write(cell_name="AccStAvgB", new_value=0.64)
        writer.named_write(cell_name="PFatStAvgNB", new_value=0.006)
        writer.named_write(cell_name="PFatStAvgB", new_value=0.005)
        writer.named_write(cell_name="PInjStAvgNB", new_value=0.38)
        writer.named_write(cell_name="PInjStAvgB", new_value=0.321)

        writer.named_write(cell_name="TAPT1NB", new_value=1_602)
        writer.named_write(cell_name="TAPT1B", new_value=1_602)
        writer.named_write(cell_name="TAPT20NB", new_value=3_037)
        writer.named_write(cell_name="TAPT20B", new_value=4)

        writer.named_write(cell_name="TVehMi1NB", new_value=8)
        writer.named_write(cell_name="TVehMi1B", new_value=8)
        writer.named_write(cell_name="TVehMi20NB", new_value=16)
        writer.named_write(cell_name="TVehMi20B", new_value=16)

        writer.named_write(cell_name="TInTimeNBN", new_value=1)
        writer.named_write(cell_name="TInTimeNBP", new_value=10)

        writer.named_write(cell_name="TPerHwy", new_value=0)

        writer.write(cell_address="1) Project Information!W15", new_value=775)
        writer.write(cell_address="1) Project Information!W16", new_value=2_500)
        writer.write(cell_address="1) Project Information!W17", new_value=250)
        writer.write(cell_address="1) Project Information!W18", new_value=250)
        writer.write(cell_address="1) Project Information!W19", new_value=250)
        writer.write(cell_address="1) Project Information!W20", new_value=125)

        writer.write(cell_address="1) Project Information!X15", new_value=1_475)
        writer.write(cell_address="1) Project Information!X16", new_value=400)

        writer.write(cell_address="1) Project Information!Y15", new_value=5_000)
        writer.write(cell_address="1) Project Information!Y16", new_value=28_636)
        writer.write(cell_address="1) Project Information!Y17", new_value=40_000)
        writer.write(cell_address="1) Project Information!Y18", new_value=50_000)
        writer.write(cell_address="1) Project Information!Y19", new_value=10_000)
        writer.write(cell_address="1) Project Information!Y20", new_value=10_000)

        writer.write(cell_address="1) Project Information!Z24", new_value=10)
        writer.write(cell_address="1) Project Information!Z25", new_value=10)
        writer.write(cell_address="1) Project Information!Z26", new_value=10)
        writer.write(cell_address="1) Project Information!Z25", new_value=10)
        writer.write(cell_address="1) Project Information!Z26", new_value=10)
        writer.write(cell_address="1) Project Information!Z27", new_value=10)
        writer.write(cell_address="1) Project Information!Z28", new_value=10)
        writer.write(cell_address="1) Project Information!Z29", new_value=10)
        writer.write(cell_address="1) Project Information!Z30", new_value=10)
        writer.write(cell_address="1) Project Information!Z31", new_value=10)
        writer.write(cell_address="1) Project Information!Z32", new_value=10)
        writer.write(cell_address="1) Project Information!Z33", new_value=10)
        writer.write(cell_address="1) Project Information!Z34", new_value=10)
        writer.write(cell_address="1) Project Information!Z35", new_value=10)
        writer.write(cell_address="1) Project Information!Z36", new_value=10)
        writer.write(cell_address="1) Project Information!Z37", new_value=10)
        writer.write(cell_address="1) Project Information!Z38", new_value=10)
        writer.write(cell_address="1) Project Information!Z39", new_value=10)
        writer.write(cell_address="1) Project Information!Z40", new_value=10)
        writer.write(cell_address="1) Project Information!Z41", new_value=10)
        writer.write(cell_address="1) Project Information!Z42", new_value=10)
        writer.write(cell_address="1) Project Information!Z43", new_value=10)

        # 2) Model Inputs
        writer.write(cell_address="2) Model Inputs!H13", new_value=0)
        writer.write(cell_address="2) Model Inputs!H32", new_value=0)

        # 3) Results
        writer.named_write(cell_name="VehOp", new_value="N")
        writer.named_write(cell_name="Emissions", new_value="N")

        workbook.save(output_file)
