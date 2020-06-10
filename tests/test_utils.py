import os


def _get_test_case_path(name: str) -> str:
    """Get the loaded JSON schema for a test case"""
    return os.path.realpath(os.path.join(os.path.dirname(__file__), "cases", f"{name}.json"))
