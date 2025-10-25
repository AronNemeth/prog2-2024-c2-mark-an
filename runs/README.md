# 2025-10-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.44584  |       1.06292  |   0.096434 |
| solution-pl        |     0.482175 |       0.152027 |   0.234442 |
| solution-aron-mark |     0.481904 |       0.153652 |   0.235341 |
| solution-1-flask   |     0.482302 |       1.00803  |   0.266506 |
| solution-1         |     7.79679  |       1e-06    |   0.669336 |
| solution-2         |     4.73083  |       0.688237 |   1.14081  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.480886 |       0.154093 |   0.358904 |
| solution-aron-mark |     0.478123 |       0.154032 |   0.364774 |
| solution-flask     |     0.476888 |       1.00825  |   0.3751   |
| solution-1-flask   |     0.481441 |       1.00971  |   0.794054 |
| solution-2         |     0.476707 |       0.4937   |   2.14526  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.479492 |       0.161952 |    1.05269 |
| solution-aron-mark |     0.477445 |       0.161    |    1.06176 |
| solution-flask     |     0.47781  |       1.00809  |    1.54973 |
| solution-1-flask   |     0.483468 |       1.0081   |    5.57203 |
| solution-2         |     0.474095 |       0.548272 |   41.4158  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.475899 |       0.192297 |    3.20515 |
| solution-aron-mark |     0.477956 |       0.191246 |    3.23338 |
| solution-flask     |     0.479293 |       1.00818  |    5.00541 |