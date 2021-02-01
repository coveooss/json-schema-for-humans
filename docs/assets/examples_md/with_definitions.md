# Schema Docs
Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [billing_address](#billing_address)|No|object|No|No| No||
| [shipping_address](#shipping_address)|No|object|No|No| No||

## <a name="billing_address"></a> 1. Property `root > billing_address`

    Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|street_address|No|string|Yes|No| No||
|city|No|string|Yes|No| No||
|state|No|string|Yes|No| No||

### <a name="billing_address_street_address"></a> 1.1. Property `root > billing_address > street_address`

    Type: `string`

### <a name="billing_address_city"></a> 1.2. Property `root > billing_address > city`

    Type: `string`

### <a name="billing_address_state"></a> 1.3. Property `root > billing_address > state`

    Type: `string`

## <a name="shipping_address"></a> 2. Property `root > shipping_address`

    Type: `object`

        Same definition as [billing_address](#billing_address)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-01 at 09:18:47 +0100