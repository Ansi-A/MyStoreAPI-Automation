import json
from pathlib import Path
from jsonschema import validate,ValidationError



def validate_schema(get_data,schema_file):
    schema_path = Path(__file__).resolve().parent / "schemas" / schema_file
    with open(schema_path, 'r') as json_file:
        schema_body = json.load(json_file)


        try:
            validate(instance=get_data,schema=schema_body)
            print("Schema is validated successfully")
        except ValidationError as e:
            print(e)
            assert False

