import sys
import logging

logger = logging.getLogger(__name__)


class FileReader:
    def read(self, file_path: str) -> list:
        # Declaration of method to read a file
        raise NotImplementedError


class TextFileReader(FileReader):
    def read(self, file_path: str) -> list:
        # Overrides FileReader.read()
        try:
            f = open(file_path)
            file_content = f.read()
        except FileNotFoundError as e:
            logger.error(f"File {file_path} not found. Aborting")
            sys.exit(1)
        except OSError:
            logger.error(f"OS error occurred trying to open {file_path}")
            sys.exit(1)
        except Exception as err:
            logger.error(f"Unexpected error opening {file_path} is", repr(err))
            sys.exit(1)
        else:
            lines_from_file = file_content.splitlines()
            f.close()
            if len(lines_from_file) == 0:
                logger.debug(f"File {file_path} is empty")
            return list(map(lambda x: (x.split(" ")), lines_from_file))
