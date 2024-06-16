# 2024-06-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.51369  |       1.06336  |   0.077622 |
| solution-pl        |     0.655594 |       0.102893 |   0.159117 |
| solution-aron-mark |     6.07956  |       0.102216 |   0.162374 |
| solution-1-flask   |     0.682406 |       1.00863  |   0.264423 |
| solution-1         |     8.2284   |       1e-06    |   0.580598 |
| solution-2         |     0.65339  |       0.506175 |   0.785154 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.667754 |       1.0094   |   0.161893 |
| solution-pl        |     0.676084 |       0.104061 |   0.257661 |
| solution-aron-mark |     0.670939 |       0.103764 |   0.266307 |
| solution-1-flask   |     0.684524 |       1.0095   |   0.800208 |
| solution-2         |     0.664947 |       0.474375 |   4.58522  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.670489 |       1.00901  |   0.704455 |
| solution-aron-mark |     0.670369 |       0.11487  |   0.804121 |
| solution-pl        |     0.67638  |       0.112863 |   0.81536  |
| solution-1-flask   |     0.675401 |       1.00914  |   5.57761  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.666471 |       1.00951  |    2.56019 |
| solution-pl        |     0.675314 |       0.153156 |    2.63407 |
| solution-aron-mark |     0.686194 |       0.153957 |    2.64282 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.671243 |       1.00927  |    16.1546 |
| solution-pl        |     0.679658 |       0.279097 |    22.0625 |
| solution-aron-mark |     0.669107 |       0.281351 |    22.476  |