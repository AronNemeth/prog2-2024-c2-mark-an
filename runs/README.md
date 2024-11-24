# 2024-11-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.23277  |       1.1644   |   0.107794 |
| solution-pl        |     5.68523  |       0.108686 |   0.175023 |
| solution-aron-mark |     0.56557  |       0.108983 |   0.195273 |
| solution-1-flask   |     0.563515 |       1.00905  |   0.25003  |
| solution-1         |     7.33835  |       1e-06    |   0.579284 |
| solution-2         |     0.555546 |       0.507075 |   1.36896  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.560031 |       0.108552 |   0.305093 |
| solution-pl        |     0.558268 |       0.10874  |   0.317135 |
| solution-flask     |     0.560324 |       1.00891  |   0.484566 |
| solution-1-flask   |     0.565356 |       1.00889  |   0.771315 |
| solution-2         |     0.56022  |       0.474326 |   3.90141  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.558761 |       0.118157 |    1.00601 |
| solution-pl        |     0.576689 |       0.116276 |    1.01072 |
| solution-flask     |     0.559476 |       1.00913  |    2.13971 |
| solution-1-flask   |     0.561624 |       1.0096   |    5.41697 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.578591 |       0.146279 |    4.2604  |
| solution-pl        |     0.565948 |       0.146857 |    4.28672 |
| solution-flask     |     0.557249 |       1.00908  |    8.42362 |