# 2025-09-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.47949  |       1.00805  |   0.099541 |
| solution-aron-mark |     0.474805 |       0.150424 |   0.237385 |
| solution-pl        |     5.73919  |       0.159939 |   0.238989 |
| solution-1-flask   |     1.0988   |       1.11709  |   0.264555 |
| solution-1         |     7.44853  |       1e-06    |   0.603323 |
| solution-2         |     0.477982 |       0.544641 |   1.13934  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.481825 |       0.153668 |   0.360792 |
| solution-aron-mark |     0.483534 |       0.155376 |   0.36623  |
| solution-flask     |     0.495095 |       1.00838  |   0.381176 |
| solution-1-flask   |     0.482736 |       1.00842  |   0.799365 |
| solution-2         |     0.47841  |       0.498433 |   2.82083  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.476793 |       0.159925 |    1.07885 |
| solution-pl        |     0.482418 |       0.159354 |    1.0823  |
| solution-flask     |     0.476086 |       1.00837  |    1.57693 |
| solution-1-flask   |     0.502057 |       1.00824  |    5.681   |
| solution-2         |     0.479448 |       0.553691 |  173.065   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.477008 |       0.190141 |    3.23062 |
| solution-aron-mark |     0.480098 |       0.191527 |    3.24652 |
| solution-flask     |     0.483366 |       1.00839  |    5.10485 |