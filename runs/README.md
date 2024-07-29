# 2024-07-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.525871 |       1.0095   |   0.097134 |
| solution-aron-mark |     0.497296 |       0.100787 |   0.166245 |
| solution-pl        |     5.76598  |       0.102309 |   0.169072 |
| solution-1-flask   |     1.0678   |       1.11485  |   0.257886 |
| solution-1         |     7.70806  |       1e-06    |   0.575818 |
| solution-2         |     0.519282 |       0.512872 |   1.00125  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.500195 |       1.00932  |   0.232135 |
| solution-aron-mark |     0.504056 |       0.103733 |   0.286497 |
| solution-pl        |     0.505536 |       0.103704 |   0.287811 |
| solution-1-flask   |     0.50598  |       1.00921  |   0.77498  |
| solution-2         |     0.499763 |       0.468673 |   4.32223  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.499205 |       1.00904  |   0.893691 |
| solution-pl        |     0.495707 |       0.111203 |   0.988491 |
| solution-aron-mark |     0.500048 |       0.11204  |   0.994258 |
| solution-1-flask   |     0.506827 |       1.0091   |   5.60122  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.498384 |       1.00959  |    4.24684 |
| solution-aron-mark |     0.506844 |       0.147669 |    4.26998 |
| solution-pl        |     0.518922 |       0.148566 |    4.35874 |