# 2025-09-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.77939  |       1.15092  |   0.111098 |
| solution-pl        |     0.492259 |       0.154855 |   0.243865 |
| solution-aron-mark |     0.490473 |       0.156075 |   0.249497 |
| solution-1-flask   |     0.504673 |       1.00828  |   0.26976  |
| solution-2         |     4.48222  |       1.23553  |   0.920303 |
| solution-1         |     7.5988   |       1e-06    |   1.17596  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.494807 |       0.157773 |   0.363976 |
| solution-aron-mark |     0.500148 |       0.160733 |   0.366905 |
| solution-flask     |     0.489702 |       1.00829  |   0.378109 |
| solution-1-flask   |     0.501206 |       1.00842  |   0.802795 |
| solution-2         |     0.493425 |       0.525562 |   5.63893  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.496123 |       0.163598 |    1.07333 |
| solution-pl        |     0.498953 |       0.165083 |    1.07942 |
| solution-flask     |     0.493657 |       1.00865  |    1.61782 |
| solution-1-flask   |     0.500157 |       1.00845  |    5.69435 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.490881 |       0.196302 |    3.28865 |
| solution-aron-mark |     0.495114 |       0.19814  |    3.35406 |
| solution-flask     |     0.495391 |       1.00848  |    5.23705 |