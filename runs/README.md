# 2026-03-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.55703  |       1.06123  |   0.108713 |
| solution-pl        |     5.21039  |       0.146975 |   0.23626  |
| solution-aron-mark |     0.91164  |       0.150242 |   0.237773 |
| solution-1-flask   |     0.910097 |       1.00962  |   0.265437 |
| solution-1         |     9.43145  |       1e-06    |   0.64301  |
| solution-2         |     0.903355 |       0.653749 |   1.04157  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.445639 |       0.170205 |   0.372417 |
| solution-aron-mark |     0.450978 |       0.152279 |   0.373712 |
| solution-flask     |     0.448347 |       1.00895  |   0.395113 |
| solution-1-flask   |     0.454079 |       1.00892  |   0.799421 |
| solution-2         |     0.445444 |       0.507436 |   4.79672  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.447969 |       0.156597 |    1.13738 |
| solution-aron-mark |     0.446523 |       0.157135 |    1.14718 |
| solution-flask     |     0.447029 |       1.00911  |    1.63134 |
| solution-1-flask   |     0.450375 |       1.00917  |    5.6424  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.449158 |       0.183714 |    3.92826 |
| solution-aron-mark |     0.449133 |       0.183211 |    3.98768 |
| solution-flask     |     0.447263 |       1.00901  |    5.22935 |