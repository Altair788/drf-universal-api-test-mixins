import pytest
from mixins import CRUDAPITestMixin

def test_crud_mixin_exists():
    assert hasattr(CRUDAPITestMixin, "__class__")