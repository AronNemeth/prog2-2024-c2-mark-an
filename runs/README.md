# 2026-03-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.88824  |       1.0559   |   0.109226 |
| solution-pl        |     5.57237  |       0.148236 |   0.237718 |
| solution-aron-mark |     0.470854 |       0.152761 |   0.245297 |
| solution-1-flask   |     0.454832 |       1.00999  |   0.265715 |
| solution-1         |     8.11405  |       1e-06    |   0.763124 |
| solution-2         |     0.457448 |       0.681056 |   0.873094 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.45827  |       0.150406 |   0.37828  |
| solution-flask     |     0.477523 |       1.00896  |   0.397258 |
| solution-pl        |     0.461018 |       0.148888 |   0.405286 |
| solution-1-flask   |     0.456811 |       1.00905  |   0.794014 |
| solution-2         |     0.466007 |       0.524357 |   5.51524  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.46098  |       0.155726 |    1.13969 |
| solution-pl        |     0.480217 |       0.157867 |    1.14495 |
| solution-flask     |     0.457599 |       1.00926  |    1.66819 |
| solution-1-flask   |     0.493879 |       1.00905  |    5.69314 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.455886 |       0.186096 |    3.97537 |
| solution-aron-mark |     0.46693  |       0.192497 |    4.03647 |
| solution-flask     |     0.457742 |       1.00881  |    5.42254 |