# 2024-06-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.48154  |       1.04296  |   0.077338 |
| solution-pl        |     0.652748 |       0.102114 |   0.160047 |
| solution-aron-mark |     6.00206  |       0.102967 |   0.1615   |
| solution-1-flask   |     0.67976  |       1.00941  |   0.264961 |
| solution-1         |     8.16673  |       1e-06    |   0.655452 |
| solution-2         |     0.648949 |       0.420856 |   0.761938 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.663014 |       1.00896  |   0.15912  |
| solution-aron-mark |     0.665698 |       0.103684 |   0.252328 |
| solution-pl        |     0.669035 |       0.106903 |   0.254416 |
| solution-1-flask   |     0.67463  |       1.00934  |   0.770568 |
| solution-2         |     0.656243 |       0.435379 |  21.6016   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.661321 |       1.00907  |   0.72239  |
| solution-aron-mark |     0.668024 |       0.113727 |   0.812535 |
| solution-pl        |     0.663571 |       0.11381  |   0.812628 |
| solution-1-flask   |     0.678819 |       1.00934  |   5.61093  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.661654 |       1.00912  |    2.50554 |
| solution-aron-mark |     0.673098 |       0.153255 |    2.64658 |
| solution-pl        |     0.660866 |       0.153496 |    2.65296 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.689599 |       1.00933  |    15.7917 |
| solution-aron-mark |     0.664611 |       0.2836   |    21.868  |
| solution-pl        |     0.666464 |       0.283412 |    22.7322 |