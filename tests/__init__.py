import pytest

# Show assertion details in the output https://docs.pytest.org/en/stable/writing_plugins.html#assertion-rewriting
pytest.register_assert_rewrite("tests.md_utils_asserts")
