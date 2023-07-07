from dataclasses import dataclass
from pathlib import Path
from typing import Union


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Union[Path, str]
    source_url: str
    local_data_file: Union[Path, str]
    unzip_dir: Union[Path, str]
