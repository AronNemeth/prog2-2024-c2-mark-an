# 2025-02-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.547082 |       1.00872  |   0.084585 |
| solution-aron-mark |     2.24946  |       0.150278 |   0.206248 |
| solution-pl        |     0.548217 |       0.146172 |   0.211581 |
| solution-1-flask   |     5.66885  |       1.06361  |   0.263087 |
| solution-1         |     7.91493  |       1e-06    |   0.595327 |
| solution-2         |     0.545785 |       0.547322 |   1.12586  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.535874 |       1.00864  |   0.292924 |
| solution-aron-mark |     0.53812  |       0.144594 |   0.309331 |
| solution-pl        |     0.555912 |       0.142616 |   0.310549 |
| solution-1-flask   |     0.547931 |       1.00883  |   0.80401  |
| solution-2         |     0.541811 |       0.512627 |   3.16995  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.537161 |       0.152864 |   0.924668 |
| solution-aron-mark |     0.541916 |       0.150597 |   0.931967 |
| solution-flask     |     0.543563 |       1.00886  |   1.23968  |
| solution-1-flask   |     0.548955 |       1.00885  |   5.73628  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.541542 |       0.180545 |    2.86133 |
| solution-aron-mark |     0.540694 |       0.179503 |    2.89344 |
| solution-flask     |     0.537746 |       1.00882  |    4.314   |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.542352 |       0.277782 |    16.6526 |
| solution-pl        |     0.534985 |       0.282222 |    16.7532 |