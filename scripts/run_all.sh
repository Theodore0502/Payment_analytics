#!/usr/bin/env bash
python -m src.prepare_data --input-csv "data/raw/E Commerce Dataset.csv"
python -m src.plot_channels --summary-csv data/processed/payment_channel_summary.csv
