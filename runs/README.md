# 2026-01-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.70399  |       1.1144   |   0.105965 |
| solution-pl        |     0.476024 |       0.165331 |   0.252351 |
| solution-aron-mark |     0.496237 |       0.171542 |   0.254303 |
| solution-1-flask   |     0.506552 |       1.0091   |   0.288244 |
| solution-2         |     4.61167  |       0.770595 |   0.821881 |
| solution-1         |     7.87285  |       1e-06    |   0.869408 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.46512  |       1.00868  |   0.373577 |
| solution-aron-mark |     0.47074  |       0.16739  |   0.374353 |
| solution-pl        |     0.483017 |       0.164949 |   0.376141 |
| solution-1-flask   |     0.47227  |       1.00833  |   0.782578 |
| solution-2         |     0.473799 |       0.523683 |   7.37099  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.474457 |        0.17369 |    1.0717  |
| solution-pl        |     0.473579 |        0.17195 |    1.08233 |
| solution-flask     |     0.472097 |        1.00876 |    1.61593 |
| solution-1-flask   |     0.483736 |        1.00866 |    5.8187  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.485104 |       0.204587 |    3.76315 |
| solution-pl        |     0.481897 |       0.203048 |    3.78638 |
| solution-flask     |     0.470703 |       1.0088   |    5.29438 |