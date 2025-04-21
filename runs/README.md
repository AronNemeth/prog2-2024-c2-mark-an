# 2025-04-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.506507 |       1.00869  |   0.083757 |
| solution-aron-mark |     1.79087  |       0.12057  |   0.185003 |
| solution-pl        |     0.507461 |       0.122628 |   0.187151 |
| solution-1-flask   |     4.96725  |       1.13047  |   0.271675 |
| solution-1         |     7.34754  |       1e-06    |   0.594379 |
| solution-2         |     0.509974 |       0.866364 |   1.23996  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.51544  |       0.128548 |   0.290451 |
| solution-aron-mark |     0.528191 |       0.124709 |   0.294424 |
| solution-flask     |     0.509251 |       1.00871  |   0.299967 |
| solution-1-flask   |     0.533827 |       1.00906  |   0.802839 |
| solution-2         |     0.523205 |       0.518396 |   3.97825  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.521193 |       0.131262 |   0.889174 |
| solution-aron-mark |     0.514693 |       0.128818 |   0.895727 |
| solution-flask     |     0.513227 |       1.00905  |   1.24472  |
| solution-1-flask   |     0.539275 |       1.00881  |   5.3681   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.507412 |       0.16064  |    2.85926 |
| solution-pl        |     0.510637 |       0.160528 |    2.88164 |
| solution-flask     |     0.509964 |       1.00878  |    4.32658 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.523567 |       0.263914 |    17.5066 |
| solution-aron-mark |     0.515244 |       0.272888 |    17.8129 |