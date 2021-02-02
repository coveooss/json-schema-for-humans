

# Person

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [firstName](#firstName)|No|string|No|No| No|the person's first name|
| [lastName](#lastName)|No|string|No|No| No|The person's last name.|
| [age](#age)|No|integer|No|No| No|Age in years which must be equal to or greater than zero.|
| [moreInfo](#moreInfo)|No|object|No|No| No|Any more info you want as an object|

##  <a name="firstName"></a>1.  Property `Person > firstName`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_examples.json', 'path_to_element': ['firstName'], 'html_id': 'firstName', 'breadcrumb_name': 'firstName', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fd2b0>, 'parent_key': 'firstName', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fd850>, 'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fd4c0>, 'title': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224b4f10>, 'examples': ['"Guido"', '"BDFL"']}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

**Description:** the person's first name

**Examples:** 

```
    <div class="highlight"><pre><span></span><span class="s2">&quot;Guido&quot;</span>
</pre></div>

```
```
    <div class="highlight"><pre><span></span><span class="s2">&quot;BDFL&quot;</span>
</pre></div>

```

##  <a name="lastName"></a>2.  Property `Person > lastName`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_examples.json', 'path_to_element': ['lastName'], 'html_id': 'lastName', 'breadcrumb_name': 'lastName', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fd2b0>, 'parent_key': 'lastName', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224b4250>, 'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224b4040>, 'title': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224b4130>, 'examples': ['"Van Rossum"']}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

**Description:** The person's last name.

**Example:** 

```
    <div class="highlight"><pre><span></span><span class="s2">&quot;Van Rossum&quot;</span>
</pre></div>

```

##  <a name="age"></a>3.  Property `Person > age`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_examples.json', 'path_to_element': ['age'], 'html_id': 'age', 'breadcrumb_name': 'age', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fd2b0>, 'parent_key': 'age', 'ref_path': '', 'literal': None, 'keywords': {'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224b4100>, 'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224b4070>, 'minimum': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224b44c0>, 'title': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224b4520>, 'examples': ['64']}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `integer`

**Description:** Age in years which must be equal to or greater than zero.

        Value must be greater or equal to `0`

**Example:** 

```
    <div class="highlight"><pre><span></span><span class="mi">64</span>
</pre></div>

```

##  <a name="moreInfo"></a>4.  Property `Person > moreInfo`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_examples.json', 'path_to_element': ['moreInfo'], 'html_id': 'moreInfo', 'breadcrumb_name': 'moreInfo', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fd2b0>, 'parent_key': 'moreInfo', 'ref_path': '', 'literal': None, 'keywords': {'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224b4190>, 'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224b4820>, 'examples': ['{\n    "birthplace": "Haarlem, Netherlands",\n    "favorite_emoji": "🐍",\n    "motto": "Beautiful is better than ugly.\\\\nExplicit is better than implicit.\\\\nSimple is better than complex.\\\\nComplex is better than complicated.\\\\nFlat is better than nested.\\\\nSparse is better than dense.\\\\nReadability counts.\\\\nSpecial cases aren\'t special enough to break the rules.\\\\nAlthough practicality beats purity.\\\\nErrors should never pass silently.\\\\nUnless explicitly silenced.\\\\nIn the face of ambiguity, refuse the temptation to guess.\\\\nThere should be one-- and preferably only one --obvious way to do it.\\\\nAlthough that way may not be obvious at first unless you\'re Dutch.\\\\nNow is better than never.\\\\nAlthough never is often better than *right* now.\\\\nIf the implementation is hard to explain, it\'s a bad idea.\\\\nIf the implementation is easy to explain, it may be a good idea.\\\\nNamespaces are one honking great idea -- let\'s do more of those!"\n}']}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

**Description:** Any more info you want as an object

**Example:** 

```
    <div class="highlight"><pre><span></span><span class="p">{</span>
    <span class="s2">&quot;birthplace&quot;</span><span class="o">:</span> <span class="s2">&quot;Haarlem, Netherlands&quot;</span><span class="p">,</span>
    <span class="s2">&quot;favorite_emoji&quot;</span><span class="o">:</span> <span class="s2">&quot;🐍&quot;</span><span class="p">,</span>
    <span class="s2">&quot;motto&quot;</span><span class="o">:</span> <span class="s2">&quot;Beautiful is better than ugly.\\nExplicit is better than implicit.\\nSimple is better than complex.\\nComplex is better than complicated.\\nFlat is better than nested.\\nSparse is better than dense.\\nReadability counts.\\nSpecial cases aren&#39;t special enough to break the rules.\\nAlthough practicality beats purity.\\nErrors should never pass silently.\\nUnless explicitly silenced.\\nIn the face of ambiguity, refuse the temptation to guess.\\nThere should be one-- and preferably only one --obvious way to do it.\\nAlthough that way may not be obvious at first unless you&#39;re Dutch.\\nNow is better than never.\\nAlthough never is often better than *right* now.\\nIf the implementation is hard to explain, it&#39;s a bad idea.\\nIf the implementation is easy to explain, it may be a good idea.\\nNamespaces are one honking great idea -- let&#39;s do more of those!&quot;</span>
<span class="p">}</span>
</pre></div>

```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 22:00:56 +0100