<h1>User Preference</h1>

<code>Type: object</code>

<details>
<summary>
  <strong><a name="favorite_os"></a>favorite_os</strong></summary>

<code>Type: enum (of string)</code>
<code>Default: "Linux"</code>

<h4>Must be one of:</h4>
<ul>
<li><code>"Windows"</code></li>
<li><code>"Mac"</code></li>
<li><code>"Linux"</code></li>
</ul>

</details>

<details>
<summary>
  <strong><a name="favorite_colors"></a>favorite_colors</strong></summary>

<code>Type: array of enum (of string)</code>
<code>Default: ["white", "blue"]</code>

<h5>Array items: User Preference > favorite_colors > favorite_colors items</h5>
<blockquote>

<code>Type: enum (of string)</code>

<h4>Must be one of:</h4>
<ul>
<li><code>"green"</code></li>
<li><code>"blue"</code></li>
<li><code>"orange"</code></li>
<li><code>"red"</code></li>
<li><code>"white"</code></li>
<li><code>"black"</code></li>
</ul>

</blockquote>

</details>

<details>
<summary>
  <strong><a name="desired_number_of_shoes"></a>desired_number_of_shoes</strong></summary>

<code>Type: integer</code>
<code>Default: 2</code>

<code>Value must be greater or equal to 0 and lesser or equal to 2</code>

</details>

<hr/>
<footer>
<p>Generated using <a href="https://github.com/coveooss/json-schema-for-humans">json-schema-for-humans</a></p>
</footer>