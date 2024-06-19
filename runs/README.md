# 2024-06-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.703885 |       1.0094   |   0.073853 |
| solution-pl        |     0.665024 |       0.104787 |   0.161757 |
| solution-aron-mark |     5.9257   |       0.103843 |   0.162464 |
| solution-1-flask   |     1.43249  |       1.08962  |   0.263238 |
| solution-2         |     0.664751 |       0.56997  |   0.787795 |
| solution-1         |     8.35522  |       1e-06    |   0.849432 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.6788   |       1.00899  |   0.164493 |
| solution-aron-mark |     0.666202 |       0.105204 |   0.256156 |
| solution-pl        |     0.672194 |       0.104833 |   0.257273 |
| solution-1-flask   |     0.68278  |       1.00887  |   0.789335 |
| solution-2         |     0.679826 |       0.474389 |   2.86453  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.664127 |       1.00927  |   0.710907 |
| solution-aron-mark |     0.6786   |       0.115959 |   0.812389 |
| solution-pl        |     0.667253 |       0.114827 |   0.813884 |
| solution-1-flask   |     0.684433 |       1.00914  |   5.47486  |
| solution-2         |     0.66464  |       0.524178 | 171.138    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.662684 |       1.00917  |    2.4828  |
| solution-pl        |     0.669559 |       0.153596 |    2.61144 |
| solution-aron-mark |     0.668896 |       0.154438 |    2.612   |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.661927 |       1.00921  |    17.8914 |
| solution-pl        |     0.666457 |       0.280032 |    23.1701 |
| solution-aron-mark |     0.664278 |       0.278872 |    23.4627 |