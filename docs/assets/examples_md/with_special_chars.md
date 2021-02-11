# Personne

- [1. Property `Personne > prénom`](#pr_nom)
- [2. Property `Personne > nomDeFamille`](#nomDeFamille)
- [3. Property `Personne > âge`](#a_ge)
- [4. Property `Personne > 0 de quoi d'autre`](#a0_de_quoi_d_autre)

Type: `object`

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
| [prénom](#pr_nom)|No|string|No| No|Le prénom de la personne.|
| [nomDeFamille](#nomDeFamille)|No|string|No| No|Le nom de famille de la personne.|
| [âge](#a_ge)|No|integer|No| No|L'âge en années qui doit être plus grand ou égal à 0.|
| [0 de quoi d'autre](#a0_de_quoi_d_autre)|No|string|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="pr_nom"></a>1. Property `Personne > prénom`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `string`

**Description:** Le prénom de la personne.

## <a name="nomDeFamille"></a>2. Property `Personne > nomDeFamille`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `string`

**Description:** Le nom de famille de la personne.

## <a name="a_ge"></a>3. Property `Personne > âge`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `integer`

**Description:** L'âge en années qui doit être plus grand ou égal à 0.

| Restrictions |   |
| ------------ | - |
| **Minimum** | &ge; 0 |

## <a name="a0_de_quoi_d_autre"></a>4. Property `Personne > 0 de quoi d'autre`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `string`

**Examples:** 

```json
"🖖"
```
```json
"صباح الخير"
```
```json
"你好"
```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-11 at 01:21:04 +0100