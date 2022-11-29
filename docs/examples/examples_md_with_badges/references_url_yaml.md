# Schema Docs

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > address`](#address-72657373)
  - [1.1. ![Required](https://img.shields.io/badge/Required-blue) Property `root > address > street_address`](#address_street_address-72657373)
  - [1.2. ![Required](https://img.shields.io/badge/Required-blue) Property `root > address > city`](#address_city-63697479)
  - [1.3. ![Required](https://img.shields.io/badge/Required-blue) Property `root > address > state`](#address_state-74617465)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

**Description:** Testing $ref with URL with YAML destination

| Property                        | Pattern | Type   | Deprecated | Definition                                                                                                                   | Title/Description |
| ------------------------------- | ------- | ------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| - [address](#address-72657373 ) | No      | object | No         | In https://raw.githubusercontent.com/coveooss/json-schema-for-humans/main/docs/examples/cases/yaml.yaml#/definitions/address | -                 |

## <a name="address-72657373"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > address`

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | https://raw.githubusercontent.com/coveooss/json-schema-for-humans/main/docs/examples/cases/yaml.yaml#/definitions/address         |

| Property                                              | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [street_address](#address_street_address-72657373 ) | No      | string | No         | -          | -                 |
| + [city](#address_city-63697479 )                     | No      | string | No         | -          | -                 |
| + [state](#address_state-74617465 )                   | No      | string | No         | -          | -                 |

### <a name="address_street_address-72657373"></a>1.1. ![Required](https://img.shields.io/badge/Required-blue) Property `root > address > street_address`

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="address_city-63697479"></a>1.2. ![Required](https://img.shields.io/badge/Required-blue) Property `root > address > city`

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="address_state-74617465"></a>1.3. ![Required](https://img.shields.io/badge/Required-blue) Property `root > address > state`

|          |          |
| -------- | -------- |
| **Type** | `string` |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
