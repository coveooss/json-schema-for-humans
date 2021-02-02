

# Person

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [firstName](#firstName)|No|string|No|No| No|The person's first name.|
| [lastName](#lastName)|No|string|No|No| No|The person's last name.|
| [$[a-c][0-9]^](#pattern1)|Yes|object|No|No| No|Review of a paper size.|

##  <a name="firstName"></a>1.  Property `Person > firstName`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/pattern_properties.json', 'path_to_element': ['firstName'], 'html_id': 'firstName', 'breadcrumb_name': 'firstName', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248e850>, 'parent_key': 'firstName', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248e130>, 'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248e910>, 'title': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248efd0>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

**Description:** The person's first name.

##  <a name="lastName"></a>2.  Property `Person > lastName`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/pattern_properties.json', 'path_to_element': ['lastName'], 'html_id': 'lastName', 'breadcrumb_name': 'lastName', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248e850>, 'parent_key': 'lastName', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248e040>, 'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248ea90>, 'title': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248ef10>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

**Description:** The person's last name.

##  <a name="pattern1"></a>3. Pattern Property `Person > paperSize`
> All property whose name matches the following regular expression must respect the following conditions
  Property name regular expression: 
[`$[a-c][0-9]^`](https://regex101.com/?regex=$[a-c][0-9]^

> All property whose name matches the following regular expression must respect the following conditions
  Property name regular expression: 
[`$[a-c][0-9]^`](https://regex101.com/?regex=$[a-c][0-9]^

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/pattern_properties.json', 'path_to_element': ['$[a-c][0-9]^'], 'html_id': 'pattern1', 'breadcrumb_name': '$[a-c][0-9]^', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248e850>, 'parent_key': '$[a-c][0-9]^', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248edf0>, 'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248e700>, 'title': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248e4f0>, 'required': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248eaf0>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {'rating': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248eee0>, 'review': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248e9d0>}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

**Description:** Review of a paper size.

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [rating](#pattern1_rating)|No|integer|Yes|No| No|Numerical rating for paper size.|
| [review](#pattern1_review)|No|string|Yes|No| No|Narrative review of the paper size.|

###  <a name="pattern1_rating"></a>3.1.  Property `Person > paperSize > rating`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/pattern_properties.json', 'path_to_element': ['$[a-c][0-9]^', 'rating'], 'html_id': 'pattern1_rating', 'breadcrumb_name': 'rating', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248e3d0>, 'parent_key': 'rating', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248ed30>, 'title': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248e340>, 'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248e760>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `integer`

**Description:** Numerical rating for paper size.

###  <a name="pattern1_review"></a>3.2.  Property `Person > paperSize > review`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/pattern_properties.json', 'path_to_element': ['$[a-c][0-9]^', 'review'], 'html_id': 'pattern1_review', 'breadcrumb_name': 'review', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248e3d0>, 'parent_key': 'review', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248e490>, 'title': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248ecd0>, 'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248e820>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

**Description:** Narrative review of the paper size.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 22:00:59 +0100