# Test

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|aProperty|No|enum (of string)|No|No| No|This is the description from the definition|
| [aDictPropertyARequired](#aDictPropertyARequired)|No|object|No|No| No||

## <a name="aProperty"></a> 1. Property `aProperty`

**Description**:  This is the description from the definition

      Test
 >   aProperty

Type: `enum (of string)`
             Default: `"Default from property"`

**Description:** This is the description from the definition

                Must be one of:
                    * "value1"
                    * "value2"

## <a name="aDictPropertyARequired"></a> 2. Property `aDictPropertyARequired`

      Test
 >   aDictPropertyARequired

Type: `object`
             Default: `{"a": "a", "b": "b"}`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|a|No|string|Yes|No| No||
|b|No|string|Yes|No| No||

### <a name="aDictPropertyARequired_a"></a> 2.1. Property `a`

      Test
 >   aDictPropertyARequired
 >   a

Type: `string`

### <a name="aDictPropertyARequired_b"></a> 2.2. Property `b`

      Test
 >   aDictPropertyARequired
 >   b

Type: `string`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-01-31 at 23:30:20 +0100