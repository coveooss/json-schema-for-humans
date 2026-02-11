<h1>Schema Docs</h1>

<code>Type: object</code>

<h5>If (<code>country = "United States of America"</code>)</h5>
<blockquote>

<code>Type: object</code>

<details>
<summary>
  <strong><a name="then_postal_code"></a>postal_code</strong></summary>

<code>Type: object</code>

<code>Must match regex: [0-9]{5}(-[0-9]{4})?</code>

</details>

</blockquote>
<h5>Else (<code>country != "United States of America"</code>)</h5>
<blockquote>

<code>Type: object</code>

<details>
<summary>
  <strong><a name="else_postal_code"></a>postal_code</strong></summary>

<code>Type: object</code>

<code>Must match regex: [A-Z][0-9][A-Z] [0-9][A-Z][0-9]</code>

</details>

</blockquote>

<details>
<summary>
  <strong><a name="street_address"></a>street_address</strong></summary>

<code>Type: string</code>

</details>

<details>
<summary>
  <strong><a name="country"></a>country</strong></summary>

<code>Type: enum (of string)</code>

<h4>Must be one of:</h4>
<ul>
<li><code>"United States of America"</code></li>
<li><code>"Canada"</code></li>
</ul>

</details>

<hr/>
<footer>
<p>Generated using <a href="https://github.com/coveooss/json-schema-for-humans">json-schema-for-humans</a></p>
</footer>