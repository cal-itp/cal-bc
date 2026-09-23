import os
import urllib.request

from tqdm import tqdm

VERSIONS = {
    "cal-bc-8-1-sketch": {
        "name": "Cal-B/C Sketch v8.1",
        "url": "https://dot.ca.gov/-/media/dot-media/programs/transportation-planning/documents/new-state-planning/transportation-economics/cal-bc/2023-cal-bc/2023-non-federal-model/cal-bc-8-1-sketch-a11y.xlsm",
    },
}


class Downloader:
    @staticmethod
    def from_version(version_id: str) -> None:
        return Downloader(url=VERSIONS[version_id]["url"])

    def __init__(self, url: str) -> None:
        self.url = url

    @property
    def request(self) -> urllib.request.Request:
        return urllib.request.Request(self.url)

    @property
    def response(self) -> bytes:
        return urllib.request.urlopen(self.request)

    @property
    def filename(self) -> str:
        return self.url.split('/')[-1]

    def to_bytes(self) -> bytes:
        return self.response.read()

    def download(self, output_dir: str) -> None:
        output_path = os.path.join(output_dir, self.filename)
        os.makedirs(output_dir, exist_ok=True)
        with tqdm.wrapattr(open(output_path, "wb"), "write", miniters=1, desc=self.filename) as file:
            for chunk in self.response:
                file.write(chunk)
