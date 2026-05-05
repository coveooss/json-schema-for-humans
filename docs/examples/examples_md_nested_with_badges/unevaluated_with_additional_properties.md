# unevaluatedProperties with additionalProperties

- [1. [Optional] PropertyunevaluatedProperties with additionalProperties > name](#name)
- [2. [Optional] PropertyunevaluatedProperties with additionalProperties > nested](#nested)
  - [2.1. [Optional] PropertyunevaluatedProperties with additionalProperties > nested > nestedProp](#nested_nestedProp)
- [3. [Optional] PropertyunevaluatedProperties with additionalProperties > withAdditionalFalse](#withAdditionalFalse)
  - [3.1. [Optional] PropertyunevaluatedProperties with additionalProperties > withAdditionalFalse > allowedProp](#withAdditionalFalse_allowedProp)
- [4. [Optional] PropertyunevaluatedProperties with additionalProperties > withAdditionalSchema](#withAdditionalSchema)
  - [4.1. [Optional] PropertyunevaluatedProperties with additionalProperties > withAdditionalSchema > knownProp](#withAdditionalSchema_knownProp)
  - [4.2. Additional PropertiesunevaluatedProperties with additionalProperties > withAdditionalSchema > additionalProperties](#withAdditionalSchema_additionalProperties)
- [5. [Optional] PropertyunevaluatedProperties with additionalProperties > withUnevaluatedFalse](#withUnevaluatedFalse)
  - [5.1. [Optional] PropertyunevaluatedProperties with additionalProperties > withUnevaluatedFalse > baseProp](#withUnevaluatedFalse_baseProp)
  - [5.2. [Optional] PropertyunevaluatedProperties with additionalProperties > withUnevaluatedFalse > extendedProp](#withUnevaluatedFalse_extendedProp)
- [6. [Optional] PropertyunevaluatedProperties with additionalProperties > anInt](#anInt)
- [7. Additional PropertiesunevaluatedProperties with additionalProperties > additionalProperties](#additionalProperties)
  - [7.1. [Required] PropertyunevaluatedProperties with additionalProperties > additionalProperties > type](#additionalProperties_type)

**Title:** unevaluatedProperties with additionalProperties

|                            |                                                                                              |
| -------------------------- | -------------------------------------------------------------------------------------------- |
| **Type**                   | `object`                                                                                     |
| **Additional properties**  | [![Should-conform](https://img.shields.io/badge/Should-conform-blue)](#additionalProperties) |
| **Unevaluated properties** | ![Not allowed](https://img.shields.io/badge/Not%20allowed-red)                               |

**Description:** Demonstrates the interaction between unevaluatedProperties and additionalProperties

<details>
<summary>
<strong> <a name="name"></a>1. [Optional] PropertyunevaluatedProperties with additionalProperties > name</strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Name field

</blockquote>
</details>

<details>
<summary>
<strong> <a name="nested"></a>2. [Optional] PropertyunevaluatedProperties with additionalProperties > nested</strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `object` |

**Description:** Nested object without explicit additional/unevaluated properties constraint

<details>
<summary>
<strong> <a name="nested_nestedProp"></a>2.1. [Optional] PropertyunevaluatedProperties with additionalProperties > nested > nestedProp</strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `number` |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="withAdditionalFalse"></a>3. [Optional] PropertyunevaluatedProperties with additionalProperties > withAdditionalFalse</strong>  

</summary>
<blockquote>

|                           |                                                                |
| ------------------------- | -------------------------------------------------------------- |
| **Type**                  | `object`                                                       |
| **Additional properties** | ![Not allowed](https://img.shields.io/badge/Not%20allowed-red) |

**Description:** Nested object with additionalProperties: false

<details>
<summary>
<strong> <a name="withAdditionalFalse_allowedProp"></a>3.1. [Optional] PropertyunevaluatedProperties with additionalProperties > withAdditionalFalse > allowedProp</strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `string` |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="withAdditionalSchema"></a>4. [Optional] PropertyunevaluatedProperties with additionalProperties > withAdditionalSchema</strong>  

</summary>
<blockquote>

|                           |                                                                                                                   |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                          |
| **Additional properties** | [![Should-conform](https://img.shields.io/badge/Should-conform-blue)](#withAdditionalSchema_additionalProperties) |

**Description:** Nested object with additionalProperties schema

<details>
<summary>
<strong> <a name="withAdditionalSchema_knownProp"></a>4.1. [Optional] PropertyunevaluatedProperties with additionalProperties > withAdditionalSchema > knownProp</strong>  

</summary>
<blockquote>

|          |           |
| -------- | --------- |
| **Type** | `integer` |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="withAdditionalSchema_additionalProperties"></a>4.2. Additional PropertiesunevaluatedProperties with additionalProperties > withAdditionalSchema > additionalProperties</strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `string` |

| Restrictions                      |                                                               |
| --------------------------------- | ------------------------------------------------------------- |
| **Must match regular expression** | ```^[A-Z]``` [Test](https://regex101.com/?regex=%5E%5BA-Z%5D) |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="withUnevaluatedFalse"></a>5. [Optional] PropertyunevaluatedProperties with additionalProperties > withUnevaluatedFalse</strong>  

</summary>
<blockquote>

|                            |                                                                |
| -------------------------- | -------------------------------------------------------------- |
| **Type**                   | `object`                                                       |
| **Unevaluated properties** | ![Not allowed](https://img.shields.io/badge/Not%20allowed-red) |

**Description:** Nested object with unevaluatedProperties: false and allOf

<details>
<summary>
<strong> <a name="withUnevaluatedFalse_baseProp"></a>5.1. [Optional] PropertyunevaluatedProperties with additionalProperties > withUnevaluatedFalse > baseProp</strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `string` |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="withUnevaluatedFalse_extendedProp"></a>5.2. [Optional] PropertyunevaluatedProperties with additionalProperties > withUnevaluatedFalse > extendedProp</strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** Property from allOf - should be evaluated

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="anInt"></a>6. [Optional] PropertyunevaluatedProperties with additionalProperties > anInt</strong>  

</summary>
<blockquote>

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** This is an integer, it should not show additional properties. (issue #132)

</blockquote>
</details>

<details>
<summary>
<strong> <a name="additionalProperties"></a>7. Additional PropertiesunevaluatedProperties with additionalProperties > additionalProperties</strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `object` |

**Description:** Additional properties must be objects with a type field

<details>
<summary>
<strong> <a name="additionalProperties_type"></a>7.1. [Required] PropertyunevaluatedProperties with additionalProperties > additionalProperties > type</strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Type of the additional property

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)