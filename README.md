# PaymentChannelAnalytics v2 — E-Commerce Transactions Dataset

Dự án phân tích **kênh thanh toán** dựa trên **E-Commerce Transactions Dataset** (50,000 bản ghi) từ Kaggle.

## 🎯 Mục tiêu
- Chuẩn hoá dữ liệu thanh toán (`PaymentMethod`, `Amount`).
- Tính **tỷ lệ giao dịch** và **tổng số tiền** theo từng phương thức thanh toán.
- Xuất CSV tổng hợp và biểu đồ (Pie & Bar) sẵn sàng đưa vào Power BI.

## 📦 Dataset
**E-Commerce Transactions Dataset** — [Kaggle link](https://www.kaggle.com/datasets/smayanj/e-commerce-transactions-dataset)

Dataset chính: `data/raw/E Commerce Dataset.csv`

## ⚙️ Cách chạy
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt

python -m src.prepare_data --input-csv "data/ecommerce_transactions.csv"

python -m src.plot_channels --summary-csv data/processed/payment_channel_summary.csv

```

Hoặc dùng script nhanh:
- Windows: `scripts\run_all.bat`
- macOS/Linux: `bash scripts/run_all.sh`

## 📊 Đầu ra
- `data/processed/payment_channel_summary.csv`
- `outputs/channel_share_pie.png`
- `outputs/channel_amount_bar.png`

## 💡 Nhúng Power BI
1. Import CSV processed
2. Pie chart: Legend = payment_type, Values = share_tx_pct
3. Bar chart: Axis = payment_type, Values = total_amount
4. Xem DAX + theme trong `powerbi/`

