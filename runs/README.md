# 2024-07-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.21265  |       1.07846  |   0.096686 |
| solution-pl        |     5.87573  |       0.102343 |   0.167172 |
| solution-aron-mark |     0.505329 |       0.100881 |   0.16931  |
| solution-1-flask   |     0.503192 |       1.00908  |   0.257992 |
| solution-1         |     7.92212  |       1e-06    |   0.616919 |
| solution-2         |     0.498947 |       0.514365 |   0.958838 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.496875 |       1.00867  |   0.226312 |
| solution-aron-mark |     0.495664 |       0.103533 |   0.285252 |
| solution-pl        |     0.494906 |       0.102035 |   0.286677 |
| solution-1-flask   |     0.502199 |       1.00913  |   0.771319 |
| solution-2         |     0.492881 |       0.469049 |   5.77183  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.493837 |       1.00883  |   0.89173  |
| solution-aron-mark |     0.495811 |       0.111799 |   0.991787 |
| solution-pl        |     0.496504 |       0.111332 |   0.99759  |
| solution-1-flask   |     0.49888  |       1.00875  |   5.53571  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.496071 |       1.00931  |    4.09607 |
| solution-pl        |     0.495378 |       0.149884 |    4.17894 |
| solution-aron-mark |     0.494149 |       0.1487   |    4.243   |