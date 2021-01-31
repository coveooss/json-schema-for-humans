# Delivery Schema

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [shipping_address](#shipping_address)|No|object|No|No| No|Exact address|
| [billing_address](#billing_address)|No|object|No|No| No|Exact address|
| [delivery_info](#delivery_info)|No|object|No|No| No|Delivery info depending on the delivery type|

## <a name="shipping_address"></a> 1. Property `shipping_address`

**Description**:  Exact address

      Delivery Schema
 >   shipping_address

Type: `object`

**Description:** Exact address

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|street_address|No|string|Yes|No| No||
|city|No|string|Yes|No| No||
|state|No|string|Yes|No| No||

## <a name="billing_address"></a> 2. Property `billing_address`

**Description**:  Exact address

      Delivery Schema
 >   billing_address

Type: `object`

**Description:** Exact address
        Same definition as [shipping_address](#shipping_address)

## <a name="delivery_info"></a> 3. Property `delivery_info`

**Description**:  Delivery info depending on the delivery type

      Delivery Schema
 >   delivery_info

Type: `object`

**Description:** Delivery info depending on the delivery type

                [[]
<a id="delivery_info_oneOf" href="#delivery_info_oneOf">
    <h2 class="handle ml-2 mt-2">
      <label>One of</label>
    </h2>
</a>
    <div class="card">
        <h3 class="ml-2 mt-2"><a id="delivery_info_oneOf_i0" href="#delivery_info_oneOf_i0">classic</a></h3>
        <div class="card-body">
              Delivery Schema
 >   delivery_info
 >   oneOf
 >   classic

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|price|No|number|No|No| No||

        </div>
    </div>
    <div class="card">
        <h3 class="ml-2 mt-2"><a id="delivery_info_oneOf_i1" href="#delivery_info_oneOf_i1">gift</a></h3>
        <div class="card-body">
              Delivery Schema
 >   delivery_info
 >   oneOf
 >   gift

Type: `object`

**Description:** The delivery is a gift, no prices displayed

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|with_wrap|No|boolean|No|No| No||

        </div>
    </div>
](delivery_info_oneOf)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-01-31 at 23:00:06 +0100