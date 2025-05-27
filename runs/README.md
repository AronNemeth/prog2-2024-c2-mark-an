# 2025-05-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.81847  |       1.00803  |   0.096267 |
| solution-aron-mark |     0.489172 |       0.145386 |   0.229194 |
| solution-pl        |     0.490443 |       0.145148 |   0.230981 |
| solution-1-flask   |     5.04984  |       1.06314  |   0.262588 |
| solution-1         |     8.74449  |       1e-06    |   0.72577  |
| solution-2         |     0.488575 |       0.661803 |   1.13239  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.4934   |       0.148997 |   0.346713 |
| solution-pl        |     0.490166 |       0.144986 |   0.351961 |
| solution-flask     |     0.492736 |       1.00821  |   0.381276 |
| solution-1-flask   |     0.501896 |       1.00825  |   0.769971 |
| solution-2         |     0.487815 |       0.491918 |  11.3605   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.49406  |       0.1528   |    1.03598 |
| solution-aron-mark |     0.492528 |       0.153145 |    1.04361 |
| solution-flask     |     0.493296 |       1.00825  |    1.5382  |
| solution-1-flask   |     0.496028 |       1.00824  |    5.38992 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.491738 |       0.186301 |    3.10118 |
| solution-pl        |     0.49718  |       0.185881 |    3.11012 |
| solution-flask     |     0.488493 |       1.00834  |    4.90213 |