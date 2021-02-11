# Schema Docs

- [1. ~~ Property `root > deprecated1`~~](#deprecated1)
- [2. ~~ Property `root > deprecated2`~~](#deprecated2)
- [3. Property `root > not_deprecated`](#not_deprecated)

Type: `object`

**Description:** Test schema with deprecated in description

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
| [deprecated1](#deprecated1)|No|object|![made-with-Markdown](https://img.shields.io/badge/Deprecated-red)| No|[Deprecated]|
| [deprecated2](#deprecated2)|No|object|![made-with-Markdown](https://img.shields.io/badge/Deprecated-red)| No|[Deprecated - Use \`not_deprecated\` instead]|
| [not_deprecated](#not_deprecated)|No|string|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="deprecated1"></a>1. ~~ Property `root > deprecated1`~~

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
![made-with-Markdown](https://img.shields.io/badge/Deprecated-red) Type: `object`

**Description:** [Deprecated]

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="deprecated2"></a>2. ~~ Property `root > deprecated2`~~

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
![made-with-Markdown](https://img.shields.io/badge/Deprecated-red) Type: `object`

**Description:** [Deprecated - Use `not_deprecated` instead]

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="not_deprecated"></a>3. Property `root > not_deprecated`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `string`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-11 at 01:21:07 +0100