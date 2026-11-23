from json_schema_for_humans.const import DocumentationTemplate
from json_schema_for_humans.generate import generate_from_schema
from json_schema_for_humans.generation_configuration import GenerationConfiguration

from tests.test_utils import get_test_case_path


def test_default_values() -> None:
    """Test init GenerationConfiguration with default values"""
    config = GenerationConfiguration()
    assert config.markdown_options == {
        "breaks": {
            "on_newline": True,
            "on_backslash": True,
        },
        "fenced-code-blocks": {"cssclass": "highlight jumbotron"},
        "tables": None,
    }
    assert config.template_md_options is not None
    assert config.template_md_options["badge_as_image"] is False


def test_override_markdown_options() -> None:
    """Test init GenerationConfiguration with default values"""

    # override break-on-newline key
    config = GenerationConfiguration(markdown_options={"breaks": {"on_newline": False}})
    assert config.markdown_options == {
        "breaks": {"on_newline": False},
        "fenced-code-blocks": {"cssclass": "highlight jumbotron"},
        "tables": None,
    }
    # override fenced-code-blocks key
    config = GenerationConfiguration(
        markdown_options={
            "fenced-code-blocks": {"cssclass": "test"},
        }
    )
    assert config.markdown_options == {
        "breaks": {"on_newline": True, "on_backslash": True},
        "fenced-code-blocks": {"cssclass": "test"},
        "tables": None,
    }
    # override tables key
    config = GenerationConfiguration(markdown_options={"tables": ["test"]})
    assert config.markdown_options == {
        "breaks": {"on_newline": True, "on_backslash": True},
        "fenced-code-blocks": {"cssclass": "highlight jumbotron"},
        "tables": ["test"],
    }

    # add a new key
    config = GenerationConfiguration(markdown_options={"newKey": "test"})
    assert config.markdown_options == {
        "breaks": {"on_newline": True, "on_backslash": True},
        "fenced-code-blocks": {"cssclass": "highlight jumbotron"},
        "tables": None,
        "newKey": "test",
    }


def test_override_template_md_options() -> None:
    """Test init GenerationConfiguration with default values"""

    # add new new_property key
    config = GenerationConfiguration(
        template_md_options={
            "new_property": True,
        }
    )
    assert config.template_md_options == {
        "new_property": True,
        "badge_as_image": False,
        "show_heading_numbers": True,
        "show_array_restrictions": True,
        "properties_table_columns": [
            "Property",
            "Pattern",
            "Type",
            "Deprecated",
            "Definition",
            "Title/Description",
        ],
    }

    # override badge_as_image key
    config = GenerationConfiguration(
        deprecated_from_description=True,
        template_name=DocumentationTemplate.MD.value,
        template_md_options={"badge_as_image": "test"},
    )
    assert config.template_md_options is not None
    assert config.template_md_options["badge_as_image"] == "test"

    # override badge_as_image key
    config = GenerationConfiguration(
        deprecated_from_description=True,
        template_name=DocumentationTemplate.MD.value,
        template_md_options={"badge_as_image": True},
    )
    assert config.template_md_options is not None
    assert config.template_md_options["badge_as_image"] is True


class TestExtraFields:
    def test_extra_fields_default_values(self) -> None:
        """Test that extra_fields defaults to an empty dict."""
        config = GenerationConfiguration()
        assert config.extra_fields == {}

    def test_extra_fields_badges_appear_after_default(self) -> None:
        """Extra-field badges are rendered after Default and before <br/>."""
        config = GenerationConfiguration(
            extra_fields={"Unit": "#1a3a5c", "User Level": "#c47c00"},
        )
        result = generate_from_schema(get_test_case_path("extra_fields"), config=config)
        assert '<span class="badge extra-field-value" style="background-color: #1a3a5c' in result
        assert "Unit: seconds" in result
        assert "User Level: basic" in result
        # buffer_size has Unit but not User Level
        assert "Unit: bytes" in result

    def test_extra_fields_empty_dict_renders_no_badges(self) -> None:
        """An empty extra_fields dict (the default) produces no extra-field badges."""
        config = GenerationConfiguration()
        result = generate_from_schema(get_test_case_path("extra_fields"), config=config)
        assert "extra-field-value" not in result

    def test_extra_fields_absent_key_is_skipped(self) -> None:
        """A key in extra_fields that doesn't exist in a schema node is silently skipped."""
        config = GenerationConfiguration(
            extra_fields={"NonExistentKey": None},
        )
        result = generate_from_schema(get_test_case_path("extra_fields"), config=config)
        assert "NonExistentKey" not in result

    def test_extra_fields_none_color_uses_default(self) -> None:
        """A key in extra_fields with a None color uses the default color #1a3a5c."""
        config = GenerationConfiguration(
            extra_fields={"Unit": None},
        )
        result = generate_from_schema(get_test_case_path("extra_fields"), config=config)
        assert "background-color: #1a3a5c" in result
