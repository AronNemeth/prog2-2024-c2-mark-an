# 2024-11-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.1493   |       1.01206  |   0.114292 |
| solution-aron-mark |     0.582305 |       0.111541 |   0.182095 |
| solution-pl        |     6.21655  |       0.118366 |   0.182144 |
| solution-1-flask   |     0.589149 |       1.00906  |   0.259544 |
| solution-1         |     7.71241  |       1e-06    |   0.613421 |
| solution-2         |     0.576331 |       0.537564 |   1.15814  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.583521 |       0.113014 |   0.307339 |
| solution-pl        |     0.593143 |       0.111431 |   0.312135 |
| solution-flask     |     0.5842   |       1.00938  |   0.488156 |
| solution-1-flask   |     0.599454 |       1.00941  |   0.780607 |
| solution-2         |     0.582743 |       0.509304 |   2.92254  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.574234 |       0.117305 |    1.0326  |
| solution-aron-mark |     0.579519 |       0.120193 |    1.03493 |
| solution-flask     |     0.579134 |       1.00942  |    2.16838 |
| solution-1-flask   |     0.572033 |       1.00906  |    5.45501 |
| solution-2         |     0.573014 |       0.532212 |   37.7151  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.567321 |       0.149742 |    4.52699 |
| solution-pl        |     0.585741 |       0.152152 |    4.66871 |
| solution-flask     |     0.572459 |       1.00973  |    8.93509 |