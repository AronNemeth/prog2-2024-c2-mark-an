# 2025-02-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.1808   |       1.07006  |   0.084706 |
| solution-pl        |     4.67129  |       0.138685 |   0.205448 |
| solution-aron-mark |     0.538864 |       0.138055 |   0.206699 |
| solution-1-flask   |     0.547876 |       1.00897  |   0.265991 |
| solution-1         |     7.89269  |       1e-06    |   0.669858 |
| solution-2         |     0.539692 |       0.618649 |   0.822334 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.540796 |       1.00942  |   0.295987 |
| solution-aron-mark |     0.544848 |       0.141868 |   0.309976 |
| solution-pl        |     0.565149 |       0.141809 |   0.310386 |
| solution-1-flask   |     0.5465   |       1.00883  |   0.814522 |
| solution-2         |     0.54961  |       0.506117 |   5.66648  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.543148 |       0.149164 |   0.90694  |
| solution-pl        |     0.542135 |       0.147614 |   0.911818 |
| solution-flask     |     0.537546 |       1.00908  |   1.25466  |
| solution-1-flask   |     0.546766 |       1.00898  |   5.76498  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.538279 |       0.176879 |    2.83736 |
| solution-pl        |     0.561121 |       0.178555 |    2.85291 |
| solution-flask     |     0.537351 |       1.01013  |    4.24491 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.539326 |       0.281938 |    17.4772 |
| solution-aron-mark |     0.541552 |       0.284801 |    17.6128 |