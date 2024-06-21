# 2024-06-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.694384 |       1.00924  |   0.076049 |
| solution-pl        |     0.678669 |       0.105412 |   0.162915 |
| solution-aron-mark |     6.02281  |       0.107593 |   0.164405 |
| solution-1-flask   |     1.40084  |       1.11123  |   0.261802 |
| solution-1         |     8.3563   |       1e-06    |   0.676633 |
| solution-2         |     0.682073 |       0.588796 |   1.12091  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.688955 |       1.00894  |   0.165777 |
| solution-aron-mark |     0.694309 |       0.107918 |   0.269262 |
| solution-pl        |     0.681796 |       0.107025 |   0.27047  |
| solution-1-flask   |     0.709927 |       1.00894  |   0.794896 |
| solution-2         |     0.716933 |       0.493749 |   2.1939   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.697658 |       1.00947  |   0.716022 |
| solution-pl        |     0.70524  |       0.114737 |   0.810801 |
| solution-aron-mark |     0.706257 |       0.118606 |   0.819651 |
| solution-1-flask   |     0.702832 |       1.00924  |   5.69917  |
| solution-2         |     0.696695 |       0.547918 | 153.836    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.688406 |       1.0091   |    2.63047 |
| solution-pl        |     0.690193 |       0.157651 |    2.74986 |
| solution-aron-mark |     0.696587 |       0.154163 |    2.78742 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.685886 |       1.00909  |    17.4181 |
| solution-aron-mark |     0.674016 |       0.278872 |    22.7553 |
| solution-pl        |     0.693233 |       0.278057 |    22.8335 |