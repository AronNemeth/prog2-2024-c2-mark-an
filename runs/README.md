# 2026-05-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.5895   |       1.14613  |   0.1128   |
| solution-aron-mark |     0.423054 |       0.151425 |   0.238948 |
| solution-pl        |     0.433455 |       0.153665 |   0.239787 |
| solution-1-flask   |     0.435814 |       1.00805  |   0.272122 |
| solution-1         |     7.29596  |       1e-06    |   0.78443  |
| solution-2         |     4.23421  |       0.885589 |   0.83115  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.430024 |       0.151205 |   0.372736 |
| solution-pl        |     0.466802 |       0.152943 |   0.376609 |
| solution-flask     |     0.429437 |       1.00797  |   0.407499 |
| solution-1-flask   |     0.431504 |       1.00807  |   0.81899  |
| solution-2         |     0.428102 |       0.503356 |   1.80687  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.429088 |       0.157554 |    1.12605 |
| solution-aron-mark |     0.427178 |       0.157094 |    1.15066 |
| solution-flask     |     0.42546  |       1.00862  |    1.70469 |
| solution-1-flask   |     0.427566 |       1.00841  |    5.6673  |
| solution-2         |     0.425247 |       0.555475 |  167.762   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.438048 |       0.184951 |    4.04229 |
| solution-pl        |     0.429415 |       0.189636 |    4.08097 |
| solution-flask     |     0.428733 |       1.00816  |    5.43431 |