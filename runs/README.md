# 2025-07-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.19523  |       1.07619  |   0.101331 |
| solution-aron-mark |     4.41227  |       0.14787  |   0.235344 |
| solution-pl        |     0.513522 |       0.150036 |   0.238483 |
| solution-1-flask   |     0.498984 |       1.00812  |   0.268903 |
| solution-1         |     7.40743  |       1e-06    |   0.659962 |
| solution-2         |     0.492869 |       0.609865 |   0.829382 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.5      |       0.1583   |   0.362746 |
| solution-pl        |     0.495663 |       0.14872  |   0.36778  |
| solution-flask     |     0.495175 |       1.00831  |   0.381073 |
| solution-1-flask   |     0.505032 |       1.00827  |   0.810244 |
| solution-2         |     0.497039 |       0.503407 |   3.43957  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.507066 |       0.157733 |    1.06607 |
| solution-pl        |     0.492976 |       0.157211 |    1.08039 |
| solution-flask     |     0.499603 |       1.00849  |    1.59263 |
| solution-1-flask   |     0.497999 |       1.00846  |    5.58909 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.495798 |       0.190598 |    3.20088 |
| solution-aron-mark |     0.499708 |       0.193396 |    3.21416 |
| solution-flask     |     0.495405 |       1.00852  |    5.08326 |