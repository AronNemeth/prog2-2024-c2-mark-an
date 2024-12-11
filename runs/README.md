# 2024-12-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.11555  |       1.07099  |   0.111159 |
| solution-aron-mark |     0.574475 |       0.11024  |   0.180759 |
| solution-pl        |     5.75069  |       0.110337 |   0.186792 |
| solution-1-flask   |     0.567285 |       1.00886  |   0.253438 |
| solution-1         |     7.55297  |       1e-06    |   0.586963 |
| solution-2         |     0.564685 |       0.515011 |   1.41205  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.58506  |       0.110416 |   0.316768 |
| solution-pl        |     0.566186 |       0.110737 |   0.330338 |
| solution-flask     |     0.596018 |       1.00913  |   0.503406 |
| solution-1-flask   |     0.603209 |       1.00905  |   0.780746 |
| solution-2         |     0.568914 |       0.485006 |   3.97533  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.609634 |       0.122638 |    1.03113 |
| solution-aron-mark |     0.595682 |       0.121865 |    1.03607 |
| solution-flask     |     0.591749 |       1.00918  |    2.25318 |
| solution-1-flask   |     0.590896 |       1.00974  |    5.57105 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.581242 |       0.152952 |    4.55959 |
| solution-pl        |     0.587336 |       0.153332 |    4.69287 |
| solution-flask     |     0.564908 |       1.00953  |    8.87914 |