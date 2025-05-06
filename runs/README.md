# 2025-05-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.1641   |       1.08188  |   0.083483 |
| solution-pl        |     5.89209  |       0.123364 |   0.191099 |
| solution-aron-mark |     0.494307 |       0.122926 |   0.191662 |
| solution-1-flask   |     0.488355 |       1.00879  |   0.268283 |
| solution-1         |     7.46931  |       1e-06    |   0.617943 |
| solution-2         |     0.485221 |       0.580878 |   1.22245  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.479436 |       1.00868  |   0.291219 |
| solution-pl        |     0.488423 |       0.125325 |   0.296686 |
| solution-aron-mark |     0.474531 |       0.126186 |   0.298847 |
| solution-1-flask   |     0.480672 |       1.00891  |   0.775686 |
| solution-2         |     0.473408 |       0.519731 |   3.02089  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.476856 |       0.130729 |   0.90786  |
| solution-aron-mark |     0.480152 |       0.133198 |   0.916454 |
| solution-flask     |     0.477848 |       1.00921  |   1.23349  |
| solution-1-flask   |     0.492577 |       1.00898  |   5.52495  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.487949 |       0.163861 |    2.89123 |
| solution-aron-mark |     0.481011 |       0.162108 |    2.89822 |
| solution-flask     |     0.47617  |       1.0105   |    4.33146 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.484526 |       0.269691 |    17.3507 |
| solution-aron-mark |     0.487059 |       0.273631 |    17.3838 |