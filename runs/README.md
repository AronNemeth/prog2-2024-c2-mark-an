# 2026-01-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.97808  |       1.0589   |   0.102529 |
| solution-pl        |     0.487344 |       0.1665   |   0.252664 |
| solution-aron-mark |     0.473619 |       0.163632 |   0.253298 |
| solution-1-flask   |     0.484301 |       1.00831  |   0.272573 |
| solution-1         |     8.76243  |       1e-06    |   0.711887 |
| solution-2         |     5.31469  |       0.638835 |   0.980331 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.498867 |       0.170752 |   0.386131 |
| solution-aron-mark |     0.505102 |       0.17185  |   0.386416 |
| solution-flask     |     0.481032 |       1.00875  |   0.405766 |
| solution-1-flask   |     0.508991 |       1.0091   |   0.819363 |
| solution-2         |     0.486385 |       0.52382  |   3.93506  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.50484  |       0.179732 |    1.12458 |
| solution-aron-mark |     0.506646 |       0.179167 |    1.12569 |
| solution-flask     |     0.50487  |       1.00872  |    1.68896 |
| solution-1-flask   |     0.495807 |       1.00898  |    5.66476 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.476764 |       0.195047 |    3.69017 |
| solution-aron-mark |     0.476135 |       0.200848 |    3.77765 |
| solution-flask     |     0.507823 |       1.00976  |    5.39859 |