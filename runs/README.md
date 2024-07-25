# 2024-07-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.508938 |       1.00929  |   0.091998 |
| solution-pl        |     5.73112  |       0.103105 |   0.166522 |
| solution-aron-mark |     0.518162 |       0.105815 |   0.171833 |
| solution-1-flask   |     1.07035  |       1.08728  |   0.263346 |
| solution-1         |     7.93247  |       1e-06    |   0.622817 |
| solution-2         |     0.527516 |       0.58317  |   1.00098  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.50383  |       1.00891  |   0.220608 |
| solution-aron-mark |     0.531257 |       0.103589 |   0.283455 |
| solution-pl        |     0.507035 |       0.10348  |   0.288522 |
| solution-1-flask   |     0.521845 |       1.00897  |   0.779058 |
| solution-2         |     0.520878 |       0.4892   |  12.7694   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.501346 |       1.00932  |   0.89207  |
| solution-aron-mark |     0.521976 |       0.115866 |   0.982333 |
| solution-pl        |     0.500931 |       0.111857 |   0.987391 |
| solution-1-flask   |     0.510611 |       1.0089   |   5.61566  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.495462 |       1.00954  |    4.28911 |
| solution-aron-mark |     0.503186 |       0.144793 |    4.34855 |
| solution-pl        |     0.501868 |       0.150155 |    4.41415 |