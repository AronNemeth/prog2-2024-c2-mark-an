# 2024-08-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.578527 |       1.00929  |   0.092535 |
| solution-aron-mark |     1.78695  |       0.105207 |   0.186104 |
| solution-pl        |     0.594879 |       0.109075 |   0.187003 |
| solution-1-flask   |     1.0786   |       1.05219  |   0.262747 |
| solution-1         |     7.49499  |       1e-06    |   0.585268 |
| solution-2         |     4.4723   |       0.532521 |   1.52445  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.568137 |       1.00917  |   0.226594 |
| solution-aron-mark |     0.56206  |       0.105797 |   0.294837 |
| solution-pl        |     0.564477 |       0.108809 |   0.296788 |
| solution-1-flask   |     0.587834 |       1.00895  |   0.795438 |
| solution-2         |     0.569188 |       0.512099 |   3.05014  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.555203 |       1.00923  |   0.914114 |
| solution-aron-mark |     0.569418 |       0.112405 |   1.02256  |
| solution-pl        |     0.564269 |       0.116815 |   1.03277  |
| solution-1-flask   |     0.580569 |       1.00951  |   5.55349  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.5794   |       1.00956  |    4.40854 |
| solution-pl        |     0.562304 |       0.144373 |    4.4536  |
| solution-aron-mark |     0.57643  |       0.153242 |    4.58378 |