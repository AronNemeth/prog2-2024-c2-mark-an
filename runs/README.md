# 2024-07-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.08685  |       1.05554  |   0.093096 |
| solution-pl        |     5.65275  |       0.105134 |   0.167219 |
| solution-aron-mark |     0.496972 |       0.10294  |   0.167865 |
| solution-1-flask   |     0.501997 |       1.00895  |   0.256241 |
| solution-1         |     7.64701  |       1e-06    |   0.71615  |
| solution-2         |     0.49614  |       0.543519 |   1.222    |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.506591 |       1.00897  |   0.223498 |
| solution-aron-mark |     0.496327 |       0.105103 |   0.286985 |
| solution-pl        |     0.500673 |       0.103455 |   0.287538 |
| solution-1-flask   |     0.512    |       1.00906  |   0.785646 |
| solution-2         |     0.501023 |       0.479272 |   2.66144  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.506912 |       1.00934  |   0.898551 |
| solution-pl        |     0.510079 |       0.115046 |   1.00157  |
| solution-aron-mark |     0.504424 |       0.115499 |   1.04172  |
| solution-1-flask   |     0.506336 |       1.0089   |   5.6399   |
| solution-2         |     0.507364 |       0.534188 |  35.8381   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.496857 |       1.00945  |    4.40538 |
| solution-pl        |     0.504558 |       0.146124 |    4.44254 |
| solution-aron-mark |     0.502027 |       0.147839 |    4.5325  |