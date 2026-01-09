# 2026-01-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.60817  |       1.06511  |   0.095616 |
| solution-aron-mark |     0.460917 |       0.159043 |   0.240588 |
| solution-pl        |     0.462705 |       0.161254 |   0.247083 |
| solution-1-flask   |     0.476173 |       1.00916  |   0.262038 |
| solution-1         |     7.83561  |       1e-06    |   0.812104 |
| solution-2         |     4.89077  |       0.663914 |   1.1222   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.461583 |       0.163569 |   0.365132 |
| solution-aron-mark |     0.46256  |       0.160583 |   0.367392 |
| solution-flask     |     0.469014 |       1.00817  |   0.374133 |
| solution-1-flask   |     0.469672 |       1.00829  |   0.781694 |
| solution-2         |     0.465137 |       0.515977 |   5.05591  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.4683   |       0.162064 |    1.04627 |
| solution-pl        |     0.472435 |       0.167742 |    1.05187 |
| solution-flask     |     0.461106 |       1.0083   |    1.52846 |
| solution-1-flask   |     0.4723   |       1.00842  |    5.50732 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.462394 |       0.187718 |    3.44406 |
| solution-pl        |     0.467568 |       0.187165 |    3.48808 |
| solution-flask     |     0.462356 |       1.00813  |    5.02088 |