# 2026-02-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.5483   |       1.06591  |   0.102098 |
| solution-pl        |     0.447041 |       0.19399  |   0.253663 |
| solution-aron-mark |     0.449124 |       0.169762 |   0.254695 |
| solution-1-flask   |     0.45068  |       1.0084   |   0.264166 |
| solution-1         |     7.5869   |       1e-06    |   0.714934 |
| solution-2         |     4.51415  |       0.693788 |   1.09481  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.447659 |       0.168517 |   0.386239 |
| solution-flask     |     0.449449 |       1.0084   |   0.387048 |
| solution-aron-mark |     0.461351 |       0.172113 |   0.391089 |
| solution-1-flask   |     0.451741 |       1.00863  |   0.813249 |
| solution-2         |     0.451772 |       0.522991 |   2.37109  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.446358 |       0.175653 |    1.12334 |
| solution-pl        |     0.461968 |       0.174027 |    1.12771 |
| solution-flask     |     0.445972 |       1.00857  |    1.58038 |
| solution-1-flask   |     0.45568  |       1.00867  |    5.5328  |
| solution-2         |     0.448567 |       0.564174 |   40.5155  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.451612 |       0.201381 |    3.87262 |
| solution-aron-mark |     0.449223 |       0.20213  |    3.94647 |
| solution-flask     |     0.460904 |       1.00856  |    5.13724 |