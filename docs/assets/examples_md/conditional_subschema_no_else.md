

# Schema Docs

| Node | 
| ---- |
| [All of(Requirement) 1](#allOf_i0) |
| [All of(Requirement) 2](#allOf_i1) |
| [All of(Requirement) 3](#allOf_i2) |
##  1.  Property `root > allOf > item 0`

Type: `object`

## Conditional Subschema
If the conditions in the "If" tab are respected, then the conditions in the "Then" tab should be respected.
Otherwise, the conditions in the "Else" tab should be respected.
**[If](#tab-pane_allOf_i0_if"):**

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [country](#allOf_i0_if_country)|No|const|No|No| No|-|

##  <a name="allOf_i0_if_country"></a>1.  Property `root > allOf > item 0 > if > country`

      {'depth': 4, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/conditional_subschema_no_else.json', 'path_to_element': ['allOf', 0, 'if', 'country'], 'html_id': 'allOf_i0_if_country', 'breadcrumb_name': 'country', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fdc10>, 'parent_key': 'country', 'ref_path': '', 'literal': None, 'keywords': {'const': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fd4c0>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `const`

            Specific value: `"United States of America"`

**[Then](#tab-pane_allOf_i0_then):**

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [postal_code](#allOf_i0_then_postal_code)|No|object|No|No| No|-|

##  <a name="allOf_i0_then_postal_code"></a>1.  Property `root > allOf > item 0 > then > postal_code`

      {'depth': 4, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/conditional_subschema_no_else.json', 'path_to_element': ['allOf', 0, 'then', 'postal_code'], 'html_id': 'allOf_i0_then_postal_code', 'breadcrumb_name': 'postal_code', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fd7f0>, 'parent_key': 'postal_code', 'ref_path': '', 'literal': None, 'keywords': {'pattern': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fdd60>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

            Must match regular expression: `[0-9]{5}(-[0-9]{4})?` [Test](https://regex101.com/?regex=[0-9]{5}(-[0-9]{4})?)

##  2.  Property `root > allOf > item 1`

Type: `object`

## Conditional Subschema
If the conditions in the "If" tab are respected, then the conditions in the "Then" tab should be respected.
Otherwise, the conditions in the "Else" tab should be respected.
**[If](#tab-pane_allOf_i1_if"):**

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [country](#allOf_i1_if_country)|No|const|No|No| No|-|

##  <a name="allOf_i1_if_country"></a>1.  Property `root > allOf > item 1 > if > country`

      {'depth': 4, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/conditional_subschema_no_else.json', 'path_to_element': ['allOf', 1, 'if', 'country'], 'html_id': 'allOf_i1_if_country', 'breadcrumb_name': 'country', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fda90>, 'parent_key': 'country', 'ref_path': '', 'literal': None, 'keywords': {'const': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fdb50>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `const`

            Specific value: `"Canada"`

**[Then](#tab-pane_allOf_i1_then):**

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [postal_code](#allOf_i1_then_postal_code)|No|object|No|No| No|-|

##  <a name="allOf_i1_then_postal_code"></a>1.  Property `root > allOf > item 1 > then > postal_code`

      {'depth': 4, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/conditional_subschema_no_else.json', 'path_to_element': ['allOf', 1, 'then', 'postal_code'], 'html_id': 'allOf_i1_then_postal_code', 'breadcrumb_name': 'postal_code', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fd850>, 'parent_key': 'postal_code', 'ref_path': '', 'literal': None, 'keywords': {'pattern': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fde50>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

            Must match regular expression: `[A-Z][0-9][A-Z] [0-9][A-Z][0-9]` [Test](https://regex101.com/?regex=[A-Z][0-9][A-Z] [0-9][A-Z][0-9])

##  3.  Property `root > allOf > item 2`

Type: `object`

## Conditional Subschema
If the conditions in the "If" tab are respected, then the conditions in the "Then" tab should be respected.
Otherwise, the conditions in the "Else" tab should be respected.
**[If](#tab-pane_allOf_i2_if"):**

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [country](#allOf_i2_if_country)|No|const|No|No| No|-|

##  <a name="allOf_i2_if_country"></a>1.  Property `root > allOf > item 2 > if > country`

      {'depth': 4, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/conditional_subschema_no_else.json', 'path_to_element': ['allOf', 2, 'if', 'country'], 'html_id': 'allOf_i2_if_country', 'breadcrumb_name': 'country', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223981c0>, 'parent_key': 'country', 'ref_path': '', 'literal': None, 'keywords': {'const': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223982e0>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `const`

            Specific value: `"Netherlands"`

**[Then](#tab-pane_allOf_i2_then):**

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [postal_code](#allOf_i2_then_postal_code)|No|object|No|No| No|-|

##  <a name="allOf_i2_then_postal_code"></a>1.  Property `root > allOf > item 2 > then > postal_code`

      {'depth': 4, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/conditional_subschema_no_else.json', 'path_to_element': ['allOf', 2, 'then', 'postal_code'], 'html_id': 'allOf_i2_then_postal_code', 'breadcrumb_name': 'postal_code', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223988b0>, 'parent_key': 'postal_code', 'ref_path': '', 'literal': None, 'keywords': {'pattern': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122398760>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

            Must match regular expression: `[0-9]{4} [A-Z]{2}` [Test](https://regex101.com/?regex=[0-9]{4} [A-Z]{2})

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [street_address](#street_address)|No|string|No|No| No|-|
| [country](#country)|No|enum (of string)|No|No| No|-|

##  <a name="street_address"></a>1.  Property `root > street_address`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/conditional_subschema_no_else.json', 'path_to_element': ['street_address'], 'html_id': 'street_address', 'breadcrumb_name': 'street_address', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fd370>, 'parent_key': 'street_address', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fd8e0>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

##  <a name="country"></a>2.  Property `root > country`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/conditional_subschema_no_else.json', 'path_to_element': ['country'], 'html_id': 'country', 'breadcrumb_name': 'country', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fd370>, 'parent_key': 'country', 'ref_path': '', 'literal': None, 'keywords': {'enum': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fdcd0>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `enum (of string)`

            Must be one of:
                * "United States of America"
                * "Canada"
                * "Netherlands"

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 22:00:58 +0100