# Schema Docs

- [1. Property `root > billing_address`](#billing_address)
  - [1.1. Property `root > billing_address > street_address`](#billing_address_street_address)
  - [1.2. Property `root > billing_address > city`](#billing_address_city)
  - [1.3. Property `root > billing_address > state`](#billing_address_state)
  - [1.4. Property `root > billing_address > futureProperty`](#billing_address_futureProperty)
- [2. Property `root > shipping_address`](#shipping_address)

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
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td>Any type allowed</td>
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
<li><a href="#">billing_address</a></li>
</ul></td>
    <td>No</td>
    <td>object</td>
    <td>No</td>
    <td>In #/definitions/address</td>
    <td>-</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">shipping_address</a></li>
</ul></td>
    <td>No</td>
    <td>object</td>
    <td>No</td>
    <td>Same as <a href="#">billing_address</a></td>
    <td>-</td>
  </tr>
</table>

## <a name="billing_address"></a>1. Property `root > billing_address`

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
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td>Any type allowed</td>
  </tr>
  <tr>
    <td><strong>Defined in</strong></td>
    <td><h1>/definitions/address</h1></td>
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
  <tr>
    <td><ul>
<li><a href="#">futureProperty</a></li>
</ul></td>
    <td>No</td>
    <td>null</td>
    <td>No</td>
    <td>-</td>
    <td>-</td>
  </tr>
</table>

### <a name="billing_address_street_address"></a>1.1. Property `root > billing_address > street_address`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>string</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>Yes</td>
  </tr>
</table>

### <a name="billing_address_city"></a>1.2. Property `root > billing_address > city`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>string</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>Yes</td>
  </tr>
</table>

### <a name="billing_address_state"></a>1.3. Property `root > billing_address > state`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>string</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>Yes</td>
  </tr>
</table>

### <a name="billing_address_futureProperty"></a>1.4. Property `root > billing_address > futureProperty`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>null</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
</table>

## <a name="shipping_address"></a>2. Property `root > shipping_address`

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
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td>Any type allowed</td>
  </tr>
  <tr>
    <td><strong>Same definition as</strong></td>
    <td><a href="#billing_address">billing_address</a></td>
  </tr>
</table>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
