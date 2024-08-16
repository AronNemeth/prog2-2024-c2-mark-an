# 2024-08-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.592567 |       1.00931  |   0.100971 |
| solution-pl        |     0.578609 |       0.10612  |   0.180174 |
| solution-aron-mark |     2.16292  |       0.107891 |   0.193358 |
| solution-1-flask   |     1.43905  |       1.09256  |   0.266898 |
| solution-1         |     8.4795   |       1e-06    |   0.610312 |
| solution-2         |     4.85426  |       0.540194 |   1.04775  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.605266 |       1.00909  |   0.227724 |
| solution-aron-mark |     0.576625 |       0.108904 |   0.296521 |
| solution-pl        |     0.585528 |       0.108282 |   0.296651 |
| solution-1-flask   |     0.585041 |       1.00896  |   0.77437  |
| solution-2         |     0.58091  |       0.500418 |   2.86672  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.572416 |       1.00903  |    1.01904 |
| solution-aron-mark |     0.578625 |       0.115871 |    1.02903 |
| solution-pl        |     0.582707 |       0.113557 |    1.03112 |
| solution-1-flask   |     0.579765 |       1.00917  |    5.7126  |
| solution-2         |     0.589122 |       0.563826 |   30.3628  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.569771 |       1.00904  |    4.58251 |
| solution-aron-mark |     0.577893 |       0.149097 |    4.6819  |
| solution-pl        |     0.57388  |       0.151114 |    4.84309 |