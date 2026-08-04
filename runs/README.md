# 2026-08-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.45445  |       1.00896  |   0.109334 |
| solution-pl        |     0.51844  |       0.166978 |   0.272753 |
| solution-1-flask   |     1.50135  |       1.08549  |   0.284692 |
| solution-aron-mark |     0.539222 |       0.186986 |   0.303838 |
| solution-1         |     8.52199  |       2e-06    |   0.740331 |
| solution-2         |     4.65593  |       0.741307 |   1.2033   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.492953 |       0.16883  |   0.404678 |
| solution-aron-mark |     0.511905 |       0.174094 |   0.40649  |
| solution-flask     |     0.488074 |       1.00907  |   0.425344 |
| solution-1-flask   |     0.49892  |       1.00914  |   0.895717 |
| solution-2         |     0.50275  |       0.618625 |   3.44477  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.497168 |       0.169938 |    1.16571 |
| solution-pl        |     0.485371 |       0.174685 |    1.17674 |
| solution-flask     |     0.534015 |       1.00996  |    1.79305 |
| solution-1-flask   |     0.507257 |       1.00948  |    6.51765 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.492608 |       0.196263 |    4.3938  |
| solution-aron-mark |     0.493546 |       0.199124 |    4.43159 |
| solution-flask     |     0.485074 |       1.00878  |    6.01217 |