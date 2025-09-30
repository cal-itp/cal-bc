import logging
import pytest

from xlcalculator import Evaluator, Model, ModelCompiler
from calbc import functions

logging.basicConfig(level=logging.DEBUG)

class TestCalculation:
    # @pytest.fixture
    # def compiler(self) -> ModelCompiler:
    #     compiler = ModelCompiler()
    #     new_model = compiler.read_and_parse_archive('cal-bc-8-1-sketch-a11y-complete.xlsm', build_code=False)
    #     new_model.persist_to_json_file('cal-bc-8-1-sketch-a11y-complete.json')

    @pytest.fixture
    def model(self) -> Model:
        model = Model()
        model.construct_from_json_file('cal-bc-8-1-sketch-a11y.json', build_code=True)
        return model

    @pytest.fixture
    def evaluator(self, model: Model) -> Evaluator:
        return Evaluator(model)

    def test_calculation(self, evaluator: Evaluator):
        # Project Data
        evaluator.set_cell_value("ProjName", "Testing Project")
        evaluator.set_cell_value("ProjType", "    HOV Lane Addition")
        evaluator.set_cell_value("ProjLoc", 1)
        evaluator.set_cell_value("Construct", 6)

        # Highway design and traffic data
        evaluator.set_cell_value("GenLanesNB", 2)
        evaluator.set_cell_value("GenLanesB", 2)
        evaluator.set_cell_value("HOVLanesNB", 0)
        evaluator.set_cell_value("HOVLanesB", 2)
        evaluator.set_cell_value("HOVRest", 2)
        evaluator.set_cell_value("FFSpeedNB", 65)
        evaluator.set_cell_value("SegmentNB", 1.1)
        evaluator.set_cell_value("ADT0", 90_000)
        evaluator.set_cell_value("ADT1NB", 101_617)
        evaluator.set_cell_value("ADT1B", 117_490)
        evaluator.set_cell_value("ADT20NB", 138_405)
        evaluator.set_cell_value("ADT20B", 148_823)
        evaluator.set_cell_value("HOVvolNB", 0)
        evaluator.set_cell_value("HOVvolB", 2_030)
        evaluator.set_cell_value("PerWeaveB", 0.1)
        evaluator.set_cell_value("TruckSpeed", 55)
        evaluator.set_cell_value("AVONonNB", 1.38)
        evaluator.set_cell_value("AVONonB", 1.65)
        evaluator.set_cell_value("AVOPeakNB", 1.42)
        evaluator.set_cell_value("AVOPeakB", 1.7)
        evaluator.set_cell_value("AVOHovNB", 0)
        evaluator.set_cell_value("AVOHovB", 2.15)

        evaluator.set_cell_value("PARAMETERS!P11", 150)
        evaluator.set_cell_value("PARAMETERS!P12", 3)
        evaluator.set_cell_value("PARAMETERS!P13", 34)

        evaluator.set_cell_value("RateGroupNB", "H")
        evaluator.set_cell_value("RateGroupB", "H")
        evaluator.set_cell_value("AccStAvgNB", 1.14)
        evaluator.set_cell_value("AccStAvgB", 0.64)
        evaluator.set_cell_value("PFatStAvgNB", 0.006)
        evaluator.set_cell_value("PFatStAvgB", 0.005)
        evaluator.set_cell_value("PInjStAvgNB", 0.38)
        evaluator.set_cell_value("PInjStAvgB", 0.321)

        evaluator.set_cell_value("TAPT1NB", 1_602)
        evaluator.set_cell_value("TAPT1B", 1_602)
        evaluator.set_cell_value("TAPT20NB", 3_037)
        evaluator.set_cell_value("TAPT20B", 4)

        evaluator.set_cell_value("TVehMi1NB", 8)
        evaluator.set_cell_value("TVehMi1B", 8)
        evaluator.set_cell_value("TVehMi20NB", 16)
        evaluator.set_cell_value("TVehMi20B", 16)

        evaluator.set_cell_value("TInTimeNBN", 1)
        evaluator.set_cell_value("TInTimeNBP", 10)

        evaluator.set_cell_value("1) Project Information!W15", 775)
        evaluator.set_cell_value("1) Project Information!W16", 2_500)
        evaluator.set_cell_value("1) Project Information!W17", 250)
        evaluator.set_cell_value("1) Project Information!W18", 250)
        evaluator.set_cell_value("1) Project Information!W19", 250)
        evaluator.set_cell_value("1) Project Information!W20", 125)

        evaluator.set_cell_value("1) Project Information!X15", 1_475)
        evaluator.set_cell_value("1) Project Information!X16", 400)

        evaluator.set_cell_value("1) Project Information!Y15", 5_000)
        evaluator.set_cell_value("1) Project Information!Y16", 28_636)
        evaluator.set_cell_value("1) Project Information!Y17", 40_000)
        evaluator.set_cell_value("1) Project Information!Y18", 50_000)
        evaluator.set_cell_value("1) Project Information!Y19", 10_000)
        evaluator.set_cell_value("1) Project Information!Y20", 10_000)

        evaluator.set_cell_value("1) Project Information!Z24", 10)
        evaluator.set_cell_value("1) Project Information!Z25", 10)
        evaluator.set_cell_value("1) Project Information!Z26", 10)
        evaluator.set_cell_value("1) Project Information!Z25", 10)
        evaluator.set_cell_value("1) Project Information!Z26", 10)
        evaluator.set_cell_value("1) Project Information!Z27", 10)
        evaluator.set_cell_value("1) Project Information!Z28", 10)
        evaluator.set_cell_value("1) Project Information!Z29", 10)
        evaluator.set_cell_value("1) Project Information!Z31", 10)
        evaluator.set_cell_value("1) Project Information!Z32", 10)
        evaluator.set_cell_value("1) Project Information!Z33", 10)
        evaluator.set_cell_value("1) Project Information!Z34", 10)
        evaluator.set_cell_value("1) Project Information!Z35", 10)
        evaluator.set_cell_value("1) Project Information!Z36", 10)
        evaluator.set_cell_value("1) Project Information!Z37", 10)
        evaluator.set_cell_value("1) Project Information!Z38", 10)
        evaluator.set_cell_value("1) Project Information!Z39", 10)
        evaluator.set_cell_value("1) Project Information!Z41", 10)
        evaluator.set_cell_value("1) Project Information!Z42", 10)
        evaluator.set_cell_value("1) Project Information!Z43", 10)

        # Cost table
        evaluator.set_cell_value("1) Project Information!AE44", 136_683_626)

        # Intermediate calculations
        # assert evaluator.evaluate("PNV1NB") == 37266.075756
        # assert evaluator.evaluate("Travel Time!C55") == 13602117.65094 # returns 13_602_091 when PNV1NB is truncated to 0 decimal points
        # assert evaluator.evaluate("2) Model Inputs!G29") == 50_757.26565000001
        # assert evaluator.evaluate("2) Model Inputs!G38") == 75_191.28435
        assert evaluator.evaluate("Final Calculations!R55") ==  75_570_260.78103024
        assert evaluator.evaluate("Final Calculations!R55") == 343_162_064

        # Investment Analysis
        # lifecycle_costs = evaluator.evaluate("3) Results!H13")
        # assert lifecycle_costs == 136.653989
        # lifecycle_benefits = evaluator.evaluate("3) Results!H14")
        # assert lifecycle_benefits == 9.5
