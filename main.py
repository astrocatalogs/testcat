"""Entry point for the Testcat Catalog
"""


def main(args, clargs, log):
    from .testnovacatalog import Test_Catalog
    from astrocats.structures.argshandler import ArgsHandler

    # Create an `ArgsHandler` instance with the appropriate argparse machinery
    log.debug("Initializing `ArgsHandler`")
    args_handler = ArgsHandler(log)
    # Parse the arguments to get the configuration settings
    args = args_handler.load_args(args=args, clargs=clargs)
    # Returns 'None' if no subcommand is given
    if args is None:
        return

    log.debug("Initializing `Test_Catalog`")
    catalog = Test_Catalog(args, log)

    # Run the subcommand given in `args`
    log.debug("Running subcommand")
    args_handler.run_subcommand(args, catalog)

    return
