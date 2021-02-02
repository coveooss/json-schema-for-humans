

# Delivery Schema

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [shipping_address](#shipping_address)|No|object|No|No| No|Exact address|
| [billing_address](#billing_address)|No|object|No|No| No|Exact address|
| [delivery_info](#delivery_info)|No|object|No|No| No|Delivery info depending on the delivery type|

##  <a name="shipping_address"></a>1.  Property `Delivery Schema > shipping_address`

Type: `object`

**Description:** Exact address

Type: `object`

**Description:** Exact address

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [street_address](#shipping_address_street_address)|No|string|Yes|No| No|-|
| [city](#shipping_address_city)|No|string|Yes|No| No|-|
| [state](#shipping_address_state)|No|string|Yes|No| No|-|

###  <a name="shipping_address_street_address"></a>1.1.  Property `Delivery Schema > shipping_address > street_address`

Type: `string`

###  <a name="shipping_address_city"></a>1.2.  Property `Delivery Schema > shipping_address > city`

Type: `string`

###  <a name="shipping_address_state"></a>1.3.  Property `Delivery Schema > shipping_address > state`

Type: `string`

##  <a name="billing_address"></a>2.  Property `Delivery Schema > billing_address`

Type: `object`

**Description:** Exact address
    Same definition as [shipping_address](#shipping_address)

##  <a name="delivery_info"></a>3.  Property `Delivery Schema > delivery_info`

Type: `object`

**Description:** Delivery info depending on the delivery type

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

Type: `object`

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [price](#delivery_info_oneOf_i0_price)|No|number|No|No| No|-|

##  <a name="delivery_info_oneOf_i0_price"></a>1.  Property `Delivery Schema > delivery_info > oneOf > item 0 > price`

Type: `number`

        </div>
    </div>
    <div class="card">
        <h3 class="ml-2 mt-2"><a id="delivery_info_oneOf_i1" href="#delivery_info_oneOf_i1">gift</a></h3>
        <div class="card-body">

Type: `object`

**Description:** The delivery is a gift, no prices displayed

Type: `object`

**Description:** The delivery is a gift, no prices displayed

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [with_wrap](#delivery_info_oneOf_i1_with_wrap)|No|boolean|No|No| No|-|

##  <a name="delivery_info_oneOf_i1_with_wrap"></a>1.  Property `Delivery Schema > delivery_info > oneOf > item 1 > with_wrap`

Type: `boolean`

        </div>
    </div>
](delivery_info_oneOf)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 21:26:32 +0100