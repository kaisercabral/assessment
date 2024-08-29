import click
from controller.transaction_controller import TransactionController
from datetime import datetime

DATE_FORMAT = '%Y-%m-%d'

arg_start_date = click.argument('start_date', type=click.DateTime(formats=[DATE_FORMAT]), metavar='START_DATE')
arg_end_date = click.argument('end_date', type=click.DateTime(formats=[DATE_FORMAT]), metavar='END_DATE',
                              default=datetime.now().strftime(DATE_FORMAT))


@click.group()
def cli():
    pass


#
# Each of the functions below is the entry point of a use case for the command line application.
# Cions, but do not include all of your code in the functions
# in this file.
#

@cli.command(name='import')
@click.argument('transactions_file', type=click.Path(exists=True, dir_okay=False))
def transactions_import_command(transactions_file):
    """Imports the transactions from a file."""
    TransactionController.import_transactions(transactions_file)


@cli.command(name='classify')
@click.option('--rules', type=click.Path(exists=True, dir_okay=False),
              help='CSV file containing the classification rules')
@arg_start_date
@arg_end_date
def classify_command(rules, start_date, end_date):
    """Classifies each transaction in a time period."""
    TransactionController.classify_transactions(rules, start_date, end_date)


@cli.command(name='list')
@click.option('--label',
              help=("Output transactions corresponding to this label only. "
                    "If not set, all transactions are shown."))
@arg_start_date
@arg_end_date
def list_command(label, start_date, end_date):
    """Lists transactions corresponding to a given label in a time period."""
    transactions = TransactionController.list_transactions(label, start_date, end_date)
    print(f'{transactions} transactions listed')


@cli.command(name='report')
@arg_start_date
@arg_end_date
def report_command(start_date, end_date):
    """Summarises expenditure in a period of time."""
    TransactionController.summarise_transactions(start_date, end_date)


if __name__ == '__main__':
    cli()
