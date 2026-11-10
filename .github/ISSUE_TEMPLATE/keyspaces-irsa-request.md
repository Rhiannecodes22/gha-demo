---
name: AWS Keyspaces - IRSA Role
about: Request IRSA IAM roles for a Kubernetes service account to access AWS Keyspaces.
title: "Provision IAM Roles for IRSA Authentication - "
labels: AWS,Persistence - AWS Keyspaces
assignees: ""
---

## Description of work

<!-- Say what the application is, and whether the keyspaces already exist. -->

## Priority

- [ ] Urgent (today or this week)
- [ ] Normal (next or upcoming Sprint)
- [ ] Low (after next Sprint or later)

## Proposition

- [ ] SkyEU
- [ ] Peacock (NBCU)
- [ ] SkyShowtime (Summer)

## Environment

- [ ] dev
- [ ] stage
- [ ] prod

## Description of Requirements

Provision IAM Roles for IRSA with the following requirements.

**Team:**
**Application:**

**1. Trust Relationship (IRSA):**

All roles must trust the Service Account `` in the following namespaces. Separate namespaces with a comma. Leave a proposition empty when this request has no role there.

SkyEU:
NBCU:
Summer:

**2. Regional IAM Policy Permissions (Keyspaces):**

One keyspace name per line under the heading that matches where it runs. A dual-region heading means that name is in both regions. Leave a heading empty when it does not apply. Stage is NBCU only.

- **SkyEU dual-region (eu-central-1 & eu-west-1):**

- **SkyEU single-region eu-central-1:**

- **SkyEU single-region eu-west-1:**

- **NBCU dual-region (us-west-2 & us-east-2):**

- **NBCU single-region us-west-2:**

- **NBCU single-region us-east-2:**

- **Summer single-region us-east-2:**

- **Summer single-region eu-central-1:**

## Point of Contact

Name and email
#slack

## Definition of Done

- [ ] IAM roles created for each proposition in this request
- [ ] Trust relationship limited to the service account in the namespaces listed
- [ ] Role ARNs provided to the team
