# 2024-04-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.45166  |       1.06461  |   0.067488 |
| solution-aron-mark |     0.703041 |       0.112707 |   0.169209 |
| solution-pl        |     0.679007 |       0.11653  |   0.175566 |
| solution-1-flask   |     0.686805 |       1.00943  |   0.263657 |
| solution-1         |     7.83676  |       1e-06    |   0.600254 |
| solution-2         |     4.59472  |       0.594887 |   1.45956  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.682291 |       1.00948  |   0.177048 |
| solution-aron-mark |     0.672238 |       0.117201 |   0.260775 |
| solution-pl        |     0.711487 |       0.120858 |   0.265216 |
| solution-1-flask   |     0.696743 |       1.00893  |   0.810203 |
| solution-2         |     0.669843 |       0.452826 |   4.27759  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.689748 |       0.122638 |   0.816798 |
| solution-aron-mark |     0.671109 |       0.121778 |   0.829688 |
| solution-flask     |     0.672956 |       1.00962  |   0.957141 |
| solution-1-flask   |     0.677042 |       1.009    |   5.52169  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.665496 |       0.156186 |    3.39215 |
| solution-pl        |     0.69624  |       0.158959 |    3.39387 |
| solution-flask     |     0.665236 |       1.0093   |    5.50191 |