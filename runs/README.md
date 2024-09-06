# 2024-09-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |      1.63711 |       1.14485  |   0.119902 |
| solution-aron-mark |      5.98148 |       0.103931 |   0.170081 |
| solution-pl        |      1.03099 |       0.103981 |   0.174604 |
| solution-1-flask   |      1.02336 |       1.00877  |   0.262905 |
| solution-2         |      0.8285  |       0.830649 |   0.76068  |
| solution-1         |      7.9404  |       1e-06    |   1.0251   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.548183 |       1.00939  |   0.189549 |
| solution-aron-mark |     0.554971 |       0.105221 |   0.288359 |
| solution-pl        |     0.559806 |       0.104204 |   0.288951 |
| solution-1-flask   |     0.558827 |       1.009    |   0.768323 |
| solution-2         |     0.552312 |       0.47365  |   3.44917  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.551146 |       1.00916  |   0.882983 |
| solution-pl        |     0.550643 |       0.111761 |   0.992198 |
| solution-aron-mark |     0.553233 |       0.111514 |   0.993178 |
| solution-1-flask   |     0.558002 |       1.00904  |   5.50097  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.546275 |       1.00956  |    4.17268 |
| solution-aron-mark |     0.555481 |       0.146526 |    4.21683 |
| solution-pl        |     0.55367  |       0.146963 |    4.23581 |