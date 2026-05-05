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

|                            |                                                                              |
| -------------------------- | ---------------------------------------------------------------------------- |
| **Type**                   | `object`                                                                     |
| **Required**               | No                                                                           |
| **Additional properties**  | [Each additional property must conform to the schema](#additionalProperties) |
| **Unevaluated properties** | Not allowed                                                                  |

**Description:** Demonstrates the interaction between unevaluatedProperties and additionalProperties

<details>
<summary>
<strong> <a name="name"></a>1. [Optional] PropertyunevaluatedProperties with additionalProperties > name</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Name field

</blockquote>
</details>

<details>
<summary>
<strong> <a name="nested"></a>2. [Optional] PropertyunevaluatedProperties with additionalProperties > nested</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `object` |
| **Required** | No       |

**Description:** Nested object without explicit additional/unevaluated properties constraint

<details>
<summary>
<strong> <a name="nested_nestedProp"></a>2.1. [Optional] PropertyunevaluatedProperties with additionalProperties > nested > nestedProp</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="withAdditionalFalse"></a>3. [Optional] PropertyunevaluatedProperties with additionalProperties > withAdditionalFalse</strong>  

</summary>
<blockquote>

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Nested object with additionalProperties: false

<details>
<summary>
<strong> <a name="withAdditionalFalse_allowedProp"></a>3.1. [Optional] PropertyunevaluatedProperties with additionalProperties > withAdditionalFalse > allowedProp</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="withAdditionalSchema"></a>4. [Optional] PropertyunevaluatedProperties with additionalProperties > withAdditionalSchema</strong>  

</summary>
<blockquote>

|                           |                                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                          |
| **Required**              | No                                                                                                |
| **Additional properties** | [Each additional property must conform to the schema](#withAdditionalSchema_additionalProperties) |

**Description:** Nested object with additionalProperties schema

<details>
<summary>
<strong> <a name="withAdditionalSchema_knownProp"></a>4.1. [Optional] PropertyunevaluatedProperties with additionalProperties > withAdditionalSchema > knownProp</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="withAdditionalSchema_additionalProperties"></a>4.2. Additional PropertiesunevaluatedProperties with additionalProperties > withAdditionalSchema > additionalProperties</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

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

|                            |             |
| -------------------------- | ----------- |
| **Type**                   | `object`    |
| **Required**               | No          |
| **Unevaluated properties** | Not allowed |

**Description:** Nested object with unevaluatedProperties: false and allOf

<details>
<summary>
<strong> <a name="withUnevaluatedFalse_baseProp"></a>5.1. [Optional] PropertyunevaluatedProperties with additionalProperties > withUnevaluatedFalse > baseProp</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="withUnevaluatedFalse_extendedProp"></a>5.2. [Optional] PropertyunevaluatedProperties with additionalProperties > withUnevaluatedFalse > extendedProp</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

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

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** This is an integer, it should not show additional properties. (issue #132)

</blockquote>
</details>

<details>
<summary>
<strong> <a name="additionalProperties"></a>7. Additional PropertiesunevaluatedProperties with additionalProperties > additionalProperties</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `object` |
| **Required** | No       |

**Description:** Additional properties must be objects with a type field

<details>
<summary>
<strong> <a name="additionalProperties_type"></a>7.1. [Required] PropertyunevaluatedProperties with additionalProperties > additionalProperties > type</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Type of the additional property

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)