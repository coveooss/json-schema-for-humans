

# Schema Docs

Type: `object`

**Description:** Testing $ref

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [a_gift](#a_gift)|No|string|No|No| No|A gift, or is it?|
| [anchor_with_slash](#anchor_with_slash)|No|object|No|No| No|-|
| [anchor_no_slash](#anchor_no_slash)|No|array of string|No|No| No|Description for array_def|
| [anchor_nested_reference](#anchor_nested_reference)|No|string|No|No| No|-|
| [same_file_anchor_with_slash](#same_file_anchor_with_slash)|No|string|No|No| No|Description for string_def|
| [same_file_anchor_no_slash](#same_file_anchor_no_slash)|No|object|No|No| No|-|
| [same_file_nested_reference](#same_file_nested_reference)|No|string|No|No| No|-|
| [other_file_anchor](#other_file_anchor)|No|object|No|No| No|The delivery is a gift, no prices displayed|
| [other_file_dot_anchor](#other_file_dot_anchor)|No|object|No|No| No|The delivery is a gift, no prices displayed|
| [other_file_dot_dot_anchor](#other_file_dot_dot_anchor)|No|object|No|No| No|The delivery is a gift, no prices displayed|
| [other_file_only](#other_file_only)|No|object|No|No| No|Test schema with a not|
| [multi_hierarchy_reference](#multi_hierarchy_reference)|No|object|No|No| No|-|

##  <a name="a_gift"></a>1.  Property `root > a_gift`

Type: `string`

**Description:** A gift, or is it?

Type: `string`

**Description:** A gift, or is it?

##  <a name="anchor_with_slash"></a>2.  Property `root > anchor_with_slash`

Type: `object`

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [propertyA](#anchor_with_slash_propertyA)|No|string|No|No| No|Description for object_def/items/propertyA|
| additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") | - |

###  <a name="anchor_with_slash_propertyA"></a>2.1.  Property `root > anchor_with_slash > propertyA`

Type: `string`

**Description:** Description for object_def/items/propertyA

##  <a name="anchor_no_slash"></a>3.  Property `root > anchor_no_slash`

Type: `array of string`

**Description:** Description for array_def

Type: `array of string`

**Description:** Description for array_def

<table>
 	<tr>
    <td><b>Min items</b></td>
    <td>N/A</td>
 	</tr>
	<tr>
    <td><b>Max items</b></td>
    <td>N/A</td>
	</tr>
	<tr>
    <td><b>Items unicity</b></td>
    <td>False</td>
 	</tr>
</table>

###  3. Each item of this array must be

Type: `string`

##  <a name="anchor_nested_reference"></a>4.  Property `root > anchor_nested_reference`

Type: `string`

Type: `string`

Type: `string`

##  <a name="same_file_anchor_with_slash"></a>5.  Property `root > same_file_anchor_with_slash`

Type: `string`

**Description:** Description for string_def

Type: `string`

**Description:** Description for string_def

##  <a name="same_file_anchor_no_slash"></a>6.  Property `root > same_file_anchor_no_slash`

Type: `object`

    Same definition as [anchor_with_slash](#anchor_with_slash)

##  <a name="same_file_nested_reference"></a>7.  Property `root > same_file_nested_reference`

Type: `string`

    Same definition as [anchor_nested_reference](#anchor_nested_reference)

##  <a name="other_file_anchor"></a>8.  Property `root > other_file_anchor`

Type: `object`

**Description:** The delivery is a gift, no prices displayed

Type: `object`

**Description:** The delivery is a gift, no prices displayed

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [with_wrap](#other_file_anchor_with_wrap)|No|boolean|No|No| No|-|

###  <a name="other_file_anchor_with_wrap"></a>8.1.  Property `root > other_file_anchor > with_wrap`

Type: `boolean`

##  <a name="other_file_dot_anchor"></a>9.  Property `root > other_file_dot_anchor`

Type: `object`

**Description:** The delivery is a gift, no prices displayed
    Same definition as [other_file_anchor](#other_file_anchor)

##  <a name="other_file_dot_dot_anchor"></a>10.  Property `root > other_file_dot_dot_anchor`

Type: `object`

**Description:** The delivery is a gift, no prices displayed
    Same definition as [other_file_anchor](#other_file_anchor)

##  <a name="other_file_only"></a>11.  Property `root > other_file_only`

Type: `object`

**Description:** Test schema with a not

Type: `object`

**Description:** Test schema with a not

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [not_a_string](#other_file_only_not_a_string)|No|object|Yes|No| No|-|

###  <a name="other_file_only_not_a_string"></a>11.1.  Property `root > other_file_only > not_a_string`

#### Must **not** be

Type: `string`

##  <a name="multi_hierarchy_reference"></a>12.  Property `root > multi_hierarchy_reference`

Type: `object`

Type: `object`

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [propertyA](#multi_hierarchy_reference_propertyA)|No|string|No|No| No|Contents of propertyA in final.json|
| additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") | - |

###  <a name="multi_hierarchy_reference_propertyA"></a>12.1.  Property `root > multi_hierarchy_reference > propertyA`

Type: `string`

**Description:** Contents of propertyA in final.json

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 21:26:33 +0100