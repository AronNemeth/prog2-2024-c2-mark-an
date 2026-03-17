# 2026-03-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.96938  |       1.09806  |   0.108784 |
| solution-aron-mark |     0.453645 |       0.151776 |   0.237115 |
| solution-pl        |     4.9472   |       0.148733 |   0.238112 |
| solution-1-flask   |     0.493195 |       1.0088   |   0.266548 |
| solution-1         |     7.98503  |       1e-06    |   0.941045 |
| solution-2         |     0.448722 |       0.759989 |   1.13005  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.451798 |       0.153412 |   0.369057 |
| solution-pl        |     0.477623 |       0.152578 |   0.369253 |
| solution-flask     |     0.447366 |       1.00894  |   0.411451 |
| solution-1-flask   |     0.454579 |       1.00874  |   0.786181 |
| solution-2         |     0.476629 |       0.529369 |  14.1249   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.455987 |       0.157822 |    1.1184  |
| solution-pl        |     0.449356 |       0.159702 |    1.1356  |
| solution-flask     |     0.459802 |       1.00902  |    1.66784 |
| solution-1-flask   |     0.458353 |       1.00898  |    5.67218 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.455845 |       0.182897 |    4.04063 |
| solution-pl        |     0.451468 |       0.186505 |    4.08579 |
| solution-flask     |     0.447177 |       1.00937  |    5.23161 |