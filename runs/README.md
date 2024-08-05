# 2024-08-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.06449  |       1.06894  |   0.087333 |
| solution-aron-mark |     0.551189 |       0.10106  |   0.165088 |
| solution-pl        |     1.84293  |       0.101837 |   0.165582 |
| solution-1-flask   |     0.556537 |       1.00884  |   0.256582 |
| solution-1         |     7.61127  |       1e-06    |   0.570812 |
| solution-2         |     4.47706  |       0.549488 |   1.58895  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.568747 |       1.00904  |   0.191988 |
| solution-pl        |     0.556377 |       0.103657 |   0.285813 |
| solution-aron-mark |     0.549899 |       0.103322 |   0.28675  |
| solution-1-flask   |     0.560018 |       1.00906  |   0.774035 |
| solution-2         |     0.54864  |       0.467913 |   3.94067  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.551939 |       1.00928  |   0.909392 |
| solution-pl        |     0.555178 |       0.111556 |   0.990653 |
| solution-aron-mark |     0.552293 |       0.111321 |   0.993302 |
| solution-1-flask   |     0.558881 |       1.0092   |   5.53673  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.55039  |       1.00885  |    4.07801 |
| solution-aron-mark |     0.55126  |       0.145965 |    4.20126 |
| solution-pl        |     0.549043 |       0.145332 |    4.21683 |