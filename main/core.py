import logging

import pandas as pd
from datetime import datetime

logger = logging.getLogger(__name__)


def determine_call_cost(call_duration):
    """ Function to determine the cost of a call based on the duration of the call.
    Cost of a call under 3 minutes is 0.05p/sec, over 3 minutes it is 0.03p/sec
    The result is rounded to 1 decimal precision """
    parsed_time = datetime.strptime(call_duration, '%H:%M:%S')
    if parsed_time > datetime.strptime('00:03:00', '%H:%M:%S'):
        call_cost = ((parsed_time.time().minute * 60) + parsed_time.time().second) * 0.03
    else:
        call_cost = ((parsed_time.time().minute * 60) + parsed_time.time().second) * 0.05
    return round(call_cost, 1)


def determine_most_called_number(call_log):
    # Function to determine the phone no with the greatest total cost
    return pd.DataFrame(data=call_log, columns=['customer_id', 'phone_no', 'call_duration']) \
        .assign(call_cost=lambda row: row['call_duration'].apply(determine_call_cost)) \
        .groupby('phone_no') \
        .agg({'call_cost': sum}) \
        .sort_values(by='call_cost', ascending=False) \
        .head(1) \
        .rename_axis('phone_no').reset_index().at[0, 'phone_no']


class MobileBill:
    def __init__(self, call_log):
        self.call_log = call_log
        self.most_called_number = determine_most_called_number(call_log)

    def total_cost_for_each_customer(self):
        # Function to calculate the total call cost for each customer
        return pd.DataFrame(data=self.call_log, columns=['customer_id', 'phone_no', 'call_duration']) \
            .query('phone_no != @self.most_called_number') \
            .assign(call_cost=lambda row: row['call_duration'].apply(determine_call_cost)) \
            .groupby('customer_id') \
            .agg({'call_cost': sum}) \
            .rename_axis('customer_id').reset_index()
