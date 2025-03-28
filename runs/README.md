# 2025-03-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.514889 |       1.00901  |   0.081941 |
| solution-pl        |     0.508384 |       0.11939  |   0.185621 |
| solution-aron-mark |     2.21897  |       0.122791 |   0.186458 |
| solution-1-flask   |     5.46926  |       1.05934  |   0.270525 |
| solution-1         |     7.87482  |       1e-06    |   0.597281 |
| solution-2         |     0.514452 |       0.559112 |   1.20685  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.50785  |       0.120606 |   0.28574  |
| solution-pl        |     0.511805 |       0.120613 |   0.288789 |
| solution-flask     |     0.506718 |       1.00879  |   0.313107 |
| solution-1-flask   |     0.514028 |       1.0092   |   0.768563 |
| solution-2         |     0.515069 |       0.506175 |  22.2789   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.512217 |       0.129521 |   0.898968 |
| solution-pl        |     0.512347 |       0.135376 |   0.899705 |
| solution-flask     |     0.510336 |       1.0091   |   1.25595  |
| solution-1-flask   |     0.516223 |       1.0093   |   5.68871  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.524711 |       0.158568 |    2.80663 |
| solution-aron-mark |     0.508778 |       0.161571 |    2.8088  |
| solution-flask     |     0.508362 |       1.00864  |    4.15855 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.506042 |       0.269654 |     16.712 |
| solution-pl        |     0.506653 |       0.264596 |     16.948 |