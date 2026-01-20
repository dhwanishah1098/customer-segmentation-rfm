# Customer Segmentation — RFM Analysis

RFM (Recency, Frequency, Monetary) analysis pipeline for customer segmentation, CLV estimation, and targeted marketing strategy.

## Segments Identified
| Segment | Action |
|---------|--------|
| Champions | Reward & upsell |
| Loyal Customers | Loyalty program |
| At Risk | Reactivation campaign |
| Lost | Win-back or deprioritise |

## Modules
- `rfm/calculator.py` — RFM metric computation
- `rfm/segmentation.py` — Segment assignment rules
- `rfm/visualizer.py` — Distribution and heatmap plots
- `rfm/clv.py` — Customer lifetime value estimation
- `rfm/recommendations.py` — Segment-level marketing actions

## Usage
```bash
pip install -r requirements.txt
python main.py --input data/transactions.csv
```
