# Bug

- [1. Property`Bug > Code`](#Code)
- [2. Property`Bug > RecursiveArray`](#RecursiveArray)
  - [2.1. Bug > RecursiveArray > Bug](#RecursiveArray_items)
- [3. Property`Bug > DecoratedRecursiveArray`](#DecoratedRecursiveArray)
  - [3.1. Bug > DecoratedRecursiveArray > DecoratedRecursiveArray items](#DecoratedRecursiveArray_items)
    - [3.1.1. Property`Bug > DecoratedRecursiveArray > DecoratedRecursiveArray items > SomeName`](#DecoratedRecursiveArray_items_SomeName)
    - [3.1.2. Property`Bug > DecoratedRecursiveArray > DecoratedRecursiveArray items > TheThing`](#DecoratedRecursiveArray_items_TheThing)

**Title:** Bug

|              |          |
| ------------ | -------- |
| **Type**     | `object` |
| **Required** | No       |

**Description:** Display the issue.

| Property                                               | Pattern | Type            | Deprecated | Definition | Title/Description                |
| ------------------------------------------------------ | ------- | --------------- | ---------- | ---------- | -------------------------------- |
| - [Code](#Code )                                       | No      | string          | No         | -          | Code property                    |
| - [RecursiveArray](#RecursiveArray )                   | No      | array           | No         | -          | RecursiveArray property          |
| - [DecoratedRecursiveArray](#DecoratedRecursiveArray ) | No      | array of object | No         | -          | DecoratedRecursiveArray property |

## <a name="Code"></a>1. Property`Bug > Code`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Code property

## <a name="RecursiveArray"></a>2. Property`Bug > RecursiveArray`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** RecursiveArray property

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be | Description        |
| ------------------------------- | ------------------ |
| [Bug](#RecursiveArray_items)    | Display the issue. |

### <a name="RecursiveArray_items"></a>2.1. Bug > RecursiveArray > Bug

**Title:** Bug

|                        |              |
| ---------------------- | ------------ |
| **Type**               | `object`     |
| **Required**           | No           |
| **Same definition as** | [Bug](#root) |

**Description:** Display the issue.

## <a name="DecoratedRecursiveArray"></a>3. Property`Bug > DecoratedRecursiveArray`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of object` |
| **Required** | No                |

**Description:** DecoratedRecursiveArray property

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                 | Description |
| --------------------------------------------------------------- | ----------- |
| [DecoratedRecursiveArray items](#DecoratedRecursiveArray_items) | -           |

### <a name="DecoratedRecursiveArray_items"></a>3.1. Bug > DecoratedRecursiveArray > DecoratedRecursiveArray items

|              |          |
| ------------ | -------- |
| **Type**     | `object` |
| **Required** | No       |

| Property                                               | Pattern | Type   | Deprecated | Definition            | Title/Description |
| ------------------------------------------------------ | ------- | ------ | ---------- | --------------------- | ----------------- |
| - [SomeName](#DecoratedRecursiveArray_items_SomeName ) | No      | string | No         | -                     | -                 |
| - [TheThing](#DecoratedRecursiveArray_items_TheThing ) | No      | object | No         | Same as [Bug](#root ) | Bug               |

#### <a name="DecoratedRecursiveArray_items_SomeName"></a>3.1.1. Property`Bug > DecoratedRecursiveArray > DecoratedRecursiveArray items > SomeName`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="DecoratedRecursiveArray_items_TheThing"></a>3.1.2. Property`Bug > DecoratedRecursiveArray > DecoratedRecursiveArray items > TheThing`

**Title:** Bug

|                        |              |
| ---------------------- | ------------ |
| **Type**               | `object`     |
| **Required**           | No           |
| **Same definition as** | [Bug](#root) |

**Description:** Display the issue.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
