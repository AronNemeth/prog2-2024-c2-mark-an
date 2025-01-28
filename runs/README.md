# 2025-01-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.58491  |       1.06332  |   0.083286 |
| solution-aron-mark |     0.550558 |       0.141515 |   0.203677 |
| solution-pl        |     4.8349   |       0.141817 |   0.203684 |
| solution-1-flask   |     0.557661 |       1.00914  |   0.27028  |
| solution-1         |     7.92138  |       1e-06    |   0.860395 |
| solution-2         |     0.54734  |       0.768025 |   1.29809  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.550612 |       0.143739 |   0.307606 |
| solution-aron-mark |     0.551671 |       0.143912 |   0.309895 |
| solution-flask     |     0.547275 |       1.00951  |   0.318579 |
| solution-1-flask   |     0.555234 |       1.00899  |   0.83063  |
| solution-2         |     0.548436 |       0.50807  |   5.72816  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.544903 |       0.147975 |   0.899483 |
| solution-pl        |     0.549969 |       0.151944 |   0.917117 |
| solution-flask     |     0.580581 |       1.00936  |   1.24739  |
| solution-1-flask   |     0.594089 |       1.01036  |   5.72896  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.546059 |       0.178374 |    2.89063 |
| solution-aron-mark |     0.540324 |       0.17878  |    2.90858 |
| solution-flask     |     0.557098 |       1.00948  |    4.29983 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.562005 |       0.288525 |    17.96   |
| solution-aron-mark |     0.547412 |       0.278072 |    18.8255 |