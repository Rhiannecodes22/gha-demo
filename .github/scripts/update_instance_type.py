#!/usr/bin/env python3
"""Validate an EC2 resize issue and update existing demo configuration."""

from __future__ import annotations

import os
import re
from pathlib import Path


ALLOWED_SERVICES = {
    "inventory-api": Path("infra/services/inventory-api.yaml"),
}
ALLOWED_ENVIRONMENTS = {"dev", "prod"}
ALLOWED_INSTANCE_TYPES = {"t3.small", "t3.medium", "t3.large"}


def issue_field(body: str, label: str) -> str:
    pattern = rf"(?ms)^### {re.escape(label)}\s*\n+(.*?)(?=^### |\Z)"
    match = re.search(pattern, body)
    if not match:
        raise ValueError(f"Issue is missing the {label!r} field")

    value = match.group(1).strip()
    if not value or value == "_No response_":
        raise ValueError(f"Issue field {label!r} is empty")
    return value


def parse_request(body: str) -> tuple[str, str, str]:
    service = issue_field(body, "Service")
    environment = issue_field(body, "Environment")
    instance_type = issue_field(body, "Requested instance type")

    if service not in ALLOWED_SERVICES:
        raise ValueError(f"Unsupported service: {service}")
    if environment not in ALLOWED_ENVIRONMENTS:
        raise ValueError(f"Unsupported environment: {environment}")
    if instance_type not in ALLOWED_INSTANCE_TYPES:
        raise ValueError(f"Unsupported instance type: {instance_type}")

    return service, environment, instance_type


def update_instance_type(
    path: Path, service: str, environment: str, instance_type: str
) -> str:
    lines = path.read_text().splitlines(keepends=True)
    if f"service: {service}\n" not in lines:
        raise ValueError(f"{path} does not describe service {service}")

    in_environment = False
    for index, line in enumerate(lines):
        environment_match = re.fullmatch(r"  ([a-z0-9-]+):\s*\n?", line)
        if environment_match:
            in_environment = environment_match.group(1) == environment
            continue

        if not in_environment:
            continue

        instance_match = re.fullmatch(r"    instance_type:\s*(\S+)\s*\n?", line)
        if not instance_match:
            continue

        previous = instance_match.group(1)
        if previous == instance_type:
            raise ValueError(
                f"{service} in {environment} already uses {instance_type}"
            )
        newline = "\n" if line.endswith("\n") else ""
        lines[index] = f"    instance_type: {instance_type}{newline}"
        path.write_text("".join(lines))
        return previous

    raise ValueError(f"Could not find {environment}.instance_type in {path}")


def write_output(name: str, value: str) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT")
    if output_path:
        with Path(output_path).open("a") as output:
            output.write(f"{name}={value}\n")


def main() -> None:
    service, environment, instance_type = parse_request(os.environ["ISSUE_BODY"])
    config_path = ALLOWED_SERVICES[service]
    previous = update_instance_type(
        config_path, service, environment, instance_type
    )

    write_output("service", service)
    write_output("environment", environment)
    write_output("previous_instance_type", previous)
    write_output("instance_type", instance_type)
    write_output("config_path", str(config_path))

    print(
        f"Updated {service} {environment}: "
        f"{previous} -> {instance_type}"
    )


if __name__ == "__main__":
    main()
