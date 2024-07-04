# 2024-07-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.508016 |       1.00878  |   0.077447 |
| solution-aron-mark |     5.78909  |       0.099703 |   0.164498 |
| solution-pl        |     0.48846  |       0.099708 |   0.166173 |
| solution-1-flask   |     1.19058  |       1.11155  |   0.260568 |
| solution-1         |     7.85756  |       1e-06    |   0.735634 |
| solution-2         |     0.488342 |       0.520545 |   1.45417  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.515582 |       1.00918  |   0.223535 |
| solution-aron-mark |     0.512115 |       0.105379 |   0.281847 |
| solution-pl        |     0.499483 |       0.101586 |   0.284878 |
| solution-1-flask   |     0.492283 |       1.009    |   0.784166 |
| solution-2         |     0.496587 |       0.468396 |   3.33233  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.497516 |       1.00895  |   0.88673  |
| solution-aron-mark |     0.521721 |       0.110105 |   0.9948   |
| solution-pl        |     0.497628 |       0.115728 |   0.997797 |
| solution-1-flask   |     0.504892 |       1.00902  |   5.6427   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.493361 |       1.00943  |    4.07969 |
| solution-aron-mark |     0.49822  |       0.154319 |    4.10849 |
| solution-pl        |     0.491849 |       0.141656 |    4.138   |