# 2026-06-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.17411  |       1.05267  |   0.098743 |
| solution-pl        |     6.16458  |       0.177379 |   0.231379 |
| solution-1-flask   |     0.441742 |       1.00863  |   0.232136 |
| solution-aron-mark |     0.450824 |       0.150264 |   0.242697 |
| solution-1         |     7.67345  |       1e-06    |   0.616946 |
| solution-2         |     0.431313 |       0.607883 |   0.967908 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.440144 |       0.154961 |   0.354192 |
| solution-pl        |     0.436881 |       0.156937 |   0.356359 |
| solution-flask     |     0.438148 |       1.00925  |   0.392274 |
| solution-1-flask   |     0.463691 |       1.00893  |   0.706876 |
| solution-2         |     0.446557 |       0.525741 |  11.4535   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.436146 |       0.158876 |    1.04266 |
| solution-aron-mark |     0.433268 |       0.159447 |    1.04482 |
| solution-flask     |     0.465459 |       1.00914  |    1.67785 |
| solution-1-flask   |     0.448355 |       1.00906  |    5.52851 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.435691 |       0.18365  |    3.83203 |
| solution-pl        |     0.435967 |       0.187001 |    4.02637 |
| solution-flask     |     0.445048 |       1.00941  |    5.3949  |