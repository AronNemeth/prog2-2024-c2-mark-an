# 2024-10-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.0727   |       1.08392  |   0.08611  |
| solution-pl        |     0.553804 |       0.101041 |   0.176318 |
| solution-aron-mark |     1.79599  |       0.101255 |   0.176555 |
| solution-1-flask   |     0.574365 |       1.00812  |   0.286943 |
| solution-1         |     7.49222  |       1e-06    |   0.719146 |
| solution-2         |     4.31867  |       0.515867 |   0.949804 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.562794 |       1.00819  |   0.210436 |
| solution-pl        |     0.562374 |       0.104511 |   0.305478 |
| solution-aron-mark |     0.557857 |       0.102107 |   0.306888 |
| solution-1-flask   |     0.564924 |       1.00806  |   0.779398 |
| solution-2         |     0.568623 |       0.468762 |   3.2004   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.549921 |       1.00819  |   0.987871 |
| solution-pl        |     0.551786 |       0.108805 |   1.04953  |
| solution-aron-mark |     0.557628 |       0.110807 |   1.07668  |
| solution-1-flask   |     0.563255 |       1.00796  |   5.44335  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.566782 |       1.00803  |    4.06292 |
| solution-pl        |     0.555777 |       0.13811  |    4.14629 |
| solution-aron-mark |     0.558436 |       0.138557 |    4.20704 |