# 2025-12-31

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.55879  |       1.05419  |   0.097814 |
| solution-pl        |     0.470948 |       0.160849 |   0.242182 |
| solution-aron-mark |     0.483665 |       0.161555 |   0.246177 |
| solution-1-flask   |     0.47989  |       1.00807  |   0.260193 |
| solution-1         |     7.63546  |       1e-06    |   0.637105 |
| solution-2         |     4.64118  |       0.646125 |   1.44562  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.473406 |       0.162682 |   0.369073 |
| solution-flask     |     0.473883 |       1.00851  |   0.38652  |
| solution-aron-mark |     0.477258 |       0.16305  |   0.397431 |
| solution-1-flask   |     0.478383 |       1.00849  |   0.780571 |
| solution-2         |     0.471448 |       0.51708  |   4.00628  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.4774   |       0.171481 |    1.06708 |
| solution-aron-mark |     0.472993 |       0.172786 |    1.06931 |
| solution-flask     |     0.468162 |       1.00866  |    1.56917 |
| solution-1-flask   |     0.490821 |       1.00868  |    5.45767 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.471685 |       0.191104 |    3.46705 |
| solution-pl        |     0.471541 |       0.194233 |    3.51369 |
| solution-flask     |     0.485443 |       1.00863  |    5.03105 |