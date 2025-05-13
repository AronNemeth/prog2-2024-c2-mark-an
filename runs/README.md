# 2025-05-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.792648 |       1.00853  |   0.08149  |
| solution-pl        |     0.948812 |       0.121284 |   0.188361 |
| solution-aron-mark |     2.27691  |       0.12112  |   0.192947 |
| solution-1-flask   |     1.65249  |       1.05338  |   0.265825 |
| solution-1         |     8.28674  |       1e-06    |   0.868499 |
| solution-2         |     5.07115  |       0.895614 |   1.54667  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.472963 |       0.12157  |   0.293926 |
| solution-flask     |     0.468997 |       1.00882  |   0.294465 |
| solution-pl        |     0.462368 |       0.126295 |   0.30769  |
| solution-1-flask   |     0.513817 |       1.00899  |   0.786989 |
| solution-2         |     0.514345 |       0.571477 |   4.81871  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.481328 |       0.128658 |   0.886214 |
| solution-aron-mark |     0.466917 |       0.131103 |   0.924799 |
| solution-flask     |     0.460514 |       1.00888  |   1.24971  |
| solution-1-flask   |     0.472715 |       1.00904  |   5.37621  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.464233 |        0.15958 |    2.80214 |
| solution-aron-mark |     0.462346 |        0.1599  |    2.81543 |
| solution-flask     |     0.463798 |        1.00867 |    4.17165 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.460006 |       0.275432 |    15.7756 |
| solution-aron-mark |     0.462656 |       0.273208 |    15.8046 |