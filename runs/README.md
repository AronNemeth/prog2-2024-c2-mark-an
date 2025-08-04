# 2025-08-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.44916  |       1.07792  |   0.099168 |
| solution-aron-mark |     4.4163   |       0.150334 |   0.236813 |
| solution-pl        |     0.509307 |       0.152691 |   0.238383 |
| solution-1-flask   |     0.520982 |       1.00836  |   0.266025 |
| solution-1         |     7.50391  |       1e-06    |   0.86357  |
| solution-2         |     0.50436  |       0.788092 |   1.34114  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.501578 |       0.153748 |   0.361841 |
| solution-flask     |     0.509269 |       1.00851  |   0.379162 |
| solution-aron-mark |     0.509452 |       0.153668 |   0.383711 |
| solution-1-flask   |     0.511944 |       1.0086   |   0.799577 |
| solution-2         |     0.497263 |       0.514215 |  13.2775   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.514298 |       0.16124  |    1.06296 |
| solution-pl        |     0.507293 |       0.161547 |    1.07665 |
| solution-flask     |     0.513151 |       1.00862  |    1.57458 |
| solution-1-flask   |     0.512764 |       1.00839  |    5.65332 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.504332 |       0.190227 |    3.23702 |
| solution-aron-mark |     0.509259 |       0.195287 |    3.27241 |
| solution-flask     |     0.511409 |       1.00858  |    5.09543 |