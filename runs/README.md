# 2025-04-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.508    |       1.00861  |   0.07918  |
| solution-pl        |     0.501598 |       0.122994 |   0.184098 |
| solution-aron-mark |     1.97234  |       0.128891 |   0.186313 |
| solution-1-flask   |     4.82841  |       1.10797  |   0.263896 |
| solution-1         |     6.99564  |       1e-06    |   0.588314 |
| solution-2         |     0.517064 |       0.54235  |   1.67727  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.51181  |       0.119233 |   0.286222 |
| solution-aron-mark |     0.510494 |       0.120493 |   0.290917 |
| solution-flask     |     0.500248 |       1.0086   |   0.291218 |
| solution-1-flask   |     0.506862 |       1.00886  |   0.794791 |
| solution-2         |     0.498073 |       0.495203 |   4.92405  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.506133 |       0.128556 |   0.895329 |
| solution-aron-mark |     0.504695 |       0.127131 |   0.89844  |
| solution-flask     |     0.509188 |       1.00869  |   1.24801  |
| solution-1-flask   |     0.506589 |       1.00901  |   5.70557  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.504165 |       0.155933 |    2.79847 |
| solution-aron-mark |     0.508634 |       0.156533 |    2.80661 |
| solution-flask     |     0.501457 |       1.00914  |    4.22546 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.502034 |       0.277282 |    16.1922 |
| solution-aron-mark |     0.500333 |       0.264933 |    16.2901 |