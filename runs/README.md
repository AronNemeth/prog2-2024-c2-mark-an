# 2025-03-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.515038 |       1.00879  |   0.083277 |
| solution-aron-mark |     1.83938  |       0.119995 |   0.18507  |
| solution-pl        |     0.523076 |       0.122097 |   0.199569 |
| solution-1-flask   |     5.33329  |       1.08258  |   0.271775 |
| solution-1         |     7.57676  |       1e-06    |   0.609658 |
| solution-2         |     0.514741 |       0.571268 |   1.188    |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.530137 |       0.12376  |   0.29297  |
| solution-pl        |     0.541237 |       0.124433 |   0.300126 |
| solution-flask     |     0.529583 |       1.00876  |   0.30207  |
| solution-1-flask   |     0.530791 |       1.00899  |   0.810949 |
| solution-2         |     0.514638 |       0.513076 |   3.00996  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.526316 |       0.130738 |   0.898402 |
| solution-pl        |     0.552713 |       0.134952 |   0.917624 |
| solution-flask     |     0.528685 |       1.00919  |   1.26169  |
| solution-1-flask   |     0.533447 |       1.00924  |   5.76329  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.520515 |       0.159973 |    2.9237  |
| solution-aron-mark |     0.527524 |       0.159856 |    2.92896 |
| solution-flask     |     0.551118 |       1.00903  |    4.39291 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.521708 |       0.26492  |    16.4435 |
| solution-aron-mark |     0.531789 |       0.268823 |    16.9571 |