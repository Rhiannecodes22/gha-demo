# GitHub Actions demo

Workflows for the introduction. The build demonstration uses `ubuntu-latest`, read-only contents permission, and commands that only print text. The EC2 resize demonstration writes one configuration change and opens a pull request. It does not call AWS or apply Terraform.

The timed demo follows one path:

1. `build-and-test.yaml` starts manually or from a push to `main`.
2. `build` validates configuration.
3. Four isolated matrix jobs print one inventory target each.
4. `notify-slack.yaml` is called as a reusable workflow.
5. `release-after-ci.yaml` starts a separate run after successful completion.
6. An EC2 resize issue updates existing service configuration and opens a pull request for SRE review.

| Open this | What it shows |
| --- | --- |
| `.github/workflows/triggers.yaml` | Several triggers, two London schedules, and staggered minutes |
| `.github/workflows/build-and-test.yaml` | `needs` plus an SRE inventory matrix |
| `.github/workflows/notify-slack.yaml` | Shared notification job called by other workflows |
| `.github/workflows/release-after-ci.yaml` | A separate run starts only after CI succeeds |
| `.github/workflows/ec2-resize-request.yaml` | An issue event produces a reviewed configuration change |
| `.github/ISSUE_TEMPLATE/ec2-resize.yml` | A structured service request with fixed choices |
| `infra/services/inventory-api.yaml` | Existing service configuration changed by the request |
| `.github/workflows/cassandra-repair.yaml` | Shared repair implementation |
| `.github/workflows/nbcu-prod-repair.yaml` | NBCU production entry, Monday schedule, and the manual input form |
| `.github/workflows/sky-prod-repair.yaml` | The same implementation for Sky production, with a different schedule |

`triggers.yaml` requests runs at 06:05 and 18:35 `Europe/London`. GitHub may delay scheduled execution, and schedules use the default branch. It has no Jenkins `H` hash, so the timezone and minute are set explicitly.

The trigger catalogue and repair workflows are optional follow-up material, not part of the timed demo. The repair files follow the seeded Cassandra maintenance jobs: one shared implementation, then a separate entry and cron per target. Running the NBCU workflow does not evaluate the Sky workflow.

The inventory matrix replaces repeated Jenkins shell blocks with data. Each matrix row produces a visible job with its own runner and workspace, while `needs` keeps validation before the fan-out.

Slack is centralised in `notify-slack.yaml`, following a similar DPE pattern. Callers use `secrets: inherit`; explicit named secrets provide a narrower interface. With no configured webhook, the reusable workflow prints a skip message and succeeds.

## EC2 resize demonstration setup

Merge the issue form and workflow to the default branch before the session. GitHub only handles an `issues` event with a workflow that exists on that branch.

Create the `ec2-resize` issue label before the session. In repository Actions settings, allow workflows to create and approve pull requests. The issue form applies that label, and the workflow is skipped without it.

The workflow treats the issue body as untrusted input. A Python helper parses the form fields, accepts only known services, environments, and instance types, and updates one existing `instance_type` value.

Use the form to change `inventory-api` in `dev` from `t3.small` to `t3.medium`. The generated pull request is the approval boundary. It has no apply step.

A pull request created with the built-in `GITHUB_TOKEN` does not start another workflow. The generated pull request therefore does not run the `pull_request` path-filter demonstration. A production flow would use a GitHub App token if a Terraform plan workflow must run on that pull request.
