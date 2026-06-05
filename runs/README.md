# 2026-06-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.28248  |       1.05884  |   0.108331 |
| solution-aron-mark |     0.449372 |       0.152746 |   0.235797 |
| solution-pl        |     0.435788 |       0.152698 |   0.23767  |
| solution-1-flask   |     0.440032 |       1.00803  |   0.268076 |
| solution-1         |     7.82536  |       1e-06    |   0.627692 |
| solution-2         |     4.62567  |       0.597952 |   1.0196   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.438115 |       0.15548  |   0.375579 |
| solution-pl        |     0.447798 |       0.15163  |   0.382702 |
| solution-flask     |     0.427158 |       1.00812  |   0.405085 |
| solution-1-flask   |     0.432652 |       1.00806  |   0.821704 |
| solution-2         |     0.443359 |       0.519908 |   2.83162  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.435633 |       0.153472 |    1.11844 |
| solution-aron-mark |     0.439158 |       0.157048 |    1.12804 |
| solution-flask     |     0.434707 |       1.00821  |    1.69176 |
| solution-1-flask   |     0.432735 |       1.00836  |    5.78493 |
| solution-2         |     0.44164  |       0.57686  |   22.4499  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.431074 |       0.180184 |    4.01447 |
| solution-pl        |     0.437004 |       0.185236 |    4.08434 |
| solution-flask     |     0.425073 |       1.00854  |    5.41657 |