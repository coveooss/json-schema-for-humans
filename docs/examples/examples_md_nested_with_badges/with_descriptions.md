<h1>Delivery Schema</h1>

<code>Type: object</code>

<details>
<summary>
  <strong><a name="shipping_address"></a>shipping_address</strong></summary>

<code>Type: object</code>

<p>Exact address</p>

<details>
<summary>
  <strong><a name="shipping_address_street_address"></a>street_address</strong> <code>Required</code></summary>

<code>Type: string</code>

</details>

<details>
<summary>
  <strong><a name="shipping_address_city"></a>city</strong> <code>Required</code></summary>

<code>Type: string</code>

</details>

<details>
<summary>
  <strong><a name="shipping_address_state"></a>state</strong> <code>Required</code></summary>

<code>Type: string</code>

</details>

</details>

<details>
<summary>
  <strong><a name="billing_address"></a>billing_address</strong></summary>

<code>Type: object</code>

<p>Exact address</p>

<a href="#shipping_address">Same definition as shipping_address</a>

</details>

<details>
<summary>
  <strong><a name="delivery_info"></a>delivery_info</strong></summary>

<code>Type: object</code>

<p>Delivery info depending on the delivery type</p>

<h4>One of</h4>

<blockquote>
<h5><a name="delivery_info_oneOf_i0"></a>classic</h5>

<code>Type: object</code>

<details>
<summary>
  <strong><a name="delivery_info_oneOf_i0_price"></a>price</strong></summary>

<code>Type: number</code>

</details>

</blockquote>
<blockquote>
<h5><a name="delivery_info_oneOf_i1"></a>gift</h5>

<code>Type: object</code>

<p>The delivery is a gift, no prices displayed</p>

<details>
<summary>
  <strong><a name="delivery_info_oneOf_i1_with_wrap"></a>with_wrap</strong></summary>

<code>Type: boolean</code>

</details>

</blockquote>

</details>

<hr/>
<footer>
<p>Generated using <a href="https://github.com/coveooss/json-schema-for-humans">json-schema-for-humans</a></p>
</footer>