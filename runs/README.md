# 2024-06-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.663949 |       1.0091   |   0.072394 |
| solution-aron-mark |     5.88596  |       0.103245 |   0.157209 |
| solution-pl        |     0.653259 |       0.101435 |   0.158561 |
| solution-1-flask   |     1.29337  |       1.10915  |   0.254848 |
| solution-1         |     7.97763  |       1e-06    |   0.750535 |
| solution-2         |     0.657902 |       0.779644 |   1.72655  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.662815 |       1.00862  |   0.160812 |
| solution-pl        |     0.663775 |       0.104165 |   0.256996 |
| solution-aron-mark |     0.666411 |       0.103194 |   0.262731 |
| solution-1-flask   |     0.680587 |       1.00883  |   0.784542 |
| solution-2         |     0.660746 |       0.460964 |   3.30484  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.662966 |       1.00885  |   0.711431 |
| solution-aron-mark |     0.677323 |       0.1134   |   0.809602 |
| solution-pl        |     0.664524 |       0.112095 |   0.818605 |
| solution-1-flask   |     0.683383 |       1.00914  |   5.50878  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.658758 |       1.00915  |    2.4993  |
| solution-pl        |     0.666401 |       0.15392  |    2.58675 |
| solution-aron-mark |     0.672539 |       0.152552 |    2.61378 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.665436 |       1.0087   |    15.3917 |
| solution-pl        |     0.664098 |       0.279255 |    21.3516 |
| solution-aron-mark |     0.661897 |       0.278472 |    21.5785 |