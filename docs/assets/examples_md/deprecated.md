# Schema Docs

- [1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)~~ Property `root > deprecated1`~~](#deprecated1)
- [2. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)~~ Property `root > deprecated2`~~](#deprecated2)
- [3. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `root > not_deprecated`](#not_deprecated)

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|

**Description:** Test schema with deprecated in description

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |
|-  [deprecated1](#deprecated1)|No|object|![made-with-Markdown](https://img.shields.io/badge/Deprecated-red)|[Deprecated]|
|-  [deprecated2](#deprecated2)|No|object|![made-with-Markdown](https://img.shields.io/badge/Deprecated-red)|[Deprecated - Use \`not_deprecated\` instead]|
|-  [not_deprecated](#not_deprecated)|No|string|No|-|

## <a name="deprecated1"></a>1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)~~ Property `root > deprecated1`~~

| Type | `object` |
| ---- | --- |
| **Deprecated** | ![made-with-Markdown](https://img.shields.io/badge/Deprecated-red) |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|

**Description:** [Deprecated]

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |

## <a name="deprecated2"></a>2. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)~~ Property `root > deprecated2`~~

| Type | `object` |
| ---- | --- |
| **Deprecated** | ![made-with-Markdown](https://img.shields.io/badge/Deprecated-red) |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|

**Description:** [Deprecated - Use `not_deprecated` instead]

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |

## <a name="not_deprecated"></a>3. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `root > not_deprecated`

| Type | `string` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-11 at 22:25:46 +0100