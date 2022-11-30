# Personne

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Personne > prénom`](#prénom)
- [2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Personne > nomDeFamille`](#nomDeFamille)
- [3. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Personne > âge`](#âge)
- [4. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Personne > 0 de quoi d'autre`](#0_de_quoi_dautre)
- [5. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Personne > 名前`](#名前)
- [6. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Personne > 年齢`](#年齢)

**Title:** Personne

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

| Property                                  | Pattern | Type    | Deprecated | Definition | Title/Description                                     |
| ----------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------------------------------------------- |
| - [prénom](#prénom )                      | No      | string  | No         | -          | Le prénom de la personne.                             |
| - [nomDeFamille](#nomDeFamille )          | No      | string  | No         | -          | Le nom de famille de la personne.                     |
| - [âge](#âge )                            | No      | integer | No         | -          | L'âge en années qui doit être plus grand ou égal à 0. |
| - [0 de quoi d'autre](#0_de_quoi_dautre ) | No      | string  | No         | -          | -                                                     |
| - [名前](#名前 )                              | No      | string  | No         | -          | 顧客の名前                                                 |
| - [年齢](#年齢 )                              | No      | integer | No         | -          | 顧客の年齢                                                 |

## <a name="prénom"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Personne > prénom`

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Le prénom de la personne.

## <a name="nomDeFamille"></a>2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Personne > nomDeFamille`

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Le nom de famille de la personne.

## <a name="âge"></a>3. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Personne > âge`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** L'âge en années qui doit être plus grand ou égal à 0.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

## <a name="0_de_quoi_dautre"></a>4. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Personne > 0 de quoi d'autre`

|          |          |
| -------- | -------- |
| **Type** | `string` |

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

## <a name="名前"></a>5. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Personne > 名前`

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** 顧客の名前

## <a name="年齢"></a>6. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Personne > 年齢`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** 顧客の年齢

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
