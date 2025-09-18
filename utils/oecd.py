from typing import Final
import pandas as pd
from urllib.parse import urlencode, quote
from pathlib import Path


DATA_DIR: Final[Path] = Path('data/oecd/')
BASE_URL: Final[str] = "https://sdmx.oecd.org/public/rest/data/"

headers: dict[str, str] = {
    "User-Agent": "TestAgent/1.0"
}

params: dict[str, str] = {
    "format": "csvfile",
}

# build URL with params
def build_url(id: str) -> str:
    return f"{BASE_URL}{id}?{urlencode(params)}"

def cache_path(id_str: str) -> Path:
    return DATA_DIR / f"{quote(id_str, safe='')}.parquet"


def get_oecd_data(id: str) -> pd.DataFrame:
    path = cache_path(id)
    if path.exists():
        return pd.read_parquet(path, engine="fastparquet")

    df = pd.read_csv(
        build_url(id),
        storage_options=headers,
        parse_dates=["TIME_PERIOD"],
        index_col="TIME_PERIOD"
    )
    df.to_parquet(path, engine='fastparquet')
    return df