# 2026-02-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.0374   |       1.16614  |   0.106514 |
| solution-aron-mark |     0.449006 |       0.152961 |   0.233903 |
| solution-pl        |     4.63375  |       0.146152 |   0.239995 |
| solution-1-flask   |     0.452662 |       1.0088   |   0.268768 |
| solution-1         |     8        |       1e-06    |   0.756418 |
| solution-2         |     0.454111 |       0.632399 |   1.08137  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.458262 |       0.149111 |   0.368506 |
| solution-aron-mark |     0.44756  |       0.148705 |   0.37815  |
| solution-flask     |     0.450975 |       1.01009  |   0.387616 |
| solution-1-flask   |     0.469373 |       1.00889  |   0.793138 |
| solution-2         |     0.454421 |       0.515438 |   3.93428  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.451863 |       0.15613  |    1.12726 |
| solution-pl        |     0.467605 |       0.156797 |    1.14085 |
| solution-flask     |     0.449885 |       1.00898  |    1.71332 |
| solution-1-flask   |     0.462052 |       1.00924  |    5.63017 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.449819 |       0.182062 |    3.83672 |
| solution-aron-mark |     0.448513 |       0.178912 |    4.00848 |
| solution-flask     |     0.449504 |       1.00909  |    5.32036 |