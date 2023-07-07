from dataclasses import dataclass
from pathlib import Path
from typing import Union


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Union[Path, str]
    source_url: str
    local_data_file: Union[Path, str]
    unzip_dir: Union[Path, str]


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int
