# 2026-04-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.69351  |       1.03323  |   0.094072 |
| solution-pl        |     0.412848 |       0.143924 |   0.220728 |
| solution-aron-mark |     7.62814  |       0.144209 |   0.222987 |
| solution-1-flask   |     0.41194  |       1.0086   |   0.226961 |
| solution-1         |     9.14572  |       1e-06    |   0.584002 |
| solution-2         |     0.40328  |       0.543833 |   1.01949  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.424715 |       0.146856 |   0.332247 |
| solution-pl        |     0.405179 |       0.149763 |   0.334379 |
| solution-flask     |     0.406053 |       1.00865  |   0.367004 |
| solution-1-flask   |     0.408647 |       1.00856  |   0.713816 |
| solution-2         |     0.404591 |       0.492019 |   2.88827  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.405836 |       0.152012 |   0.968066 |
| solution-pl        |     0.40606  |       0.154294 |   0.971904 |
| solution-flask     |     0.412976 |       1.00878  |   1.52153  |
| solution-1-flask   |     0.408655 |       1.00892  |   5.45386  |
| solution-2         |     0.405893 |       0.552956 | 178.752    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.407645 |       0.179164 |    3.49906 |
| solution-pl        |     0.40754  |       0.178998 |    3.50519 |
| solution-flask     |     0.405505 |       1.00884  |    4.80437 |