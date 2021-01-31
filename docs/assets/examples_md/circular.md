# Circular reference Schema

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [person](#person)|No|object|No|No| No||

## <a name="person"></a> 1. Property `person`

      Circular reference Schema
 >   person

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|a1|No|string|No|No| No|Description from b|

### <a name="person_a1"></a> 1.1. Property `a1`

**Description**:  Description from b

      Circular reference Schema
 >   person
 >   a1

Type: `string`
             Default: `"Default from c"`

**Description:** Description from b

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-01-31 at 23:30:20 +0100