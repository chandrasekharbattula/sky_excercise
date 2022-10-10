import logging
from main.core import MobileBill
from main.filereader import TextFileReader
from main.outputwriter import ConsoleWriter

logging.basicConfig(format='%(asctime)s %(levelname)s:%(name)s:%(message)s')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    data_from_file = TextFileReader().read("calls.log")
    if data_from_file:
        total_call_cost_for_each_customer = MobileBill(data_from_file).total_cost_for_each_customer()
        ConsoleWriter().write(total_call_cost_for_each_customer)


if __name__ == "__main__":
    main()
