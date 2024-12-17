import argparse
import logging

from app import App
 
if __name__ == "__main__" :
    parser = argparse.ArgumentParser(
        prog="AutomataApp",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Cellular automatas are fun!")

    parser.add_argument(
        "--verbose",
        help="turn on more logging",
        action="store_true"
    )

    parser.add_argument(
        "--debug",
        help="turn on a ton of logging",
        action="store_true"
    )

    parser.add_argument(
        "--text",
        help="enable text",
        action="store_true"
    )

    parser.add_argument(
        "--wrap",
        help="enable edge wrapping",
        action="store_true"
    )

    parser.add_argument(
        "--type",
        help="choose which rules to use. rps = rock-paper-scissors. gol = game of life",
        choices = ['simple','rps', 'rps_spiral', 'gol'],
        default = "simple"
    )

    args = parser.parse_args()
    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler())
    if(args.debug):
        logger.setLevel(logging.DEBUG)
        logger.info("set log level to DEBUG logging")
    elif(args.verbose):
        logger.setLevel(logging.INFO)
        logger.info("set log level to INFO logging")

    automataApp = App(args.type, args.text, args.wrap)
    automataApp.run()

