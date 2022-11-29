# Person

- [1. [Optional] Property Person > subType1](#subType1-79706531)
  - [1.1. [Optional] Property Person > subType1 > subProp1](#subType1_subProp1-726f7031)
- [2. [Optional] Property Person > subType2](#subType2-79706532)
  - [2.1. [Optional] Property Person > subType2 > subProp2](#subType2_subProp2-726f7032)
- [3. [Optional] Property Person > anInt](#anInt-6e496e74)
- [4. [Optional] Property Person > additionalProperties](#additionalProperties-74696573)
  - [4.1. [Optional] Property Person > additionalProperties > propA](#additionalProperties_propA-726f7041)

**Title:** Person

|                           |                                                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                                           |
| **Required**              | No                                                                                                                 |
| **Additional properties** | [[Should-conform]](#additionalProperties-74696573 "Each additional property must conform to the following schema") |

<details>
<summary><strong> <a name="subType1-79706531"></a>1. [Optional] Property Person > subType1</strong>  

</summary>
<blockquote>

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** A sub type with additionalProperties false.

<details>
<summary><strong> <a name="subType1_subProp1-726f7031"></a>1.1. [Optional] Property Person > subType1 > subProp1</strong>  

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
<summary><strong> <a name="subType2-79706532"></a>2. [Optional] Property Person > subType2</strong>  

</summary>
<blockquote>

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** A sub type with additionalProperties true.

<details>
<summary><strong> <a name="subType2_subProp2-726f7032"></a>2.1. [Optional] Property Person > subType2 > subProp2</strong>  

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
<summary><strong> <a name="anInt-6e496e74"></a>3. [Optional] Property Person > anInt</strong>  

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
<summary><strong> <a name="additionalProperties-74696573"></a>4. [Optional] Property Person > additionalProperties</strong>  

</summary>
<blockquote>

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** additionalProperties schema.

<details>
<summary><strong> <a name="additionalProperties_propA-726f7041"></a>4.1. [Optional] Property Person > additionalProperties > propA</strong>  

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

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)