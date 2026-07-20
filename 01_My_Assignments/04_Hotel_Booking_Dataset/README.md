# Hotel Booking Demand Dataset — EDA

Exploratory data analysis of the **Hotel Booking Demand** dataset, used to study and predict booking cancellations across a City Hotel and a Resort Hotel.

## Dataset Overview

- **Rows:** 119,390
- **Columns:** 36
- **Target:** `is_canceled` — whether a booking was ultimately canceled (`1`) or not (`0`)
- **Date range:** July 2015 – August 2017

| Column (selected) | Type | Description |
|---|---|---|
| `hotel` | categorical | City Hotel or Resort Hotel |
| `is_canceled` | binary | Target — booking canceled (1) or not (0) |
| `lead_time` | numeric | Days between booking and arrival |
| `arrival_date_year/month/day` | — | Combined into a single `arrival_date` datetime |
| `adr` | numeric | Average daily rate |
| `deposit_type` | categorical | No Deposit / Non Refund / Refundable |
| `agent` / `company` | categorical | Booking agent / company ID (high missingness) |
| `previous_cancellations` | numeric | Guest's prior cancellation count |
| `total_of_special_requests` | numeric | Number of special requests made |
| `reserved_room_type` / `assigned_room_type` | categorical | Room reserved vs. actually assigned |
| `reservation_status` / `reservation_status_date` | — | **Excluded** — directly encodes the target (data leakage) |

## Key Findings

- **`reservation_status` is data leakage** — it maps 1:1 onto `is_canceled` and must be dropped before modeling, along with `reservation_status_date`.
- **`company`** is 94.3% missing with no dominant category — collapsed to a binary `has_company` flag rather than used as a raw categorical.
- **`agent`** and **`country`** are high-cardinality (333 / 177 categories) but have a meaningful top-N — bucketed into top categories + "Other" rather than dropped.
- **Strongest, most reliable predictors:** `lead_time` (cancellation rises steadily from 9.6% to 57% with longer lead times), `previous_cancellations` (33.9% → 91.6% with prior history), and `total_of_special_requests` (cleanly declines from 47.7% to 5%).
- **`deposit_type = "Non Refund"` shows a counterintuitive 99.4% cancellation rate** — flagged as a likely data quirk rather than genuine guest behavior, warranting further investigation before use.
- **`assigned_room_type`** is likely set at/near check-in, not at booking time — using it (or the derived `room_type_changed`) as a feature risks leakage and should be excluded from prediction.
- Contains PII-style columns (`name`, `email`, `phone-number`, `credit_card`) — dropped immediately; these are synthetic but excluded as a privacy best practice.

## Data Cleaning Steps

1. Drop PII columns (`name`, `email`, `phone-number`, `credit_card`).
2. Drop `reservation_status` and `reservation_status_date` (leakage).
3. Combine `arrival_date_year/month/day` into a single `arrival_date` datetime; drop the originals.
4. Fill missing `children` (4 rows) with 0.
5. Fill missing `agent`/`country` with `"Unknown"` or `"Direct"`; bucket rare categories.
6. Collapse `company` to a `has_company` binary flag.
7. Remove the 1 negative and 1 extreme outlier value in `adr`.
8. Treat `"Undefined"` entries in `meal`, `market_segment`, `distribution_channel` as missing.

## Repository Structure

```
├── data/
│   └── hotel_booking.csv
├── notebooks/
│   └── eda.ipynb
├── README.md
└── requirements.txt
```

## Source

[Hotel Booking Demand Dataset](https://www.sciencedirect.com/science/article/pii/S2352340918315191) — originally published in *Data in Brief*.
