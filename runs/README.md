# 2025-09-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.48415  |       1.00826  |   0.098442 |
| solution-aron-mark |     0.474551 |       0.151648 |   0.236116 |
| solution-pl        |     5.64119  |       0.187364 |   0.237886 |
| solution-1-flask   |     1.04952  |       1.15171  |   0.26533  |
| solution-1         |     7.24841  |       1e-06    |   0.787907 |
| solution-2         |     0.483344 |       0.677188 |   1.45955  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.479937 |       0.154913 |   0.364201 |
| solution-aron-mark |     0.481573 |       0.154865 |   0.364644 |
| solution-flask     |     0.483126 |       1.00845  |   0.372173 |
| solution-1-flask   |     0.491497 |       1.00846  |   0.799704 |
| solution-2         |     0.485782 |       0.499336 |   4.10926  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.481495 |       0.161352 |    1.05885 |
| solution-pl        |     0.480224 |       0.160982 |    1.05956 |
| solution-flask     |     0.481962 |       1.00872  |    1.53956 |
| solution-1-flask   |     0.483749 |       1.00875  |    5.5953  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.481219 |       0.190304 |    3.2227  |
| solution-aron-mark |     0.480352 |       0.199408 |    3.23008 |
| solution-flask     |     0.479327 |       1.00856  |    5.09818 |