"""Adds functionality to allow slow tests to be skipped by pytest when specified."""
import pytest


def pytest_addoption(parser):
    """Add the `runslow` option to pytest."""
    parser.addoption("--runslow", action="store_true",
                     default=False, help="run slow tests")


def pytest_collection_modifyitems(config, items):
    """Checks collected tests for slow tests."""
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)


pytest_plugins = "render"
