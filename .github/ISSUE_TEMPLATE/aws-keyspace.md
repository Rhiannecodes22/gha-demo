---
name: AWS Keyspaces - Provisioning
about: Raises a request to create a new keyspace in "AWS Keyspaces (for Apache Cassandra)", and the IRSA IAM roles if the application uses IRSA
title: "Provision <<a keyspace or keyspaces>> in AWS Keyspaces"
labels: AWS,Persistence - AWS Keyspaces
assignees: ""
---

AWS Keyspace names are limited to 48 characters and agreed naming is documented [here](https://gspcloud.atlassian.net/wiki/spaces/OVP/pages/684861219/Keyspace+naming+recommendations).

> ℹ️ Keyspaces must not contain the minus `-` character and thus all below entries use underscore `_`.

> ℹ️ Please refer to the guidance provided in the [AWS Keyspaces Onboarding process runbook](https://gspcloud.atlassian.net/wiki/spaces/OVP/pages/684860287/AWS+Keyspaces+onboarding+process+runbook#AWS-KeySpace-provisioning-process) for help with completing this request.

---

## ✅ Required

### App Name

- [ ] dds
- [ ] drm_kg
- [ ] els
- [ ] geobridge
- [ ] roman
- [ ] rms
- [ ] rm
- [ ] meo
- [ ] tm
- [ ] rs (for RSS and RSI)
- [ ] pc (Parental Control)
- [ ] Other\*

> ℹ️ If your app is not listed above, please write it here after selecting Other and ensure it is in the [OVP Apps Register](https://github.com/NBCUDTC/ovp-docs/blob/main/docs/ovp-guidelines/application-names.md)

---

### Deployment Environment / Replication

> ℹ️ Single-region for Peacock is `usw2` and for NowTV `euc1`.

> ⚠️ If you require dual-region support for `stable_int`, `int`, `stubbed_functional`, or `stubbed_showcase`, include reasoning below.

#### Application Keyspaces (Copy and Paste ✅ this beside the environment needed)

| ✅  | Environment        | Standard Replication | Notes |
| --- | ------------------ | -------------------- | ----- |
| [ ] | stubbed_functional | single-region        |       |
| [ ] | stubbed_showcase   | single-region        |       |
| [ ] | stubbed_nft        | single-region        |       |
| [ ] | extended_nft       | single-region        |       |
| [ ] | int                | single-region        |       |
| [ ] | stable_int         | single-region        |       |
| [ ] | int_nft (Stage)    | dual-region          |       |
| [ ] | prod (Prod)        | dual-region          |       |

If requesting **non-standard replication settings**, explain below:

```
<Your justification for non-standard replication here>
```

---

### Supporting Keyspaces

Provisioning of **test data management keyspaces** for dev/NFT testing.

> [NFT strategy reference](https://github.com/NBCUDTC/ovp-nft/wiki/M.-AWS-Keyspaces-NFT-Strategy#4-test-data-management)

**Please make sure to edit the below table for your needs and not use it just for the stubbed-nft and extended-nft.**

| ✅  | Environment  | Standard Replication | Keyspace Names                                                 |
| --- | ------------ | -------------------- | -------------------------------------------------------------- |
| [ ] | stubbed_nft  | single-region        | appName_goldendst_stubbed_nft, appName_goldensrc_stubbed_nft   |
| [ ] | extended_nft | single-region        | appName_goldendst_extended_nft, appName_goldensrc_extended_nft |

If requesting **non-standard replication settings**, explain below:

```
<Your justification for non-standard replication here>
```

---

### Project Name

- [ ] NowTV (Sky Account)
- [ ] Peacock (NBCU Account)
- [ ] Showmax (Summer Account)
- [ ] SkyShowtime (Summer Account)

---

### Authentication

Choose how the application will access the requested keyspaces:

- [ ] IRSA IAM role (default)
- [ ] IAM user credentials in Vault

#### Trust relationship

Complete this only if you selected IRSA. Add one line for each namespace that needs access.

- Team: `team-name`
- `<Project> <environment>`: ServiceAccount `app-sa` in namespace `app-namespace`

<!-- Example:
SkyEU dev: ServiceAccount `app-sa` in namespace `app-stubbed-functional`,`app-stubbed-showcase`
SkyEU prod: ServiceAccount `app-sa` in namespace `app-prod`
-->
---

## 📝 Optional

### Additional Purpose

(e.g. Stack version or `_copy` for analysis)

---

### Priority

- [ ] Urgent (today or this week)
- [ ] Normal (next or upcoming Sprint)
- [ ] Low (after next Sprint or later)

---

### Required Completion Date

_Add due date if relevant_

---

### DARP Requirements

- [x] This app requires data backups that are up to **35 days** old (per-second resolution)
- [ ] This app requires data backups that are more than **35 days** old

If more than 35 days old, how many?

```
<Insert number of days>
```

---

### Point of Contact

- Tomasz Juszczyk
- Zdenek Tubel
- _(or specify if different from requestor)_

---

## ✅ Definition of Done (OVP SRE will):

- [ ] Create Keyspace in [GPE repo](https://github.com/NBCUDTC/gpe-central-persistence-infra-config/tree/main/aws/services/keyspaces/residents/ovp) and deploy
- [ ] If IAM user is selected: provide credentials to Dev Team in Vault
- [ ] If IRSA is selected: create an IAM role for each Project and environment, with trust limited to the service account in the namespaces listed for it, and add the role ARNs, keyspace names, and VPCE endpoints to this request
- [ ] For test data management keyspaces:
  - Create associated IAM roles
  - Provide credentials in Vault
  - [Runbook](https://gspcloud.atlassian.net/wiki/spaces/ODO/pages/673824797/AWS+Keyspaces+-+Creating+additional+IAM+users)

---

### Any Other Relevant Information

_Is this part of a migration or upcoming CHG?_

```
<Add info here>
```
