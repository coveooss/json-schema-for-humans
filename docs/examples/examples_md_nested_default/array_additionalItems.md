# Schema Docs

- [1. [Optional] Property root > address](#address)
  - [1.1. root > address > items > a number](#address_items_i0)
  - [1.2. root > address > items > item 1](#address_items_i1)
  - [1.3. root > address > items > again a string](#address_items_i2)
  - [1.4. root > address > items > finally an enum](#address_items_i3)
- [2. [Optional] Property root > addressLines](#addressLines)
  - [2.1. root > addressLines > items > item 0](#addressLines_items_i0)
- [3. [Optional] Property root > arrayEmpty](#arrayEmpty)
  - [3.1. root > arrayEmpty > items](#arrayEmpty_items)

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** A little food fun

<details>
<summary><strong> <a name="address"></a>1. [Optional] Property root > address</strong>  

</summary>
<blockquote>

| Type                      | `array`                                                                   |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | True               |
| **Tuple validation** | See below          |
|                      |                    |

| Each item of this array must be      | Description          |
| ------------------------------------ | -------------------- |
| [a number](#address_items_i0)        | -                    |
| [item 1](#address_items_i1)          | followed by a string |
| [again a string](#address_items_i2)  | -                    |
| [finally an enum](#address_items_i3) | -                    |
|                                      |                      |

### <a name="address_items_i0"></a>1.1. root > address > items > a number

**Title:** a number

| Type                      | `number`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

### <a name="address_items_i1"></a>1.2. root > address > items > item 1

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** followed by a string

### <a name="address_items_i2"></a>1.3. root > address > items > again a string

**Title:** again a string

| Type                      | `enum (of string)`                                                        |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

Must be one of:
* "Street"
* "Avenue"
* "Boulevard"

### <a name="address_items_i3"></a>1.4. root > address > items > finally an enum

**Title:** finally an enum

| Type                      | `enum (of string)`                                                        |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

Must be one of:
* "NW"
* "NE"
* "SW"
* "SE"

**Example:** 

```json
[
    1600,
    "Pennsylvania",
    "Avenue",
    "NW",
    "Washington"
]
```

</blockquote>
</details>

<details>
<summary><strong> <a name="addressLines"></a>2. [Optional] Property root > addressLines</strong>  

</summary>
<blockquote>

| Type                      | `array`                                                                   |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** list of address lines

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |
|                      |                    |

| Each item of this array must be  | Description |
| -------------------------------- | ----------- |
| [item 0](#addressLines_items_i0) | -           |
|                                  |             |

### <a name="addressLines_items_i0"></a>2.1. root > addressLines > items > item 0

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

<details>
<summary><strong> <a name="arrayEmpty"></a>3. [Optional] Property root > arrayEmpty</strong>  

</summary>
<blockquote>

| Type                      | `array`                                                                   |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |
|                      |                    |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [items](#arrayEmpty_items)      | -           |
|                                 |             |

### <a name="arrayEmpty_items"></a>3.1. root > arrayEmpty > items

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date