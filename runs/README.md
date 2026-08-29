# 2026-08-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.88415  |        1.03818 |   0.106098 |
| solution-pl        |     0.428992 |        0.15739 |   0.240806 |
| solution-aron-mark |     4.61424  |        0.1544  |   0.260097 |
| solution-1-flask   |     0.4478   |        1.00814 |   0.284807 |
| solution-1         |     7.6947   |        1e-06   |   0.598903 |
| solution-2         |     0.430498 |        0.54239 |   0.87339  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.440602 |       0.153133 |   0.377727 |
| solution-aron-mark |     0.427492 |       0.156519 |   0.384907 |
| solution-flask     |     0.427016 |       1.0084   |   0.391968 |
| solution-1-flask   |     0.429042 |       1.0084   |   0.82224  |
| solution-2         |     0.432008 |       0.507468 |   2.68287  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.427782 |       0.163491 |    1.13698 |
| solution-pl        |     0.430138 |       0.162882 |    1.13901 |
| solution-flask     |     0.428672 |       1.00852  |    1.6562  |
| solution-1-flask   |     0.436808 |       1.00849  |    5.82182 |
| solution-2         |     0.429547 |       0.564471 |   28.0065  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.427761 |       0.187847 |    3.53802 |
| solution-pl        |     0.42737  |       0.186487 |    3.54809 |
| solution-flask     |     0.42755  |       1.00862  |    5.37851 |