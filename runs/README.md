# 2025-09-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.484485 |       1.0079   |   0.104321 |
| solution-pl        |     5.63999  |       0.324586 |   0.239136 |
| solution-aron-mark |     0.473468 |       0.153201 |   0.241893 |
| solution-1-flask   |     1.07464  |       1.05152  |   0.279165 |
| solution-1         |     7.39634  |       1e-06    |   0.713366 |
| solution-2         |     0.475453 |       0.639021 |   0.862516 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.48105  |       0.155194 |   0.367226 |
| solution-pl        |     0.478681 |       0.153239 |   0.370274 |
| solution-flask     |     0.481884 |       1.00808  |   0.383129 |
| solution-1-flask   |     0.483801 |       1.00838  |   0.803929 |
| solution-2         |     0.482091 |       0.497583 |   2.5206   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.480588 |       0.161434 |    1.09325 |
| solution-aron-mark |     0.47931  |       0.161211 |    1.09944 |
| solution-flask     |     0.48699  |       1.00856  |    1.60762 |
| solution-1-flask   |     0.48563  |       1.0084   |    5.72889 |
| solution-2         |     0.481378 |       0.552467 |  166.902   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.48146  |        0.19383 |    3.27386 |
| solution-pl        |     0.483643 |        0.19047 |    3.30296 |
| solution-flask     |     0.481571 |        1.0085  |    5.20265 |