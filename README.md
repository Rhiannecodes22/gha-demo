# GitHub Actions demo

Workflows for the introduction. Every job uses `ubuntu-latest`, requests read-only contents permission, and only prints text.

| Open this | What it shows |
| --- | --- |
| `.github/workflows/triggers.yaml` | Several triggers, two London schedules, and staggered minutes |
| `.github/workflows/build-and-test.yaml` | `needs` plus an SRE inventory matrix |
| `.github/workflows/notify-slack.yaml` | Shared notification job called by other workflows |
| `.github/workflows/release-after-ci.yaml` | A separate run starts only after CI succeeds |
| `.github/workflows/cassandra-repair.yaml` | Shared repair implementation |
| `.github/workflows/nbcu-prod-repair.yaml` | NBCU production entry, Monday schedule, and the manual input form |
| `.github/workflows/sky-prod-repair.yaml` | The same implementation for Sky production, with a different schedule |

`triggers.yaml` runs at 06:05 and 18:35 `Europe/London`. GitHub cron is exact and defaults to UTC. It has no Jenkins `H` hash, so the timezone and minute are set explicitly.

The repair files follow the seeded Cassandra maintenance jobs: one shared implementation, then a separate entry and cron per target. Running the NBCU workflow does not evaluate the Sky workflow.

The inventory matrix replaces repeated Jenkins shell blocks with data. Each matrix row produces a visible job for one AWS profile, while `needs` keeps setup before the fan-out.

Slack is centralised in `notify-slack.yaml`, following similar DPE pattern. Callers use `secrets: inherit` and do not name the webhook.. With no secret, the reusable workflow prints a skip message and succeeds.
