# 2025-06-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.85142  |       1.00799  |   0.098751 |
| solution-aron-mark |     0.500395 |       0.14582  |   0.229763 |
| solution-pl        |     0.500288 |       0.146019 |   0.231615 |
| solution-1-flask   |     5.02633  |       1.09192  |   0.265346 |
| solution-1         |     7.95692  |       1e-06    |   0.654058 |
| solution-2         |     0.497706 |       0.644204 |   1.0756   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.496447 |       0.148324 |   0.348333 |
| solution-pl        |     0.497754 |       0.147488 |   0.353903 |
| solution-flask     |     0.493375 |       1.00829  |   0.362944 |
| solution-1-flask   |     0.504672 |       1.00846  |   0.798064 |
| solution-2         |     0.492979 |       0.499984 |   5.56658  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.494288 |       0.154717 |    1.03554 |
| solution-pl        |     0.498065 |       0.158051 |    1.03894 |
| solution-flask     |     0.495503 |       1.0085   |    1.53642 |
| solution-1-flask   |     0.531584 |       1.00851  |    5.39048 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.49574  |       0.184563 |    3.13043 |
| solution-aron-mark |     0.493868 |       0.189414 |    3.14922 |
| solution-flask     |     0.491676 |       1.00833  |    4.92869 |