import logging

LOGGER = logging.getLogger(__name__)

def test_myloggings():
    LOGGER.info("Info logs")
    LOGGER.warning("Warning logs")
    LOGGER.error("Error logs")
    LOGGER.critical(("Critical Logs"))
    assert True

