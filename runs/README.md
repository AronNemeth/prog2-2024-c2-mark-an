# 2026-08-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.22056  |       1.05428  |   0.098197 |
| solution-aron-mark |     4.94163  |       0.14823  |   0.213767 |
| solution-pl        |     0.735813 |       0.138401 |   0.214329 |
| solution-1-flask   |     0.890335 |       1.00659  |   0.235924 |
| solution-1         |     7.67365  |       1e-06    |   0.642447 |
| solution-2         |     0.389871 |       0.70039  |   1.8183   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.393728 |       0.141048 |   0.330467 |
| solution-pl        |     0.39748  |       0.141196 |   0.340647 |
| solution-flask     |     0.397969 |       1.0069   |   0.421379 |
| solution-1-flask   |     0.402046 |       1.00666  |   0.728352 |
| solution-2         |     0.399431 |       0.484493 |   3.76265  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.393767 |       0.147681 |    1.03698 |
| solution-pl        |     0.396035 |       0.146165 |    1.05303 |
| solution-flask     |     0.398596 |       1.00736  |    1.79419 |
| solution-1-flask   |     0.400094 |       1.00689  |    5.60215 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.404264 |       0.17686  |    4.38804 |
| solution-pl        |     0.401875 |       0.173485 |    4.45838 |
| solution-flask     |     0.400869 |       1.00679  |    5.96379 |