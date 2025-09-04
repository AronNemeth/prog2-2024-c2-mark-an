# 2025-09-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.488213 |       1.00843  |   0.103157 |
| solution-pl        |     6.1298   |       0.315531 |   0.236907 |
| solution-aron-mark |     0.471757 |       0.151195 |   0.241059 |
| solution-1-flask   |     1.48384  |       1.10046  |   0.270104 |
| solution-2         |     0.485403 |       0.771933 |   0.811185 |
| solution-1         |     7.94779  |       1e-06    |   0.823868 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.494014 |       0.157727 |   0.368926 |
| solution-flask     |     0.479987 |       1.00839  |   0.37628  |
| solution-aron-mark |     0.49033  |       0.155437 |   0.3838   |
| solution-1-flask   |     0.49771  |       1.00827  |   0.801705 |
| solution-2         |     0.488358 |       0.500771 |   2.20732  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.48711  |       0.160302 |    1.08074 |
| solution-aron-mark |     0.477743 |       0.170654 |    1.09455 |
| solution-flask     |     0.513708 |       1.00852  |    1.59832 |
| solution-1-flask   |     0.485067 |       1.0086   |    5.62832 |
| solution-2         |     0.477497 |       0.565007 |   28.4431  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.490505 |       0.195022 |    3.29718 |
| solution-aron-mark |     0.480483 |       0.19836  |    3.31349 |
| solution-flask     |     0.493587 |       1.00834  |    5.17188 |