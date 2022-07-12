# Person

- [1. [Optional] Property Person > subType1](#subType1)
  - [1.1. [Optional] Property Person > subType1 > subProp1](#subType1_subProp1)
- [2. [Optional] Property Person > subType2](#subType2)
  - [2.1. [Optional] Property Person > subType2 > subProp2](#subType2_subProp2)
- [3. [Optional] Property Person > anInt](#anInt)
- [4. [Optional] Property Person > additionalProperties](#additionalProperties)
  - [4.1. [Optional] Property Person > additionalProperties > propA](#additionalProperties_propA)

**Title:** Person

| Type                      | `object`                                                                                                  |
| ------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [[Should-conform]](#additionalProperties "Each additional property must conform to the following schema") |

<details>
<summary><strong> <a name="subType1"></a>1. [Optional] Property Person > subType1</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** A sub type with additionalProperties false.

<details>
<summary><strong> <a name="subType1_subProp1"></a>1.1. [Optional] Property Person > subType1 > subProp1</strong>  

</summary>
<blockquote>

| Type | `number` |
| ---- | -------- |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary><strong> <a name="subType2"></a>2. [Optional] Property Person > subType2</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** A sub type with additionalProperties true.

<details>
<summary><strong> <a name="subType2_subProp2"></a>2.1. [Optional] Property Person > subType2 > subProp2</strong>  

</summary>
<blockquote>

| Type | `number` |
| ---- | -------- |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary><strong> <a name="anInt"></a>3. [Optional] Property Person > anInt</strong>  

</summary>
<blockquote>

| Type | `integer` |
| ---- | --------- |

**Description:** This is an integer, it should not show additional properties. (issue #132)

</blockquote>
</details>

<details>
<summary><strong> <a name="additionalProperties"></a>4. [Optional] Property Person > additionalProperties</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** additionalProperties schema.

<details>
<summary><strong> <a name="additionalProperties_propA"></a>4.1. [Optional] Property Person > additionalProperties > propA</strong>  

</summary>
<blockquote>

| Type | `number` |
| ---- | -------- |

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)