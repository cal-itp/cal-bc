import logging
from xlcalculator import ModelCompiler

logging.basicConfig(level=logging.DEBUG)

compiler = ModelCompiler()

filename = r"AT_model_updated.xlsx"
new_model = compiler.read_and_parse_archive(filename, build_code=False)

json_file_name = r"AT_model_updated.json"
new_model.persist_to_json_file(json_file_name)
