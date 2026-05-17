# 2026-05-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.14129  |       1.15749  |   0.223244 |
| solution-aron-mark |     6.7502   |       0.16032  |   0.22704  |
| solution-pl        |     0.430578 |       0.146884 |   0.2298   |
| solution-1-flask   |     0.429275 |       1.00878  |   0.238965 |
| solution-1         |     7.99651  |       1e-06    |   0.63077  |
| solution-2         |     0.429964 |       0.821997 |   0.939213 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.426697 |       0.148564 |   0.350835 |
| solution-aron-mark |     0.430162 |       0.150505 |   0.357153 |
| solution-flask     |     0.427849 |       1.00886  |   0.405898 |
| solution-1-flask   |     0.431417 |       1.00882  |   0.717997 |
| solution-2         |     0.433508 |       0.498547 |   3.85343  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.430515 |       0.152951 |    1.05423 |
| solution-aron-mark |     0.424375 |       0.153857 |    1.06103 |
| solution-flask     |     0.435258 |       1.00898  |    1.67051 |
| solution-1-flask   |     0.433517 |       1.00892  |    5.59137 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.427645 |       0.179729 |    3.74084 |
| solution-pl        |     0.427708 |       0.179308 |    3.7573  |
| solution-flask     |     0.426152 |       1.00899  |    5.28402 |