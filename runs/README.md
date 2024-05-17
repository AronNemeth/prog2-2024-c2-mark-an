# 2024-05-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.57687  |       1.12215  |   0.073282 |
| solution-pl        |     0.64908  |       0.117287 |   0.172745 |
| solution-aron-mark |     5.93102  |       0.182199 |   0.175561 |
| solution-1-flask   |     0.671185 |       1.00957  |   0.258104 |
| solution-1         |     8.15501  |       1e-06    |   0.575405 |
| solution-2         |     0.655798 |       0.415963 |   1.22741  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.656441 |       1.00935  |   0.161199 |
| solution-aron-mark |     0.662635 |       0.125985 |   0.269584 |
| solution-pl        |     0.660166 |       0.125032 |   0.274003 |
| solution-1-flask   |     0.679708 |       1.00871  |   0.782344 |
| solution-2         |     0.660326 |       0.419917 |   4.98757  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.657793 |       1.00882  |   0.672689 |
| solution-aron-mark |     0.657565 |       0.131363 |   0.811771 |
| solution-pl        |     0.669103 |       0.132415 |   0.828866 |
| solution-1-flask   |     0.674484 |       1.00887  |   5.49308  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.664224 |       1.00883  |    2.4441  |
| solution-pl        |     0.665147 |       0.16587  |    2.58812 |
| solution-aron-mark |     0.657575 |       0.167109 |    2.63864 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.654702 |       1.00922  |    14.9892 |
| solution-aron-mark |     0.660137 |       0.295055 |    15.3942 |
| solution-pl        |     0.660034 |       0.294373 |    15.5611 |