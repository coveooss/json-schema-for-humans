# Delivery Schema

- [1. [Optional] Property Delivery Schema > shipping_address](#shipping_address)
  - [1.1. [Required] Property Delivery Schema > shipping_address > street_address](#shipping_address_street_address)
  - [1.2. [Required] Property Delivery Schema > shipping_address > city](#shipping_address_city)
  - [1.3. [Required] Property Delivery Schema > shipping_address > state](#shipping_address_state)
- [2. [Optional] Property Delivery Schema > billing_address](#billing_address)
- [3. [Optional] Property Delivery Schema > delivery_info](#delivery_info)
  - [3.1. Property `Delivery Schema > delivery_info > oneOf > classic`](#delivery_info_oneOf_i0)
    - [3.1.1. [Optional] Property Delivery Schema > delivery_info > oneOf > item 0 > price](#delivery_info_oneOf_i0_price)
  - [3.2. Property `Delivery Schema > delivery_info > oneOf > gift`](#delivery_info_oneOf_i1)
    - [3.2.1. [Optional] Property Delivery Schema > delivery_info > oneOf > item 1 > with_wrap](#delivery_info_oneOf_i1_with_wrap)

<p><strong>Title:</strong> Delivery Schema</p>

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

<details>
<summary>
<strong> <a name="shipping_address"></a>1. [Optional] Property Delivery Schema > shipping_address</strong>  

</summary>

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

<p><strong>Description:</strong> Exact address</p>

<details>
<summary>
<strong> <a name="shipping_address_street_address"></a>1.1. [Required] Property Delivery Schema > shipping_address > street_address</strong>  

</summary>

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

</details>

<details>
<summary>
<strong> <a name="shipping_address_city"></a>1.2. [Required] Property Delivery Schema > shipping_address > city</strong>  

</summary>

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

</details>

<details>
<summary>
<strong> <a name="shipping_address_state"></a>1.3. [Required] Property Delivery Schema > shipping_address > state</strong>  

</summary>

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

</details>

</details>

<details>
<summary>
<strong> <a name="billing_address"></a>2. [Optional] Property Delivery Schema > billing_address</strong>  

</summary>

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

<p><strong>Description:</strong> Exact address</p>

</details>

<details>
<summary>
<strong> <a name="delivery_info"></a>3. [Optional] Property Delivery Schema > delivery_info</strong>  

</summary>

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

<p><strong>Description:</strong> Delivery info depending on the delivery type</p>

<details>
<summary>One of(Option)</summary>

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

<details>
<summary>
### <a name="delivery_info_oneOf_i0"></a>3.1. Property `Delivery Schema > delivery_info > oneOf > classic`</summary>

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

<details>
<summary>
<strong> <a name="delivery_info_oneOf_i0_price"></a>3.1.1. [Optional] Property Delivery Schema > delivery_info > oneOf > item 0 > price</strong>  

</summary>

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

</details>

</details>
<details>
<summary>
### <a name="delivery_info_oneOf_i1"></a>3.2. Property `Delivery Schema > delivery_info > oneOf > gift`</summary>

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

<p><strong>Description:</strong> The delivery is a gift, no prices displayed</p>

<details>
<summary>
<strong> <a name="delivery_info_oneOf_i1_with_wrap"></a>3.2.1. [Optional] Property Delivery Schema > delivery_info > oneOf > item 1 > with_wrap</strong>  

</summary>

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

</details>

</details>

</details>

</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)