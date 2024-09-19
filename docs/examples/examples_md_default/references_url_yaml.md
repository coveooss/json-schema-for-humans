# Schema Docs

- [1. Property `root > address`](#address)
  - [1.1. Property `root > address > street_address`](#address_street_address)
  - [1.2. Property `root > address > city`](#address_city)
  - [1.3. Property `root > address > state`](#address_state)

|                           |                                                                         |
| ------------------------- | ----------------------------------------------------------------------- |
| **Type**                  | `object`                                                                |
| **Required**              | No                                                                      |
| **Additional properties** | [[Any type: allowed]]("Additional Properties of any type are allowed.") |

**Description:** Testing $ref with URL with YAML destination

| Property               | Pattern | Type   | Deprecated | Definition                                                                                                                   | Title/Description |
| ---------------------- | ------- | ------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| - [address](#address ) | No      | object | No         | In https://raw.githubusercontent.com/coveooss/json-schema-for-humans/main/docs/examples/cases/yaml.yaml#/definitions/address | -                 |

## <a name="address"></a>1. Property `root > address`

|                           |                                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                  |
| **Required**              | No                                                                                                                        |
| **Additional properties** | [[Any type: allowed]]("Additional Properties of any type are allowed.")                                                   |
| **Defined in**            | https://raw.githubusercontent.com/coveooss/json-schema-for-humans/main/docs/examples/cases/yaml.yaml#/definitions/address |

| Property                                     | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [street_address](#address_street_address ) | No      | string | No         | -          | -                 |
| + [city](#address_city )                     | No      | string | No         | -          | -                 |
| + [state](#address_state )                   | No      | string | No         | -          | -                 |

### <a name="address_street_address"></a>1.1. Property `root > address > street_address`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

### <a name="address_city"></a>1.2. Property `root > address > city`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

### <a name="address_state"></a>1.3. Property `root > address > state`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
