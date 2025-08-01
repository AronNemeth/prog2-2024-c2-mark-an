# 2025-08-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.42945  |       1.08645  |   0.10092  |
| solution-pl        |     0.50192  |       0.150799 |   0.238144 |
| solution-aron-mark |     4.62378  |       0.159002 |   0.23918  |
| solution-1-flask   |     0.563396 |       1.0082   |   0.268101 |
| solution-1         |     7.42861  |       1e-06    |   0.670432 |
| solution-2         |     0.501011 |       0.643128 |   1.34038  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.499741 |       0.16296  |   0.35809  |
| solution-aron-mark |     0.502296 |       0.154479 |   0.359567 |
| solution-flask     |     0.502754 |       1.00847  |   0.369107 |
| solution-1-flask   |     0.523497 |       1.00855  |   0.78161  |
| solution-2         |     0.499985 |       0.50459  |  21.8048   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.502073 |       0.163468 |    1.0608  |
| solution-aron-mark |     0.51066  |       0.160513 |    1.07778 |
| solution-flask     |     0.505587 |       1.00846  |    1.5581  |
| solution-1-flask   |     0.515643 |       1.00838  |    5.65783 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.497155 |       0.192585 |    3.25487 |
| solution-aron-mark |     0.499635 |       0.192165 |    3.27409 |
| solution-flask     |     0.507004 |       1.00817  |    5.08774 |