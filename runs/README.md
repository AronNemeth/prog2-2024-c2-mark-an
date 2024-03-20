# 2024-03-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.77928  |       1.0612   |   0.067894 |
| solution-aron-mark |     0.657198 |       0.111459 |   0.165196 |
| solution-pl        |     0.658771 |       0.109788 |   0.16534  |
| solution-1-flask   |     0.677867 |       1.00892  |   0.262406 |
| solution-1         |     8.27636  |       1e-06    |   0.703184 |
| solution-2         |     4.74103  |       0.506626 |   0.825234 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.670365 |       1.00848  |   0.171646 |
| solution-aron-mark |     0.6546   |       0.115544 |   0.255448 |
| solution-pl        |     0.655988 |       0.115313 |   0.257943 |
| solution-1-flask   |     0.687176 |       1.00851  |   0.782585 |
| solution-2         |     0.705167 |       0.449452 |   6.36873  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.667462 |        0.12134 |   0.806424 |
| solution-pl        |     0.654399 |        0.12197 |   0.812119 |
| solution-flask     |     0.652281 |        1.00878 |   0.920807 |
| solution-1-flask   |     0.668097 |        1.00867 |   5.50542  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.654828 |       0.15694  |    3.30073 |
| solution-aron-mark |     0.652134 |       0.158038 |    3.31805 |
| solution-flask     |     0.648937 |       1.00862  |    5.39164 |