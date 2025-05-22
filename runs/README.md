# 2025-05-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.00621  |       1.00822  |   0.098153 |
| solution-aron-mark |     0.502997 |       0.147596 |   0.227289 |
| solution-pl        |     0.49917  |       0.148728 |   0.229091 |
| solution-1-flask   |     5.7043   |       1.06052  |   0.2758   |
| solution-1         |     8.01146  |       1e-06    |   0.669321 |
| solution-2         |     0.496065 |       0.591417 |   0.897156 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.497942 |       0.149925 |   0.347578 |
| solution-aron-mark |     0.500498 |       0.150465 |   0.353339 |
| solution-flask     |     0.497632 |       1.00823  |   0.374288 |
| solution-1-flask   |     0.504144 |       1.00919  |   0.791666 |
| solution-2         |     0.50887  |       0.518873 |   2.41345  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.499621 |       0.154787 |    1.06137 |
| solution-aron-mark |     0.496277 |       0.155272 |    1.06139 |
| solution-flask     |     0.500481 |       1.00849  |    1.55009 |
| solution-1-flask   |     0.504838 |       1.00883  |    5.41714 |
| solution-2         |     0.502202 |       0.558156 |   44.3289  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.496752 |       0.189368 |    3.16602 |
| solution-pl        |     0.49418  |       0.184918 |    3.16991 |
| solution-flask     |     0.499452 |       1.00851  |    5.07758 |