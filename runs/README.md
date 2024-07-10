# 2024-07-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.31591  |       1.05525  |   0.093152 |
| solution-pl        |     6.01263  |       0.103454 |   0.167779 |
| solution-aron-mark |     0.523541 |       0.103304 |   0.169915 |
| solution-1-flask   |     0.527066 |       1.00932  |   0.259434 |
| solution-1         |     8.25257  |       1e-06    |   0.872391 |
| solution-2         |     0.523228 |       0.781461 |   1.55539  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.509089 |       1.00909  |   0.193524 |
| solution-pl        |     0.500379 |       0.105742 |   0.28744  |
| solution-aron-mark |     0.506823 |       0.103901 |   0.288732 |
| solution-1-flask   |     0.550632 |       1.00894  |   0.794612 |
| solution-2         |     0.506316 |       0.471372 |   2.56989  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.515149 |       1.00915  |   0.897243 |
| solution-pl        |     0.520043 |       0.114275 |   0.981463 |
| solution-aron-mark |     0.515785 |       0.115837 |   0.998257 |
| solution-1-flask   |     0.520405 |       1.00914  |   5.55541  |
| solution-2         |     0.515273 |       0.542595 | 163.607    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.517462 |       0.146975 |    4.28928 |
| solution-pl        |     0.509416 |       0.149635 |    4.33171 |
| solution-flask     |     0.505769 |       1.00931  |    4.44134 |