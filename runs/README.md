# 2025-05-31

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.85597  |       1.00823  |   0.098372 |
| solution-aron-mark |     0.505415 |       0.147007 |   0.230443 |
| solution-pl        |     0.503412 |       0.149457 |   0.235089 |
| solution-1-flask   |     5.64801  |       1.09156  |   0.271487 |
| solution-1         |     8.23605  |       1e-06    |   0.684962 |
| solution-2         |     0.517359 |       0.626828 |   1.29413  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.502788 |       0.150759 |   0.354065 |
| solution-aron-mark |     0.502602 |       0.149408 |   0.354694 |
| solution-flask     |     0.50981  |       1.00838  |   0.376799 |
| solution-1-flask   |     0.508657 |       1.00854  |   0.793134 |
| solution-2         |     0.503006 |       0.530491 |   3.28617  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.501378 |       0.156096 |    1.05424 |
| solution-pl        |     0.508289 |       0.157019 |    1.05451 |
| solution-flask     |     0.529871 |       1.00847  |    1.58297 |
| solution-1-flask   |     0.508987 |       1.00854  |    5.40812 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.499476 |       0.191651 |    3.18695 |
| solution-pl        |     0.500687 |       0.186265 |    3.18789 |
| solution-flask     |     0.502977 |       1.00854  |    5.00735 |