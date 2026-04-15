#!/usr/bin/env python3
from argparse import ArgumentParser
from sys import argv
from os.path import exists
from json import load
from rich import print
from rich.traceback import install
from isera.simulate import simulate_graph
install(show_locals=True)

parser: ArgumentParser = ArgumentParser(
    description='GFA manipulation tools.', add_help=True)
subparsers = parser.add_subparsers(
    help='Available subcommands', dest="subcommands")

parser._positionals.title = 'Subcommands'
parser._optionals.title = 'Global Arguments'

## Subparser for offset_in_gfa ##

parser_simulate: ArgumentParser = subparsers.add_parser(
    'simulate', help='Simulate a graph with variations from a linear sequence'
)
parser_simulate.add_argument(
    "backbone", type=str, help='Path to a fasta backbone'
)
parser_simulate.add_argument(
    'config', type=str, help='Path to an XML configuration file'
)

#######################################

args = parser.parse_args()


def main() -> None:
    "Main call for subprograms"
    if len(argv) == 1:
        print(
            "[dark_orange]You need to provide a command and its arguments for the program to work.\n"
            "Try to use -h or --help to get list of available commands."
        )
        exit()

    for identifier, syspath in [(key, path) for key, path in args.__dict__.items() if key in ['backbone', 'config',]]:
        if not exists(syspath):
            raise RuntimeError(
                f"Specified path '{syspath}' for argument '{identifier}' does not exists."
            )

    configuration: dict = load(open(args.config, 'r', encoding='utf-8'))

    ##############################################################################
    #                                    COMMANDS                                #
    ##############################################################################

    if args.subcommands == 'simulate':
        "This command creates a graph from a backbone with parameters"
        simulate_graph(
            backbone=args.backbone,
            parameters=configuration,
        )

    else:
        print(
            "[dark_orange]Unknown command. Please use the help to see available commands."
        )
        exit(1)
