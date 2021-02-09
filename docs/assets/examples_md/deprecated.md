# Schema Docs

- [1. Property `root > deprecated1`](#deprecated1)
- [2. Property `root > deprecated2`](#deprecated2)
- [3. Property `root > not_deprecated`](#not_deprecated)

Type: `object`

**Description:** <p>Test schema with deprecated in description</p>

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [deprecated1](#deprecated1)|No|Combination|No|No| No|[Deprecated]|
| [deprecated2](#deprecated2)|No|Combination|No|No| No|[Deprecated - Use \`not_deprecated\` instead]|
| [not_deprecated](#not_deprecated)|No|Combination|No|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="deprecated1"></a>1. Property `root > deprecated1`

Type: `object`

**Description:** <p>[Deprecated]</p>

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="deprecated2"></a>2. Property `root > deprecated2`

Type: `object`

**Description:** <p>[Deprecated - Use <code>not_deprecated</code> instead]</p>

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="not_deprecated"></a>3. Property `root > not_deprecated`

Type: `string`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-09 at 19:16:36 +0100