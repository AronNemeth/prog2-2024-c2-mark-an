# 2026-03-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.53213  |       1.16764  |   0.099073 |
| solution-pl        |     4.0913   |       0.13612  |   0.215987 |
| solution-aron-mark |     0.414051 |       0.145996 |   0.229743 |
| solution-1-flask   |     0.423749 |       1.00694  |   0.235985 |
| solution-1         |     6.94999  |       2e-06    |   0.65466  |
| solution-2         |     0.423306 |       0.692142 |   1.01209  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.446493 |       0.145232 |   0.33533  |
| solution-aron-mark |     0.430326 |       0.142678 |   0.348819 |
| solution-flask     |     0.4347   |       1.0069   |   0.459019 |
| solution-1-flask   |     0.485271 |       1.00687  |   0.746521 |
| solution-2         |     0.435934 |       0.532016 |   2.24568  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.421614 |       0.146278 |    1.03807 |
| solution-aron-mark |     0.425891 |       0.149912 |    1.10475 |
| solution-flask     |     0.479934 |       1.00774  |    2.05048 |
| solution-1-flask   |     0.42718  |       1.00689  |    5.96843 |
| solution-2         |     0.432138 |       0.569872 |   34.9919  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.433587 |       0.181969 |    5.6583  |
| solution-pl        |     0.429975 |       0.183777 |    6.28407 |
| solution-flask     |     0.489157 |       1.00863  |    6.85714 |