# 2025-12-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.74307  |       1.10601  |   0.103138 |
| solution-aron-mark |     0.509438 |       0.168746 |   0.250967 |
| solution-pl        |     0.500175 |       0.17064  |   0.25449  |
| solution-1-flask   |     0.494416 |       1.0083   |   0.289758 |
| solution-2         |     4.55284  |       0.869292 |   0.728966 |
| solution-1         |     7.72767  |       1e-06    |   1.31367  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.506576 |       0.170337 |   0.374104 |
| solution-flask     |     0.505836 |       1.00851  |   0.380124 |
| solution-aron-mark |     0.492123 |       0.168239 |   0.381048 |
| solution-1-flask   |     0.489649 |       1.00868  |   0.811058 |
| solution-2         |     0.49556  |       0.555806 |   2.96416  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.476429 |       0.168741 |    1.06791 |
| solution-aron-mark |     0.489004 |       0.174861 |    1.07611 |
| solution-flask     |     0.475965 |       1.00846  |    1.55822 |
| solution-1-flask   |     0.477331 |       1.00893  |    5.63694 |
| solution-2         |     0.479828 |       0.591262 |  164.194   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.4787   |       0.194407 |    3.73624 |
| solution-aron-mark |     0.47553  |       0.203746 |    3.83703 |
| solution-flask     |     0.473578 |       1.00853  |    5.11235 |