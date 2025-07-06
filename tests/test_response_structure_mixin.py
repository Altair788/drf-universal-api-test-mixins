from mixins import ResponseStructureMixin

def test_response_structure_mixin_exists():
    assert hasattr(ResponseStructureMixin, "__class__")
