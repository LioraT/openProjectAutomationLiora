from framework.utils.driver_factory import DriverFactory
from utils.read_properties import ReadConfig
import pytest


@pytest.fixture()
def setup():
    driver = DriverFactory.create(ReadConfig.getBrowser())
    yield driver

    driver.quit()


def pytest_configure(config):
    config._metadata['Project Name'] = 'ProjectNameX'
    config._metadata['Module Name'] = 'HomePage'
    config._metadata['Tester'] = 'Admin'
    config._metadata['Package'] = 'python'


# hook for delete/modify environment info to HTML Report

@pytest.mark.parametrize
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
