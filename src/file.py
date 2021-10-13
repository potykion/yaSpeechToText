import os
from glob import glob

from src.config import DATA_DIR


def filename_from_path(path: str) -> str:
    """
    >>> filename_from_path(r'../data/aac\\v vendetta.aac')
    'v vendetta.aac'
    """
    return os.path.basename(path)


def filename_without_extension_from_path(path: str) -> str:
    """
    >>> filename_without_extension_from_path(r'../data/aac\\v vendetta.aac')
    'v vendetta'
    """
    return os.path.splitext(filename_from_path(path))[0]


def get_all_aac():
    aac_files = glob(os.path.join(DATA_DIR, "aac/*.aac"), recursive=True)
    return aac_files
