import logging


def main():
    logging.basicConfig(
        level=logging.ERROR,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logging.debug("This is a debug log.")
    logging.info("This is an info log.")
    logging.warning("This is a warning log.")
    logging.error("This is an error log.")
    logging.critical("This is a critical log.")


if __name__ == "__main__":
    main()
