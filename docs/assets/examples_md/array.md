# Schema Docs
Type: `object`

**Description:** A schema with an array

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|fruits|No|array of string|No|No| No||
|vegetables|No|array|No|No| No||

## <a name="fruits"></a> 1. Property `root > fruits`

    Type: `array of string`

#### Each item of this array must be
Type: `string`

## <a name="vegetables"></a> 2. Property `root > vegetables`

    Type: `array`

#### Each item of this array must be
Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|veggieName|No|string|Yes|No| No|The name of the vegetable.|
|veggieLike|No|boolean|Yes|No| No|Do I like this vegetable?|

### <a name="vegetables_items_veggieName"></a> 2.1. Property `root > vegetables > items > veggieName`

**Description**:  The name of the vegetable.

    Type: `string`

**Description:** The name of the vegetable.

### <a name="vegetables_items_veggieLike"></a> 2.2. Property `root > vegetables > items > veggieLike`

**Description**:  Do I like this vegetable?

    Type: `boolean`

**Description:** Do I like this vegetable?

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-01 at 09:18:49 +0100