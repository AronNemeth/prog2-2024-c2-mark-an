# 2026-07-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.30344  |       1.00733  |   0.116834 |
| solution-1-flask   |     2.27388  |       1.08896  |   0.177078 |
| solution-pl        |     0.35162  |       0.125279 |   0.183764 |
| solution-aron-mark |     0.353805 |       0.122698 |   0.184686 |
| solution-1         |     7.19625  |       0        |   0.591553 |
| solution-2         |     4.60591  |       1.26957  |   0.988602 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.35603  |       0.123226 |   0.281986 |
| solution-pl        |     0.347324 |       0.126714 |   0.282505 |
| solution-flask     |     0.348755 |       1.00761  |   0.307084 |
| solution-1-flask   |     0.358248 |       1.00757  |   0.568215 |
| solution-2         |     0.35723  |       0.422512 |   3.26185  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.349095 |       0.127506 |   0.814428 |
| solution-aron-mark |     0.35071  |       0.131487 |   0.818641 |
| solution-flask     |     0.364898 |       1.00775  |   1.29228  |
| solution-1-flask   |     0.350956 |       1.0078   |   4.44464  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.348843 |       0.14779  |    2.86128 |
| solution-aron-mark |     0.356476 |       0.148498 |    2.88498 |
| solution-flask     |     0.36893  |       1.00745  |    4.27586 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.347651 |       0.210584 |    17.242  |
| solution-pl        |     0.366651 |       0.207719 |    17.6041 |