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

## <a name="a_gift"></a> 1. Property `a_gift`

**Description**:  A gift, or is it?

      root
 >   a_gift

Type: `string`

**Description:** A gift, or is it?

## <a name="anchor_with_slash"></a> 2. Property `anchor_with_slash`

      root
 >   anchor_with_slash

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|propertyA|No|string|No|No| No|Description for object_def/items/propertyA|
`No Additional Properties`

### <a name="anchor_with_slash_propertyA"></a> 2.1. Property `propertyA`

**Description**:  Description for object_def/items/propertyA

      root
 >   anchor_with_slash
 >   propertyA

Type: `string`

**Description:** Description for object_def/items/propertyA

## <a name="anchor_no_slash"></a> 3. Property `anchor_no_slash`

**Description**:  Description for array_def

      root
 >   anchor_no_slash

Type: `array of string`

**Description:** Description for array_def

#### Each item of this array must be
  root
 >   anchor_no_slash
 >   items

Type: `string`

## <a name="anchor_nested_reference"></a> 4. Property `anchor_nested_reference`

      root
 >   anchor_nested_reference

Type: `string`

## <a name="same_file_anchor_with_slash"></a> 5. Property `same_file_anchor_with_slash`

**Description**:  Description for string_def

      root
 >   same_file_anchor_with_slash

Type: `string`

**Description:** Description for string_def

## <a name="same_file_anchor_no_slash"></a> 6. Property `same_file_anchor_no_slash`

      root
 >   same_file_anchor_no_slash

Type: `object`

        Same definition as [anchor_with_slash](#anchor_with_slash)

## <a name="same_file_nested_reference"></a> 7. Property `same_file_nested_reference`

      root
 >   same_file_nested_reference

Type: `string`

        Same definition as [anchor_nested_reference](#anchor_nested_reference)

## <a name="other_file_anchor"></a> 8. Property `other_file_anchor`

**Description**:  The delivery is a gift, no prices displayed

      root
 >   other_file_anchor

Type: `object`

**Description:** The delivery is a gift, no prices displayed

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|with_wrap|No|boolean|No|No| No||

### <a name="other_file_anchor_with_wrap"></a> 8.1. Property `with_wrap`

      root
 >   other_file_anchor
 >   with_wrap

Type: `boolean`

## <a name="other_file_dot_anchor"></a> 9. Property `other_file_dot_anchor`

**Description**:  The delivery is a gift, no prices displayed

      root
 >   other_file_dot_anchor

Type: `object`

**Description:** The delivery is a gift, no prices displayed
        Same definition as [other_file_anchor](#other_file_anchor)

## <a name="other_file_dot_dot_anchor"></a> 10. Property `other_file_dot_dot_anchor`

**Description**:  The delivery is a gift, no prices displayed

      root
 >   other_file_dot_dot_anchor

Type: `object`

**Description:** The delivery is a gift, no prices displayed
        Same definition as [other_file_anchor](#other_file_anchor)

## <a name="other_file_only"></a> 11. Property `other_file_only`

**Description**:  Test schema with a not

      root
 >   other_file_only

Type: `object`

**Description:** Test schema with a not

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [not_a_string](#other_file_only_not_a_string)|No|object|Yes|No| No||

### <a name="other_file_only_not_a_string"></a> 11.1. Property `not_a_string`

      root
 >   other_file_only
 >   not_a_string

#### Must **not** be
  root
 >   other_file_only
 >   not_a_string
 >   not

Type: `string`

## <a name="multi_hierarchy_reference"></a> 12. Property `multi_hierarchy_reference`

      root
 >   multi_hierarchy_reference

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|propertyA|No|string|No|No| No|Contents of propertyA in final.json|
`No Additional Properties`

### <a name="multi_hierarchy_reference_propertyA"></a> 12.1. Property `propertyA`

**Description**:  Contents of propertyA in final.json

      root
 >   multi_hierarchy_reference
 >   propertyA

Type: `string`

**Description:** Contents of propertyA in final.json

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-01-31 at 23:30:20 +0100