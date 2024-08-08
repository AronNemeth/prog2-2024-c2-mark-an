# 2024-08-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.561038 |       1.00879  |   0.075471 |
| solution-aron-mark |     2.15508  |       0.101931 |   0.165984 |
| solution-pl        |     0.548748 |       0.102821 |   0.168305 |
| solution-1-flask   |     1.23636  |       1.09486  |   0.26358  |
| solution-1         |     7.78772  |       1e-06    |   0.609361 |
| solution-2         |     4.77975  |       0.552657 |   1.05388  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.577118 |       1.00979  |   0.194195 |
| solution-pl        |     0.572645 |       0.105292 |   0.289872 |
| solution-aron-mark |     0.566008 |       0.104357 |   0.293816 |
| solution-1-flask   |     0.566128 |       1.00923  |   0.764964 |
| solution-2         |     0.54955  |       0.470212 |  16.0517   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.55881  |       1.00889  |   0.896029 |
| solution-aron-mark |     0.55426  |       0.110761 |   0.996618 |
| solution-pl        |     0.555199 |       0.110157 |   0.997116 |
| solution-1-flask   |     0.572743 |       1.00918  |   5.53678  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.550987 |       0.147337 |    4.29482 |
| solution-flask     |     0.551098 |       1.00956  |    4.42473 |
| solution-pl        |     0.5604   |       0.143913 |    4.4858  |