import re

import htmlmin
import jinja2
import markdown2
from jinja2 import FileSystemLoader, Template
from jinja2.ext import loopcontrols

from json_schema_for_humans import jinja_filters, templating_utils
from json_schema_for_humans.generation_configuration import GenerationConfiguration
from json_schema_for_humans.md_template import MarkdownTemplate
from json_schema_for_humans.schema.schema_node import SchemaNode


def _minify(rendered: str, is_markdown: bool, is_html: bool) -> str:
    if is_markdown:
        return re.sub(r"\n\s*\n", "\n\n", rendered)
    if is_html:
        return htmlmin.minify(rendered)
    return rendered


class TemplateRenderer:
    def __init__(self, config: GenerationConfiguration, template: Template = None):
        self.config = config
        self.template = template or self._get_jinja_template()

    def _get_jinja_template(self) -> Template:
        loader = FileSystemLoader(self.config.template_path.parent)
        env = jinja2.Environment(
            loader=loader,
            extensions=[loopcontrols],
            trim_blocks=(self.config.template_is_markdown),
            lstrip_blocks=(self.config.template_is_markdown),
        )
        env.globals["jsfh_config"] = self.config
        env.globals["jsfh_md"] = markdown2.Markdown(extras=self.config.markdown_options)
        if self.config.template_is_markdown:
            md_template = MarkdownTemplate(self.config)
            md_template.register_jinja(env)

        env.filters["python_to_json"] = jinja_filters.python_to_json
        env.filters["get_default"] = (
            jinja_filters.get_default_look_in_description
            if self.config.default_from_description
            else jinja_filters.get_default
        )
        env.filters["get_type_name"] = templating_utils.get_type_name
        env.filters["get_description"] = jinja_filters.get_description
        env.filters["get_numeric_restrictions_text"] = jinja_filters.get_numeric_restrictions_text

        env.filters["get_required_properties"] = jinja_filters.get_required_properties
        env.filters["get_first_property"] = jinja_filters.get_first_property
        env.filters["get_undocumented_required_properties"] = jinja_filters.get_undocumented_required_properties
        env.filters["highlight_json_example"] = jinja_filters.highlight_json_example
        env.filters["highlight_yaml_example"] = jinja_filters.highlight_yaml_example
        env.filters["yaml_example"] = jinja_filters.yaml_example
        env.filters["first_line"] = jinja_filters.first_line

        env.tests["combining"] = jinja_filters.is_combining
        env.tests["description_short"] = jinja_filters.is_text_short
        env.tests["deprecated"] = lambda schema: jinja_filters.deprecated(self.config, schema)
        env.globals["examples_as_yaml"] = self.config.examples_as_yaml
        env.globals["get_local_time"] = jinja_filters.get_local_time

        with open(self.config.template_path, "r") as template_fp:
            template = env.from_string(template_fp.read())

        return template

    def render(self, intermediate_schema: SchemaNode) -> str:
        rendered = self.template.render(schema=intermediate_schema, config=self.config)

        if self.config.minify:
            rendered = _minify(rendered, self.config.template_is_markdown, self.config.template_is_html)

        return rendered
