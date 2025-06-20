# 2025-06-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.511261 |       1.00821  |   0.102313 |
| solution-aron-mark |     5.85686  |       0.195766 |   0.242384 |
| solution-pl        |     0.509065 |       0.159428 |   0.244226 |
| solution-1-flask   |     1.14964  |       1.07812  |   0.271552 |
| solution-1         |     8.02932  |       1e-06    |   0.734169 |
| solution-2         |     0.532789 |       0.700003 |   1.02202  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.519731 |       0.154089 |   0.364763 |
| solution-pl        |     0.515152 |       0.153445 |   0.372109 |
| solution-flask     |     0.515285 |       1.00843  |   0.382488 |
| solution-1-flask   |     0.523742 |       1.00853  |   0.776582 |
| solution-2         |     0.516491 |       0.523282 |   5.00748  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.517704 |       0.160373 |    1.06675 |
| solution-pl        |     0.516728 |       0.160062 |    1.07703 |
| solution-flask     |     0.508936 |       1.00833  |    1.58252 |
| solution-1-flask   |     0.53764  |       1.00857  |    5.41335 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.511411 |       0.193782 |    3.3161  |
| solution-aron-mark |     0.523215 |       0.209521 |    3.36902 |
| solution-flask     |     0.508759 |       1.00864  |    5.20283 |