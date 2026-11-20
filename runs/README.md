# 2026-11-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.440777 |       1.01062  |   0.094776 |
| solution-pl        |     7.11263  |       0.170226 |   0.251384 |
| solution-aron-mark |     0.44283  |       0.171691 |   0.259991 |
| solution-1-flask   |     2.33194  |       1.04315  |   0.268484 |
| solution-1         |     8.68872  |       1e-06    |   0.620197 |
| solution-2         |     0.445933 |       0.571135 |   1.03749  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.447712 |       1.0107   |   0.22974  |
| solution-pl        |     0.461366 |       0.183775 |   0.394687 |
| solution-aron-mark |     0.468225 |       0.179263 |   0.394755 |
| solution-1-flask   |     0.44547  |       1.01082  |   0.803269 |
| solution-2         |     0.449795 |       0.552096 |   3.43194  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.427295 |       1.0109   |    1.01626 |
| solution-pl        |     0.433008 |       0.192286 |    1.13668 |
| solution-aron-mark |     0.437422 |       0.17909  |    1.13702 |
| solution-1-flask   |     0.437041 |       1.01103  |    5.52076 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.437698 |       0.216082 |    3.55839 |
| solution-aron-mark |     0.435177 |       0.208711 |    3.62545 |
| solution-flask     |     0.453659 |       1.01109  |    4.41631 |