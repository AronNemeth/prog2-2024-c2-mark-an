# 2026-04-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.61404  |       1.06704  |   0.098127 |
| solution-pl        |     0.410957 |       0.145906 |   0.22316  |
| solution-aron-mark |     4.8385   |       0.144992 |   0.224785 |
| solution-1-flask   |     0.411819 |       1.00788  |   0.260251 |
| solution-1         |     9.37169  |       1e-06    |   0.672723 |
| solution-2         |     0.406619 |       0.606192 |   1.18154  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.41727  |       0.147779 |   0.345649 |
| solution-aron-mark |     0.411729 |       0.146617 |   0.34915  |
| solution-flask     |     0.409526 |       1.00827  |   0.367139 |
| solution-1-flask   |     0.417841 |       1.00825  |   0.794834 |
| solution-2         |     0.407077 |       0.497095 |   4.65282  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.408713 |       0.151915 |    1.04132 |
| solution-pl        |     0.409697 |       0.153525 |    1.04231 |
| solution-flask     |     0.409585 |       1.008    |    1.51343 |
| solution-1-flask   |     0.413666 |       1.0083   |    5.60198 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.407884 |       0.181482 |    3.62834 |
| solution-pl        |     0.408971 |       0.179942 |    3.68984 |
| solution-flask     |     0.406401 |       1.00826  |    5.02663 |