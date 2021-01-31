# Schema Docs

Type: `object`

**Description:** Testing $ref with URL with YAML destination

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [address](#address)|No|object|No|No| No||

## <a name="address"></a> 1. Property `address`

      root
 >   address

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|street_address|No|string|Yes|No| No||
|city|No|string|Yes|No| No||
|state|No|string|Yes|No| No||

### <a name="address_street_address"></a> 1.1. Property `street_address`

      root
 >   address
 >   street_address

Type: `string`

### <a name="address_city"></a> 1.2. Property `city`

      root
 >   address
 >   city

Type: `string`

### <a name="address_state"></a> 1.3. Property `state`

      root
 >   address
 >   state

Type: `string`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-01-31 at 23:30:19 +0100