# Configuration With Extra Fields

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Configuration With Extra Fields > timeout`](#timeout)
- [2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Configuration With Extra Fields > buffer_size`](#buffer_size)
- [3. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Configuration With Extra Fields > name`](#name)

**Title:** Configuration With Extra Fields

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

| Property                       | Pattern | Type    | Deprecated | Definition | Title/Description                                                  |
| ------------------------------ | ------- | ------- | ---------- | ---------- | ------------------------------------------------------------------ |
| - [timeout](#timeout )         | No      | integer | No         | -          | Connection timeout.                                                |
| - [buffer_size](#buffer_size ) | No      | integer | No         | -          | Read buffer size.                                                  |
| - [name](#name )               | No      | string  | No         | -          | Identifier (no extra fields, for coverage of the absent-key path). |

## <a name="timeout"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Configuration With Extra Fields > timeout`

|             |           |
| ----------- | --------- |
| **Type**    | `integer` |
| **Default** | `30`      |

**Description:** Connection timeout.

## <a name="buffer_size"></a>2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Configuration With Extra Fields > buffer_size`

|             |           |
| ----------- | --------- |
| **Type**    | `integer` |
| **Default** | `4096`    |

**Description:** Read buffer size.

## <a name="name"></a>3. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Configuration With Extra Fields > name`

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Identifier (no extra fields, for coverage of the absent-key path).

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
