# 2026-10-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.0362   |       1.13786  |   0.095082 |
| solution-pl        |     0.377783 |       0.138795 |   0.208702 |
| solution-1-flask   |     0.390306 |       1.00664  |   0.225189 |
| solution-aron-mark |     6.08473  |       0.272362 |   0.239423 |
| solution-1         |     6.93172  |       1e-06    |   0.762467 |
| solution-2         |     0.389967 |       0.995382 |   1.2321   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.381984 |       0.139792 |   0.312223 |
| solution-aron-mark |     0.392719 |       0.183012 |   0.32239  |
| solution-flask     |     0.379844 |       1.00708  |   0.362266 |
| solution-1-flask   |     0.38956  |       1.00702  |   0.692884 |
| solution-2         |     0.387074 |       0.490188 |  11.1924   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.385006 |       0.146708 |   0.968033 |
| solution-aron-mark |     0.386246 |       0.145614 |   0.981379 |
| solution-flask     |     0.385283 |       1.00714  |   1.55943  |
| solution-1-flask   |     0.389519 |       1.00719  |   5.49909  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.380241 |       0.169832 |    3.79908 |
| solution-aron-mark |     0.390472 |       0.168287 |    3.80441 |
| solution-flask     |     0.380455 |       1.00725  |    5.14518 |