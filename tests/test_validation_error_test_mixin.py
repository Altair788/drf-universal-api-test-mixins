from mixins import ValidationErrorTestMixin

def test_validation_error_test_mixin_exists():
    assert hasattr(ValidationErrorTestMixin, "__class__")