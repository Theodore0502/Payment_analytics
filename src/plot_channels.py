import argparse, os, pandas as pd, matplotlib.pyplot as plt

def plot_pie(df, outp):
    plt.figure(figsize=(6,6))
    plt.pie(df['share_tx_pct'], labels=df['payment_type'], autopct='%1.1f%%', startangle=90)
    plt.title('Tỷ lệ giao dịch theo kênh (%)')
    plt.axis('equal')
    os.makedirs(os.path.dirname(outp), exist_ok=True)
    plt.savefig(outp, bbox_inches='tight')
    plt.close()

def plot_bar(df, outp):
    plt.figure(figsize=(7,4))
    plt.bar(df['payment_type'], df['total_amount'])
    plt.xlabel('Kênh thanh toán'); plt.ylabel('Tổng số tiền')
    plt.title('Tổng số tiền theo kênh'); plt.xticks(rotation=20)
    os.makedirs(os.path.dirname(outp), exist_ok=True)
    plt.savefig(outp, bbox_inches='tight')
    plt.close()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--summary-csv', required=True)
    ap.add_argument('--pie-out', default='outputs/channel_share_pie.png')
    ap.add_argument('--bar-out', default='outputs/channel_amount_bar.png')
    args = ap.parse_args()
    df = pd.read_csv(args.summary_csv)
    plot_pie(df, args.pie_out)
    plot_bar(df, args.bar_out)
    print('[OK] plots saved ->', args.pie_out, args.bar_out)

if __name__ == '__main__': main()
