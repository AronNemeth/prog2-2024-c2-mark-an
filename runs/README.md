# 2024-05-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.31004  |       1.06808  |   0.073504 |
| solution-aron-mark |     5.84564  |       0.126314 |   0.175508 |
| solution-pl        |     0.656074 |       0.120554 |   0.177117 |
| solution-1-flask   |     0.678406 |       1.0089   |   0.268147 |
| solution-1         |     7.95782  |       1e-06    |   0.601192 |
| solution-2         |     0.655407 |       0.419445 |   1.01179  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.665796 |       1.00899  |   0.160574 |
| solution-pl        |     0.671378 |       0.127074 |   0.269027 |
| solution-aron-mark |     0.668575 |       0.126247 |   0.276587 |
| solution-1-flask   |     0.67217  |       1.00887  |   0.781642 |
| solution-2         |     0.659216 |       0.433846 |   2.70202  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.686547 |       1.00948  |   0.699293 |
| solution-pl        |     0.671906 |       0.131519 |   0.814346 |
| solution-aron-mark |     0.686246 |       0.132816 |   0.818864 |
| solution-1-flask   |     0.678838 |       1.00929  |   5.54691  |
| solution-2         |     0.664263 |       0.478731 | 168.787    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.666549 |       1.00986  |    2.4777  |
| solution-aron-mark |     0.671466 |       0.172705 |    2.6029  |
| solution-pl        |     0.662999 |       0.171142 |    2.62824 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.659438 |       1.00963  |    15.233  |
| solution-pl        |     0.663672 |       0.294501 |    15.2624 |
| solution-aron-mark |     0.661907 |       0.293463 |    15.7338 |