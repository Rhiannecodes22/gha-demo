---
name: AWS Keyspaces - IRSA Role
about: Request IRSA IAM roles for a Kubernetes service account to access AWS Keyspaces.
title: "Provision IAM Roles for IRSA Authentication - <Team> - <App> - <Environment>"
labels: AWS,Persistence - AWS Keyspaces
assignees: ""
---

## Description of Requirements

Provision IAM Roles for IRSA with the following requirements.

**Team:**
**Application:**
**Service Account**: `service-account-name`

### Priority

- [ ] Urgent (today or this week)
- [ ] Normal (next or upcoming Sprint)
- [ ] Low (after next Sprint or later)

### Proposition

- [ ] SkyEU
- [ ] Peacock (NBCU)
- [ ] SkyShowtime (Summer)

### Environment
> **One environment per issue.** For dev, stage, and prod, raise a new issue from this template for each environment. Do not tick more than one environment below.

- [ ] dev
- [ ] stage
- [ ] prod


**1. Trust Relationship (IRSA):**

All roles must trust the Service Account `` in the following namespaces. List namespaces after the label, separated by commas. Leave empty when this request has no role there.

SkyEU:
NBCU:
Summer:

**2. Regional IAM Policy Permissions (Keyspaces):**
<!-- 
List the keyspaces for each region after its heading, separated by commas. Leave a heading empty when it does not apply.

Example: **SkyEU dual-region (eu-central-1 & eu-west-1):** keyspace_example1_skyeu,keyspace_example2_skyeu

Dev usually runs in a single region: SkyEU in eu-central-1, NBCU in us-west-2, and Summer in us-east-2. Stage is NBCU only and may use us-west-2 and us-east-2. Prod may use dual regions: SkyEU in eu-central-1 and eu-west-1, NBCU in us-west-2 and us-east-2, and Summer in eu-central-1.
 -->
- **SkyEU dual-region (eu-central-1 & eu-west-1):**

- **SkyEU single-region eu-central-1:**

- **SkyEU single-region eu-west-1:**

- **NBCU dual-region (us-west-2 & us-east-2):**

- **NBCU single-region us-west-2:**

- **NBCU single-region us-east-2:**

- **Summer single-region us-east-2:**

- **Summer single-region eu-central-1:**

### Point of Contact

Name and email
#slack

## Useful docs

The page covers how OVP SRE manages AWS Keyspaces, including
IRSA: [High Level How OVP SRE Manages AWS Keyspaces](https://gspcloud.atlassian.net/wiki/spaces/ODO/pages/1862205461/High+Level+How+OVP+SRE+Manages+AWS+Keyspaces)

### Definition of Done

<!-- For OVP SRE after the request is submitted. The requester leaves these unticked. -->
- [ ] IAM roles created for each proposition in this request
- [ ] Trust relationship limited to the service account in the namespaces listed
- [ ] Role ARNs provided to the team
