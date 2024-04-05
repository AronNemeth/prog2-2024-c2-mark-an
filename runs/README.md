# 2024-04-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.668301 |       1.00896  |   0.066147 |
| solution-pl        |     6.19772  |       0.117361 |   0.171978 |
| solution-aron-mark |     0.655058 |       0.114497 |   0.17199  |
| solution-1-flask   |     1.459    |       1.04671  |   0.270826 |
| solution-1         |     8.18679  |       1e-06    |   0.595299 |
| solution-2         |     0.657724 |       0.447017 |   0.987887 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.67686  |       1.00925  |   0.174245 |
| solution-pl        |     0.683274 |       0.115375 |   0.261786 |
| solution-aron-mark |     0.670024 |       0.114605 |   0.264288 |
| solution-1-flask   |     0.697251 |       1.00882  |   0.784124 |
| solution-2         |     0.672648 |       0.45465  |  13.225    |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.675107 |       0.126246 |   0.823199 |
| solution-aron-mark |     0.679396 |       0.124103 |   0.823761 |
| solution-flask     |     0.674378 |       1.00923  |   0.920229 |
| solution-1-flask   |     0.687293 |       1.00917  |   5.55167  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.668343 |       0.157219 |    3.3185  |
| solution-pl        |     0.661427 |       0.154541 |    3.34134 |
| solution-flask     |     0.678555 |       1.00908  |    5.67976 |