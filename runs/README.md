# 2025-02-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.535671 |       1.00882  |   0.080662 |
| solution-aron-mark |     0.536361 |       0.139405 |   0.203905 |
| solution-pl        |     1.76606  |       0.220977 |   0.207023 |
| solution-1-flask   |     5.2033   |       1.07295  |   0.264657 |
| solution-1         |     7.51328  |       1e-06    |   0.718083 |
| solution-2         |     0.555746 |       0.686336 |   1.04253  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.53351  |       1.0091   |   0.288931 |
| solution-aron-mark |     0.541203 |       0.142421 |   0.303481 |
| solution-pl        |     0.539783 |       0.141286 |   0.306059 |
| solution-1-flask   |     0.530333 |       1.00898  |   0.797195 |
| solution-2         |     0.528425 |       0.493628 |  13.4303   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.532768 |       0.149595 |   0.900442 |
| solution-aron-mark |     0.542398 |       0.149495 |   0.924172 |
| solution-flask     |     0.531552 |       1.00912  |   1.22862  |
| solution-1-flask   |     0.539123 |       1.00895  |   5.74691  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.530596 |       0.174307 |    2.84124 |
| solution-pl        |     0.535022 |       0.180993 |    2.88892 |
| solution-flask     |     0.534662 |       1.00876  |    4.16749 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.53395  |       0.275242 |    17.3403 |
| solution-aron-mark |     0.530245 |       0.277383 |    17.7764 |