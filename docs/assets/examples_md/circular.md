# Circular reference Schema

- [1. Property `Circular reference Schema > person`](#person)
  - [1.1. Property `Circular reference Schema > person > a1`](#person_a1)

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [person](#person)|No|Combination|No|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="person"></a>1. Property `Circular reference Schema > person`

Type: `object`

Defined in: #/definitions/a

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [a1](#person_a1)|No|Combination|No|No| No|Description from b|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

### <a name="person_a1"></a>1.1. Property `Circular reference Schema > person > a1`

Type: `string`
Default: `"Default from c"`

**Description:** <p>Description from b</p>

Defined in: #/definitions/b

Defined in: #/definitions/c

Defined in: #/definitions/a/properties/a1

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-09 at 19:16:34 +0100