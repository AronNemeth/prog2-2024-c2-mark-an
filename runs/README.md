# 2025-02-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.41773  |       1.11039  |   0.081618 |
| solution-aron-mark |     0.534906 |       0.13812  |   0.200856 |
| solution-pl        |     4.65351  |       0.137151 |   0.202941 |
| solution-1-flask   |     0.545192 |       1.00876  |   0.265732 |
| solution-1         |     7.70125  |       1e-06    |   0.691471 |
| solution-2         |     0.537403 |       0.580989 |   0.989904 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.542497 |       1.00944  |   0.291267 |
| solution-aron-mark |     0.557232 |       0.142195 |   0.30154  |
| solution-pl        |     0.537146 |       0.141719 |   0.302784 |
| solution-1-flask   |     0.551527 |       1.00889  |   0.805768 |
| solution-2         |     0.541497 |       0.494858 |   4.22446  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.534147 |       0.1481   |   0.885813 |
| solution-pl        |     0.534304 |       0.146167 |   0.91758  |
| solution-flask     |     0.529071 |       1.00888  |   1.22318  |
| solution-1-flask   |     0.53792  |       1.00874  |   5.72201  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.525368 |       0.178463 |    2.8268  |
| solution-pl        |     0.531697 |       0.176966 |    2.83277 |
| solution-flask     |     0.531983 |       1.00896  |    4.26351 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.533527 |       0.280963 |    16.5972 |
| solution-aron-mark |     0.533359 |       0.284606 |    16.8269 |