# 2025-06-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.52296  |       1.00845  |   0.098103 |
| solution-aron-mark |     6.03034  |       0.189229 |   0.2331   |
| solution-pl        |     0.50465  |       0.153711 |   0.238902 |
| solution-1-flask   |     1.28429  |       1.05645  |   0.266149 |
| solution-1         |     8.05445  |       1e-06    |   0.91081  |
| solution-2         |     0.532232 |       0.86461  |   1.52214  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.516209 |       0.161937 |   0.358947 |
| solution-aron-mark |     0.513655 |       0.155638 |   0.365435 |
| solution-flask     |     0.522344 |       1.00841  |   0.375465 |
| solution-1-flask   |     0.527025 |       1.00839  |   0.824027 |
| solution-2         |     0.526382 |       0.537247 |   2.20486  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.513487 |       0.163869 |    1.04964 |
| solution-pl        |     0.517237 |       0.162507 |    1.06236 |
| solution-flask     |     0.526171 |       1.00867  |    1.57883 |
| solution-1-flask   |     0.549114 |       1.00897  |    5.49899 |
| solution-2         |     0.516988 |       0.585795 |   30.6364  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.508266 |       0.191381 |    3.22925 |
| solution-aron-mark |     0.513536 |       0.194982 |    3.28118 |
| solution-flask     |     0.506469 |       1.00862  |    5.03318 |