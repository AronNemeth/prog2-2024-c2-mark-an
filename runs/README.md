# 2024-11-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.20839  |       1.11078  |   0.109426 |
| solution-pl        |     5.8439   |       0.109342 |   0.17748  |
| solution-aron-mark |     0.549278 |       0.107841 |   0.177678 |
| solution-1-flask   |     0.559118 |       1.00944  |   0.255911 |
| solution-1         |     7.61988  |       1e-06    |   0.624037 |
| solution-2         |     0.552502 |       0.487178 |   1.17246  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.553457 |       0.108949 |   0.294491 |
| solution-pl        |     0.583137 |       0.111113 |   0.32957  |
| solution-flask     |     0.575481 |       1.0091   |   0.484239 |
| solution-1-flask   |     0.562574 |       1.00907  |   0.76299  |
| solution-2         |     0.555822 |       0.465097 |  10.8104   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.554484 |       0.115572 |    1.01454 |
| solution-pl        |     0.552071 |       0.11629  |    1.04533 |
| solution-flask     |     0.554975 |       1.00931  |    2.12753 |
| solution-1-flask   |     0.566942 |       1.00892  |    5.37201 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.579976 |       0.147127 |    4.28744 |
| solution-aron-mark |     0.555392 |       0.150487 |    4.36593 |
| solution-flask     |     0.552661 |       1.00931  |    8.25508 |