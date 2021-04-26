# Schema Docs

- [1. [Optional] Property `root > billing_address`](#billing_address)
  - [1.1. [Required] Property `root > billing_address > street_address`](#billing_address_street_address)
  - [1.2. [Required] Property `root > billing_address > city`](#billing_address_city)
  - [1.3. [Required] Property `root > billing_address > state`](#billing_address_state)
  - [1.4. [Optional] Property `root > billing_address > futureProperty`](#billing_address_futureProperty)
- [2. [Optional] Property `root > shipping_address`](#shipping_address)

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

| Property                                 | Pattern | Type   | Deprecated | Definition                                   | Title/Description |
| ---------------------------------------- | ------- | ------ | ---------- | -------------------------------------------- | ----------------- |
| - [billing_address](#billing_address )   | No      | object | No         | In #/definitions/address                     | -                 |
| - [shipping_address](#shipping_address ) | No      | object | No         | Same as [billing_address](#billing_address ) | -                 |
|                                          |         |        |            |                                              |                   |

## <a name="billing_address"></a>1. [Optional] Property `root > billing_address`

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/address                                                     |
|                           |                                                                           |

| Property                                             | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [street_address](#billing_address_street_address ) | No      | string | No         | -          | -                 |
| + [city](#billing_address_city )                     | No      | string | No         | -          | -                 |
| + [state](#billing_address_state )                   | No      | string | No         | -          | -                 |
| - [futureProperty](#billing_address_futureProperty ) | No      | null   | No         | -          | -                 |
|                                                      |         |        |            |            |                   |

### <a name="billing_address_street_address"></a>1.1. [Required] Property `root > billing_address > street_address`

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

### <a name="billing_address_city"></a>1.2. [Required] Property `root > billing_address > city`

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

### <a name="billing_address_state"></a>1.3. [Required] Property `root > billing_address > state`

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

### <a name="billing_address_futureProperty"></a>1.4. [Optional] Property `root > billing_address > futureProperty`

| Type                      | `null`                                                                    |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

## <a name="shipping_address"></a>2. [Optional] Property `root > shipping_address`

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [billing_address](#billing_address)                                       |
|                           |                                                                           |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date