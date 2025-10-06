import os
import urllib.request
from tqdm import tqdm


VERSIONS = {
    "cal-bc-8-1-sketch": {
        "name": "Cal-B/C Sketch v8.1",
        "url": "https://dot.ca.gov/-/media/dot-media/programs/transportation-planning/documents/new-state-planning/transportation-economics/cal-bc/2023-cal-bc/2023-non-federal-model/cal-bc-8-1-sketch-a11y.xlsm",
    },
}


def progress(t):
    last_b = [0]

    def update_to(b=1, bsize=1, tsize=None):
        if tsize is not None:
            t.total = tsize
        t.update((b - last_b[0]) * bsize)
        last_b[0] = b

    return update_to


class Downloader:
    def __init__(self, version_id: str) -> None:
        self.version_id = version_id

    def download(self, output_dir: str) -> None:
        filename = os.path.join(output_dir, f"{self.version_id}.xlsm")
        os.makedirs(output_dir, exist_ok=True)
        version = VERSIONS[self.version_id]
        with tqdm(
            unit="B", unit_scale=True, unit_divisor=1024, miniters=1, desc=filename
        ) as t:
            urllib.request.urlretrieve(
                version["url"], filename=filename, reporthook=progress(t)
            )
