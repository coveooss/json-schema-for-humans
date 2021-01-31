# Schema Docs

Type: `object`

**Description:** Testing $ref

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|a_gift|No|string|No|No| No|A gift, or is it?|
| [anchor_with_slash](#anchor_with_slash)|No|object|No|No| No||
|anchor_no_slash|No|array of string|No|No| No|Description for array_def|
|anchor_nested_reference|No|string|No|No| No||
|same_file_anchor_with_slash|No|string|No|No| No|Description for string_def|
| [same_file_anchor_no_slash](#same_file_anchor_no_slash)|No|object|No|No| No||
|same_file_nested_reference|No|string|No|No| No||
| [other_file_anchor](#other_file_anchor)|No|object|No|No| No|The delivery is a gift, no prices displayed|
| [other_file_dot_anchor](#other_file_dot_anchor)|No|object|No|No| No|The delivery is a gift, no prices displayed|
| [other_file_dot_dot_anchor](#other_file_dot_dot_anchor)|No|object|No|No| No|The delivery is a gift, no prices displayed|
| [other_file_only](#other_file_only)|No|object|No|No| No|Test schema with a not|
| [multi_hierarchy_reference](#multi_hierarchy_reference)|No|object|No|No| No||

## <a name="anchor_with_slash"></a>Property `anchor_with_slash`

      root
 >   anchor_with_slash

Type: `object`

                 `No Additional Properties`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|propertyA|No|string|No|No| No|Description for object_def/items/propertyA|

## <a name="same_file_anchor_no_slash"></a>Property `same_file_anchor_no_slash`

      root
 >   same_file_anchor_no_slash

Type: `object`

        Same definition as [anchor_with_slash](#anchor_with_slash)

## <a name="other_file_anchor"></a>Property `other_file_anchor`

**Description**:The delivery is a gift, no prices displayed

      root
 >   other_file_anchor

Type: `object`

**Description:** The delivery is a gift, no prices displayed

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|with_wrap|No|boolean|No|No| No||

## <a name="other_file_dot_anchor"></a>Property `other_file_dot_anchor`

**Description**:The delivery is a gift, no prices displayed

      root
 >   other_file_dot_anchor

Type: `object`

**Description:** The delivery is a gift, no prices displayed
        Same definition as [other_file_anchor](#other_file_anchor)

## <a name="other_file_dot_dot_anchor"></a>Property `other_file_dot_dot_anchor`

**Description**:The delivery is a gift, no prices displayed

      root
 >   other_file_dot_dot_anchor

Type: `object`

**Description:** The delivery is a gift, no prices displayed
        Same definition as [other_file_anchor](#other_file_anchor)

## <a name="other_file_only"></a>Property `other_file_only`

**Description**:Test schema with a not

      root
 >   other_file_only

Type: `object`

**Description:** Test schema with a not

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [not_a_string](#other_file_only_not_a_string)|No|object|Yes|No| No||

## <a name="other_file_only_not_a_string"></a>Property `not_a_string`

      root
 >   other_file_only
 >   not_a_string

#### Must **not** be
  root
 >   other_file_only
 >   not_a_string
 >   not

Type: `string`

## <a name="multi_hierarchy_reference"></a>Property `multi_hierarchy_reference`

      root
 >   multi_hierarchy_reference

Type: `object`

                 `No Additional Properties`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|propertyA|No|string|No|No| No|Contents of propertyA in final.json|

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-01-31 at 13:13:14 +0100