import logging
from pathlib import Path

def get_logger(name="TestLogger", test_file_name=None):
    logger = logging.getLogger(name)
    if not logger.handlers:
        # Ensure logs folder exists
        logs_path = Path(__file__).parent.parent.parent / "logs"
        logs_path.mkdir(exist_ok=True)

        # File handler path
        if test_file_name:
            file_path = logs_path / f"{test_file_name}.log"
        else:
            file_path = logs_path / "default.log"

        file_handler = logging.FileHandler(file_path, mode='a')
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)

    return logger
