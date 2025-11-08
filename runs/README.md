# 2025-11-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.52095  |       1.13147  |   0.103548 |
| solution-pl        |     0.481334 |       0.161971 |   0.244061 |
| solution-aron-mark |     0.482992 |       0.167336 |   0.247432 |
| solution-1-flask   |     0.493814 |       1.00819  |   0.26461  |
| solution-1         |     7.65523  |       1e-06    |   0.749646 |
| solution-2         |     4.56367  |       0.773984 |   0.858052 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.481257 |       0.159819 |   0.369207 |
| solution-aron-mark |     0.473738 |       0.162677 |   0.372504 |
| solution-flask     |     0.483749 |       1.00846  |   0.374539 |
| solution-1-flask   |     0.48451  |       1.0086   |   0.814234 |
| solution-2         |     0.479361 |       0.521616 |   2.87483  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.470842 |       0.16441  |    1.07296 |
| solution-aron-mark |     0.468499 |       0.165232 |    1.07522 |
| solution-flask     |     0.479661 |       1.00865  |    1.5664  |
| solution-1-flask   |     0.480218 |       1.00849  |    5.56208 |
| solution-2         |     0.479619 |       0.576232 |  175.611   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.469242 |       0.197143 |    3.21334 |
| solution-pl        |     0.472227 |       0.196389 |    3.24889 |
| solution-flask     |     0.464691 |       1.00868  |    5.09513 |