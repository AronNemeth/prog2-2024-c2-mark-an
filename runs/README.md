# 2026-07-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.43382  |       1.1281   |   0.110361 |
| solution-pl        |     6.46922  |       0.16987  |   0.23916  |
| solution-aron-mark |     0.43293  |       0.151067 |   0.241873 |
| solution-1-flask   |     0.432264 |       1.00851  |   0.275287 |
| solution-1         |     7.89448  |       1e-06    |   0.664203 |
| solution-2         |     0.421212 |       0.600539 |   1.10107  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.430067 |       0.156453 |   0.378309 |
| solution-aron-mark |     0.441095 |       0.153311 |   0.381422 |
| solution-flask     |     0.442287 |       1.00852  |   0.407609 |
| solution-1-flask   |     0.440654 |       1.00837  |   0.81544  |
| solution-2         |     0.424589 |       0.507299 |   7.8837   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.438886 |       0.158159 |    1.14751 |
| solution-pl        |     0.445446 |       0.159743 |    1.1552  |
| solution-flask     |     0.428192 |       1.00882  |    1.72788 |
| solution-1-flask   |     0.454301 |       1.00908  |    5.76212 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.44004  |       0.185993 |    4.18849 |
| solution-pl        |     0.433204 |       0.184773 |    4.1976  |
| solution-flask     |     0.43132  |       1.00897  |    5.57527 |