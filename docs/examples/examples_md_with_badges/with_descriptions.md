# Delivery Schema

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Delivery Schema > shipping_address`](#shipping_address)
  - [1.1. ![Required](https://img.shields.io/badge/Required-blue) Property `Delivery Schema > shipping_address > street_address`](#shipping_address_street_address)
  - [1.2. ![Required](https://img.shields.io/badge/Required-blue) Property `Delivery Schema > shipping_address > city`](#shipping_address_city)
  - [1.3. ![Required](https://img.shields.io/badge/Required-blue) Property `Delivery Schema > shipping_address > state`](#shipping_address_state)
- [2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Delivery Schema > billing_address`](#billing_address)
- [3. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Delivery Schema > delivery_info`](#delivery_info)
  - [3.1. Property `Delivery Schema > delivery_info > oneOf > classic`](#delivery_info_oneOf_i0)
    - [3.1.1. Property `Delivery Schema > delivery_info > oneOf > item 0 > price`](#delivery_info_oneOf_i0_price)
  - [3.2. Property `Delivery Schema > delivery_info > oneOf > gift`](#delivery_info_oneOf_i1)
    - [3.2.1. Property `Delivery Schema > delivery_info > oneOf > item 1 > with_wrap`](#delivery_info_oneOf_i1_with_wrap)

**Title:** Delivery Schema

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>object</code></td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td><img src="https://img.shields.io/badge/Any%20type-allowed-green" alt="Any type: allowed" /></td>
  </tr>
</table>

<table>
  <tr>
    <th>Property</th>
    <th>Pattern</th>
    <th>Type</th>
    <th>Deprecated</th>
    <th>Definition</th>
    <th>Title/Description</th>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">shipping_address</a></li>
</ul></td>
    <td>No</td>
    <td>object</td>
    <td>No</td>
    <td>In #/definitions/address</td>
    <td>Exact address</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">billing_address</a></li>
</ul></td>
    <td>No</td>
    <td>object</td>
    <td>No</td>
    <td>Same as <a href="#">shipping_address</a></td>
    <td>Exact address</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">delivery_info</a></li>
</ul></td>
    <td>No</td>
    <td>object</td>
    <td>No</td>
    <td>In #/definitions/delivery_info</td>
    <td>Delivery info depending on the delivery type</td>
  </tr>
</table>

## <a name="shipping_address"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Delivery Schema > shipping_address`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>object</code></td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td><img src="https://img.shields.io/badge/Any%20type-allowed-green" alt="Any type: allowed" /></td>
  </tr>
  <tr>
    <td><strong>Defined in</strong></td>
    <td><h1>/definitions/address</h1></td>
  </tr>
</table>

**Description:** Exact address

<table>
  <tr>
    <th>Property</th>
    <th>Pattern</th>
    <th>Type</th>
    <th>Deprecated</th>
    <th>Definition</th>
    <th>Title/Description</th>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">street_address</a></li>
</ul></td>
    <td>No</td>
    <td>string</td>
    <td>No</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">city</a></li>
</ul></td>
    <td>No</td>
    <td>string</td>
    <td>No</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">state</a></li>
</ul></td>
    <td>No</td>
    <td>string</td>
    <td>No</td>
    <td>-</td>
    <td>-</td>
  </tr>
</table>

### <a name="shipping_address_street_address"></a>1.1. ![Required](https://img.shields.io/badge/Required-blue) Property `Delivery Schema > shipping_address > street_address`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>string</code></td>
  </tr>
</table>

### <a name="shipping_address_city"></a>1.2. ![Required](https://img.shields.io/badge/Required-blue) Property `Delivery Schema > shipping_address > city`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>string</code></td>
  </tr>
</table>

### <a name="shipping_address_state"></a>1.3. ![Required](https://img.shields.io/badge/Required-blue) Property `Delivery Schema > shipping_address > state`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>string</code></td>
  </tr>
</table>

## <a name="billing_address"></a>2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Delivery Schema > billing_address`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>object</code></td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td><img src="https://img.shields.io/badge/Any%20type-allowed-green" alt="Any type: allowed" /></td>
  </tr>
  <tr>
    <td><strong>Same definition as</strong></td>
    <td><a href="#shipping_address">shipping_address</a></td>
  </tr>
</table>

**Description:** Exact address

## <a name="delivery_info"></a>3. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Delivery Schema > delivery_info`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>combining</code></td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td><img src="https://img.shields.io/badge/Any%20type-allowed-green" alt="Any type: allowed" /></td>
  </tr>
  <tr>
    <td><strong>Defined in</strong></td>
    <td><h1>/definitions/delivery_info</h1></td>
  </tr>
</table>

**Description:** Delivery info depending on the delivery type

<table>
  <tr>
    <th>One of(Option)</th>
  </tr>
  <tr>
    <td><a href="#delivery_info_oneOf_i0">classic</a></td>
  </tr>
  <tr>
    <td><a href="#delivery_info_oneOf_i1">gift</a></td>
  </tr>
</table>

### <a name="delivery_info_oneOf_i0"></a>3.1. Property `Delivery Schema > delivery_info > oneOf > classic`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>object</code></td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td><img src="https://img.shields.io/badge/Any%20type-allowed-green" alt="Any type: allowed" /></td>
  </tr>
  <tr>
    <td><strong>Defined in</strong></td>
    <td><h1>/definitions/classic</h1></td>
  </tr>
</table>

<table>
  <tr>
    <th>Property</th>
    <th>Pattern</th>
    <th>Type</th>
    <th>Deprecated</th>
    <th>Definition</th>
    <th>Title/Description</th>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">price</a></li>
</ul></td>
    <td>No</td>
    <td>number</td>
    <td>No</td>
    <td>-</td>
    <td>-</td>
  </tr>
</table>

#### <a name="delivery_info_oneOf_i0_price"></a>3.1.1. Property `Delivery Schema > delivery_info > oneOf > item 0 > price`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>number</code></td>
  </tr>
</table>

### <a name="delivery_info_oneOf_i1"></a>3.2. Property `Delivery Schema > delivery_info > oneOf > gift`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>object</code></td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td><img src="https://img.shields.io/badge/Any%20type-allowed-green" alt="Any type: allowed" /></td>
  </tr>
  <tr>
    <td><strong>Defined in</strong></td>
    <td><h1>/definitions/gift</h1></td>
  </tr>
</table>

**Description:** The delivery is a gift, no prices displayed

<table>
  <tr>
    <th>Property</th>
    <th>Pattern</th>
    <th>Type</th>
    <th>Deprecated</th>
    <th>Definition</th>
    <th>Title/Description</th>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">with_wrap</a></li>
</ul></td>
    <td>No</td>
    <td>boolean</td>
    <td>No</td>
    <td>-</td>
    <td>-</td>
  </tr>
</table>

#### <a name="delivery_info_oneOf_i1_with_wrap"></a>3.2.1. Property `Delivery Schema > delivery_info > oneOf > item 1 > with_wrap`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>boolean</code></td>
  </tr>
</table>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
