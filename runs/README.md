# 2024-11-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.25525  |       1.14078  |   0.108574 |
| solution-aron-mark |     0.607919 |       0.110913 |   0.183275 |
| solution-pl        |     5.81165  |       0.113822 |   0.195243 |
| solution-1-flask   |     0.5892   |       1.00977  |   0.259614 |
| solution-1         |     7.86286  |       1e-06    |   0.623129 |
| solution-2         |     0.591403 |       0.521852 |   1.08639  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.583192 |       0.110466 |   0.299338 |
| solution-aron-mark |     0.5659   |       0.109154 |   0.302852 |
| solution-flask     |     0.579    |       1.00907  |   0.482081 |
| solution-1-flask   |     0.594257 |       1.00907  |   0.766212 |
| solution-2         |     0.591242 |       0.503381 |   3.24338  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.563316 |       0.115192 |   0.988476 |
| solution-aron-mark |     0.578115 |       0.117672 |   0.996695 |
| solution-flask     |     0.597937 |       1.00956  |   2.09033  |
| solution-1-flask   |     0.576248 |       1.00914  |   5.47049  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.587185 |       0.146157 |    4.27575 |
| solution-aron-mark |     0.568952 |       0.154028 |    4.47009 |
| solution-flask     |     0.581813 |       1.00893  |    8.62666 |