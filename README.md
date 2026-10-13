# GitHub Actions demo

Workflows for the introduction. Every job uses `ubuntu-latest`, requests read-only contents permission, and only prints text.

The timed demo follows one path:

1. `build-and-test.yaml` starts manually or from a push to `main`.
2. `build` validates configuration.
3. Four isolated matrix jobs print one inventory target each.
4. `notify-slack.yaml` is called as a reusable workflow.
5. `release-after-ci.yaml` starts a separate run after successful completion.

| Open this | What it shows |
| --- | --- |
| `.github/workflows/triggers.yaml` | Several triggers, two London schedules, and staggered minutes |
| `.github/workflows/build-and-test.yaml` | `needs` plus an SRE inventory matrix |
| `.github/workflows/notify-slack.yaml` | Shared notification job called by other workflows |
| `.github/workflows/release-after-ci.yaml` | A separate run starts only after CI succeeds |
| `.github/workflows/cassandra-repair.yaml` | Shared repair implementation |
| `.github/workflows/nbcu-prod-repair.yaml` | NBCU production entry, Monday schedule, and the manual input form |
| `.github/workflows/sky-prod-repair.yaml` | The same implementation for Sky production, with a different schedule |

`triggers.yaml` requests runs at 06:05 and 18:35 `Europe/London`. GitHub may delay scheduled execution, and schedules use the default branch. It has no Jenkins `H` hash, so the timezone and minute are set explicitly.

The trigger catalogue and repair workflows are optional follow-up material, not part of the timed demo. The repair files follow the seeded Cassandra maintenance jobs: one shared implementation, then a separate entry and cron per target. Running the NBCU workflow does not evaluate the Sky workflow.

The inventory matrix replaces repeated Jenkins shell blocks with data. Each matrix row produces a visible job with its own runner and workspace, while `needs` keeps validation before the fan-out.

Slack is centralised in `notify-slack.yaml`, following a similar DPE pattern. Callers use `secrets: inherit`; explicit named secrets provide a narrower interface. With no configured webhook, the reusable workflow prints a skip message and succeeds.
