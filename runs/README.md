# 2025-01-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.83473  |       1.00891  |   0.103557 |
| solution-pl        |     0.527694 |       0.110949 |   0.186846 |
| solution-aron-mark |     0.529254 |       0.109659 |   0.189748 |
| solution-1-flask   |     5.21871  |       1.0667   |   0.269429 |
| solution-1         |     7.867    |       1e-06    |   0.589277 |
| solution-2         |     0.527355 |       0.645098 |   1.34639  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.521837 |       0.111652 |   0.317601 |
| solution-pl        |     0.539079 |       0.114479 |   0.32044  |
| solution-flask     |     0.528374 |       1.00862  |   0.485638 |
| solution-1-flask   |     0.541017 |       1.00883  |   0.79491  |
| solution-2         |     0.525179 |       0.485324 |   2.79417  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.53097  |       0.119283 |    1.06534 |
| solution-aron-mark |     0.531375 |       0.139388 |    1.14386 |
| solution-flask     |     0.533582 |       1.00896  |    2.14456 |
| solution-1-flask   |     0.534477 |       1.00904  |    5.7784  |
| solution-2         |     0.526213 |       0.540803 |   35.413   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.526254 |       0.146959 |    4.35341 |
| solution-pl        |     0.53788  |       0.145737 |    4.36926 |
| solution-flask     |     0.538738 |       1.00866  |    8.51435 |