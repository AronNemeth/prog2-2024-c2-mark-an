# 2026-10-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.09133  |       1.04414  |   0.073491 |
| solution-1-flask   |     0.357627 |       1.00775  |   0.182443 |
| solution-aron-mark |     5.81966  |       0.165075 |   0.196104 |
| solution-pl        |     0.346273 |       0.137238 |   0.209925 |
| solution-1         |     6.67408  |       1e-06    |   0.511524 |
| solution-2         |     0.350235 |       0.624279 |   0.865873 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.382307 |       1.00822  |   0.176658 |
| solution-aron-mark |     0.358955 |       0.139308 |   0.306597 |
| solution-pl        |     0.352179 |       0.140165 |   0.310614 |
| solution-1-flask   |     0.388905 |       1.00778  |   0.587099 |
| solution-2         |     0.339645 |       0.41311  |   2.35904  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.353574 |       1.00849  |   0.770042 |
| solution-pl        |     0.362198 |       0.144483 |   0.859786 |
| solution-aron-mark |     0.422209 |       0.153348 |   0.874724 |
| solution-1-flask   |     0.389685 |       1.00788  |   4.30465  |
| solution-2         |     0.361198 |       0.508689 |  44.5853   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.347152 |       0.166642 |    2.79673 |
| solution-aron-mark |     0.371864 |       0.168587 |    2.86217 |
| solution-flask     |     0.342888 |       1.0077   |    3.3195  |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.340038 |       0.238595 |    17.3249 |
| solution-pl        |     0.350655 |       0.228207 |    18.1155 |