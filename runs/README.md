# 2024-12-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.80752  |       1.00869  |   0.10608  |
| solution-pl        |     0.53724  |       0.108866 |   0.184542 |
| solution-aron-mark |     0.560129 |       0.10948  |   0.189207 |
| solution-1-flask   |     4.91934  |       1.06846  |   0.270175 |
| solution-1         |     7.45943  |       1e-06    |   0.594361 |
| solution-2         |     0.540057 |       0.525597 |   0.69999  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.535634 |       0.108824 |   0.314122 |
| solution-aron-mark |     0.534122 |       0.108757 |   0.315575 |
| solution-flask     |     0.536542 |       1.00875  |   0.503387 |
| solution-1-flask   |     0.542215 |       1.00899  |   0.815851 |
| solution-2         |     0.542293 |       0.486032 |   4.01212  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.532197 |       0.116601 |    1.06835 |
| solution-aron-mark |     0.529359 |       0.115331 |    1.07236 |
| solution-flask     |     0.533331 |       1.00882  |    2.25881 |
| solution-1-flask   |     0.539708 |       1.00899  |    5.8688  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.532969 |       0.148482 |    4.41818 |
| solution-aron-mark |     0.543527 |       0.145527 |    4.44069 |
| solution-flask     |     0.537819 |       1.00927  |    8.95357 |