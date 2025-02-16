# 2025-02-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.528202 |       1.00884  |   0.080217 |
| solution-pl        |     1.78025  |       0.180979 |   0.202907 |
| solution-aron-mark |     0.558652 |       0.138795 |   0.203826 |
| solution-1-flask   |     5.02497  |       1.06103  |   0.275066 |
| solution-1         |     7.30109  |       1e-06    |   0.654737 |
| solution-2         |     0.530689 |       0.64184  |   1.00315  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.528367 |       1.00886  |   0.293399 |
| solution-pl        |     0.537311 |       0.144459 |   0.306806 |
| solution-aron-mark |     0.531071 |       0.142105 |   0.317993 |
| solution-1-flask   |     0.541329 |       1.00984  |   0.8074   |
| solution-2         |     0.53508  |       0.504833 |   3.13173  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.541038 |       0.147889 |   0.904602 |
| solution-pl        |     0.566828 |       0.148749 |   0.91179  |
| solution-flask     |     0.531979 |       1.00918  |   1.22472  |
| solution-1-flask   |     0.539383 |       1.00934  |   5.65977  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.532964 |       0.176888 |    2.81646 |
| solution-pl        |     0.529222 |       0.177424 |    2.85221 |
| solution-flask     |     0.537821 |       1.0091   |    4.2538  |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.53128  |       0.283746 |    16.8776 |
| solution-pl        |     0.529091 |       0.288492 |    17.1178 |