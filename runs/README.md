# 2025-11-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.81435  |       1.10401  |   0.102175 |
| solution-pl        |     0.486118 |       0.163147 |   0.244638 |
| solution-aron-mark |     0.499086 |       0.163253 |   0.245867 |
| solution-1-flask   |     0.509469 |       1.00867  |   0.263294 |
| solution-1         |     8.43906  |       1e-06    |   0.716584 |
| solution-2         |     4.90388  |       0.625304 |   0.931638 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.486668 |       0.161064 |   0.365997 |
| solution-pl        |     0.482465 |       0.159664 |   0.368372 |
| solution-flask     |     0.48576  |       1.00858  |   0.379292 |
| solution-1-flask   |     0.487678 |       1.009    |   0.79644  |
| solution-2         |     0.485627 |       0.51869  |  12.7016   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.489105 |       0.16644  |    1.06179 |
| solution-aron-mark |     0.495522 |       0.167387 |    1.08822 |
| solution-flask     |     0.479997 |       1.00886  |    1.57434 |
| solution-1-flask   |     0.484298 |       1.0085   |    5.6809  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.49647  |       0.198858 |    3.30718 |
| solution-pl        |     0.477272 |       0.208149 |    3.3421  |
| solution-flask     |     0.489602 |       1.00879  |    5.26745 |