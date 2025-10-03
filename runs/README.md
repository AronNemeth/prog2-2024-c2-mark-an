# 2025-10-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.5684   |       1.07161  |   0.105509 |
| solution-aron-mark |     0.501855 |       0.157773 |   0.24449  |
| solution-pl        |     0.495428 |       0.16079  |   0.248637 |
| solution-1-flask   |     0.494127 |       1.00842  |   0.273566 |
| solution-1         |     7.94545  |       1e-06    |   0.759707 |
| solution-2         |     4.49796  |       0.751246 |   0.785651 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.497059 |       0.161396 |   0.374899 |
| solution-pl        |     0.493553 |       0.161037 |   0.381417 |
| solution-flask     |     0.49328  |       1.00867  |   0.38198  |
| solution-1-flask   |     0.499199 |       1.00874  |   0.80108  |
| solution-2         |     0.488107 |       0.5166   |   6.46509  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.497533 |       0.167961 |    1.08463 |
| solution-aron-mark |     0.500095 |       0.170992 |    1.09337 |
| solution-flask     |     0.492797 |       1.00889  |    1.61528 |
| solution-1-flask   |     0.509189 |       1.00865  |    5.76014 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.490754 |       0.198014 |    3.28842 |
| solution-aron-mark |     0.492449 |       0.203001 |    3.32387 |
| solution-flask     |     0.494035 |       1.00879  |    5.1919  |