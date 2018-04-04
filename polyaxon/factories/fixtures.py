from polyaxon_schemas.polyaxonfile.specification import Specification, PluginSpecification


experiment_group_spec_content = """---
    version: 1

    project:
      name: project1
      
    matrix:
      lr:
        logspace: 0.01:0.1:5

    model:
      model_type: regressor
      loss:
        MeanSquaredError:
      optimizer:
        Adam:
          learning_rate: "{{ lr }}"
      graph:
        input_layers: images
        layers:
          - Conv2D:
              filters: 64
              kernel_size: [3, 3]
              strides: [1, 1]
              activation: relu
              kernel_initializer: Ones
          - MaxPooling2D:
              kernels: 2
          - Flatten:
          - Dense:
              units: 10
              activation: softmax

    train:
      data_pipeline:
        TFRecordImagePipeline:
          batch_size: 64
          num_epochs: 1
          shuffle: true
          dynamic_pad: false
          data_files: ["../data/mnist/mnist_train.tfrecord"]
          meta_data_file: "../data/mnist/meta_data.json"
"""

experiment_group_spec_content_2_xps = """---
    version: 1

    project:
      name: project1
      
    settings:
      concurrent_experiments: 2
      
    matrix:
      lr:
        values: [0.01, 0.1]

    run:
      image: my_image
      cmd: video_prediction_train --model=DNA --num_masks=1
"""

experiment_group_spec_content_early_stopping = """---
    version: 1

    project:
      name: project1

    settings:
      concurrent_experiments: 2
      n_experiments: 2
      early_stopping:
        - metric: precision
          value: 0.9
        - metric: loss
          value: 0.1
          optimization: minimize 


    matrix:
      lr:
        values: [0.01, 0.1, 0.2]

    run:
      image: my_image
      cmd: video_prediction_train --model=DNA --num_masks=1
"""

experiment_spec_content = """---
    version: 1

    project:
      name: project1

    model:
      model_type: regressor
      loss:
        MeanSquaredError:
      optimizer:
        Adam:
          learning_rate: 0.7
      graph:
        input_layers: images
        layers:
          - Conv2D:
              filters: 64
              kernel_size: [3, 3]
              strides: [1, 1]
              activation: relu
              kernel_initializer: Ones
          - MaxPooling2D:
              kernels: 2
          - Flatten:
          - Dense:
              units: 10
              activation: softmax

    train:
      data_pipeline:
        TFRecordImagePipeline:
          batch_size: 64
          num_epochs: 1
          shuffle: true
          dynamic_pad: false
          data_files: ["../data/mnist/mnist_train.tfrecord"]
          meta_data_file: "../data/mnist/meta_data.json"
"""
experiment_spec_parsed_content = Specification.read(experiment_spec_content)

exec_experiment_spec_content = """---
    version: 1

    project:
      name: project1

    run:
      image: my_image
      cmd: video_prediction_train --model=DNA --num_masks=1
"""

exec_experiment_spec_parsed_content = Specification.read(exec_experiment_spec_content)


exec_experiment_resources_content = """---
    version: 1

    project:
      name: project1
    
    environment:
      resources:
        cpu:
          requests: 1
          limits: 1    
        memory:
          requests: 100
          limits: 200
    
      tensorflow:  
        n_workers: 1
        n_ps: 1  
        
        default_worker_resources:
          cpu:
            requests: 1
            limits: 1
            
          memory:
            requests: 100
            limits: 200
        
        default_ps_resources:
          cpu:
            requests: 1
            limits: 1
            
          memory:
            requests: 100
            limits: 200

    model:
      model_type: regressor
      loss:
        MeanSquaredError:
      optimizer:
        Adam:
          learning_rate: 0.7
      graph:
        input_layers: images
        layers:
          - Conv2D:
              filters: 64
              kernel_size: [3, 3]
              strides: [1, 1]
              activation: relu
              kernel_initializer: Ones
          - MaxPooling2D:
              kernels: 2
          - Flatten:
          - Dense:
              units: 10
              activation: softmax

    train:
      data_pipeline:
        TFRecordImagePipeline:
          batch_size: 64
          num_epochs: 1
          shuffle: true
          dynamic_pad: false
          data_files: ["../data/mnist/mnist_train.tfrecord"]
          meta_data_file: "../data/mnist/meta_data.json"
"""

exec_experiment_resources_parsed_content = Specification.read(exec_experiment_resources_content)


plugin_spec_content = """---
    version: 1

    project:
      name: project1

    run:
      image: my_image
"""

plugin_spec_parsed_content = PluginSpecification.read(plugin_spec_content)
