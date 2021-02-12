# Schema Docs

- [1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `root > described`](#described)
  - [1.1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `root > described > name`](#described_name)
  - [1.2. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `root > described > alignment`](#described_alignment)

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
|  |  |

**Description:** Testing $ref of a remote $ref

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |
|-  [described](#described)|No|object|No|-|
|  |  |  |  |  |

## <a name="described"></a>1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `root > described`

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
| **Defined in** | https://raw.githubusercontent.com/coveooss/json-schema-for-humans/master/tests/cases/description_from_ref.json |
|  |  |

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |
|-  [name](#described_name)|No|string|No|a filled string|
|-  [alignment](#described_alignment)|No|string|No|a filled string|
|  |  |  |  |  |

### <a name="described_name"></a>1.1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `root > described > name`

| Type | `string` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
| **Defined in** | #/definitions/filled_string |
|  |  |

**Description:** a filled string

| Restrictions |   |
| ------------ | - |
| **Min length** | 1 |

### <a name="described_alignment"></a>1.2. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `root > described > alignment`

| Type | `string` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
| **Same definition as** | [name](#described_name) |
|  |  |

**Description:** a filled string

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-12 at 23:56:24 +0100