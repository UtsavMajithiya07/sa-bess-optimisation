"""Download South Australian 5-minute dispatch prices (energy and FCAS) from AEMO via NEMOSIS."""
from pathlib import Path
import argparse

import pandas as pd
from nemosis import dynamic_data_compiler

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "processed"


def main(start, end):
    RAW.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)

    df = dynamic_data_compiler(
        start, end, "DISPATCHPRICE", str(RAW),
        fformat="parquet", keep_csv=False,
        filter_cols=["REGIONID", "INTERVENTION"],
        filter_values=(["SA1"], [0]),
    )

    df = (df.drop(columns=["INTERVENTION", "PRICE_STATUS"], errors="ignore")
            .drop_duplicates("SETTLEMENTDATE")
            .sort_values("SETTLEMENTDATE")
            .reset_index(drop=True))

    expected = pd.date_range(df.SETTLEMENTDATE.min(), df.SETTLEMENTDATE.max(), freq="5min")
    missing = expected.difference(df.SETTLEMENTDATE)
    print(f"Rows: {len(df):,} from {df.SETTLEMENTDATE.min()} to {df.SETTLEMENTDATE.max()}")
    print(f"Missing 5-minute intervals: {len(missing)}")
    print(df.RRP.describe().round(2).to_string())

    path = OUT / "sa1_dispatch_prices.parquet"
    df.to_parquet(path, index=False)
    print(f"Saved {path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", default="2019/01/01 00:00:00")
    parser.add_argument("--end", default="2026/10/01 00:00:00")
    args = parser.parse_args()
    main(args.start, args.end)
