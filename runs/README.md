# 2026-05-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     4.2163   |       1.04332  |   0.07866  |
| solution-1-flask   |     0.329689 |       1.00733  |   0.174879 |
| solution-aron-mark |     4.975    |       0.116629 |   0.17974  |
| solution-pl        |     0.341472 |       0.13316  |   0.187644 |
| solution-2         |     0.336758 |       0.931942 |   0.943304 |
| solution-1         |     8.05087  |       1e-06    |   0.945939 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.337391 |       0.117185 |   0.271436 |
| solution-pl        |     0.322376 |       0.121865 |   0.275449 |
| solution-flask     |     0.324543 |       1.00721  |   0.306219 |
| solution-1-flask   |     0.324523 |       1.00717  |   0.555274 |
| solution-2         |     0.334007 |       0.413733 |   1.99807  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.326085 |       0.126432 |   0.808716 |
| solution-pl        |     0.333418 |       0.123688 |   0.813178 |
| solution-flask     |     0.326818 |       1.00745  |   1.28209  |
| solution-1-flask   |     0.326316 |       1.0074   |   4.39721  |
| solution-2         |     0.341082 |       0.45125  |  35.6075   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.328429 |       0.145103 |    3.01864 |
| solution-aron-mark |     0.340548 |       0.145976 |    3.08568 |
| solution-flask     |     0.329023 |       1.00749  |    4.20715 |