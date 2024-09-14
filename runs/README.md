# 2024-09-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.28072  |       1.08289  |   0.096534 |
| solution-pl        |     0.587895 |       0.108047 |   0.19109  |
| solution-aron-mark |     5.97909  |       0.11368  |   0.197368 |
| solution-1-flask   |     0.596895 |       1.00923  |   0.271326 |
| solution-1         |     8.10877  |       2e-06    |   0.6257   |
| solution-2         |     0.591359 |       0.55191  |   0.929419 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.629174 |       1.00966  |   0.225873 |
| solution-pl        |     0.594228 |       0.109619 |   0.299068 |
| solution-aron-mark |     0.617417 |       0.113802 |   0.300742 |
| solution-1-flask   |     0.592465 |       1.00927  |   0.787732 |
| solution-2         |     0.588593 |       0.518768 |   3.05905  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.585453 |       1.00914  |   0.911903 |
| solution-pl        |     0.598439 |       0.119121 |   0.989779 |
| solution-aron-mark |     0.611367 |       0.118778 |   0.997363 |
| solution-1-flask   |     0.602654 |       1.0092   |   5.74043  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.594847 |       0.15094  |    4.84235 |
| solution-flask     |     0.60871  |       1.00921  |    5.07539 |
| solution-pl        |     0.60883  |       0.152576 |    5.09421 |