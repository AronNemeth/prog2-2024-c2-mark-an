# 2024-03-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.4697   |       1.09556  |   0.066163 |
| solution-aron-mark |     0.661158 |       0.10953  |   0.164817 |
| solution-pl        |     0.690551 |       0.115394 |   0.165838 |
| solution-1-flask   |     0.672424 |       1.009    |   0.264624 |
| solution-1         |     7.97788  |       1e-06    |   0.906541 |
| solution-2         |     4.58473  |       0.52103  |   0.954916 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.661132 |       1.0088   |   0.16993  |
| solution-aron-mark |     0.661166 |       0.114579 |   0.256629 |
| solution-pl        |     0.67661  |       0.113907 |   0.259959 |
| solution-1-flask   |     0.668334 |       1.00876  |   0.775396 |
| solution-2         |     0.660604 |       0.444599 |  12.0736   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.666656 |       0.120238 |   0.820472 |
| solution-aron-mark |     0.661522 |       0.120798 |   0.823717 |
| solution-flask     |     0.674509 |       1.0088   |   0.922059 |
| solution-1-flask   |     0.67202  |       1.00892  |   5.57562  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.674536 |       0.15589  |    3.33883 |
| solution-pl        |     0.671057 |       0.155445 |    3.34742 |
| solution-flask     |     0.657326 |       1.00925  |    5.33964 |