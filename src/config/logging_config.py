from dataclasses import dataclass

@dataclass
class LoggingConfig:

    level = "INFO"
    save_to_file = False