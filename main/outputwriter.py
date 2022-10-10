import logging

logger = logging.getLogger(__name__)


class OutputWriter:
    def write(self, data):
        # Declaration of method to write data
        raise NotImplementedError


class ConsoleWriter(OutputWriter):
    def write(self, data):
        # Overrides OutputWriter.write method
        print(data.to_string(index=False))
