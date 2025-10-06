# 2025-10-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.48178  |       1.04947  |   0.101758 |
| solution-pl        |     0.488671 |       0.158029 |   0.241855 |
| solution-aron-mark |     0.498715 |       0.155103 |   0.242709 |
| solution-1-flask   |     0.505383 |       1.00839  |   0.265602 |
| solution-1         |     7.63988  |       1e-06    |   0.762436 |
| solution-2         |     4.47152  |       0.887672 |   0.874587 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.494177 |       0.162349 |   0.370083 |
| solution-aron-mark |     0.498255 |       0.163738 |   0.370829 |
| solution-flask     |     0.497437 |       1.00838  |   0.384088 |
| solution-1-flask   |     0.502291 |       1.00829  |   0.804633 |
| solution-2         |     0.488481 |       0.513858 |   4.61814  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.493574 |       0.168997 |    1.0813  |
| solution-pl        |     0.496913 |       0.170381 |    1.09503 |
| solution-flask     |     0.496036 |       1.0085   |    1.58007 |
| solution-1-flask   |     0.496813 |       1.00853  |    5.63553 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.492119 |       0.198601 |    3.29444 |
| solution-pl        |     0.488467 |       0.199524 |    3.34585 |
| solution-flask     |     0.490266 |       1.00849  |    5.14356 |