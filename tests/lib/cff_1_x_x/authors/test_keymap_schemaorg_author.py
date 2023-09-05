# pylint:disable = protected-access
import inspect
import types
import pytest
from cffconvert.lib.cff_1_x_x.authors.schemaorg import SchemaorgAuthor
from .get_every_key import get_every_key


@pytest.mark.lib
@pytest.mark.parametrize("key", get_every_key())
def test_keys_schemaorg_author(key):
    author = SchemaorgAuthor(author=None)
    assert key in author._behaviors
    assert isinstance(author._behaviors[key], (types.MethodType, types.FunctionType))


@pytest.mark.lib
def test_number_of_keys():
    expected = len(get_every_key())
    actual = len(SchemaorgAuthor(author=None)._behaviors)
    assert actual == expected


@pytest.mark.lib
def test_all_methods_used():
    author = SchemaorgAuthor(author=None)
    used_method_names = [elem.__name__ for elem in author._behaviors.values()]
    implementation_names = [
        k for k, v in inspect.getmembers(author, predicate=inspect.ismethod) if k.startswith("_from")
    ]
    for implementation_name in implementation_names:
        assert implementation_name in used_method_names
