import autoschema as schema


def test_import():
  assert hasattr(schema, "__version__")
