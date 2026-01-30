# 2026-01-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.62155  |       1.0736   |   0.101961 |
| solution-aron-mark |     0.467548 |       0.160118 |   0.243632 |
| solution-pl        |     0.457033 |       0.16111  |   0.244246 |
| solution-1-flask   |     0.46625  |       1.00812  |   0.270316 |
| solution-2         |     4.52079  |       0.693455 |   0.713491 |
| solution-1         |     7.46399  |       1e-06    |   0.715758 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.45785  |       0.162337 |   0.369084 |
| solution-aron-mark |     0.462055 |       0.169896 |   0.36975  |
| solution-flask     |     0.460183 |       1.00841  |   0.381295 |
| solution-1-flask   |     0.4793   |       1.00844  |   0.805563 |
| solution-2         |     0.455585 |       0.497741 |   4.10482  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.459924 |       0.167702 |    1.075   |
| solution-pl        |     0.465793 |       0.169111 |    1.07722 |
| solution-flask     |     0.461544 |       1.00836  |    1.58737 |
| solution-1-flask   |     0.463839 |       1.0084   |    5.52054 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.467043 |       0.193692 |    3.53837 |
| solution-aron-mark |     0.459324 |       0.195917 |    3.5446  |
| solution-flask     |     0.460915 |       1.00843  |    5.01359 |