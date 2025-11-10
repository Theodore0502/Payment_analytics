import argparse, os, pandas as pd

ALT_CHANNELS = ["payment_type", "PaymentMethod", "Payment Method"]
ALT_VALUES = ["payment_value", "Amount", "amount"]

def detect_columns(df):
    ch = next((c for c in ALT_CHANNELS if c in df.columns), None)
    val = next((c for c in ALT_VALUES if c in df.columns), None)
    if not ch or not val:
        raise ValueError("Không tìm thấy cột PaymentMethod hoặc Amount.")
    return ch, val

MAP = {"credit card": "credit_card","debit card": "debit_card","paypal": "paypal","upi": "upi","cash": "cash","cod": "cash_on_delivery","wallet": "e_wallet"}

def canon(x):
    if pd.isna(x): return "unknown"
    key = str(x).strip().lower()
    return MAP.get(key, key.replace(" ", "_"))

def summarize(df, ch, val):
    df[ch] = df[ch].apply(canon)
    df[val] = pd.to_numeric(df[val], errors='coerce')
    df = df.dropna(subset=[val])
    df = df[df[val] >= 0]
    grp = df.groupby(ch, as_index=False).agg(transactions=(ch,'count'), total_amount=(val,'sum'))
    grp['share_tx_pct'] = (grp['transactions']/grp['transactions'].sum()*100).round(2)
    grp['share_amount_pct'] = (grp['total_amount']/grp['total_amount'].sum()*100).round(2)
    grp = grp.rename(columns={ch:'payment_type'}).sort_values('total_amount',ascending=False).reset_index(drop=True)
    return grp

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input-csv', required=True)
    ap.add_argument('--output-csv', default='data/processed/payment_channel_summary.csv')
    args = ap.parse_args()
    df = pd.read_csv(args.input_csv)
    ch, val = detect_columns(df)
    summary = summarize(df, ch, val)
    os.makedirs(os.path.dirname(args.output_csv), exist_ok=True)
    summary.to_csv(args.output_csv, index=False)
    print('[OK] saved summary ->', args.output_csv)
    print(summary.head())

if __name__ == '__main__': main()
