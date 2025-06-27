# 2025-06-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.27589  |       1.0497   |   0.102664 |
| solution-pl        |     0.490746 |       0.14989  |   0.231212 |
| solution-aron-mark |     6.07314  |       0.222444 |   0.234835 |
| solution-1-flask   |     0.530959 |       1.00819  |   0.263283 |
| solution-1         |     7.93866  |       1e-06    |   0.995529 |
| solution-2         |     0.502323 |       0.718953 |   1.42627  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.500561 |       0.149123 |   0.362242 |
| solution-pl        |     0.501677 |       0.149098 |   0.363081 |
| solution-flask     |     0.497004 |       1.00815  |   0.379266 |
| solution-1-flask   |     0.502429 |       1.00845  |   0.79941  |
| solution-2         |     0.497941 |       0.49393  |   3.58137  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.505613 |       0.161499 |    1.07157 |
| solution-pl        |     0.495207 |       0.157976 |    1.08001 |
| solution-flask     |     0.495191 |       1.00845  |    1.57575 |
| solution-1-flask   |     0.500378 |       1.00823  |    5.70911 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.499691 |       0.190905 |    3.23792 |
| solution-pl        |     0.493635 |       0.199555 |    3.28353 |
| solution-flask     |     0.498687 |       1.00829  |    5.09392 |