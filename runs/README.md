# 2024-08-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.564104 |       1.00913  |   0.087581 |
| solution-aron-mark |     1.90219  |       0.103796 |   0.174454 |
| solution-pl        |     0.5551   |       0.105057 |   0.190088 |
| solution-1-flask   |     1.32365  |       1.06977  |   0.258219 |
| solution-1         |     7.72723  |       1e-06    |   0.565958 |
| solution-2         |     4.59326  |       0.497368 |   1.34578  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.550298 |       1.00898  |   0.230506 |
| solution-aron-mark |     0.558165 |       0.126786 |   0.29896  |
| solution-pl        |     0.551638 |       0.103307 |   0.312701 |
| solution-1-flask   |     0.553141 |       1.00906  |   0.767076 |
| solution-2         |     0.546602 |       0.468034 |   3.06635  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.548388 |       1.00919  |   0.905864 |
| solution-pl        |     0.589128 |       0.113029 |   1.01039  |
| solution-aron-mark |     0.546029 |       0.111686 |   1.01299  |
| solution-1-flask   |     0.558244 |       1.0088   |   5.5636   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.550401 |       1.00893  |    4.11707 |
| solution-pl        |     0.545464 |       0.142795 |    4.23785 |
| solution-aron-mark |     0.556975 |       0.142989 |    4.50017 |