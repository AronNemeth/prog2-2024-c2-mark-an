# 2026-06-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.60987  |       1.02804  |   0.106007 |
| solution-pl        |     6.34547  |       0.17222  |   0.230627 |
| solution-aron-mark |     0.437905 |       0.150466 |   0.236144 |
| solution-1-flask   |     0.438519 |       1.00827  |   0.315446 |
| solution-1         |     8.18349  |       1e-06    |   0.672813 |
| solution-2         |     0.417006 |       0.67749  |   2.41362  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.423307 |       0.151426 |   0.372649 |
| solution-pl        |     0.450649 |       0.153429 |   0.375309 |
| solution-flask     |     0.431593 |       1.00863  |   0.415821 |
| solution-1-flask   |     0.429686 |       1.00868  |   0.824344 |
| solution-2         |     0.442799 |       0.51792  |   5.37731  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.431864 |       0.158111 |    1.13294 |
| solution-pl        |     0.432497 |       0.156977 |    1.14862 |
| solution-flask     |     0.426689 |       1.00844  |    1.70208 |
| solution-1-flask   |     0.435126 |       1.00879  |    5.80887 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.436432 |       0.183963 |    4.12667 |
| solution-pl        |     0.430532 |       0.184898 |    4.13094 |
| solution-flask     |     0.432154 |       1.00823  |    5.58928 |