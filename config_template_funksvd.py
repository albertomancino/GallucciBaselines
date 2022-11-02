TEMPLATE = """experiment:
  dataset: subdatasets_{sub}
  data_config:
    strategy: dataset
    dataset_path: {path}
  splitting:
    test_splitting:
      strategy: random_subsampling
      test_ratio: 0.2
      folds: 1
  top_k: 10
  evaluation:
    cutoffs: [10, 5, 1]
    simple_metrics: [nDCGRendle2020, HR, ItemCoverage, UserCoverage]
    relevance_threshold: 3
  gpu: 0
  models:
    FunkSVD:
      meta:
        save_recs: True
        verbose: True
        hyper_max_evals: 10
        hyper_opt_alg: tpe
        validation_metric: nDCGRendle2020@10
      epochs: 100
      batch_size: 512
      factors: [16, 64, 128, 256]
      lr: [0.001, 0.003, 0.01]
      reg_w: 0.1
      reg_b: 0.001"""