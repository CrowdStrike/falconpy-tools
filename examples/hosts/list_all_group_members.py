#!/usr/bin/env python3
"""Caracara Examples Collection.

list_all_groups_members.py

This example will use the API credentials configured in your config.yml file to
list the device member IDs for every host group within your Falcon tenant.

The example demonstrates how to use the Hosts API.
"""
import logging

from caracara import Client

from examples.common import caracara_example, NoGroupsFound, Timer


@caracara_example
def list_all_group_members(**kwargs):
    """List All Host Group Members."""
    client: Client = kwargs['client']
    logger: logging.Logger = kwargs['logger']
    timer: Timer = Timer()

    logger.info("Listing all host groups and their members within the tenant")

    total_members_found = 0

    with client:
        response_data = client.hosts.describe_group_members()
        for group_id, group_data in response_data.items():
            member_list = "No members found"
            if group_data:
                member_list = ", ".join(group_data)
            logger.info("%s (%s)", group_id, member_list)
            total_members_found += len(group_data)

        logger.info("Found %d groups with %d total members in %f seconds",
                    len(response_data),
                    total_members_found,
                    float(timer)
                    )
        if not response_data:
            raise NoGroupsFound


if __name__ in ["__main__", "examples.hosts.list_all_group_members"]:
    try:
        list_all_group_members()
        raise SystemExit
    except NoGroupsFound as no_groups:
        raise SystemExit(no_groups) from no_groups