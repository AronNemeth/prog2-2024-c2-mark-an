# 2026-06-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.16653  |       1.11003  |   0.100973 |
| solution-pl        |     0.696137 |       0.133749 |   0.20754  |
| solution-aron-mark |     0.389031 |       0.134227 |   0.209175 |
| solution-1-flask   |     0.392998 |       1.00652  |   0.234792 |
| solution-1         |     7.2949   |       1e-06    |   0.614355 |
| solution-2         |     4.64565  |       0.71494  |   0.896723 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.386006 |       0.134743 |   0.319542 |
| solution-pl        |     0.387023 |       0.136991 |   0.331226 |
| solution-flask     |     0.384281 |       1.00658  |   0.423777 |
| solution-1-flask   |     0.39109  |       1.00665  |   0.720684 |
| solution-2         |     0.38276  |       0.469748 |   3.87568  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.389436 |       0.142429 |   0.997556 |
| solution-pl        |     0.402167 |       0.142281 |   1.0086   |
| solution-flask     |     0.384567 |       1.00679  |   1.81307  |
| solution-1-flask   |     0.388441 |       1.00641  |   5.35573  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.391727 |       0.172163 |    4.76088 |
| solution-aron-mark |     0.385599 |       0.169522 |    4.81066 |
| solution-flask     |     0.438861 |       1.00661  |    5.94965 |