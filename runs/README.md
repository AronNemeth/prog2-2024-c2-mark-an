# 2024-06-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.56368  |       1.08055  |   0.076758 |
| solution-aron-mark |     6.32269  |       0.104842 |   0.164939 |
| solution-pl        |     0.661241 |       0.102926 |   0.168466 |
| solution-1-flask   |     0.702055 |       1.00917  |   0.267951 |
| solution-1         |     8.57846  |       1e-06    |   0.609893 |
| solution-2         |     0.662094 |       0.442613 |   0.715032 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.689171 |       1.00914  |   0.166644 |
| solution-pl        |     0.686657 |       0.104716 |   0.264257 |
| solution-aron-mark |     0.695732 |       0.108318 |   0.26757  |
| solution-1-flask   |     0.712178 |       1.00892  |   0.779012 |
| solution-2         |     0.681253 |       0.441902 |   6.05666  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.661236 |       1.00926  |   0.734273 |
| solution-pl        |     0.656288 |       0.112586 |   0.810209 |
| solution-aron-mark |     0.661028 |       0.115834 |   0.886042 |
| solution-1-flask   |     0.679271 |       1.00921  |   5.59558  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.709534 |       1.00993  |    2.58088 |
| solution-aron-mark |     0.667323 |       0.153584 |    2.67104 |
| solution-pl        |     0.696042 |       0.159955 |    2.83321 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.673875 |       1.00914  |    16.5898 |
| solution-pl        |     0.666066 |       0.280395 |    22.9542 |
| solution-aron-mark |     0.672828 |       0.280774 |    23.8366 |