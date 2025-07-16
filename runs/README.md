# 2025-07-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.21145  |       1.16124  |   0.102849 |
| solution-pl        |     0.503515 |       0.149276 |   0.235631 |
| solution-aron-mark |     4.47044  |       0.146873 |   0.236223 |
| solution-1-flask   |     0.511773 |       1.00814  |   0.26726  |
| solution-1         |     7.37538  |       1e-06    |   0.761317 |
| solution-2         |     0.502087 |       0.616884 |   0.879545 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.498986 |       0.153761 |   0.360471 |
| solution-aron-mark |     0.498621 |       0.150738 |   0.362352 |
| solution-flask     |     0.500905 |       1.00843  |   0.382949 |
| solution-1-flask   |     0.504664 |       1.00826  |   0.808132 |
| solution-2         |     0.492153 |       0.502568 |   2.83526  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.502436 |       0.157482 |    1.066   |
| solution-aron-mark |     0.500053 |       0.157973 |    1.07596 |
| solution-flask     |     0.497825 |       1.00857  |    1.57476 |
| solution-1-flask   |     0.510518 |       1.00864  |    5.67759 |
| solution-2         |     0.499632 |       0.555653 |   27.3671  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.502478 |       0.187132 |    3.20433 |
| solution-pl        |     0.503267 |       0.188751 |    3.21021 |
| solution-flask     |     0.499694 |       1.00845  |    5.08208 |