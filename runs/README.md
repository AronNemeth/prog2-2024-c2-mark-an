# 2024-11-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.21621  |       1.05842  |   0.108876 |
| solution-aron-mark |     0.556066 |       0.108478 |   0.179019 |
| solution-pl        |     5.64012  |       0.109011 |   0.191427 |
| solution-1-flask   |     0.562704 |       1.00919  |   0.254286 |
| solution-1         |     7.59534  |       1e-06    |   0.69127  |
| solution-2         |     0.549657 |       0.599371 |   1.04273  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.553967 |       0.109084 |   0.298223 |
| solution-aron-mark |     0.561869 |       0.107685 |   0.300691 |
| solution-flask     |     0.556653 |       1.00936  |   0.478175 |
| solution-1-flask   |     0.563015 |       1.00908  |   0.772573 |
| solution-2         |     0.555701 |       0.474642 |   2.60037  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.552324 |       0.115622 |    1.00518 |
| solution-aron-mark |     0.554187 |       0.117636 |    1.02448 |
| solution-flask     |     0.553712 |       1.00905  |    2.10805 |
| solution-1-flask   |     0.560992 |       1.00897  |    5.50794 |
| solution-2         |     0.552545 |       0.522142 |   27.6292  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.556644 |       0.145982 |    4.22613 |
| solution-pl        |     0.558678 |       0.145549 |    4.25821 |
| solution-flask     |     0.550204 |       1.00901  |    8.18417 |