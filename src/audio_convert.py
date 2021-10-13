import os

from pydub import AudioSegment

from src.config import DATA_DIR
from src.file import filename_without_extension_from_path, get_all_aac

OpusPath = str


def aac_to_opus(aac_path: str) -> OpusPath:
    opus_dir = os.path.join(DATA_DIR, "opus")
    os.makedirs(opus_dir, exist_ok=True)

    filename = filename_without_extension_from_path(aac_path)
    opus_path = os.path.join(opus_dir, f"{filename}.opus")

    if os.path.exists(opus_path):
        return opus_path

    aac = AudioSegment.from_file(aac_path, "aac")
    aac.export(opus_path, format="ogg", codec="opus")

    return opus_path


if __name__ == '__main__':
    aac_files = get_all_aac()
    for index, path in enumerate(aac_files):
        print(f"{index + 1} / {len(aac_files)}: {path}")
        aac_to_opus(path)
