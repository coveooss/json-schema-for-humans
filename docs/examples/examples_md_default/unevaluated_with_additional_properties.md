# unevaluatedProperties with additionalProperties

- [1. Property`unevaluatedProperties with additionalProperties > name`](#name)
- [2. Property`unevaluatedProperties with additionalProperties > nested`](#nested)
  - [2.1. Property`unevaluatedProperties with additionalProperties > nested > nestedProp`](#nested_nestedProp)
- [3. Property`unevaluatedProperties with additionalProperties > withAdditionalFalse`](#withAdditionalFalse)
  - [3.1. Property`unevaluatedProperties with additionalProperties > withAdditionalFalse > allowedProp`](#withAdditionalFalse_allowedProp)
- [4. Property`unevaluatedProperties with additionalProperties > withAdditionalSchema`](#withAdditionalSchema)
  - [4.1. Property`unevaluatedProperties with additionalProperties > withAdditionalSchema > knownProp`](#withAdditionalSchema_knownProp)
  - [4.2. Additional Properties`unevaluatedProperties with additionalProperties > withAdditionalSchema > additionalProperties`](#withAdditionalSchema_additionalProperties)
- [5. Property`unevaluatedProperties with additionalProperties > withUnevaluatedFalse`](#withUnevaluatedFalse)
  - [5.1. Property`unevaluatedProperties with additionalProperties > withUnevaluatedFalse > baseProp`](#withUnevaluatedFalse_baseProp)
  - [5.2. Property`unevaluatedProperties with additionalProperties > withUnevaluatedFalse > extendedProp`](#withUnevaluatedFalse_extendedProp)
- [6. Property`unevaluatedProperties with additionalProperties > anInt`](#anInt)
- [7. Additional Properties`unevaluatedProperties with additionalProperties > additionalProperties`](#additionalProperties)
  - [7.1. Property`unevaluatedProperties with additionalProperties > additionalProperties > type`](#additionalProperties_type)

**Title:** unevaluatedProperties with additionalProperties

|                            |                                                                              |
| -------------------------- | ---------------------------------------------------------------------------- |
| **Type**                   | `object`                                                                     |
| **Required**               | No                                                                           |
| **Additional properties**  | [Each additional property must conform to the schema](#additionalProperties) |
| **Unevaluated properties** | Not allowed                                                                  |

**Description:** Demonstrates the interaction between unevaluatedProperties and additionalProperties

| Property                                          | Pattern | Type    | Deprecated | Definition | Title/Description                                                           |
| ------------------------------------------------- | ------- | ------- | ---------- | ---------- | --------------------------------------------------------------------------- |
| - [name](#name )                                  | No      | string  | No         | -          | Name field                                                                  |
| - [nested](#nested )                              | No      | object  | No         | -          | Nested object without explicit additional/unevaluated properties constraint |
| - [withAdditionalFalse](#withAdditionalFalse )    | No      | object  | No         | -          | Nested object with additionalProperties: false                              |
| - [withAdditionalSchema](#withAdditionalSchema )  | No      | object  | No         | -          | Nested object with additionalProperties schema                              |
| - [withUnevaluatedFalse](#withUnevaluatedFalse )  | No      | object  | No         | -          | Nested object with unevaluatedProperties: false and allOf                   |
| - [anInt](#anInt )                                | No      | integer | No         | -          | This is an integer, it should not show additional properties. (issue #132)  |
| - [Additional Properties](#additionalProperties ) | No      | object  | No         | -          | Additional properties must be objects with a type field                     |

## <a name="name"></a>1. Property`unevaluatedProperties with additionalProperties > name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Name field

## <a name="nested"></a>2. Property`unevaluatedProperties with additionalProperties > nested`

|              |          |
| ------------ | -------- |
| **Type**     | `object` |
| **Required** | No       |

**Description:** Nested object without explicit additional/unevaluated properties constraint

| Property                            | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [nestedProp](#nested_nestedProp ) | No      | number | No         | -          | -                 |

### <a name="nested_nestedProp"></a>2.1. Property`unevaluatedProperties with additionalProperties > nested > nestedProp`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

## <a name="withAdditionalFalse"></a>3. Property`unevaluatedProperties with additionalProperties > withAdditionalFalse`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Nested object with additionalProperties: false

| Property                                           | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [allowedProp](#withAdditionalFalse_allowedProp ) | No      | string | No         | -          | -                 |

### <a name="withAdditionalFalse_allowedProp"></a>3.1. Property`unevaluatedProperties with additionalProperties > withAdditionalFalse > allowedProp`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="withAdditionalSchema"></a>4. Property`unevaluatedProperties with additionalProperties > withAdditionalSchema`

|                           |                                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                          |
| **Required**              | No                                                                                                |
| **Additional properties** | [Each additional property must conform to the schema](#withAdditionalSchema_additionalProperties) |

**Description:** Nested object with additionalProperties schema

| Property                                                               | Pattern | Type    | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [knownProp](#withAdditionalSchema_knownProp )                        | No      | integer | No         | -          | -                 |
| - [Additional Properties](#withAdditionalSchema_additionalProperties ) | No      | string  | No         | -          | -                 |

### <a name="withAdditionalSchema_knownProp"></a>4.1. Property`unevaluatedProperties with additionalProperties > withAdditionalSchema > knownProp`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

### <a name="withAdditionalSchema_additionalProperties"></a>4.2. Additional Properties`unevaluatedProperties with additionalProperties > withAdditionalSchema > additionalProperties`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions                      |                                                               |
| --------------------------------- | ------------------------------------------------------------- |
| **Must match regular expression** | ```^[A-Z]``` [Test](https://regex101.com/?regex=%5E%5BA-Z%5D) |

## <a name="withUnevaluatedFalse"></a>5. Property`unevaluatedProperties with additionalProperties > withUnevaluatedFalse`

|                            |             |
| -------------------------- | ----------- |
| **Type**                   | `object`    |
| **Required**               | No          |
| **Unevaluated properties** | Not allowed |

**Description:** Nested object with unevaluatedProperties: false and allOf

| Property                                              | Pattern | Type   | Deprecated | Definition | Title/Description                         |
| ----------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------------------------------- |
| - [baseProp](#withUnevaluatedFalse_baseProp )         | No      | string | No         | -          | -                                         |
| - [extendedProp](#withUnevaluatedFalse_extendedProp ) | No      | number | No         | -          | Property from allOf - should be evaluated |

### <a name="withUnevaluatedFalse_baseProp"></a>5.1. Property`unevaluatedProperties with additionalProperties > withUnevaluatedFalse > baseProp`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

### <a name="withUnevaluatedFalse_extendedProp"></a>5.2. Property`unevaluatedProperties with additionalProperties > withUnevaluatedFalse > extendedProp`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

**Description:** Property from allOf - should be evaluated

## <a name="anInt"></a>6. Property`unevaluatedProperties with additionalProperties > anInt`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** This is an integer, it should not show additional properties. (issue #132)

## <a name="additionalProperties"></a>7. Additional Properties`unevaluatedProperties with additionalProperties > additionalProperties`

|              |          |
| ------------ | -------- |
| **Type**     | `object` |
| **Required** | No       |

**Description:** Additional properties must be objects with a type field

| Property                              | Pattern | Type   | Deprecated | Definition | Title/Description               |
| ------------------------------------- | ------- | ------ | ---------- | ---------- | ------------------------------- |
| + [type](#additionalProperties_type ) | No      | string | No         | -          | Type of the additional property |

### <a name="additionalProperties_type"></a>7.1. Property`unevaluatedProperties with additionalProperties > additionalProperties > type`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Type of the additional property

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
