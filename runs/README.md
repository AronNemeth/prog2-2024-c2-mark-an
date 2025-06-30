# 2025-06-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.11977  |       1.08327  |   0.13087  |
| solution-aron-mark |     5.67139  |       0.332347 |   0.236133 |
| solution-pl        |     0.500795 |       0.152771 |   0.241222 |
| solution-1-flask   |     0.512867 |       1.00831  |   0.261066 |
| solution-1         |     7.45064  |       1e-06    |   0.595675 |
| solution-2         |     0.497972 |       0.758871 |   0.886878 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.534417 |       0.152499 |   0.361176 |
| solution-flask     |     0.505989 |       1.00831  |   0.380031 |
| solution-aron-mark |     0.511057 |       0.156713 |   0.38019  |
| solution-1-flask   |     0.50979  |       1.00845  |   0.800277 |
| solution-2         |     0.501799 |       0.507171 |   2.21506  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.502766 |       0.15755  |    1.07383 |
| solution-aron-mark |     0.511136 |       0.158043 |    1.0759  |
| solution-flask     |     0.500268 |       1.00841  |    1.58923 |
| solution-1-flask   |     0.513409 |       1.00844  |    5.57404 |
| solution-2         |     0.501477 |       0.565763 |  169.194   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.498054 |       0.187953 |    3.2523  |
| solution-aron-mark |     0.501657 |       0.19444  |    3.26429 |
| solution-flask     |     0.503387 |       1.00842  |    5.14816 |