# Test

- [1. [Optional] PropertyTest > aProperty](#aProperty)
- [2. [Optional] PropertyTest > aDictPropertyARequired](#aDictPropertyARequired)
  - [2.1. [Required] PropertyTest > aDictPropertyARequired > a](#aDictPropertyARequired_a)
  - [2.2. [Required] PropertyTest > aDictPropertyARequired > b](#aDictPropertyARequired_b)

**Title:** Test

|          |          |
| -------- | -------- |
| **Type** | `object` |

<details>
<summary>
<strong> <a name="aProperty"></a>1. [Optional] PropertyTest > aProperty</strong>  

</summary>
<blockquote>

**Title:** Title from definition

|                |                           |
| -------------- | ------------------------- |
| **Type**       | `enum (of string)`        |
| **Default**    | `"Default from property"` |
| **Defined in** | #/definitions/aProperty   |

**Description:** This is the description from the definition

Must be one of:
* "value1"
* "value2"

</blockquote>
</details>

<details>
<summary>
<strong> <a name="aDictPropertyARequired"></a>2. [Optional] PropertyTest > aDictPropertyARequired</strong>  

</summary>
<blockquote>

|                |                             |
| -------------- | --------------------------- |
| **Type**       | `object`                    |
| **Default**    | `{"a": "a", "b": "b"}`      |
| **Defined in** | #/definitions/aDictProperty |

<details>
<summary>
<strong> <a name="aDictPropertyARequired_a"></a>2.1. [Required] PropertyTest > aDictPropertyARequired > a</strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `string` |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="aDictPropertyARequired_b"></a>2.2. [Required] PropertyTest > aDictPropertyARequired > b</strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `string` |

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)