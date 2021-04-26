# Schema Docs

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** A little food fun

<details>
<summary><strong> <a name="address"></a>[Optional] Property address</strong>  

</summary>
<blockquote>

| Type                      | `array`                                                                   |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

| Each item of this array must be      | Description          |
| ------------------------------------ | -------------------- |
| [a number](#address_items_i0)        | -                    |
| [item 1](#address_items_i1)          | followed by a string |
| [again a string](#address_items_i2)  | -                    |
| [finally an enum](#address_items_i3) | -                    |
|                                      |                      |

### <a name="address_items_i0"></a>a number

**Title:** a number

| Type                      | `number`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

### <a name="address_items_i1"></a>item 1

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** followed by a string

### <a name="address_items_i2"></a>again a string

**Title:** again a string

| Type                      | `enum (of string)`                                                        |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

Must be one of:
* "Street"
* "Avenue"
* "Boulevard"

### <a name="address_items_i3"></a>finally an enum

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
<summary><strong> <a name="addressLines"></a>[Optional] Property addressLines</strong>  

</summary>
<blockquote>

| Type                      | `array`                                                                   |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** list of address lines

| Each item of this array must be  | Description |
| -------------------------------- | ----------- |
| [item 0](#addressLines_items_i0) | -           |
|                                  |             |

### <a name="addressLines_items_i0"></a>item 0

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

<details>
<summary><strong> <a name="arrayEmpty"></a>[Optional] Property arrayEmpty</strong>  

</summary>
<blockquote>

| Type                      | `array`                                                                   |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [items](#arrayEmpty_items)      | -           |
|                                 |             |

### <a name="arrayEmpty_items"></a>items

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date